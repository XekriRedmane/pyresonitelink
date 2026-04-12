"""Debug: Boolean-gated single-run test with connection verification.

Usage:
    python examples/dergflux_debug_gate.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import messages, primitives
from pyresonitelink.dergflux import Graph


async def dump_slot(resolink: client.Client, slot_id: str) -> None:
    """Dump all components and their references on a slot."""
    resp = await resolink.request_json(messages.GetSlot(slotId=slot_id, depth=0))
    for comp in resp.get("data", {}).get("components", []):
        cid = comp["id"]
        full = await resolink.request_json(
            messages.GetComponent(componentId=cid),
        )
        data = full.get("data", {})
        ct = (data.get("componentType") or "?").rsplit(".", 1)[-1]
        print(f"  {cid}: {ct}")
        for mname, mval in (data.get("members") or {}).items():
            if not isinstance(mval, dict):
                continue
            tid = mval.get("targetId")
            val = mval.get("value")
            dtype = mval.get("$type", "")
            if tid:
                print(f"    {mname} -> {tid}")
            elif val is not None:
                print(f"    {mname} = {val}")
            elif dtype == "reference":
                print(f"    {mname} -> (null)  *** MISSING ***")


async def main(port: int) -> None:
    """Build, verify connections, then check values."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Gate Test")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Gate Test")
    print(f"Slot: {slot.id}\n")

    # -- Build --
    g = Graph()
    s = g.Space(slot)
    s.counter = s.FloatVar("counter")
    s.ran = s.BoolVar("ran")

    with g.Under(slot):
        with g.If(s.ran == False):  # noqa: E712
            s.counter = s.counter + 1
            s.ran = True

    print("Building...")
    await g.build(resolink)
    print("Built.\n")

    # -- Verify connections --
    print("Components:")
    await dump_slot(resolink, slot.id)

    # -- Check values --
    print("\nWaiting for graph to run...")
    time.sleep(0.5)

    await s.counter.refresh(resolink)
    await s.ran.refresh(resolink)
    print(f"counter = {s.counter.value} (expected 1.0)")
    print(f"ran     = {s.ran.value} (expected True)")

    await resolink.remove_slot(slot=slot)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
