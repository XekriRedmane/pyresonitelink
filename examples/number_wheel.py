"""Example that counts on an odometer number drum.

The drum is the "Drum" node of NumberDrum.glb, next to this script. It is
a ten-sided black prism with beveled edges, and its "Digits" child holds
one white digit for each face, in DejaVu Sans. The
script imports the drum and its digits as one mesh with two submeshes, and
places it 5 m in front of the user's head with the 0 facing the head.

A ProtoFlux graph turns the drum to the next digit once a second. For most
of each second the drum rests, and for the last MOVE_SECONDS it turns
36 degrees, accelerating and then decelerating along a smoothstep curve.
The graph computes the drum's rotation from an ElapsedTimeDouble node's
time, and a ValueFieldDrive writes it to the drum slot's Rotation field
in every engine update, so the drum keeps counting after this script
exits. Each run deletes the drum from the previous run.

The ProtoFlux nodes compute this, where t is the time in seconds from
ElapsedTimeDouble.

    whole = floor(t)
    turn = smoothstep(clamp01((t - whole - REST_SECONDS) / MOVE_SECONDS))
    angle = ((whole mod 10) + turn) * 36
    rotation = AxisAngle(-X, angle)

Taking whole mod 10 keeps the angle under 360 degrees, so the float that
AxisAngle takes doesn't lose precision as t grows.

Usage:
    python examples/number_wheel.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys

import numpy as np

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import members
from pyresonitelink.data import mesh
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated.assets import static_mesh
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.generated.rendering import mesh_renderer
from pyresonitelink.protoflux import core
from pyresonitelink.protoflux import math as pf_math
from pyresonitelink.protoflux import operators
from pyresonitelink.protoflux import time as pf_time
from pyresonitelink.protoflux.core import casts
from pyresonitelink.protoflux.math import rotation
from pyresonitelink.protoflux.math import shaping
from pyresonitelink.utils import glb

GLB_PATH = os.path.join(os.path.dirname(__file__), "NumberDrum.glb")
SLOT_NAME = "Number Wheel Example"
USER_ROOT_TYPE = "[FrooxEngine]FrooxEngine.UserRoot"
DRUM_NODE = "Drum"
DIGITS_NODE = "Digits"
DISTANCE = 5.0  # meters in front of the head
# The drum's radius in the file is 1. This makes it 0.5 m.
WHEEL_SCALE = 0.5
REST_SECONDS = 0.6  # of each second, before the drum starts to turn
MOVE_SECONDS = 1.0 - REST_SECONDS
DEGREES_PER_DIGIT = 36.0

# Rotates the drum from its own coordinates, after glb.to_resonite, to the
# wheel slot's coordinates.
#
# After glb.to_resonite negates X, the drum's axis is Y, and digit d faces
# the direction 90 - 36d degrees around Y, measured from +Z toward +X. The
# top of each digit points toward the next digit, so 0 faces +X with its
# top toward +Z.
#
# The rotation turns the drum so that its axis is X, the 0 faces -Z, and
# the top of the 0 is +Y. Its rows are:
#
#   x' = -y    the drum's axis, Y, becomes horizontal
#   y' =  z    the top of the 0 points up
#   z' = -x    the 0 faces -Z, toward the user
_DRUM_TO_WHEEL = np.array([
    [0.0, -1.0, 0.0],
    [0.0, 0.0, 1.0],
    [-1.0, 0.0, 0.0],
])


def format_vector(v: primitives.Float3) -> str:
    """Formats a Float3 as "(x, y, z)" with two decimal places.

    Args:
        v (primitives.Float3): The vector.

    Returns:
        The formatted vector.
    """
    return f"({v.x:.2f}, {v.y:.2f}, {v.z:.2f})"


def load_drum(path: str) -> glb.Mesh:
    """Reads the drum and its digits from a .glb file.

    The drum node's mesh is the first submesh, and the mesh of its Digits
    child is the second. Both are in the wheel's coordinates (see
    _DRUM_TO_WHEEL).

    Args:
        path (str): The .glb file.

    Returns:
        The drum and its digits, as one mesh with two submeshes.

    Raises:
        LookupError: The file has no node named DRUM_NODE.
        ValueError: The submeshes aren't one from DRUM_NODE followed by one
            from DIGITS_NODE.
    """
    drum = glb.read_node(glb.load(path), DRUM_NODE)
    # place_drum gives the submeshes their materials by position.
    if drum.nodes != [DRUM_NODE, DIGITS_NODE]:
        raise ValueError(f"{path} has submeshes from {drum.nodes}.")
    return glb.transform(glb.to_resonite(drum), _DRUM_TO_WHEEL)


async def find_head(resolink: client.Client) -> str:
    """Finds the slot ID of the first user's head.

    The first user is the first child of Root with a UserRoot component.

    Args:
        resolink (client.Client): The connected client.

    Returns:
        The ID of the user root's child named "Head".

    Raises:
        LookupError: No user root or no head slot was found.
    """
    root = (await resolink.get_slot(workers.Slot.ROOT_SLOT_ID, depth=1)).data
    assert root is not None
    user_root = next(
        (child for child in root.children
         if any(c.componentType == USER_ROOT_TYPE for c in child.components)),
        None,
    )
    if user_root is None:
        raise LookupError("No child of Root has a UserRoot component.")
    assert user_root.id is not None
    user = (await resolink.get_slot(user_root.id, depth=1)).data
    assert user is not None
    for child in user.children:
        if child.name is not None and child.name.value == "Head":
            assert child.id is not None
            return child.id
    raise LookupError(f"The user root {user_root.id} has no Head slot.")


async def add_node(
    resolink: client.Client,
    slot: workers.Slot,
    node: GeneratedComponent,
    **inputs: GeneratedComponent,
) -> None:
    """Adds a ProtoFlux node to a slot, then wires its inputs.

    The node is added without references and wired afterwards, because
    ProtoFlux nodes wired in AddComponent are often left unwired. Each
    reference is sent with the targetType that the node's own data
    reports for it.

    Args:
        resolink (client.Client): The connected client.
        slot (workers.Slot): The slot to add the node to.
        node (GeneratedComponent): The node, which has no ID yet.
        **inputs (GeneratedComponent): The node's input members, by member
            name, and the nodes they read from.

    Raises:
        RuntimeError: The server refused the references.
    """
    await node.add_to_slot(resolink, slot)
    if not inputs:
        return
    # Without this pause the references all arrive, but the graph doesn't
    # run. The nodes apparently have to be registered in an engine update
    # before they're wired.
    await asyncio.sleep(0.05)
    references: dict[str, str | members.Reference] = {}
    for name, source in inputs.items():
        member = node.get_member(name)
        assert isinstance(member, members.Reference), f"{name} isn't a reference"
        assert source.id is not None
        references[name] = members.Reference(
            targetId=source.id, targetType=member.targetType,
        )
    assert node.id is not None
    resp = await resolink.update_references(
        componentId=node.id, references=references,
    )
    if not resp.success:
        raise RuntimeError(
            f"Failed to wire {type(node).__name__} {node.id}: {resp.errorInfo}"
        )


async def build_graph(
    resolink: client.Client,
    graph_slot: workers.Slot,
    drum_slot: workers.Slot,
) -> None:
    """Builds the ProtoFlux graph that drives the drum slot's rotation.

    Args:
        resolink (client.Client): The connected client.
        graph_slot (workers.Slot): The slot to add the nodes to.
        drum_slot (workers.Slot): The slot whose Rotation the graph drives.

    Raises:
        RuntimeError: A node couldn't be wired, or the server didn't add
            the drive's Proxy component.
    """
    Double = primitives.Double

    async def constant(value: float) -> GeneratedComponent:
        """Adds a ValueInput<double> node that outputs a constant.

        Args:
            value (float): The constant.

        Returns:
            The node.
        """
        node = core.ValueInput[Double](Double(value))
        await add_node(resolink, graph_slot, node)
        return node

    rest = await constant(REST_SECONDS)
    per_move = await constant(1.0 / MOVE_SECONDS)
    ten = await constant(10.0)
    degrees_per_digit = await constant(DEGREES_PER_DIGIT)
    # Positive angles about -X roll the front of the drum downward, which
    # brings the next digit, above the current one, to the front.
    axis = core.ValueInput[primitives.Float3](primitives.Float3(-1, 0, 0))
    await add_node(resolink, graph_slot, axis)

    elapsed = pf_time.ElapsedTimeDouble()
    await add_node(resolink, graph_slot, elapsed)
    whole = pf_math.Floor_Double()
    await add_node(resolink, graph_slot, whole, N=elapsed)
    fraction = operators.ValueSub[Double]()
    await add_node(resolink, graph_slot, fraction, A=elapsed, B=whole)
    moving = operators.ValueSub[Double]()
    await add_node(resolink, graph_slot, moving, A=fraction, B=rest)
    scaled = operators.ValueMul[Double]()
    await add_node(resolink, graph_slot, scaled, A=moving, B=per_move)
    progress = pf_math.Clamp01_Double()
    await add_node(resolink, graph_slot, progress, N=scaled)
    turn = shaping.SmoothStep_Double()
    await add_node(resolink, graph_slot, turn, Value=progress)
    digit = operators.ValueMod[Double]()
    await add_node(resolink, graph_slot, digit, A=whole, B=ten)
    position = operators.ValueAdd[Double]()
    await add_node(resolink, graph_slot, position, A=digit, B=turn)
    degrees = operators.ValueMul[Double]()
    await add_node(resolink, graph_slot, degrees, A=position, B=degrees_per_digit)
    angle = casts.Cast_double_To_float()
    await add_node(resolink, graph_slot, angle, Input=degrees)
    quaternion = rotation.AxisAngle_floatQ()
    await add_node(resolink, graph_slot, quaternion, Axis=axis, Angle=angle)
    drive = core.ValueFieldDrive[primitives.FloatQ]()
    await add_node(resolink, graph_slot, drive, Value=quaternion)

    # The field that a ValueFieldDrive drives is set on a Proxy component
    # that the server adds next to the node. The Proxy's Node member
    # identifies the node it belongs to.
    graph = (await resolink.get_slot(
        graph_slot, depth=0, includeComponentData=True,
    )).data
    assert graph is not None
    proxy = next(
        (c for c in graph.components
         if c.componentType is not None
         and c.componentType.endswith("+Proxy")
         and isinstance(node_ref := (c.members or {}).get("Node"), members.Reference)
         and node_ref.targetId == drive.id),
        None,
    )
    if proxy is None or proxy.id is None:
        raise RuntimeError(f"No Proxy component for the drive {drive.id}.")
    drum = (await resolink.get_slot(drum_slot)).data
    assert drum is not None and drum.rotation is not None
    assert drum.rotation.id is not None
    resp = await resolink.update_references(
        componentId=proxy.id,
        references={"Drive": members.Reference(
            targetId=drum.rotation.id,
            targetType="[FrooxEngine]FrooxEngine.IField<floatQ>",
        )},
    )
    if not resp.success:
        raise RuntimeError(f"Failed to set the drive target: {resp.errorInfo}")


async def place_drum(
    resolink: client.Client, slot_name: str,
) -> tuple[workers.Slot, workers.Slot]:
    """Places the drum 5 m in front of the user's head, with the 0 facing it.

    A slot under Root named slot_name, from a previous run, is deleted
    first.

    Args:
        resolink (client.Client): The connected client.
        slot_name (str): The name of the slot under Root that holds the
            drum.

    Returns:
        The drum's slot, whose Rotation turns the drum, and an empty slot
        beside it for the ProtoFlux graph.
    """
    drum = load_drum(GLB_PATH)
    print(f"Read {len(drum.positions)} vertices from {GLB_PATH}.")

    root = (await resolink.get_slot(workers.Slot.ROOT_SLOT_ID, depth=1)).data
    assert root is not None
    for child in root.children:
        if child.name is not None and child.name.value == slot_name:
            print(f"Deleting old slot {child.id}.")
            await resolink.remove_slot(child)

    # The wheel takes the head's rotation, so its -Z axis, which the 0
    # faces, points back at the head. +Z is forward in Resonite.
    head_id = await find_head(resolink)
    head = await resolink.get_global_transform(head_id)
    forward = transforms.rotate(head.rotation, primitives.Float3(0, 0, 1))
    world = transforms.Transform(
        position=primitives.Float3(
            head.position.x + DISTANCE * forward.x,
            head.position.y + DISTANCE * forward.y,
            head.position.z + DISTANCE * forward.z,
        ),
        rotation=head.rotation,
    )
    print(f"Head {head_id} is at {format_vector(head.position)}, facing {format_vector(forward)}.")

    root_transform = await resolink.get_global_transform(workers.Slot.ROOT_SLOT_ID)
    local = transforms.relative_to(root_transform, world)
    wheel = await resolink.add_slot(
        name=slot_name,
        position=local.position,
        rotation=local.rotation,
        scale=(WHEEL_SCALE, WHEEL_SCALE, WHEEL_SCALE),
    )
    drum_slot = await resolink.add_slot(parent=wheel, name="Drum")
    graph_slot = await resolink.add_slot(parent=wheel, name="ProtoFlux")
    print(f"Created slot {wheel.id} at {format_vector(world.position)}.")

    asset = await resolink.import_mesh_raw_data(
        drum.positions,
        [mesh.RawTriangles(t) for t in drum.submeshes],
        normals=drum.normals,
    )
    drum_mesh = static_mesh.StaticMesh(url=asset.assetURL)
    await drum_mesh.add_to_slot(resolink, drum_slot)
    # The colors are those of the materials in the file, which glTF gives
    # as linear values.
    black = pbs_metallic.PBS_Metallic(
        albedo_color=primitives.ColorX(0.045, 0.045, 0.045, 1, "Linear"),
        metallic=primitives.Float(0.5),
        smoothness=primitives.Float(0.4),
    )
    await black.add_to_slot(resolink, drum_slot)
    white = pbs_metallic.PBS_Metallic(
        albedo_color=primitives.ColorX(1, 1, 1, 1, "Linear"),
        emissive_color=primitives.ColorX(0.077, 0.077, 0.077, 1, "Linear"),
        metallic=primitives.Float(0),
        smoothness=primitives.Float(0.47),
    )
    await white.add_to_slot(resolink, drum_slot)
    renderer = mesh_renderer.MeshRenderer(mesh=drum_mesh)
    await renderer.add_to_slot(resolink, drum_slot)
    # The server adds a list element for each member ID it hasn't seen.
    # Materials apply to the submeshes in order.
    materials = renderer.materials
    assert materials is not None
    materials.elements.append(members.Reference(targetId=black.id))
    materials.elements.append(members.Reference(targetId=white.id))
    await renderer.update(resolink)
    return drum_slot, graph_slot


async def main(port: int | None) -> None:
    """Places the counting drum in front of the user's head.

    Args:
        port (int | None): The ResoniteLink port, or None to find the
            session from its LAN announcement.
    """
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)
    drum_slot, graph_slot = await place_drum(resolink, SLOT_NAME)
    await build_graph(resolink, graph_slot, drum_slot)
    print("The drum turns to the next digit every second, and is left in place.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
