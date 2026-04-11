"""Example: Event-driven logic using Dergflux Fire nodes.

Creates a slot with three dynamic variables:
- x (Float): a value that can be changed externally
- flag (Bool): a boolean that can be toggled externally
- log (String): a log of events that have fired

Three event sources monitor the variables:
- FireOnTrue(flag) writes "flag became true" to log
- FireOnFalse(flag) writes "flag became false" to log
- FireOnValueChange(x) increments a change counter

To test: open an inspector on the slot in Resonite, change
the x or flag dynamic variables, and watch log/change_count update.

Usage:
    python examples/dergflux_fire_events.py <port>
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Build event-driven graphs using Dergflux Fire nodes."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Dergflux Fire Events")
    if old is not None:
        print(f"Deleting old slot {old.id}...")
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Dergflux Fire Events")
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Build the graph
    # ===================================================================

    g = Graph()

    s = g.Space(slot)
    s.x = s.FloatVar("x", value=0.0)
    s.flag = s.BoolVar("flag", value=False)
    s.log = s.StringVar("log", value="waiting")
    s.change_count = s.IntVar("change_count", value=0)

    with g.Under(slot):
        # FireOnTrue: fires once when flag transitions from false to true
        with g.FireOnTrue(condition=s.flag) as e:
            with e.on_changed():
                s.log = "flag became true"

        # FireOnFalse: fires once when flag transitions from true to false
        with g.FireOnFalse(condition=s.flag) as e:
            with e.on_changed():
                s.log = "flag became false"

        # FireOnValueChange: fires whenever x changes
        with g.FireOnValueChange(value=s.x) as e:
            with e.on_changed():
                s.change_count = s.change_count + 1

    print("Building graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # ===================================================================
    # Verify initial state
    # ===================================================================

    log_var = s.log
    count_var = s.change_count
    await log_var.refresh(resolink)
    await count_var.refresh(resolink)
    print(f"Initial log: {log_var.value}")
    print(f"Initial change_count: {count_var.value}")

    print("\nSlot left in place for inspection.")
    print("Open an inspector on the slot and try:")
    print("  - Toggle the 'flag' variable to see log change")
    print("  - Change the 'x' variable to see change_count increment")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
