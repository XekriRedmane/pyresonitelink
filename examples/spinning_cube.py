"""Example that places a spinning cube 5 m in front of the user's head.

The cube is a 0.5 m BoxMesh with a default PBS_Metallic material. A Spinner
component drives the cube slot's rotation, turning it once around the
vertical axis every three seconds. The engine runs the Spinner every frame,
so the cube keeps turning after this script exits. No ProtoFlux is involved.

The cube is placed with pyresonitelink.utils.placement, which finds the
first user's head.

Usage:
    python examples/spinning_cube.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.generated.transform.drivers import spinner
from pyresonitelink.utils import placement
from pyresonitelink.utils import rendering
from pyresonitelink.utils import slots

SLOT_NAME = "Spinning Cube Example"
CUBE_SIZE = 0.5  # meters, along each edge
DISTANCE = 5.0  # meters in front of the head
SECONDS_PER_TURN = 3.0


async def main(port: int | None) -> None:
    """Places a spinning cube in front of the user's head."""
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)

    for old in await workers.Slot(id=workers.Slot.ROOT_SLOT_ID).remove_children_named(
        resolink, SLOT_NAME,
    ):
        print(f"Deleted old slot {old}.")

    # Only the position is kept, so the slot has no rotation relative to
    # the world, and its local Y axis is the world's vertical axis.
    in_front = await placement.in_front_of_head(resolink, DISTANCE)
    cube = await slots.add_slot_at(
        resolink, transforms.Transform(in_front.position), name=SLOT_NAME,
    )
    print(f"Created slot {cube.id}.")

    mesh = box_mesh.BoxMesh(size=primitives.Float3(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))
    await mesh.add_to_slot(resolink, cube)
    material = pbs_metallic.PBS_Metallic()
    await material.add_to_slot(resolink, cube)
    await rendering.add_renderer(resolink, cube, mesh, [material])

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
