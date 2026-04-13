"""Example: Imperative if-else using the Dergflux DSL.

Implements: if (x < 3) z = x + 3; else z = x - 3; z += 1;

Usage:
    python examples/dergflux_if_else.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import messages, primitives
from pyresonitelink.dergflux import Graph


async def verify_connections(
    resolink: client.Client, slot_id: str,
) -> None:
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
        issues: list[str] = []
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
                # Only flag if the member is an input (not an optional output)
                if mname not in (
                    "OnNotFound", "OnFailed", "OnFalse",
                    "UpdatingUser", "SkipIfNull",
                ):
                    issues.append(mname)
                    line += f"\n    {mname} -> (null)  *** MISSING ***"
        print(line)
        if issues:
            ok = False
    if not ok:
        print("\n*** Some references are missing! ***")
    return ok


async def main(port: int) -> None:
    """Build an if-else graph using Dergflux and test it."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    old = await resolink.find_slot("Root", name="Dergflux If-Else")
    if old is not None:
        await resolink.remove_slot(slot=old)

    slot = await resolink.add_slot(name="Dergflux If-Else")
    print(f"Created slot: {slot.id}\n")

    g = Graph()
    s = g.Space(slot)
    s.x = s.FloatDynVar("x")
    s.z = s.FloatDynVar("z")
    s.tmp = s.FloatDynVar("tmp")

    with g.Under(slot):
        with g.If(s.x < 3):
            s.tmp = s.x + 3
        with g.Else():
            s.tmp = s.x - 3
        s.z = s.tmp + 1

    print("Building graph...")
    await g.build(resolink)
    print("Graph built.\n")

    print("Verifying connections:")
    await verify_connections(resolink, slot.id)

    print("\nRunning tests...")
    x_var = s.x
    z_var = s.z

    async def run_test(x_val: float) -> object:
        """Set x, wait, return z."""
        x_var.value = primitives.Float(x_val)
        await x_var.update(resolink)
        time.sleep(0.5)
        await z_var.refresh(resolink)
        return z_var.value

    z1 = await run_test(2.0)
    print(f"Test 1: x=2, z={z1} (expected 6.0)")
    z2 = await run_test(5.0)
    print(f"Test 2: x=5, z={z2} (expected 3.0)")
    z3 = await run_test(3.0)
    print(f"Test 3: x=3, z={z3} (expected 1.0)")

    print(f"\nSlot kept: {slot.id}")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
