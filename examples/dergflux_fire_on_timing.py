"""Experiment: When does FireOnValueChange fire?

Tests whether FireOnValueChange fires in the same frame as the write
that changed the value, or in the next frame.

The graph:
  - Update drives (gated by ran==False):
      counter = counter + 1
      order = "W"
      ran = True
  - FireOnValueChange(value=counter):
      detected = detected + 1
      order = "D"

If order ends up as "D", the detection fires AFTER the write in the
same frame (overwriting "W").  If order is "W", the detection fires
before the write or in a different frame.

Usage:
    python examples/dergflux_fire_on_timing.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import messages, primitives
from pyresonitelink.dergflux import Graph


async def verify_connections(
    resolink: client.Client, slot_id: str,
) -> bool:
    """Dump all components and flag missing references."""
    resp = await resolink.request_json(
        messages.GetSlot(slotId=slot_id, depth=0),
    )
    ok = True
    for comp in resp.get("data", {}).get("components", []):
        cid = comp["id"]
        full = await resolink.request_json(
            messages.GetComponent(componentId=cid),
        )
        data = full.get("data", {})
        ct = (data.get("componentType") or "?").rsplit(".", 1)[-1]
        line = f"  {cid}: {ct}"
        for mname, mval in (data.get("members") or {}).items():
            if not isinstance(mval, dict):
                continue
            tid = mval.get("targetId")
            val = mval.get("value")
            dtype = mval.get("$type", "")
            if tid:
                line += f"\n    {mname} -> {tid}"
            elif val is not None:
                line += f"\n    {mname} = {val}"
            elif dtype == "reference":
                if mname not in (
                    "OnNotFound", "OnFailed", "OnFalse",
                    "UpdatingUser", "SkipIfNull",
                ):
                    line += f"\n    {mname} -> (null)  *** MISSING ***"
                    ok = False
        print(line)
    return ok


async def main(port: int) -> None:
    """Build a timing test graph and observe results."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Timing Test")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Timing Test")
    print(f"Created slot: {slot.id}\n")

    g = Graph()
    s = g.Space(slot)
    s.counter = s.FloatVar("counter")
    s.detected = s.FloatVar("detected")
    s.order = s.StringVar("order", value="none")
    s.ran = s.BoolVar("ran")

    with g.Under(slot):
        # Gated update: runs once then stops
        with g.If(s.ran == False):  # noqa: E712
            s.counter = s.counter + 1
            s.order = "W"
            s.ran = True

        # Event source: fires when counter changes
        with g.FireOnValueChange(value=s.counter) as e:
            with e.on_changed():
                s.detected = s.detected + 1
                s.order = "D"

    print("Building...")
    await g.build(resolink)
    print("Built.\n")

    print("Connections:")
    ok = await verify_connections(resolink, slot.id)
    if not ok:
        print("\n*** Missing connections! ***")

    print("\nWaiting for graph to run...")
    time.sleep(1.0)

    await s.counter.refresh(resolink)
    await s.detected.refresh(resolink)
    await s.order.refresh(resolink)

    print(f"counter  = {s.counter.value}")
    print(f"detected = {s.detected.value}")
    print(f"order    = {s.order.value}")
    print()

    if s.order.value == "D":
        print("Result: FireOnValueChange fires AFTER the write in the same frame")
    elif s.order.value == "W":
        print("Result: FireOnValueChange fires in a DIFFERENT frame than the write")
    else:
        print(f"Result: Unexpected order value: {s.order.value!r}")

    if s.detected.value and s.detected.value > 0:
        print(f"FireOnValueChange DID fire ({s.detected.value} times)")
    else:
        print("FireOnValueChange did NOT fire at all!")

    print(f"\nSlot left for inspection: {slot.id}")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
