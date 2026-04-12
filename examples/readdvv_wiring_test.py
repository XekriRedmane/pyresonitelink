"""Minimal reproduction: ReadDynamicValueVariable wiring failure.

Creates a ReadDynamicValueVariable<float> and a ValueAdd<float>,
then attempts to wire the ReadDVV as input A of the ValueAdd.

ResoniteLink rejects this with "Reference target is not compatible type"
even though ReadDynamicValueVariable implements INodeValueOutput<float>
at the ProtoFlux runtime level.

Usage:
    python examples/readdvv_wiring_test.py <port>
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink.data import primitives


async def main(port: int) -> None:
    """Demonstrate the ReadDVV wiring issue."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    slot = await resolink.add_slot(name="ReadDVV Wiring Test")
    print(f"Slot: {slot.id}\n")

    # --- Create components ---

    from pyresonitelink.protoflux.core import ValueInput
    from pyresonitelink.protoflux.variables.dynamic import (
        ReadDynamicValueVariable,
    )
    from pyresonitelink.protoflux.operators import ValueAdd

    rdvv = ReadDynamicValueVariable[primitives.Float]()
    await rdvv.add_to_slot(resolink, slot)
    print(f"ReadDynamicValueVariable<float>: {rdvv.id}")

    vi = ValueInput[primitives.Float](3.0)
    await vi.add_to_slot(resolink, slot)
    print(f"ValueInput<float>(3.0):          {vi.id}")

    add = ValueAdd[primitives.Float]()
    await add.add_to_slot(resolink, slot)
    print(f"ValueAdd<float>:                 {add.id}")

    # --- Attempt to wire ReadDVV -> ValueAdd.A ---

    print("\nWiring A -> ReadDVV, B -> ValueInput via update_references...")
    resp = await resolink.update_references(
        componentId=add.id,
        references={"A": rdvv.id, "B": vi.id},
    )
    print(f"  success: {resp.success}")
    if not resp.success:
        print(f"  error:   {resp.errorInfo}")

    # --- For comparison: wire ValueInput -> ValueAdd.A (this works) ---

    vi2 = ValueInput[primitives.Float](5.0)
    await vi2.add_to_slot(resolink, slot)

    add2 = ValueAdd[primitives.Float]()
    await add2.add_to_slot(resolink, slot)

    print("\nWiring A -> ValueInput, B -> ValueInput via update_references...")
    resp2 = await resolink.update_references(
        componentId=add2.id,
        references={"A": vi2.id, "B": vi.id},
    )
    print(f"  success: {resp2.success}")
    if not resp2.success:
        print(f"  error:   {resp2.errorInfo}")

    print(f"\nSlot left for inspection: {slot.id}")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
