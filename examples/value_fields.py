"""Example showing how to create, read, and update ValueField components.

Usage:
    python examples/value_fields.py <port>

Requires a running Resonite session with ResoniteLink enabled.
Before running, generate the ValueField class:
    python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
"""

import asyncio
import sys

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.components.data import ValueField


async def main(port: int) -> None:
    """Create several ValueField components and manipulate them."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Create a slot to hold our components
    slot_resp = await resolink.add_slot_to_root(name="ValueField Examples")
    slot_id = slot_resp.entityId
    assert slot_id is not None
    print(f"Created slot: {slot_id}\n")

    # --- Parameterize ValueField with different types ---

    FloatField = ValueField[primitives.Float]
    IntField = ValueField[primitives.Int]
    StringField = ValueField[primitives.String]
    Vec3Field = ValueField[primitives.Float3]

    print(f"FloatField type: {FloatField.COMPONENT_TYPE}")
    print(f"IntField type:   {IntField.COMPONENT_TYPE}")
    print(f"StringField type: {StringField.COMPONENT_TYPE}")
    print(f"Vec3Field type:  {Vec3Field.COMPONENT_TYPE}")

    # --- Create and add a float ValueField ---
    print("\n--- Float ValueField ---")
    vf = FloatField()
    await vf.add_to_slot(resolink, slot_id)
    print(f"Added component: {vf.id}")
    print(f"Initial value: {vf.value}")

    # Update the value
    vf.value = primitives.Float(42.5)
    await vf.update(resolink)

    # Verify by refreshing from server
    await vf.refresh(resolink)
    print(f"After update:   {vf.value}")

    # --- Create a Float3 ValueField ---
    print("\n--- Float3 ValueField ---")
    vf3 = Vec3Field()
    await vf3.add_to_slot(resolink, slot_id)
    print(f"Added component: {vf3.id}")
    print(f"Initial value: {vf3.value}")

    vf3.value = primitives.Float3(x=1, y=2, z=3)
    await vf3.update(resolink)
    await vf3.refresh(resolink)
    print(f"After update:   {vf3.value}")

    # --- Auto-detect type from server data ---
    print("\n--- Auto-detect type parameter ---")
    assert vf.id is not None
    get_resp = await resolink.get_component(componentId=vf.id)
    assert get_resp.data is not None
    vf_auto = ValueField(get_resp.data)
    print(f"Class:          {type(vf_auto).__name__}")
    print(f"COMPONENT_TYPE: {vf_auto.COMPONENT_TYPE}")
    print(f"Value:          {vf_auto.value}")

    # --- Clean up ---
    await resolink.remove_slot(slotId=slot_id)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
