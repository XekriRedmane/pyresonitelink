"""Example: Imperative if-else using the Dergflux DSL.

Implements: if (x < 3) z = x + 3; else z = x - 3;

This is the Dergflux equivalent of protoflux_if_else.py, using the
Dergflux domain-specific language instead of manual component wiring.

Usage:
    python examples/dergflux_if_else.py <port>
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.components.data.dynamic import DynamicValueVariable
from pyresonitelink.dergflux import Graph


async def main(port: int) -> None:
    """Build an if-else graph using Dergflux and test it."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Delete any leftover slot from a previous run
    root = await resolink.get_slot(slot="Root", depth=1)
    assert root.data is not None
    for child in root.data.children:
        if child.name and child.name.value == "Dergflux If-Else":
            print(f"Deleting old slot {child.id}...")
            await resolink.remove_slot(slot=child)

    slot_resp = await resolink.add_slot_to_root(name="Dergflux If-Else")
    assert slot_resp.entityId is not None
    slot = workers.Slot(id=slot_resp.entityId)
    print(f"Created slot: {slot.id}\n")

    # ===================================================================
    # Build the graph using Dergflux DSL
    # ===================================================================

    g = Graph()
    s = g.Space(slot)
    s.x = g.Float("x")
    s.z = g.Float("z")

    with g.If(s.x < 3):
        s.z = s.x + 3
    with g.Else():
        s.z = s.x - 3

    print("Building graph...")
    await g.build(resolink)
    print("Graph built.\n")

    # ===================================================================
    # Test the graph
    # ===================================================================

    # Find the x ValueInput to change its value
    # For now, we need to find the DynamicValueVariable<float> for x and z
    # by refreshing from the slot
    FloatDynVar = DynamicValueVariable[primitives.Float]

    # Get x and z variables by finding them on the slot
    slot_data = await resolink.get_slot(slot=slot, depth=0)
    assert slot_data.data is not None

    x_var: DynamicValueVariable[primitives.Float] | None = None
    z_var: DynamicValueVariable[primitives.Float] | None = None

    for comp in slot_data.data.components:
        if comp.componentType == FloatDynVar.COMPONENT_TYPE:
            dv = FloatDynVar(component=comp)
            if dv.variable_name == "x":
                x_var = dv
            elif dv.variable_name == "z":
                z_var = dv

    assert x_var is not None, "Could not find x variable"
    assert z_var is not None, "Could not find z variable"

    async def read_z() -> object:
        """Read the current value of dynamic variable z."""
        assert z_var is not None
        await z_var.refresh(resolink)
        return z_var.value

    # Set initial x=2 and wait for evaluation
    x_var.value = primitives.Float(2.0)
    await x_var.update(resolink)
    print("Waiting for graph evaluation...")
    time.sleep(1.0)

    # Test 1: x=2 (< 3), expect z = 2 + 3 = 5
    z1 = await read_z()
    print(f"Test 1: x=2, z={z1} (expected 5.0)")

    # Test 2: x=5 (>= 3), expect z = 5 - 3 = 2
    x_var.value = primitives.Float(5.0)
    await x_var.update(resolink)
    time.sleep(0.5)
    z2 = await read_z()
    print(f"Test 2: x=5, z={z2} (expected 2.0)")

    # Test 3: x=3 (== 3, not < 3), expect z = 3 - 3 = 0
    x_var.value = primitives.Float(3.0)
    await x_var.update(resolink)
    time.sleep(0.5)
    z3 = await read_z()
    print(f"Test 3: x=3, z={z3} (expected 0.0)")

    # Clean up
    await resolink.remove_slot(slot=slot)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
