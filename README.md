# Python bindings for [ResoniteLink](https://github.com/Yellow-Dog-Man/ResoniteLink/tree/master)

*This is a work in progress!*

pyresonitelink is a Python library for interacting with the Resonite VR platform via WebSocket. It provides async/sync interfaces for manipulating the scene graph (slots, components, assets) and building ProtoFlux visual programs programmatically.

**Python 3.13+ required.**

Because Python's native numeric types are infinite-precision integers and 64-bit floats, and Resonite has stricter types, this library uses numpy scalar types under the hood to match Resonite's C# type system precisely. Scalar aliases are provided in the `primitives` module: `primitives.Bool`, `primitives.Int`, `primitives.Long`, `primitives.Float`, `primitives.String`, etc. `primitives.DateTime` and `primitives.TimeSpan` are Python's `datetime.datetime` and `datetime.timedelta`. ResoniteLink sends both as strings, which the field classes convert. Composite types like `primitives.Float2`, `primitives.Float3`, `primitives.FloatQ`, `primitives.Color`, and `primitives.ColorX` are dataclasses with numpy-typed fields that coerce from plain Python `int`/`float` in their constructors. Spherical harmonics (`primitives.SphericalHarmonicsL1` through `L4`) are generic in Resonite, so each of their coefficients is a field instance such as `fields.FieldColorX`, which carries its own type.

## Installation

```bash
pip install <wheel-file>
```

