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
    new_slot = await resolink.add_slot(
        name="Hello from Python",
        position=(0, 1.5, 0),
    )
    print(f"Created slot: {new_slot.id}")

    await resolink.close()

asyncio.run(main(int(sys.argv[1])))
```

See `examples/get_root_slot.py` for the simplest working example.

## Client API

The client provides keyword-argument methods for all operations. Field parameters accept raw Python values that are automatically coerced:

```python
# Strings, bools, ints coerce to FieldString, FieldBool, FieldLong
await resolink.add_slot(name="My Slot", isActive=True, orderOffset=5)

# Tuples, lists, ndarrays coerce to FieldFloat3, FieldFloatQ, etc.
await resolink.add_slot(parent=some_slot, position=(1, 2, 3), rotation=[0, 0, 0, 1])

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

### Convenience Methods

The client provides high-level methods that combine multiple operations:

#### Slots

```python
# Create a slot (parent defaults to Root)
slot = await resolink.add_slot(name="My Slot")
slot = await resolink.add_slot(parent=other_slot, name="Child")

# Find a slot by name or tag (uses ProtoFlux search nodes internally)
slot = await resolink.find_slot("Root", name="SpawnPoint")
slot = await resolink.find_slot("Root", tag="audio-player")
slot = await resolink.find_slot("Root", name="spawn", match_substring=True, ignore_case=True, depth=5)

# Remove a slot
await resolink.remove_slot(slot=slot)
```

`add_slot` returns a `Slot` directly (raises `RuntimeError` on failure).
`find_slot` returns `Slot | None`, using temporary ProtoFlux search nodes for fast deep searches.

#### Audio

```python
# Import an audio file and create a StaticAudioClip on a slot (one call)
clip = await resolink.create_audio_clip(slot, "path/to/sound.wav")

# Import multiple audio files into an AssetMultiplexer (one call)
mux = await resolink.create_audio_multiplexer(slot, [
    "sounds/notification.wav",
    "sounds/ptink.wav",
    "sounds/tikatak.wav",
])
# mux.Index selects which clip is active (0, 1, 2)
```

Audio imports are **content-addressed and idempotent** — importing the same file twice returns the same URL without duplication. Safe to call on every script run.

#### Components

```python
# Add a generated component to a slot
value_field = ValueField[primitives.Float](42.5)
await value_field.add_to_slot(resolink, slot)

# Update values and push to server
value_field.value = primitives.Float(99.0)
await value_field.update(resolink)

# Pull latest state from server
await value_field.refresh(resolink)
```

## Generated Components

Components are generated from a live ResoniteLink server. The generator produces typed Python wrapper classes with properties, `__init__` parameters, and interface inheritance for type-safe wiring. Documentation from the [Resonite Wiki](https://wiki.resonite.com) is automatically scraped and merged into the generated class docstrings, so `help()` and IDE hover tooltips show descriptions for each component, its fields, inputs, and outputs.

All ~4800 components are pre-generated and included in the release. They do not need to be regenerated unless you want to pick up new Resonite components or updated wiki documentation.

### Generating Components

```bash
# Generate a single component and its type dependencies
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"

# Regenerate ALL components (discovers all types from the server)
python -m pyresonitelink.cli.gencode <port> --all

# Preview without writing
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>" --dry-run
```

The `--all` flag recursively walks every component category on the server, scrapes wiki documentation for each component, and regenerates all wrapper classes. Internal ProtoFlux proxy types (~3066 CoreNodes) are skipped automatically. The generator rebuilds `__init__.py` re-exports so new components are immediately importable via the short paths.

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

## ProtoFlux

ProtoFlux is Resonite's node-based visual programming language. See the
[ProtoFlux README](src/pyresonitelink/protoflux/README.md) for detailed
documentation on value chains, impulse chains, execution contexts, and
the three variable types (Local, Store, Data Model Store).

### Examples

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

## Dergflux DSL

Dergflux is a Pythonic domain-specific language for building ProtoFlux graphs.
Instead of manually wiring dozens of components, write Python expressions and
control flow:

```python
from pyresonitelink.dergflux import Graph

g = Graph()
s = g.Space(slot)
s.x = s.FloatVar("x")
s.z = s.FloatVar("z")

with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3
    with g.Else():
        s.z = s.x - 3

await g.build(resolink)
```

After `g.build()`, access built variables directly from the Space:

```python
await g.build(resolink)

# s.x is now the DynamicValueVariable component, not an ExprProxy
x_var = s.x
await x_var.refresh(resolink)
print(x_var.value)
```

Key features:
- **Expressions**: `+`, `-`, `*`, `/`, `%`, `**`, `abs()`, comparisons, bitwise `&`/`|`/`^`/`~`/`<<`/`>>`
- **Math functions**: `sin`, `cos`, `sqrt`, `lerp`, `clamp`, `min_`, `max_`, and [more](src/pyresonitelink/dergflux/dergflux.md#math-functions)
- **Flow control**: `g.If`/`g.Else`, `g.For`, `g.While`, `g.Range`
- **Triggers**: `g.Under(slot)` (Update every frame), `g.Under(slot, trigger="tag")` (named impulse), `g.Under(slot, trigger=("tag", type))` (with value)
- **Bindings**: `g.Bind(s.x, component, "Field")` — permanently bind a variable or expression to a component field
- **Action nodes**: `g.RaycastOne(...)`, `g.PlayOneShotAndWait(...)`, `g.SlotChildrenEvents(...)`, or define custom actions with `ActionDef`
- **Auto-bridging**: pass components directly to action inputs (e.g. `clip=my_clip`) — the builder creates `RefObjectInput` bridges automatically

See the [Dergflux reference](src/pyresonitelink/dergflux/dergflux.md) for the full API.

See also: [Dynamic Variables](src/pyresonitelink/dergflux/dynamic_variables.md) | [Sync vs Async Flow](src/pyresonitelink/dergflux/async_flow.md)

### Dergflux Examples

```bash
python examples/dergflux_if_else.py <port>                    # If/Else with continuation
python examples/dergflux_for.py <port>                         # For loop with OnStart/OnIterate
python examples/dergflux_play_one_shot_and_wait.py <port>      # Async audio playback
python examples/dergflux_play_sequence.py <port>               # Multiplexer + For + PlayOneShotAndWait
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
