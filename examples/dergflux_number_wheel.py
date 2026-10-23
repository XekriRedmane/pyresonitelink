"""Example that counts on an odometer number drum, with a Dergflux graph.

The drum is the "Drum" node of NumberDrum.glb, next to this script. It is
a ten-sided black prism with beveled edges, and its "Digits" child holds
one white digit for each face, in DejaVu Sans. The script imports the drum
and its digits as one mesh with two submeshes, and places it 5 m in front
of the user's head with the 0 facing the head.

Once a second the drum turns to the next digit. For most of each second it
rests, and for the rest of the second it turns 36 degrees, accelerating and
then decelerating along a smoothstep curve.

A binding computes the drum's rotation from the time since "started", a
model variable, and drives the drum slot's Rotation field in every engine
update, so the drum keeps counting after this script exits. The binding
holds the drum at 0 while "started" is 0. Dergflux builds the binding
before the flow, and the flow stores the world time in "started" when it
first runs, so the count starts with the drum already driven. The flow
stores the time again when the stored time is later than the world time,
which happens after the world is saved and reopened, since the world time
starts at 0 in each session. Each run deletes the drum from the previous
run.

Usage:
    python examples/dergflux_number_wheel.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys

import numpy as np

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import time
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.utils import glb
from pyresonitelink.utils import placement
from pyresonitelink.utils import rendering
from pyresonitelink.utils import slots

GLB_PATH = os.path.join(os.path.dirname(__file__), "NumberDrum.glb")
SLOT_NAME = "Dergflux Number Wheel Example"
DRUM_NODE = "Drum"
DIGITS_NODE = "Digits"
DISTANCE = 5.0  # meters in front of the head
# The drum's radius in the file is 1. This makes it 0.5 m.
WHEEL_SCALE = 0.5
REST_SECONDS = 0.6  # of each second, before the drum starts to turn
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


async def place_drum(resolink: client.Client) -> tuple[workers.Slot, workers.Slot]:
    """Places the drum 5 m in front of the user's head, with the 0 facing it.

    A slot under Root named SLOT_NAME, from a previous run, is deleted
    first.

    Args:
        resolink (client.Client): The connected client.

    Returns:
        The drum's slot, whose Rotation turns the drum, and an empty slot
        beside it for the ProtoFlux graph.
    """
    drum = load_drum(GLB_PATH)
    print(f"Read {len(drum.positions)} vertices from {GLB_PATH}.")

    for old in await workers.Slot(id=workers.Slot.ROOT_SLOT_ID).remove_children_named(
        resolink, SLOT_NAME,
    ):
        print(f"Deleted old slot {old}.")
    # The wheel takes the head's rotation, so its -Z axis, which the 0
    # faces, points back at the head.
    world = await placement.in_front_of_head(resolink, DISTANCE, scale=WHEEL_SCALE)
    wheel = await slots.add_slot_at(resolink, world, name=SLOT_NAME)
    drum_slot = await resolink.add_slot(parent=wheel, name="Drum")
    graph_slot = await resolink.add_slot(parent=wheel, name="ProtoFlux")
    print(f"Created slot {wheel.id}.")

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
    await rendering.add_mesh(resolink, drum_slot, drum, [black, white])
    return drum_slot, graph_slot


async def build_graph(
    resolink: client.Client,
    graph_slot: workers.Slot,
    drum_slot: workers.Slot,
) -> None:
    """Builds the Dergflux graph that drives the drum slot's rotation.

    Args:
        resolink (client.Client): The connected client.
        graph_slot (workers.Slot): The slot to add the nodes to.
        drum_slot (workers.Slot): The slot whose Rotation the graph drives.
    """
    g = Graph()
    s = g.Space(graph_slot, space_name="NumberWheel")
    s.started = s.DoubleModelVar("started")  # 0 until the graph first runs
    now = time.world_time()
    with g.Under(graph_slot):
        with g.If((s.started == 0) | (s.started > now)):
            s.started = now

    t = dm.conditional(s.started == 0, 0, now - s.started)
    whole = dm.floor(t)
    # 0 for the first REST_SECONDS of each second, then easing to 1.
    turn = dm.smoothstep(REST_SECONDS, 1.0, t - whole)
    # Taking whole mod 10 keeps the angle under 360 degrees, so the float
    # that axis_angle takes doesn't lose precision as t grows.
    angle = dm.to_float(((whole % 10) + turn) * DEGREES_PER_DIGIT)
    # Positive angles about -X roll the front of the drum downward, which
    # brings the next digit, above the current one, to the front.
    rotation = dm.axis_angle(primitives.Float3(-1, 0, 0), angle)
    g.Bind(rotation, drum_slot, "Rotation", slot=graph_slot)
    await g.build(resolink)


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
    drum_slot, graph_slot = await place_drum(resolink)
    await build_graph(resolink, graph_slot, drum_slot)
    print("The drum turns to the next digit every second, and is left in place.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
