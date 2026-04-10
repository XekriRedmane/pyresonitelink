"""Example: For loop using the Dergflux DSL.

Implements: total = 0; for (i = 0; i < 10; i++) total += i; total *= 2;
Result: total = 90

Usage:
    python examples/dergflux_for.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.components.data.dynamic import DynamicValueVariable
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Build a for-loop graph using Dergflux and test it."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    old = await resolink.find_slot("Root", name="Dergflux For")
    if old is not None:
        print(f"Deleting old slot {old.id}...")
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot_to_root(name="Dergflux For")
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Build the graph using Dergflux DSL
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.total = s.FloatVar("total")

    with g.Under(slot):
        # g.For(count) yields a ForProxy `f` with two sections:
        #   f.OnStart()    — runs once before the loop (loop_start)
        #   f.OnIterate()  — runs each iteration, yields index (loop_iteration)
        #
        # The For and the following If become two entries in a
        # Sequence node. The Sequence waits for the For to finish
        # (loop_end), then fires the If.

        with g.For(10) as f:
            with f.OnStart():
                # Runs once before the loop begins.
                # Good for initializing accumulators.
                s.total = 0

            with f.OnIterate() as i:
                # Runs each iteration. `i` is an Int ExprProxy
                # holding the current iteration index (0..9).
                s.total = s.total + i

        # This runs after the loop finishes (via Sequence).
        # total is now 45, so double it to 90.
        with g.If(s.total > 0):
            s.total = s.total * 2

    print("Building graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # ===================================================================
    # Test the graph
    # ===================================================================

    FloatDynVar = DynamicValueVariable[primitives.Float]

    print("Waiting for graph evaluation...")
    time.sleep(1.0)

    slot_data = await resolink.get_slot(slot=slot, depth=0)
    assert slot_data.data is not None

    for comp in slot_data.data.components:
        if comp.componentType == FloatDynVar.COMPONENT_TYPE:
            dv = FloatDynVar(component=comp)
            if dv.variable_name == "total":
                await dv.refresh(resolink)
                print(f"total = {dv.value} (expected 90.0)")

    # Clean up
    await resolink.remove_slot(slot=slot)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
