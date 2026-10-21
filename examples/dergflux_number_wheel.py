"""Example that counts on an odometer number drum, with a Dergflux graph.

This is number_wheel.py with its ProtoFlux graph written in Dergflux. The
drum is placed the same way, by number_wheel.place_drum, 5 m in front of
the user's head with the 0 facing the head. Once a second it turns to the
next digit, resting for REST_SECONDS and then turning 36 degrees along a
smoothstep curve.

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
import sys

import number_wheel

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import time

SLOT_NAME = "Dergflux Number Wheel Example"
REST_SECONDS = 0.6  # of each second, before the drum starts to turn
DEGREES_PER_DIGIT = 36.0


async def build_graph(
    resolink: client.Client,
    graph_slot: workers.Slot,
    drum_slot: workers.Slot,
) -> None:
    """Builds the Dergflux graph that drives the drum slot's rotation."""
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
    """Places the counting drum in front of the user's head."""
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)
    drum_slot, graph_slot = await number_wheel.place_drum(resolink, SLOT_NAME)
    await build_graph(resolink, graph_slot, drum_slot)
    print("The drum turns to the next digit every second, and is left in place.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
