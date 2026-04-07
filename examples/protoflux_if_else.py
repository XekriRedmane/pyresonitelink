"""Example: Imperative if-else using ProtoFlux flow nodes.

Implements: if (x < 3) z = x + 3; else z = x - 3;

Uses impulse-driven flow: a OnePerFrame node fires an If node that
branches to one of two WriteDynamicValueVariable nodes depending on
the comparison result. The result is stored in a DynamicValueVariable
on the slot.

Usage:
    python examples/protoflux_if_else.py <port>

Requires generated classes (all ProtoFlux nodes should already be
generated from the bulk generation step).
"""

import asyncio
import sys
import time

import numpy as np

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import messages
from pyresonitelink.data import workers

PFX = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes"


async def add_node(
    resolink: client.Client,
    slot_id: str,
    component_type: str,
    **refs: str,
) -> str:
    """Add a ProtoFlux node and optionally wire references.

    Args:
        resolink: Connected client.
        slot_id: Slot to create the component in.
        component_type: Full Resonite component type.
        **refs: Member name -> target ID pairs to wire.

    Returns:
        The new component ID.
    """
    resp = await resolink.add_component(
        containerSlotId=slot_id,
        componentType=component_type,
    )
    assert resp.entityId is not None, f"Failed to add {component_type}"
    if refs:
        await resolink.update_references(
            componentId=resp.entityId,
            references=refs,
        )
    return resp.entityId


