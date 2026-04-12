"""Debug: Inspect the built graph for the timing experiment."""

import asyncio
import json
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Build graph and dump component info."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Timing Test Debug")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Timing Test Debug")
    print(f"Created slot: {slot.id}\n")

    g = Graph()
    s = g.Space(slot)
    s.counter = s.FloatVar("counter")
    s.detected = s.FloatVar("detected")
    s.order = s.StringVar("order", value="none")

    with g.Under(slot):
        s.counter = s.counter + 1
        s.order = "W"

        with g.FireOnValueChange(value=s.counter) as e:
            with e.on_changed():
                s.detected = s.detected + 1
                s.order = "D"

    # Dump what was recorded before building
    print(f"Under records: {len(g._under_records)}")
    for i, rec in enumerate(g._under_records):
        print(f"  Under {i}: {len(rec.statements)} statements, async={rec.is_async}, event_source={rec.is_event_source}")
        for j, stmt in enumerate(rec.statements):
            print(f"    stmt {j}: {type(stmt).__name__}")

    print("\nBuilding graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # Dump all components on the slot
    full_slot = await resolink.get_slot(slot=slot.id, depth=0)
    print(f"Components on {slot.id}:")
    if full_slot and full_slot.components:
        for comp in full_slot.components:
            comp_type = comp.workerType or "?"
            # Print short type name
            short = comp_type.rsplit(".", 1)[-1] if "." in comp_type else comp_type
            print(f"  {comp.id}: {short}")
            if comp.members:
                for mname, mval in comp.members.items():
                    if hasattr(mval, 'targetId') and mval.targetId:
                        print(f"    {mname} -> {mval.targetId}")
                    elif hasattr(mval, 'value') and mval.value is not None:
                        print(f"    {mname} = {mval.value}")

    time.sleep(2.0)

    # Read results
    counter_var = s.counter
    detected_var = s.detected
    order_var = s.order

    await counter_var.refresh(resolink)
    await detected_var.refresh(resolink)
    await order_var.refresh(resolink)

    print(f"\ncounter  = {counter_var.value}")
    print(f"detected = {detected_var.value}")
    print(f"order    = {order_var.value}")

    print(f"\nSlot left for inspection: {slot.id}")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
