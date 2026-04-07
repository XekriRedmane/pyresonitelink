"""Example: Imperative if-else using ProtoFlux flow nodes.

Implements: if (x < 3) z = x + 3; else z = x - 3;

Uses impulse-driven flow: an Update node fires an If node that
branches to one of two WriteDynamicValueVariable nodes depending on
the comparison result. The result is stored in a DynamicValueVariable
on the slot.

Usage:
    python examples/protoflux_if_else.py <port>

Requires generated classes (all ProtoFlux nodes and Data components
should already be generated from the bulk generation step).
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.components.data.dynamic import (
    DynamicValueVariable,
    DynamicVariableSpace,
)
from pyresonitelink.protoflux.core import (
    RefObjectInput,
    ValueInput,
    ValueObjectInput,
)
from pyresonitelink.protoflux.flow import If, Update
from pyresonitelink.protoflux.operators import ValueAdd, ValueLessThan, ValueSub
from pyresonitelink.protoflux.variables.dynamic import WriteDynamicValueVariable

# Concrete parameterized types
FloatInput = ValueInput[primitives.Float]
StringInput = ValueObjectInput[primitives.String]
SlotRef = RefObjectInput[workers.Slot]
FloatAdd = ValueAdd[primitives.Float]
FloatSub = ValueSub[primitives.Float]
FloatLessThan = ValueLessThan[primitives.Float]
FloatDynVar = DynamicValueVariable[primitives.Float]
FloatWrite = WriteDynamicValueVariable[primitives.Float]


async def main(port: int) -> None:
    """Build an if-else graph and test it with different x values."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    root = await resolink.get_slot(slotId="Root", depth=1)
    assert root.data is not None
    for child in root.data.children:
        if child.name and child.name.value == "If-Else Example":
            assert child.id is not None
            print(f"Deleting old slot {child.id}...")
            await resolink.remove_slot(slotId=child.id)

    slot_resp = await resolink.add_slot_to_root(name="If-Else Example")
    slot_id = slot_resp.entityId
    assert slot_id is not None
    print(f"Created slot: {slot_id}\n")

    # ===================================================================
    # Data layer: DynamicVariableSpace + DynamicValueVariable<float> "z"
    # ===================================================================

    space = DynamicVariableSpace()
    await space.add_to_slot(resolink, slot_id)
    print(f"DynamicVariableSpace               -> {space.id}")

    z_var = FloatDynVar(variable_name="z")
    await z_var.add_to_slot(resolink, slot_id)
    print(f"DynamicValueVariable 'z'           -> {z_var.id}")

    # ===================================================================
    # Value nodes (the "expressions")
    # ===================================================================

    # x: input value (we'll change this between tests)
    x = FloatInput(primitives.Float(2.0))
    await x.add_to_slot(resolink, slot_id)
    print(f"x (ValueInput<float>)              -> {x.id}")

    # Constant 3
    three = FloatInput(primitives.Float(3.0))
    await three.add_to_slot(resolink, slot_id)
    print(f"3 (ValueInput<float>)              -> {three.id}")

    # x < 3
    less_than = FloatLessThan(a=x, b=three)
    await less_than.add_to_slot(resolink, slot_id)
    print(f"x < 3 (ValueLessThan<float>)       -> {less_than.id}")

    # x + 3
    add = FloatAdd(a=x, b=three)
    await add.add_to_slot(resolink, slot_id)
    print(f"x + 3 (ValueAdd<float>)            -> {add.id}")

    # x - 3
    sub = FloatSub(a=x, b=three)
    await sub.add_to_slot(resolink, slot_id)
    print(f"x - 3 (ValueSub<float>)            -> {sub.id}")

    # ===================================================================
    # Helpers for WriteDynamicValueVariable: slot ref and path string
    # ===================================================================

    # RefObjectInput<Slot> pointing at our slot
    slot_ref = SlotRef(target=slot_id)
    await slot_ref.add_to_slot(resolink, slot_id)
    print(f"slot_ref (RefObjectInput<Slot>)     -> {slot_ref.id}")

    # ValueObjectInput<string> = "z"  (the dynamic variable path)
    path = StringInput(value="z")
    await path.add_to_slot(resolink, slot_id)
    print(f"path 'z' (ValueObjectInput<string>) -> {path.id}")

    # ===================================================================
    # Flow nodes (the "statements")
    # ===================================================================

    # write_true: z = x + 3
    write_true = FloatWrite(
        target=slot_ref.id, path=path.id, value=add.id,
    )
    await write_true.add_to_slot(resolink, slot_id)
    print(f"write_true (WriteDynVar<float>)     -> {write_true.id}")

    # write_false: z = x - 3
    write_false = FloatWrite(
        target=slot_ref.id, path=path.id, value=sub.id,
    )
    await write_false.add_to_slot(resolink, slot_id)
    print(f"write_false (WriteDynVar<float>)    -> {write_false.id}")

    # If node: branches impulse based on x < 3
    if_node = If(
        condition=less_than.id,
        on_true=write_true.id,
        on_false=write_false.id,
    )
    await if_node.add_to_slot(resolink, slot_id)
    print(f"if (If)                            -> {if_node.id}")

    # Update: fires every frame -> If
    update = Update(on_update=if_node.id)
    await update.add_to_slot(resolink, slot_id)
    print(f"trigger (Update)                   -> {update.id}")

    # ===================================================================
    # Test the graph
    # ===================================================================

    async def read_z() -> object:
        """Read the current value of dynamic variable z."""
        await z_var.refresh(resolink)
        return z_var.value

    print("\nWaiting for graph evaluation...")
    time.sleep(1.0)

    # Test 1: x=2 (< 3), expect z = 2 + 3 = 5
    z1 = await read_z()
    print(f"\nTest 1: x=2, z={z1} (expected 5.0)")

    # Test 2: x=5 (>= 3), expect z = 5 - 3 = 2
    x.value = primitives.Float(5.0)
    await x.update(resolink)
    time.sleep(0.5)
    z2 = await read_z()
    print(f"Test 2: x=5, z={z2} (expected 2.0)")

    # Test 3: x=3 (== 3, not < 3), expect z = 3 - 3 = 0
    x.value = primitives.Float(3.0)
    await x.update(resolink)
    time.sleep(0.5)
    z3 = await read_z()
    print(f"Test 3: x=3, z={z3} (expected 0.0)")

    # Clean up
    await resolink.remove_slot(slotId=slot_id)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