async def set_field(
    resolink: client.Client,
    comp_id: str,
    member_name: str,
    field_value: fields.FieldFloat | fields.FieldString | fields.FieldBool,
) -> None:
    """Set a field member's value on an existing component.

    Args:
        resolink: Connected client.
        comp_id: Component ID.
        member_name: Name of the member to update.
        field_value: New field value (must have .id set after assignment).
    """
    get = await resolink.get_component(componentId=comp_id)
    assert get.data is not None
    existing = get.data.members[member_name]
    field_value.id = existing.id
    get.data.members[member_name] = field_value
    await resolink.update_component(data=get.data)


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
            print(f"Deleting old slot {child.id}...")
            await resolink.remove_slot(slotId=child.id)

    slot_resp = await resolink.add_slot_to_root(name="If-Else Example")
    slot_id = slot_resp.entityId
    assert slot_id is not None
    print(f"Created slot: {slot_id}\n")

    # ===================================================================
    # Data layer: DynamicVariableSpace + DynamicValueVariable<float> "z"
    # ===================================================================

    await resolink.add_component(
        containerSlotId=slot_id,
        componentType="[FrooxEngine]FrooxEngine.DynamicVariableSpace",
    )

    dv_resp = await resolink.add_component(
        containerSlotId=slot_id,
        componentType="[FrooxEngine]FrooxEngine.DynamicValueVariable<float>",
    )
    dv_id = dv_resp.entityId
    assert dv_id is not None
    await set_field(resolink, dv_id, "VariableName", fields.FieldString(value="z"))
    print(f"DynamicValueVariable 'z': {dv_id}")

    # ===================================================================
    # Value nodes (the "expressions")
    # ===================================================================

    # x: input value (we'll change this between tests)
    x_id = await add_node(resolink, slot_id, f"{PFX}.ValueInput<float>")
    await set_field(resolink, x_id, "Value", fields.FieldFloat(value=np.float32(2.0)))
    print(f"x (ValueInput<float>)              -> {x_id}")

    # Constant 3
    three_id = await add_node(resolink, slot_id, f"{PFX}.ValueInput<float>")
    await set_field(resolink, three_id, "Value", fields.FieldFloat(value=np.float32(3.0)))
    print(f"3 (ValueInput<float>)              -> {three_id}")

    # x < 3
    lt_id = await add_node(
        resolink, slot_id, f"{PFX}.Operators.ValueLessThan<float>",
        A=x_id, B=three_id,
    )
    print(f"x < 3 (ValueLessThan<float>)       -> {lt_id}")

    # x + 3
    add_id = await add_node(
        resolink, slot_id, f"{PFX}.Operators.ValueAdd<float>",
        A=x_id, B=three_id,
    )
    print(f"x + 3 (ValueAdd<float>)            -> {add_id}")

    # x - 3
    sub_id = await add_node(
        resolink, slot_id, f"{PFX}.Operators.ValueSub<float>",
        A=x_id, B=three_id,
    )
    print(f"x - 3 (ValueSub<float>)            -> {sub_id}")

    # ===================================================================
    # Helpers for WriteDynamicValueVariable: slot ref and path string
    # ===================================================================

    # RefObjectInput<Slot> pointing at our slot
    slot_ref_id = await add_node(
        resolink, slot_id,
        f"{PFX}.RefObjectInput<[FrooxEngine]FrooxEngine.Slot>",
        Target=slot_id,
    )
    print(f"slot_ref (RefObjectInput<Slot>)     -> {slot_ref_id}")

    # ValueObjectInput<string> = "z"  (the dynamic variable path)
    path_id = await add_node(
        resolink, slot_id, f"{PFX}.ValueObjectInput<string>",
    )
    await set_field(resolink, path_id, "Value", fields.FieldString(value="z"))
    print(f"path 'z' (ValueObjectInput<string>) -> {path_id}")

    # ===================================================================
    # Flow nodes (the "statements")
    # ===================================================================

    wdvv_type = (
        f"{PFX}.FrooxEngine.Variables.WriteDynamicValueVariable<float>"
    )

    # write_true: z = x + 3
    wt_id = await add_node(
        resolink, slot_id, wdvv_type,
        Target=slot_ref_id, Path=path_id, Value=add_id,
    )
    print(f"write_true (WriteDynVar<float>)     -> {wt_id}")

    # write_false: z = x - 3
    wf_id = await add_node(
        resolink, slot_id, wdvv_type,
        Target=slot_ref_id, Path=path_id, Value=sub_id,
    )
    print(f"write_false (WriteDynVar<float>)    -> {wf_id}")

    # If node: branches impulse based on x < 3
    if_id = await add_node(
        resolink, slot_id, f"{PFX}.If",
        Condition=lt_id, OnTrue=wt_id, OnFalse=wf_id,
    )
    print(f"if (If)                            -> {if_id}")

    # Update: fires every frame -> If
    update_id = await add_node(
        resolink, slot_id, f"{PFX}.Actions.Update",
        OnUpdate=if_id,
    )
    print(f"trigger (Update)                   -> {update_id}")

    # ===================================================================
    # Test the graph
    # ===================================================================

    async def read_z() -> float:
        """Read the current value of dynamic variable z."""
        get = await resolink.get_component(componentId=dv_id)
        assert get.data is not None
        return get.data.members["Value"].value

    print("\nWaiting for graph evaluation...")
    time.sleep(1.0)

    # Test 1: x=2 (< 3), expect z = 2 + 3 = 5
    z1 = await read_z()
    print(f"\nTest 1: x=2, z={z1} (expected 5.0)")

    # Test 2: x=5 (>= 3), expect z = 5 - 3 = 2
    await set_field(resolink, x_id, "Value", fields.FieldFloat(value=np.float32(5.0)))
    time.sleep(0.5)
    z2 = await read_z()
    print(f"Test 2: x=5, z={z2} (expected 2.0)")

    # Test 3: x=3 (== 3, not < 3), expect z = 3 - 3 = 0
    await set_field(resolink, x_id, "Value", fields.FieldFloat(value=np.float32(3.0)))
    time.sleep(0.5)
    z3 = await read_z()
    print(f"Test 3: x=3, z={z3} (expected 0.0)")

    # Clean up
    await resolink.remove_slot(slotId=slot_id)
    print("\nCleaned up.")
    await resolink.close()
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
