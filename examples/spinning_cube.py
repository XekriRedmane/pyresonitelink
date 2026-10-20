"""Example that places a spinning cube 5 m in front of the user's head.

The cube is a 0.5 m BoxMesh with a default PBS_Metallic material. A Spinner
component drives the cube slot's rotation, turning it once around the
vertical axis every three seconds. The engine runs the Spinner every frame,
so the cube keeps turning after this script exits. No ProtoFlux is involved.

The user's head is the "Head" slot under the user's root slot, which is the
child of Root that has a UserRoot component. If several users are in the
session, the first user root under Root is used.

Usage:
    python examples/spinning_cube.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.generated.rendering import mesh_renderer
from pyresonitelink.generated.transform.drivers import spinner

SLOT_NAME = "Spinning Cube Example"
USER_ROOT_TYPE = "[FrooxEngine]FrooxEngine.UserRoot"
CUBE_SIZE = 0.5  # meters, along each edge
DISTANCE = 5.0  # meters in front of the head
SECONDS_PER_TURN = 3.0


def format_vector(v: primitives.Float3) -> str:
    """Returns a Float3 as "(x, y, z)" with two decimal places."""
    return f"({v.x:.2f}, {v.y:.2f}, {v.z:.2f})"


async def find_head(resolink: client.Client) -> str:
    """Returns the slot ID of the first user's head.

    Raises:
        LookupError: No user root or no head slot was found.
    """
    root = (await resolink.get_slot(workers.Slot.ROOT_SLOT_ID, depth=1)).data
    assert root is not None
    # Without includeComponentData, the children still list their
    # components' types.
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


async def main(port: int | None) -> None:
    """Places a spinning cube in front of the user's head."""
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)

    # Delete the cube from a previous run.
    root = (await resolink.get_slot(workers.Slot.ROOT_SLOT_ID, depth=1)).data
    assert root is not None
    for child in root.children:
        if child.name is not None and child.name.value == SLOT_NAME:
            print(f"Deleting old slot {child.id}.")
            await resolink.remove_slot(child)

    head_id = await find_head(resolink)
    head = await resolink.get_global_transform(head_id)
    # +Z is forward in Resonite.
    forward = transforms.rotate(head.rotation, primitives.Float3(0, 0, 1))
    position = transforms.Transform(primitives.Float3(
        head.position.x + DISTANCE * forward.x,
        head.position.y + DISTANCE * forward.y,
        head.position.z + DISTANCE * forward.z,
    ))
    print(f"Head {head_id} is at {format_vector(head.position)}, facing {format_vector(forward)}.")

    # The cube's world position is converted to Root's space, since a new
    # slot's position is relative to its parent. The slot has no rotation
    # relative to Root, so its local Y axis is the world's vertical axis.
    root_transform = await resolink.get_global_transform(workers.Slot.ROOT_SLOT_ID)
    local = transforms.relative_to(root_transform, position)
    cube = await resolink.add_slot(name=SLOT_NAME, position=local.position)
    print(f"Created slot {cube.id} at {format_vector(position.position)}.")

    mesh = box_mesh.BoxMesh(size=primitives.Float3(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))
    await mesh.add_to_slot(resolink, cube)
    material = pbs_metallic.PBS_Metallic()
    await material.add_to_slot(resolink, cube)
    renderer = mesh_renderer.MeshRenderer(mesh=mesh)
    await renderer.add_to_slot(resolink, cube)

    # The renderer starts with an empty material list. The server adds an
    # element for each member ID in the update that the list doesn't have.
    materials = renderer.materials
    assert materials is not None
    materials.elements.append(members.Reference(targetId=material.id))
    await renderer.update(resolink)

    # The Spinner drives a FloatQ field, here the slot's own Rotation field,
    # so it needs that field's member ID rather than the slot's ID.
    cube_data = (await resolink.get_slot(cube)).data
    assert cube_data is not None and cube_data.rotation is not None
    degrees_per_second = 360.0 / SECONDS_PER_TURN
    spin = spinner.Spinner(
        target=cube_data.rotation.id,
        speed=primitives.Float3(0, degrees_per_second, 0),
    )
    await spin.add_to_slot(resolink, cube)
    print(f"Spinner {spin.id} turns the cube at {degrees_per_second:g} degrees per second.")

    print("The cube is left in place.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
