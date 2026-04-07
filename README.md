# Python bindings for [ResoniteLink](https://github.com/Yellow-Dog-Man/ResoniteLink/tree/master)

*This is a work in progress!*

pyresonitelink is a Python library for interacting with the Resonite VR platform via WebSocket. It provides async/sync interfaces for manipulating the scene graph (slots, components, assets) and building ProtoFlux visual programs programmatically.

**Python 3.13+ required.**

Because Python's native numeric types are infinite-precision integers and 64-bit floats, and Resonite has stricter types, this library uses numpy scalar types under the hood to match Resonite's C# type system precisely. Scalar aliases are provided in the `primitives` module: `primitives.Bool`, `primitives.Int`, `primitives.Long`, `primitives.Float`, `primitives.String`, etc. Composite types like `primitives.Float2`, `primitives.Float3`, `primitives.FloatQ`, `primitives.Color`, and `primitives.ColorX` are dataclasses with numpy-typed fields that coerce from plain Python `int`/`float` in their constructors.

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
import sys
from pyresonitelink import client

async def main(port: int):
    resolink = client.Client()
    await resolink.connect(port)

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

asyncio.run(main(int(sys.argv[1])))
```

See `examples/get_root_slot.py` for the simplest working example.

## Client API

The client provides keyword-argument methods for all operations. Field parameters accept raw Python values that are automatically coerced:

```python
# Strings, bools, ints coerce to FieldString, FieldBool, FieldLong
await resolink.add_slot_to_root(name="My Slot", isActive=True, orderOffset=5)

# Tuples, lists, ndarrays coerce to FieldFloat3, FieldFloatQ, etc.
await resolink.add_slot(parent=ref, position=(1, 2, 3), rotation=[0, 0, 0, 1])

# Add components using generated wrapper classes
# add_to_slot accepts a slot ID string or a Slot instance
value_field = ValueField[primitives.Float](42.5)
await value_field.add_to_slot(resolink, slot_id)

# Wire ProtoFlux nodes by passing component instances
add_node = FloatAdd(a=input_a, b=input_b)  # type-checked references
await add_node.add_to_slot(resolink, slot_id)

# Update a component's values and push to server
value_field.value = primitives.Float(99.0)
await value_field.update(resolink)

# Pull latest state from server
await value_field.refresh(resolink)
```

## Generated Components

Components were generated from a live ResoniteLink server; they do not need to be regenerated since they are part of the release. The generator produces typed Python wrapper classes with properties, `__init__` parameters, and interface inheritance for type-safe wiring.

### Generating Components

```bash
# Generate a single component and its type dependencies
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"

# Preview without writing
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>" --dry-run
```

All 3238 ProtoFlux nodes are pre-generated under `generated/protoflux/`. The generator automatically rebuilds `__init__.py` re-exports so new components are immediately importable via the short paths.

### Using Generated Components

Import shortcuts are provided so you don't need the deeply nested paths:

- `pyresonitelink.components` aliases `pyresonitelink.generated`
- `pyresonitelink.protoflux` aliases `pyresonitelink.generated.protoflux.runtimes.execution.nodes`

Each category package re-exports its classes, so you can import directly from the category:

```python
from pyresonitelink.data import primitives
from pyresonitelink.components.data import ValueField
from pyresonitelink.protoflux.core import ValueInput
from pyresonitelink.protoflux.operators import ValueAdd

FloatField = ValueField[primitives.Float]
FloatInput = ValueInput[primitives.Float]
FloatAdd = ValueAdd[primitives.Float]

# Create and add to server
value_field = FloatField(42.5)
await value_field.add_to_slot(resolink, slot_id)

# Update and refresh
value_field.value = primitives.Float(99.0)
await value_field.update(resolink)
await value_field.refresh(resolink)
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

### Calling Sync Methods

Components that expose sync methods (listed in their definition) get
generated async method wrappers:

```python
from pyresonitelink.components.audio import AudioClipPlayer

player = AudioClipPlayer()
await player.add_to_slot(resolink, slot)

await player.play(resolink)    # calls CallSyncMethod under the hood
await player.pause(resolink)
await player.stop(resolink)
```

See `examples/call_sync_method.py` for the complete example.

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
python -m pyresonitelink.cli.get_components <port> --category "/Data"

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
