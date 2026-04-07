# Python bindings for [ResoniteLink](https://github.com/Yellow-Dog-Man/ResoniteLink/tree/master)

*This is a work in progress!*

pyresonitelink is a Python library for interacting with the Resonite VR platform via WebSocket. It provides async/sync interfaces for manipulating the scene graph (slots, components, assets) and building ProtoFlux visual programs programmatically.

**Python 3.13+ required.** Uses numpy for numeric types (np.float32, np.uint8, etc.) to match Resonite's C# type system precisely.

## Installation

```bash
pip install <wheel-file>
```

Check the Releases section for the latest wheel. The repo uses [uv](https://docs.astral.sh/uv/) for development:

```bash
uv sync
```

## Getting Started

Enable ResoniteLink in your Resonite dashboard under Settings. It will show the port number to use for connections.

### Quick Example

```python
import asyncio
from pyresonitelink import client

async def main():
    resolink = client.Client()
    await resolink.connect(PORT)

    # Get the root slot
    slot = await resolink.get_slot(slotId="Root", depth=1)
    print(slot)

    # Create a slot with raw Python values (auto-coerced)
    resp = await resolink.add_slot_to_root(
        name="Hello from Python",
        position=(0, 1.5, 0),
    )
    print(f"Created slot: {resp.entityId}")

    await resolink.close()

asyncio.run(main())
```

See `examples/get_root_slot.py` for the simplest working example.

## Client API

The client provides keyword-argument methods for all operations. Field parameters accept raw Python values that are automatically coerced:

```python
# Strings, bools, ints coerce to FieldString, FieldBool, FieldLong
await resolink.add_slot_to_root(name="My Slot", isActive=True, orderOffset=5)

# Tuples, lists, ndarrays coerce to FieldFloat3, FieldFloatQ, etc.
await resolink.add_slot(parent=ref, position=(1, 2, 3), rotation=[0, 0, 0, 1])

# Components can be added with type string + references
await resolink.add_component(
    containerSlotId=slot_id,
    componentType="[ProtoFluxBindings]...ValueDisplay<float>",
    references={"Input": node_id, "_value": field_id},
)

# Wire references on existing components in one call
await resolink.update_references(
    componentId=comp_id,
    references={"Input": node_id},
)
```

## Generated Components

Components are generated from a live ResoniteLink server. The generator produces typed Python wrapper classes with properties, `__init__` parameters, and interface inheritance for type-safe wiring.

### Generating Components

```bash
# Generate a single component and its type dependencies
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"

# Preview without writing
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>" --dry-run
```

All 3238 ProtoFlux nodes are pre-generated under `generated/protoflux/`.

### Using Generated Components

```python
import numpy as np
from pyresonitelink.generated.data.value_field import ValueField
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.core.value_input import ValueInput
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.operators.value_add import ValueAdd

FloatField = ValueField[np.float32]
FloatInput = ValueInput[np.float32]
FloatAdd = ValueAdd[np.float32]

# Create and add to server
vf = FloatField(42.5)
await vf.add_to_slot(resolink, slot_id)

# Update and refresh
vf.value = np.float32(99.0)
await vf.update(resolink)
await vf.refresh(resolink)
```

### Type-Safe Wiring

Generated components inherit from the Resonite interfaces they implement. This means the type checker verifies that wiring is correct:

```python
input_a = FloatInput(10.0)
input_b = FloatInput(20.0)
await input_a.add_to_slot(resolink, slot_id)
await input_b.add_to_slot(resolink, slot_id)

# Valid: ValueInput implements INodeValueOutput[T]
add = FloatAdd(a=input_a, b=input_b)  # type-checks!

# Invalid: AudioClipPlayer does not implement INodeValueOutput
add = FloatAdd(a=player)  # mypy error!
```

## ProtoFlux Examples

### Dataflow: Addition Graph

Builds `(10 + 20) + 5 = 35` using value nodes and reads the result via `ValueDisplay`:

```bash
python examples/protoflux_add.py <port>
```

### Imperative Flow: If-Else

Implements `if (x < 3) z = x + 3; else z = x - 3;` using `Update`, `If`, and `WriteDynamicValueVariable` nodes with `DynamicValueVariable` storage:

```bash
python examples/protoflux_if_else.py <port>
```

## Command-Line Tools

### `pyresonitelink.cli.dumptree`: Slot Hierarchy Dumper

```bash
python -m pyresonitelink.cli.dumptree [--depth=<0|1|-1>] [--include_components] <port> <output-file>
```

Downloads the slot hierarchy and saves it as formatted JSON. Depth: 0 = self only, 1 = immediate children, -1 = all (default).

### `pyresonitelink.cli.tree`: Interactive Tree Browser

```bash
python -m pyresonitelink.cli.tree <port>
```

![Screenshot of the tree browser](docs/tree_example.png "Example of the tree browser")

### `pyresonitelink.cli.get_components`: Component Type Browser

```bash
# List component types in a category
MSYS_NO_PATHCONV=1 python -m pyresonitelink.cli.get_components <port> --category "/Data"

# Get a component's definition
python -m pyresonitelink.cli.get_components <port> --component "[FrooxEngine]FrooxEngine.WorldLink"
```

### `pyresonitelink.cli.gencode`: Component Code Generator

```bash
# Generate a component wrapper class from a live server
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"

# Generic components use <>
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
```

## Running Tests

Tests require a running Resonite session with ResoniteLink enabled:

```bash
pytest --port=<resonite-link-port> tests/
pytest --port=<port> tests/test_values.py::test_update_component -s
```

Type checking:

```bash
mypy src/
```

## Known Issues

- First WebSocket connection fails with `ConnectionClosedError`. Workaround is implemented in the client (automatic retry).
- On Git Bash (MSYS2), paths starting with `/` get mangled to Windows paths. Use `MSYS_NO_PATHCONV=1` when passing category paths.