Check the Releases section for the latest wheel. The repo uses [uv](https://docs.astral.sh/uv/) for development:

```bash
uv sync
```

The repository stores every text file with LF line endings. A pre-commit hook refuses commits that would add CRLF endings or change only a file's line endings. Enable it once in each clone:

```bash
git config core.hooksPath .githooks
```

## Getting Started

ResoniteLink runs inside one world. Enable it with the Enable ResoniteLink button in the dashboard's Session tab, which shows the port to connect to. The [AutoResoLink](https://github.com/XekriRedmane/AutoResoLink) mod can also start it for you whenever you create a new world.

### Finding a Session

Every world running ResoniteLink announces its name and port on the LAN every 10 seconds, so a program can find the port without being told it:

```python
from pyresonitelink import discovery

session = await discovery.find_session()             # the only running session
session = await discovery.find_session("My World")   # or the one with this world name
await resolink.connect(session.port)
```

`discovery.discover_sessions()` returns every session it hears. Both functions listen for 11 seconds by default, which is long enough to hear each session once.

### Quick Example

```python
import asyncio
import sys
from pyresonitelink import client

async def main(port: int):
    resolink = client.Client()
    await resolink.connect(port)

    # Get the root slot
    slot = await resolink.get_slot("Root", depth=1)
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

# Change some of a slot's fields
await resolink.update_slot(workers.Slot(
    id=slot.id, position=fields.FieldFloat3(value=primitives.Float3(0, 1, 0)),
))

# A slot's position, rotation, and scale in world space
head = await resolink.get_global_transform(head_slot)
```

`add_slot` returns a `Slot` directly (raises `RuntimeError` on failure).
`find_slot` returns `Slot | None`, using temporary ProtoFlux search nodes for fast deep searches.
`update_slot` changes only the fields that are set, and its response's `success` is true if the update was applied. The server returns an error for a second member ID for a field that already has one, and every field constructed in Python has a fresh random ID, so `update_slot` sends each field with an empty ID, which the server doesn't associate with anything.

A slot's position, rotation, and scale are relative to its parent, both in `add_slot` and in slot data. `get_global_transform` returns a `transforms.Transform` relative to the world. Any slot's transform can change in every engine update, so the ancestors' transforms can't be read one request at a time and combined. Instead, `get_global_transform` adds a temporary probe slot under Root with CopyGlobalTransform and CopyGlobalScale components, which copy the slot's world transform to the probe within one engine update. It reads the probe until the copy has happened and then deletes it, which takes about 60 ms at 60 FPS.

`pyresonitelink.data.transforms` does the arithmetic and needs no server:

```python
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms

# +Z is forward in Resonite
forward = transforms.rotate(head.rotation, primitives.Float3(0, 0, 1))

# The transform of a child in its grandparent's space, and back again
world = transforms.compose(parent, local)
local = transforms.relative_to(parent, world)

# Rotation b followed by rotation a, and the rotation that undoes q
q = transforms.multiply(a, b)
q_inv = transforms.inverse(q)
```

Use `relative_to` to find the local transform that puts a new child slot at a given place in the world. `compose` multiplies the scales component-wise, which is exact unless a non-uniform parent scale meets a rotated child. In that case the true result is sheared, and a `Transform` can't represent shear.

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

#### Importing Assets from Data

Textures, cubemaps, meshes, and audio can be imported from numpy arrays as well as from files. Each call returns an `AssetData` whose `assetURL` goes in the `URL` field of a static provider such as `StaticTexture2D`.

```python
import numpy as np
from pyresonitelink.data import mesh

# A texture from an RGBA image, shaped (height, width, 4) as uint8
asset = await resolink.import_texture_2d_raw_data(pixels)

# A cubemap from six faces, shaped (6, size, size, 4), in the order
# +X, +Y, +Z, -X, -Y, -Z
asset = await resolink.import_cubemap_raw_data([faces])

# A mesh from vertex arrays, with any of normals, tangents, colors, UVs,
# bone weights, and blendshapes
asset = await resolink.import_mesh_raw_data(
    positions,                                 # (V, 3)
    [mesh.RawTriangles(triangles)],            # (N, 3) vertex indices
    normals=normals,
    uvs=[uv0],                                 # one (V, 2) array per channel
)

# Audio from samples from -1 to 1, shaped (count,) or (count, channels)
asset = await resolink.import_audio_clip_raw_data(samples, 48000)
```

`pyresonitelink.utils.glb` reads the arrays for `import_mesh_raw_data` from a glTF file (.glb or .gltf), using [trimesh](https://trimesh.org) to parse it. `read_node` reads a node and its descendants as one `glb.Mesh`, with one set of vertices and a submesh for each primitive, and applies the descendants' transforms. glTF is right-handed and Resonite is left-handed, so `to_resonite` negates X and swaps two corners of each triangle to keep the front faces in front, as Resonite's own model importer does. `transform` applies any other linear or affine transform.

The submeshes come in trimesh's order, which differs from the file's, so `m.nodes` and `m.materials` give the node and the material of each one. glTF has no flag for a hidden node, so `read_node` takes a `skip` function, which is given each descendant's name and extras (`glb.node_extras`) and leaves out the descendants it returns True for, together with their subtrees. Some trimesh methods replace the file's normals, and the module docstring lists those and the other differences between trimesh and Resonite. Only the first UV channel is read, and tangents, colors, skins, and morph targets aren't read yet. Each material's `baseColorTexture` is a PIL image.

```python
from pyresonitelink.data import mesh
from pyresonitelink.utils import glb

m = glb.to_resonite(glb.read_node(glb.load("model.glb"), "Body"))
asset = await resolink.import_mesh_raw_data(
    m.positions,
    [mesh.RawTriangles(t) for t in m.submeshes],  # one per m.nodes entry
    normals=m.normals,
    uvs=[] if m.uvs is None else [m.uvs],
)
```

`examples/textured_card.py` places `examples/TexturedCard.glb`, a paper card with transparent decals, in front of the user. It uploads each material's texture with `import_texture_2d_raw_data` and gives each submesh an unlit material with the file's blend mode. `examples/make_textured_card.py` writes the card, including hidden nodes marked in their extras, which the example leaves out with `skip`.

The payload builders behind these calls are also available as classmethods, such as `messages.ImportMeshRawData.from_arrays`. The client checks a payload's size against its message before sending it, because the server rejects a payload of the wrong size with a less helpful error. `import_texture_2d_raw_data_hdr`, `import_cubemap_raw_data_hdr`, `import_cubemap_files`, and `import_mesh_json` cover the remaining import messages. Two of the import messages run into server bugs, which are listed under [Known Issues](#known-issues).

#### Batches

`data_model_operation_batch` sends slot and component operations and sync method calls in one message. The server runs them in order within one engine update, so nothing else in the world sees the objects halfway through, and an operation can refer to an object that an earlier operation in the same batch created.

```python
from pyresonitelink.data import fields, members, messages, workers

batch = await resolink.data_model_operation_batch([
    messages.AddSlot(data=workers.Slot(
        id=child_id,
        parent=members.Reference(targetId=slot.id),
        name=fields.FieldString(value="Child"),
    )),
    messages.GetSlot(slotId=slot.id, depth=1),
])
for response in batch.responses:
    print(type(response).__name__, response.success)
```

Each operation gets its own response, in order. The batch's own `success` only says that the batch was processed, so check each response.

Don't build a ProtoFlux graph in one batch. A node wired in the same engine update that created it can end up with every reference in place and still never run, which is why the Dergflux builder pauses between creating nodes and wiring them.

#### Session and Reflection

```python
session = await resolink.request_session_data()
print(session.resoniteVersion, session.resoniteLinkVersion)

# Any type, including interfaces and abstract classes
defn = await resolink.get_type_definition("[FrooxEngine]FrooxEngine.IAssetProvider<>")
# The generic type definition behind a concrete generic type
defn = await resolink.get_generic_type_definition("[FrooxEngine]FrooxEngine.ValueField<float>")
# An enum's names and values
enum = await resolink.get_enum_definition("[FrooxEngine]FrooxEngine.BlendMode")
# A sync object, such as UserRef
sync = await resolink.get_sync_object_definition("[FrooxEngine]FrooxEngine.UserRef")
```

The definitions decode to the dataclasses in `pyresonitelink.data.reflection`, and the members of a component or sync object definition decode to `FieldDefinition`, `ReferenceDefinition`, and the other member definition classes.

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

The `--all` flag recursively walks every component category on the server, scrapes wiki documentation for each component, and regenerates all wrapper classes. The category walk doesn't list every component, so `--all` also regenerates every component that already has a generated module. Internal ProtoFlux proxy types (~3066 CoreNodes) are skipped automatically. The generator rebuilds the `__init__.py` re-exports of every generated package, so new components are immediately importable via the short paths.

A component that references another component, such as a `TextRenderer`, imports that class only for type checking. This keeps two components that reference each other from importing each other at runtime.

#### Names of components that share a name

Resonite treats `X`, `X<T>`, and `X<T1, T2>` as different components, but in Python they'd all be the class `X` in one module, so the generator renames all but one:

| Resonite | Python | Rule |
|---|---|---|
| `ValueWrite<T>` | `ValueWrite` | The generic form with the fewest parameters keeps the name. |
| `ValueWrite<C, T>` | `ValueWriteWithContext` | A longer form adds `With` and its extra parameters, where `C` (the ProtoFlux context) is `Context` and `TValue` is `Value`. |
| `FireOnLocalTrue` | `FireOnLocalTrue` | Of a non-generic and a generic form where one derives from the other, the derived one keeps the name. |
| `FireOnLocalTrue<C>` | `FireOnLocalTrueBase` | The one it derives from gets `Base`. |
| `UIX.Slider` | `Slider` | When neither derives from the other, the non-generic one keeps the name. |
| `UIX.Slider<T>` | `SliderOf` | The generic one gets `Of`, as in `SliderOf[primitives.Float]`. |
| `Strings.Characters.NewLine` | `CharactersNewLine` | A component whose module already belongs to a namesake in another namespace gets the namespace that tells it apart. |

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

A component that drives a slot's transform, such as `Spinner`, refers to the slot's field member and not to the slot. The member ID comes from the slot's data, as in `(await resolink.get_slot(slot)).data.rotation.id`. See `examples/spinning_cube.py`, which builds a cube from a `BoxMesh`, a `PBS_Metallic` material, and a `MeshRenderer`, places it in front of the user's head, and turns it with a `Spinner` without any ProtoFlux.

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
add = FloatAdd(a=player)  # type error!
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

# Arguments are passed as plain values or component instances
await output.exlude_user(resolink, user=user_id)
```

The server only accepts method arguments tagged with their type, so a generated wrapper sends a float argument as a `FieldFloat`, and a reference argument as a `members.DataReference`. If you call `call_method` yourself, pass arguments in that form. A component or slot instance is converted to a reference for you. ResoniteLink has no way to pass an enum or a struct, so a method that takes one can't be called.

The client's `call_sync_method` and `call_static_sync_method` do the same for any target. They return a `MethodResult` whose `result` holds the returned value as a field, such as a `FieldInt`, or as a `members.DataReference` for a returned object.

```python
from pyresonitelink.data import fields

result = await resolink.call_sync_method(root, "RemoveChildrenObjectRoots")
print(result.success, result.result.value)

await resolink.call_sync_method(
    clip, "AdjustVolume", {"ratio": fields.FieldFloat(value=np.float32(0.5))},
)
```

As of Resonite 2026.9.18.82, a method marked `isAsync` in its definition, such as `AdjustVolume`, fails on the server after it has started, and most static methods fail before they start. Both are listed under [Known Issues](#known-issues).

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
s.x = s.FloatDynVar("x")
s.z = s.FloatDynVar("z")

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
- **Math functions**: `sin`, `cos`, `sqrt`, `clamp`, `min_`, `max_`, `lerp`, `smoothstep`, and [more](src/pyresonitelink/dergflux/dergflux.md#math-functions)
- **Rotations**: `math.axis_angle(axis, degrees)` and `math.from_euler(angles)` give a `FloatQ` or `DoubleQ` ([details](src/pyresonitelink/dergflux/dergflux.md#rotations))
- **Type conversions**: numeric operands widen automatically as in C#, so `float_var + int_var` works, and narrowing takes `math.to_int(x)` or `math.convert(x, primitives.Int)` ([details](src/pyresonitelink/dergflux/dergflux.md#type-conversions))
- **Time and dates**: `time.utc_now()`, `time.world_time()`, `time.hours(2)`, `now.year`, `span.total_seconds`, and DateTime/TimeSpan arithmetic, with Python `datetime` and `timedelta` values ([details](src/pyresonitelink/dergflux/dergflux.md#time-and-dates))
- **Flow control**: `g.If`/`g.Else`, `g.For`, `g.While`, `g.Range`
- **Triggers**: `g.Under(slot)` (Update every frame), `g.Under(slot, trigger="tag")` (named impulse), `g.Under(slot, trigger=("tag", type))` (with value)
- **Bindings**: `g.Bind(s.x, component, "Field")` permanently binds a variable or expression to a component field, and `g.Bind(expr, slot, "Rotation")` to a slot's Position, Rotation, Scale, IsActive, or OrderOffset
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
python examples/dergflux_number_wheel.py [port]                # A counting drum, driven by a binding
```

`dergflux_number_wheel.py` is `number_wheel.py` with its ProtoFlux graph written in Dergflux. Both place a ten-sided number drum from `examples/NumberDrum.glb` 5 m in front of the user's head and turn it to the next digit every second.

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

Tests require a running Resonite session with ResoniteLink enabled. If you leave out `--port`, the tests find the session from its LAN announcement, and `--session` picks one by world name when more than one is running:

```bash
pytest tests/
pytest --session="My World" tests/
pytest --port=<resonite-link-port> tests/
pytest --port=<port> tests/test_values.py::TestValues::test_update_component -s
```

Type checking:

```bash
pyrefly check
```

## Known Issues

- First WebSocket connection fails with `ConnectionClosedError`. Workaround is implemented in the client (automatic retry).
- On Git Bash (MSYS2), paths starting with `/` get mangled to Windows paths. Use `MSYS_NO_PATHCONV=1` when passing category paths.

The following are bugs in ResoniteLink as of Resonite 2026.9.18.82. The tests in `tests/test_link_messages.py` check for each of the first four, so a fix shows up as a failing test.

- A sync method whose definition has `isAsync` set, such as `StaticMesh.RecalculateNormals`, fails with "Type not supported: Task`1". The server has already started the method, so its effect still happens. This covers nearly all asset processing methods.
- A static sync method declared with `[SyncMethod(typeof(Delegate))]`, such as `MeterTool.FilterUsers`, fails with "Type must derive from Delegate" before it runs. Five of the seven static methods are declared this way.
- `import_mesh_json` fails for any vertex with UV coordinates. `import_mesh_raw_data` handles UVs.
- `import_cubemap_file_with_regions` always fails with "The supplied Bitmap2D's don't all have mipmaps". `import_cubemap_files` works when the six face images are the same size.
- `get_component_type_list("*")` returns nothing, although the [doc comment on `GetComponentTypeList.CategoryPath`](https://github.com/Yellow-Dog-Man/ResoniteLink/blob/067afad3d1977b3806cbad077f4e8a534f56f451/ResoniteLink/Models/Messages/Reflection/GetComponentDefinitionList.cs#L10-L15) says that it lists every component.
- `get_enum_definition` with a name that doesn't resolve fails with a NullReferenceException message.
- `get_component_definition` fails for the five components with a `SyncLinear` or `SyncCurve` member, and `get_component` leaves those members out.
