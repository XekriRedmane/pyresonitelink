"""Example: Build a ProtoFlux addition graph and read the computed result.

Creates three ValueInput<float> nodes (10, 20, 5), chains two
ValueAdd<float> nodes to compute (10 + 20) + 5 = 35, then uses a
ValueDisplay<float> node to drive the result into a ValueField<float>
where it can be read back from Python.

Usage:
    python examples/protoflux_add.py <port>

Requires generated classes. Run these first:
    python -m pyresonitelink.cli.gencode <port> \
        "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<>"
    python -m pyresonitelink.cli.gencode <port> \
        "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAdd<>"
    python -m pyresonitelink.cli.gencode <port> \
        "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<>"
    python -m pyresonitelink.cli.gencode <port> \
        "[FrooxEngine]FrooxEngine.ValueField<>"
"""

import asyncio
import sys
import time

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.components.data import ValueField
from pyresonitelink.protoflux.core import ValueDisplay, ValueInput
from pyresonitelink.protoflux.operators import ValueAdd

FloatInput = ValueInput[primitives.Float]
FloatAdd = ValueAdd[primitives.Float]
FloatDisplay = ValueDisplay[primitives.Float]
FloatField = ValueField[primitives.Float]


async def main(port: int) -> None:
    """Build a ProtoFlux graph: (10 + 20) + 5 = 35, and read the result."""
    resolink = client.Client()
    await resolink.connect(port)
    print("Connected.\n")

    # Create a slot for the graph
    slot = await resolink.add_slot(name="ProtoFlux Add Example")
    print(f"Created slot: {slot.id}\n")

    # --- Build the computation graph ---

    # Three constant inputs
    input_10 = FloatInput(primitives.Float(10.0))
    input_20 = FloatInput(primitives.Float(20.0))
    input_5 = FloatInput(primitives.Float(5.0))
    await input_10.add_to_slot(resolink, slot)
    await input_20.add_to_slot(resolink, slot)
    await input_5.add_to_slot(resolink, slot)
    print(f"Input 10 -> {input_10.id}")
    print(f"Input 20 -> {input_20.id}")
    print(f"Input  5 -> {input_5.id}")

    # First add: 10 + 20
    add1 = FloatAdd(a=input_10.id, b=input_20.id)
    await add1.add_to_slot(resolink, slot)
    print(f"\nAdd1 (10 + 20) -> {add1.id}")

    # Second add: chain Add1's output with input 5
    # ValueAdd implements INodeValueOutput<float>, so its ID can be
    # used as an input reference for another ValueAdd node.
    add2 = FloatAdd(a=add1.id, b=input_5.id)
    await add2.add_to_slot(resolink, slot)
    print(f"Add2 ((10+20) + 5) -> {add2.id}")

    # --- Read the computed result ---

    # Create a ValueField<float> to receive the output
    result_field = FloatField()
    await result_field.add_to_slot(resolink, slot)

    # Wire a ValueDisplay: reads from Add2, writes to the result field.
    # The ValueDisplay._value reference needs the **member ID** of the
    # Value field inside the ValueField component, not the component ID.
    value_member = result_field.get_member("Value")
    assert value_member is not None

    display = FloatDisplay(input_=add2.id, value=value_member.id)
    await display.add_to_slot(resolink, slot)
    print(f"\nValueDisplay {display.id}:")
    print(f"  Input  -> {add2.id} (Add2 output)")
    print(f"  _value -> {value_member.id} (result field member)")

    # Give the engine a moment to evaluate the graph
    time.sleep(1.0)

    # Read the result
    await result_field.refresh(resolink)
    print(f"\nResult: {result_field.value}")
    print(f"Expected: (10 + 20) + 5 = 35")

    # Clean up
    await resolink.remove_slot(slot=slot)
    print("\nCleaned up.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1])))
