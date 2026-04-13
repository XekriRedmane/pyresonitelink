"""Minimal test: a single bare write via Dergflux.

Implements: counter = counter + 1 (runs once via boolean gate)

Usage:
    python examples/dergflux_minimal_write.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Build a minimal write graph."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Minimal Write")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Minimal Write")
    print(f"Created slot: {slot.id}\n")

    g = Graph()
    s = g.Space(slot)
    s.counter = s.FloatDynVar("counter")
    s.ran = s.BoolDynVar("ran")

    with g.Under(slot):
        with g.If(s.ran == False):  # noqa: E712
            s.counter = s.counter + 1
            s.ran = True

    print("Building graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # Wait for a few frames to ensure graph has run
    time.sleep(0.5)

    counter_var = s.counter
    await counter_var.refresh(resolink)
    print(f"counter = {counter_var.value} (expected 1.0)")

    await resolink.remove_slot(slot=slot)
    print("Cleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
