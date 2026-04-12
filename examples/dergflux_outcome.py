"""Example: Using Outcome to label and react to flow paths.

Implements:
  if (x < 3) tmp = x + 3, outcome="high"
  else       tmp = x - 3, outcome="low"
  z = tmp + 1

  on outcome change:
    if outcome == "high": log = "high path"
    if outcome == "low":  log = "low path"

Usage:
    python examples/dergflux_outcome.py <port>
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
    """Dump components and flag missing references."""
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
    """Build an outcome-based graph and test it."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Outcome Test")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Outcome Test")
    print(f"Slot: {slot.id}\n")

    g = Graph()
    s = g.Space(slot)
    s.x = s.FloatVar("x")
    s.z = s.FloatVar("z")
    s.tmp = s.FloatVar("tmp")
    s.log = s.StringVar("log", value="none")

    outcome = g.Outcome(s, "result")

    with g.Under(slot):
        with g.If(s.x < 3):
            s.tmp = s.x + 3
            outcome.set("high")
        with g.Else():
            s.tmp = s.x - 3
            outcome.set("low")
        s.z = s.tmp + 1

        with outcome.on_changed() as oc:
            with g.If(oc == "high"):
                s.log = "high path"
            with g.If(oc == "low"):
                s.log = "low path"

    print("Building...")
    await g.build(resolink)
    print("Built.\n")

    print("Connections:")
    ok = await verify_connections(resolink, slot.id)
    if not ok:
        print("\n*** Missing connections! ***")

    # Test
    async def run_test(x_val: float) -> None:
        """Set x, wait, read results."""
        s.x.value = primitives.Float(x_val)
        await s.x.update(resolink)
        time.sleep(1.0)
        await s.z.refresh(resolink)
        await s.log.refresh(resolink)
        print(f"  x={x_val}: z={s.z.value}, log={s.log.value!r}")

    print("\nTests:")
    await run_test(2.0)   # < 3: z=(2+3)+1=6, log="high path"
    await run_test(5.0)   # >= 3: z=(5-3)+1=3, log="low path"
    await run_test(3.0)   # >= 3: z=(3-3)+1=1, log="low path"

    print(f"\nSlot kept: {slot.id}")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
