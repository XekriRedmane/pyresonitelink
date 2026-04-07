# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pyresonitelink is a Python library providing bindings for ResoniteLink, enabling Python programs to interact with the Resonite VR platform via WebSocket. It provides async/sync interfaces for manipulating the scene graph (slots, components, assets).

**Python 3.13+ required.** Uses numpy for numeric types (np.float32, np.uint8, etc.) to match Resonite's C# type system precisely.

## META - MAINTAINING THIS DOCUMENT

### Writing Effective Guidelines

When adding new rules to this document, follow these principles:

**Core Principles (Always Apply):**

1. Use absolute directives - Start with "NEVER" or "ALWAYS"
2. Lead with why - Explain the problem before the solution (1-3 bullets max)
3. Be concrete - Include actual commands/code
4. Minimize examples - One clear point per code block
5. Bullets over paragraphs - Keep explanations concise

**Optional Enhancements (Use Strategically):**

- Bad/Good examples: Only when the antipattern is subtle
- "Warning Signs" section: Only for gradual mistakes
- "General Principle": Only when abstraction is non-obvious

**Anti-Bloat Rules:**

- Don't add "Warning Signs" to obvious rules
- Don't show bad examples for trivial mistakes
- Don't write paragraphs explaining what bullets can convey

## Development Commands

The repo uses a Python venv maintained by uv.

```bash
# Install dependencies (uses uv)
uv sync

# Run tests (requires running ResoniteLink in Resonite - enable in dashboard Settings)
pytest --port=<resonite-link-port> tests/

# Run a single test
pytest --port=<port> tests/test_values.py::test_update_component -s

# Type checking
mypy src/

# CLI tools
python -m pyresonitelink.cli.tree <port>                    # Interactive TUI browser
python -m pyresonitelink.cli.dumptree <port> out.json       # Export hierarchy
python -m pyresonitelink.cli.get_components <port>          # List component types
python -m pyresonitelink.cli.get_components <port> --component "[FrooxEngine]FrooxEngine.WorldLink"
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.ValueField<>"
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"
```

## Architecture

### Data Flow
```
Client -> encode() -> JSON -> WebSocket -> ResoniteLink server
                                                |
Python objects <- decode_response() <- JSON <---+
```

### Key Modules

- **`client.py`**: WebSocket client with async/sync APIs. Entry point for all operations.
- **`data/codec.py`**: JSON serialization using `$type` discriminators for polymorphic types. Custom encode/decode for `Rect` and `BoundingBox` (nested wire format).
- **`data/primitives.py`**: PascalCase primitive types (Float3, FloatQ, Color, Rect, BoundingBox, etc.) with float/int coercion in `__post_init__`. Scalar aliases: `primitives.Float` = `np.float32`, `primitives.String` = `str`, `primitives.Char` = `str`, etc.
- **`data/fields.py`**: Typed field wrappers (FieldFloat, FieldString, ArrayFloat3, FieldRect, etc.) for component member values. Includes nullable variants (FieldNullableInt, etc.) and array variants (ArrayFloat3, etc.).
- **`data/members.py`**: Member types (Reference[T], SyncList, SyncObject, SyncPlayback, SyncDictionary, FieldEnum, EmptyElement). Reference is generic with a phantom type parameter for type-safe references.
- **`data/workers.py`**: Core data model - Worker (base) -> Slot (scene node) -> Component.
- **`data/messages.py`**: Request types (GetSlot, AddComponent, UpdateComponent, GetComponentTypeList, GetComponentDefinition, GetTypeDefinition, GetSyncObjectDefinition, CallSyncMethod, CallStaticSyncMethod, etc.).
- **`data/responses.py`**: Response types (SlotData, ComponentData, ComponentTypeList, ComponentDefinitionData, etc.).
- **`data/reflection.py`**: Reflection data types for ComponentDefinition responses.
- **`data/protocols.py`**: `ResoniteLinkClient` Protocol class that breaks the circular import between `client.py` and `generated/`. Generated components depend on this protocol, not on the concrete Client class.
- **`generated/`**: Auto-generated component wrapper classes and type hierarchy from live server.
- **`generated/_base.py`**: Base classes `GeneratedComponent` and `GenericComponent[T]`. Uses `protocols.ResoniteLinkClient` for the client parameter type.
- **`generated/_generator.py`**: Code generator for component classes and type hierarchy classes.
- **`generated/_type_map.py`**: Bidirectional mapping between Python types, Resonite wire names, and field classes.
- **`generated/_types/`**: Generated type hierarchy classes (interfaces, abstract types, asset types) used by reference properties.
- **`cli/gencode.py`**: CLI for generating component wrapper classes and their type dependencies. Automatically rebuilds `__init__.py` re-exports after generation.
- **`cli/get_components.py`**: CLI for browsing component types and definitions.

### Import Aliases

Short import paths are provided via alias packages:

- **`pyresonitelink.components`** aliases `pyresonitelink.generated` — for data components: `from pyresonitelink.components.data import ValueField`
- **`pyresonitelink.protoflux`** aliases `pyresonitelink.generated.protoflux.runtimes.execution.nodes` — for ProtoFlux nodes: `from pyresonitelink.protoflux.core import ValueInput`

Each category package has an `__init__.py` that re-exports all its classes. Python keyword conflicts (`if`, `for`, `while`, `async`) are handled via `importlib`. The `gencode` CLI rebuilds these `__init__.py` files after each generation run.

### Type System

The codec uses `$type` fields for polymorphic deserialization. When adding new types:
1. Define as a dataclass
2. Register in the appropriate type map in `codec.py`
3. Use numpy types for numeric fields to match C# precision

#### Primitive Types

All primitive structs in `primitives.py` use PascalCase names. Scalar aliases are provided: `primitives.Float` = `np.float32`, `primitives.Int` = `np.int32`, etc.

All numeric primitive constructors accept plain Python `int` and `float` and coerce to the exact numpy type in `__post_init__`. Out-of-range values raise at construction time.

```python
from pyresonitelink.data.primitives import Float3
v = Float3(x=1, y=2.5, z=3)  # x, y, z are np.float32 after construction
```

#### Wire Format Mapping

The `$type` discriminator in JSON maps to Python classes:
- Scalar fields: `"bool"` -> `FieldBool`, `"int"` -> `FieldInt`, `"float"` -> `FieldFloat`, `"decimal"` -> `FieldDecimal` (uses `decimal.Decimal`), `"char"` -> `FieldChar`, `"string"` -> `FieldString`, `"Uri"` -> `FieldUri`
- Composite fields: `"float3"` -> `FieldFloat3`, `"colorX"` -> `FieldColorX`, `"Rect"` -> `FieldRect`, `"BoundingBox"` -> `FieldBoundingBox`
- Nullable variants: `"int?"` -> `FieldNullableInt`, `"bool?"` -> `FieldNullableBool`, `"enum?"` -> `FieldEnum`
- Array variants: `"float3[]"` -> `ArrayFloat3`, `"color[]"` -> `ArrayColor`
- Member types: `"reference"` -> `Reference`, `"list"` -> `SyncList`, `"syncObject"` -> `SyncObject`, `"enum"` -> `FieldEnum`, `"playback"` -> `SyncPlayback`, `"dictionary<enum>"` -> `SyncDictionary`

ALWAYS keep wire-format strings (first arg of `_register_type()`) in their original case. These are protocol strings, not Python identifiers.

### Component Generation (`gencode.py`)

Components are generated from live ResoniteLink server data. The `gencode` CLI generates a component class and recursively generates all types it depends on.

```bash
python -m pyresonitelink.cli.gencode <port> "[FrooxEngine]FrooxEngine.AudioClipPlayer"
# Generates:
#   generated/audio/audio_clip_player.py     (component class)
#   generated/_types/iasset_provider.py      (generic interface)
#   generated/_types/iasset.py               (interface)
#   generated/_types/audio_clip.py           (asset type)
#   generated/_types/asset.py                (abstract generic)
#   ... and all their transitive dependencies
```

#### How Component Generation Works

1. **GetComponentDefinition** provides member structure (names, types, references)
2. **AddComponent + GetComponent** on a temp slot provides concrete `$type` values for each member (preferred over definition for type resolution)
3. **GetTypeDefinition** traces the base type chain to collect implemented interfaces
4. The generator resolves each member to a Python type:
   - **Fields** (bool, int, float, string, float3, etc.): getter/setter exposes the value directly
   - **Nullable fields** (int?, bool?, etc.): same pattern, uses FieldNullableXxx classes
   - **Array fields** (float3[], color[], etc.): getter/setter exposes `list[T]` via `.values`
   - **Enums**: exposed as `FieldEnum` members (value is a string)
   - **References**: getter returns target ID (`str | None`), setter accepts target ID or typed stub instance. Target type constraint is baked into the setter type annotation.
   - **SyncPlayback**: exposed as `SyncPlayback` (play, loop, position, speed)
   - **SyncList, SyncObject, SyncDictionary**: exposed as-is
   - **Generic type parameters** (`T`): exposed as `T` from `Generic[T]`, resolved at runtime via `_type_info`
5. Non-generic components inherit from `GeneratedComponent` + implemented interfaces
6. Generic components (with `<>`) inherit from `GenericComponent[T]` + interfaces (with `[T]`) and are parameterizable: `ValueField[primitives.Float]`
7. **Sync methods** listed in the definition's `methods` array become async method wrappers that call `CallSyncMethod` via the base class `call_method()`. Parameters are typed from the definition. Overloaded methods get a `_N` suffix.
8. Category path maps to directory structure under `generated/`

#### How Reference Types Are Generated

When a component has a reference member (e.g. `AudioClipPlayer.Clip -> IAssetProvider<AudioClip>`), gencode recursively generates the referenced types:

1. **Try GetComponentDefinition first** — if the type is a component, generate a full wrapper class
2. **Fall back to GetTypeDefinition** — for interfaces, abstract classes, and non-component types, generate a type hierarchy class in `_types/`

The type hierarchy generator (`generate_type_source`) produces proper Python classes:
- **Interfaces** become plain classes (Python has no interface keyword)
- **Generic types** use `Generic[T]` with `TypeVar` bounds derived from the server's generic parameter constraints
- **Base types and interfaces** become Python base classes (multiple inheritance)
- **Root types** (no bases) get an `id: str | None` attribute so they can be used as reference targets

#### Resonite's Non-Generic / Generic Type Duality

Resonite has a pattern where both a non-generic `X` and a generic `X<T>` exist as separate types, with `X<T>` inheriting from `X`. For example:
- `Asset` (non-generic, implements `IAsset`)
- `Asset<V>` (generic, base type is `Asset`)

In Python, these are **merged into one class**: the generic form. The merge logic:
1. Queries both the plain and `<>` forms from the server
2. Uses the generic form as the base (it has type parameters)
3. Folds the non-generic's interfaces into the generic class
4. Replaces the self-referential base type (`Asset<V>` -> base `Asset`) with the non-generic's base type (typically `None`)

This is handled in `gencode.py`'s `_generate_type_hierarchy`.

#### MRO Deduplication

The server reports ALL implemented interfaces, including inherited ones. In Python, listing both a base class and its parent interface causes MRO conflicts. The generator deduplicates at two levels:

**For `_types/` hierarchy classes**: `_get_all_ancestors` computes which interfaces are already reachable through the base type chain and only includes leaf interfaces.

**For component classes** (interface inheritance): A two-step dedup:
1. When both generic (`IFoo[T]`) and non-generic (`IFoo`) forms of the same interface exist, keep only the generic version
2. Remove interfaces that are ancestors of another interface in the list (using `_get_all_ancestors` with `all_type_defs`)

**Name collision avoidance**: Member names that collide with Python keywords, builtins (`str`, `int`, `float`, `bool`, `id`, `input`, etc.), or the base class `component` property get a `_` suffix via `_safe_python_name`. The `_PYTHON_KEYWORDS` set includes both language keywords and builtins used in generated annotations.

#### Self-Referential Generic Constraints

Some Resonite types have self-referential constraints like `V: IEngineAssetVariantDescriptor<V>`. This pattern ensures subclass methods return the concrete type. Since Python doesn't need this pattern, the generator drops self-referential constraints and uses a plain `TypeVar`.

#### TypeVar Bounds in `_types/` Stubs

Generated `_types/` stubs use **unbounded** TypeVars (no `bound=` parameter). Although the server reports bounds (e.g. `T: IWorldElement`), including them causes false-positive mypy errors when component classes use their own `T` (from `GenericComponent[T]`, which is unbounded) as a type argument to a bounded stub. The stubs exist for isinstance checks and type annotations, not runtime enforcement.

#### Undefined Type Parameters in Non-Generic Components

Some non-generic components reference generic interfaces with type parameters (`E`, `S`, `U`, etc.) that aren't defined in the component's scope. The generator detects these via `re.findall(r"\b([A-Z])\b", annotation)` and aliases them to `Any` with `from typing import Any`.

#### `_parse_target_type` and `<>` Handling

Resonite type strings use `<>` for empty generic markers (e.g. `IAssetProvider<>`) and `<T1, T2>` for concrete type arguments. The `_parse_target_type` function handles both:
- `IAssetProvider<>` -> base `IAssetProvider`, args `[]`
- `IAssetProvider<AudioClip>` -> base `IAssetProvider`, args `["AudioClip"]`

ALWAYS handle `<>` (empty generic) as a special case. If `<>` is not stripped by the parser, the `<` character causes downstream logic to skip the generic-form query, preventing the non-generic/generic merge from running.

### Client API

The client provides direct-parameter methods for all operations. Parameters accept both Field wrappers and raw Python values (strings, bools, tuples, etc.):

```python
resolink = client.Client()
await resolink.connect(PORT)

# Slot operations — accept raw values or Field wrappers
resp = await resolink.add_slot(parent=ref, name="My Slot", position=(0, 1.5, 0))
resp = await resolink.add_slot_to_root(name="My Slot")  # parent=Root
slot = await resolink.get_slot(slotId="Root", depth=1)
await resolink.remove_slot(slotId=slot_id)

# Component operations — componentType + references for easy wiring
resp = await resolink.add_component(
    containerSlotId=slot_id,
    componentType="[ProtoFluxBindings]...ValueDisplay<float>",
    references={"Input": node_id, "_value": field_id},
)
# Or with a pre-built Component object:
resp = await resolink.add_component(containerSlotId=slot_id, data=component)
get = await resolink.get_component(componentId=comp_id)
await resolink.update_component(data=component)
await resolink.update_references(componentId=comp_id, references={"Input": node_id})
await resolink.remove_component(componentId=comp_id)

# Reflection
types = await resolink.get_component_type_list(categoryPath="/Data")
defn = await resolink.get_component_definition(componentType="...", flattened=True)
```

`add_slot`, `add_slot_to_root`, and `add_component` return `NewEntityId` with `.entityId`. Other mutations return `Response` with `.success`.

#### Value Coercion in `add_slot` / `add_slot_to_root`

Field parameters accept raw Python values that are automatically coerced:
- `name="Hello"` → `FieldString(value="Hello")`
- `isActive=True` → `FieldBool(value=True)`
- `position=(1, 2, 3)` → `FieldFloat3(value=Float3(x=1, y=2, z=3))`
- `rotation=[0, 0, 0, 1]` or `np.array(...)` → `FieldFloatQ(value=FloatQ(...))`
- `orderOffset=5` → `FieldLong(value=np.int64(5))`

The coercion is handled by two generic functions in `client.py`:
- `_coerce_scalar_field(value, field_cls, np_type=None)` — for `FieldString`, `FieldBool`, `FieldLong`, etc.
- `_coerce_composite_field(value, field_cls, primitive_cls)` — for all multi-component types (`FieldFloat3`, `FieldFloatQ`, `FieldInt2`, `FieldColor`, `FieldFloat2x2`, etc.) using `dataclasses.fields()` to auto-discover component names

### Generated Component Lifecycle

Generated components have convenience methods for server interaction:

```python
FloatField = ValueField[primitives.Float]

# Create with initial value and add to server in one step
value_field = FloatField(42.5)
await value_field.add_to_slot(resolink, slot_id)
# value_field.id is now set, members have server-assigned IDs

# Modify and push to server
value_field.value = primitives.Float(99.0)
await value_field.update(resolink)

# Pull latest state from server
await value_field.refresh(resolink)
print(value_field.value)  # 99.0
```

`add_to_slot` accepts either a slot ID string or a `Slot` instance (whose `.id` is used). The server accepts member data on `AddComponent`, so values set before `add_to_slot` are sent with the creation request — no separate update needed.

#### Generated `__init__` Parameters

The generator produces `__init__` methods with optional parameters for init-able members:

- **Generic-parameter fields** (like `ValueField.value`, `ValueInput.value`): typed as `T | None`
- **References with known target types** (like `ValueAdd.a`, `ValueAdd.b`): typed as `str | TargetType | None`

```python
# Single-value generic components
vi = ValueInput[primitives.Float](10.0)
value_field = ValueField[primitives.Float3](primitives.Float3(1, 2, 3))

# Multi-reference components — pass IDs or component instances directly
add = ValueAdd[primitives.Float](a=input_a, b=input_b)

# Reference-type generics — e.g. RefObjectInput[Slot]
slot_ref = RefObjectInput[workers.Slot](target=slot_id)

# Wrapping server data (keyword-only)
value_field = ValueField(component=get_resp.data)
```

Components without init-able members (e.g. `AudioClipPlayer` whose members are `SyncPlayback` and `Reference`) use the base `__init__(component=...)`.

#### Interface Inheritance and Type-Safe Wiring

Generated components inherit from the Resonite interfaces they implement (via `_types/` stubs). This enables the type checker to verify wiring correctness:

```python
FloatAdd = ValueAdd[primitives.Float]
FloatInput = ValueInput[primitives.Float]

# Valid: ValueAdd and ValueInput implement INodeValueOutput[T]
add = FloatAdd(a=input_a, b=input_b)  # type-checks

# Invalid: AudioClipPlayer does not implement INodeValueOutput
add = FloatAdd(a=player)  # mypy error!
```

The generator collects interfaces by tracing the component's base type chain via `GetTypeDefinition`, then deduplicates:
1. When both generic (`IFoo[T]`) and non-generic (`IFoo`) forms exist, keep only the generic
2. Remove interfaces that are ancestors of other interfaces in the list (using `_get_all_ancestors`)

This produces clean base class lists like `class ValueAdd(GenericComponent[T], INodeValueOutput[T], ...)` without MRO conflicts.

### Testing Components Against the Server

The ResoniteLink server port changes each session:

```python
resolink = client.Client()
await resolink.connect(PORT)

# 1. Create a temporary slot
slot_resp = await resolink.add_slot_to_root(name="__test__")
slot_id = slot_resp.entityId

# 2. Add a generated component (accepts slot ID or Slot instance)
value_field = ValueField[primitives.Float](42.5)
await value_field.add_to_slot(resolink, slot_id)

# 3. Read back
await value_field.refresh(resolink)
print(value_field.value)  # 42.5

# 4. Update
value_field.value = primitives.Float(99.0)
await value_field.update(resolink)

# 5. Clean up
await resolink.remove_slot(slotId=slot_id)
```

Key points:
- Component type names MUST be assembly-qualified: `"[FrooxEngine]FrooxEngine.WorldLink"`
- Generic components can't be instantiated with bare `<>` — use concrete types: `ValueField[primitives.Float]`
- `add_to_slot` automatically refreshes from the server to get member IDs
- ALWAYS delete test slots when done

### Reflection API

The server provides two levels of type introspection:

```python
# List component types in a category
resp = await resolink.get_component_type_list(
    messages.GetComponentTypeList(categoryPath="/Data")
)

# Get a component's full definition (members, types, methods)
# Only works for component types. Use generic form for generics.
def_resp = await resolink.request_json(
    messages.GetComponentDefinition(
        componentType="[FrooxEngine]FrooxEngine.ValueField<>",
        flattened=True,  # include inherited members
    )
)

# Get any type's definition (interfaces, abstract classes, enums, etc.)
# Works for ALL types, not just components.
type_resp = await resolink.request_json(
    messages.GetTypeDefinition(
        type="[FrooxEngine]FrooxEngine.IAssetProvider<>"
    )
)
# Returns TypeDefinition with: fullTypeName, isInterface, isAbstract,
# isGenericType, genericParameters (with constraints), baseType,
# interfaces, etc.
```

`GetComponentDefinition` returns member definitions with `$type` values like `"field"`, `"reference"`, `"array"`, `"list"`, `"playback"`, `"dictionary"`.

`GetTypeDefinition` returns type metadata for ANY type, including interfaces. This is what the generator uses for the `_types/` hierarchy.

`GetSyncObjectDefinition` returns member definitions for sync object types — types that inherit from `SyncObject` (nested data containers within workers/components). Uses parameter `syncObjectType`. Response `$type` is `syncObjectDefinitionData`. Note: `Slot` and `Component` are NOT sync objects — they are Workers. `UserRef` is an example of a type that works.

```python
resp = await resolink.request_json(
    messages.GetSyncObjectDefinition(
        syncObjectType="[FrooxEngine]FrooxEngine.UserRef",
        flattened=True,
    )
)
# resp["definition"]["members"] is a dict of member name -> member info
```

### Calling Sync Methods

Components can expose callable methods (listed in `GetComponentDefinition`'s `methods` array). These are called via `CallSyncMethod` (field names: `targetID`, `methodName`, `arguments` dict). Generated components get async wrapper methods automatically:

```python
player = AudioClipPlayer()
await player.add_to_slot(resolink, slot)
await player.play(resolink)   # generated wrapper for CallSyncMethod
await player.stop(resolink)
```

Methods with parameters accept typed Python arguments:

```python
await audio_output.exlude_user(resolink, user="some-user-id")
```

**Important**: Only methods in the definition's `methods` array are callable. ProtoFlux node methods like `CallInput.Trigger` are C# methods but NOT sync methods — they throw `NullReferenceException` because the ProtoFlux execution context isn't available through ResoniteLink.

`CallStaticSyncMethod` calls static methods on a type (field: `targetType` instead of `targetID`).

### ProtoFlux

ProtoFlux is Resonite's visual programming system. Nodes are components that wire together via references. Understanding the execution model is important:

- **Value nodes are lazy/pull-based**: a node computes its value only when asked by a downstream consumer. It "pulls" from its inputs, which recursively pull from their inputs.
- **Impulse/flow connections are push-based**: the source node's output reference points to the downstream node (e.g. `FireOnTrue.OnChanged -> If`).
- **Value inputs are references**: a node's input members are `$type: "reference"` targeting `INodeValueOutput<T>` — the output of another node.
- **Impulse outputs are references**: targeting `ISyncNodeOperation` or `INodeOperation` — the next node in the flow.
- **Outputs are implicit**: a node IS its own output. Other nodes reference it by component ID.
- **The definition lies for generic ProtoFlux nodes**: `GetComponentDefinition` for `ValueAdd<>` shows members `A` and `B` as `$type: "field"` with generic `valueType`, but the actual instantiated component has `$type: "reference"`. ALWAYS prefer component data over definitions for ProtoFlux nodes.

#### Key ProtoFlux Node Types

All under `[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes`:

**Value nodes** (pull-based, compute on demand):
- **`ValueInput<T>`** (Core): Holds a settable value. Has a `Value` field of type `T`. Use this to feed constants into a graph.
- **`ValueObjectInput<T>`** (Core): Like ValueInput but for object/reference types (e.g. `string`, `Slot`). Use this for string constants.
- **`RefObjectInput<T>`** (Core): Holds a reference to a world object (e.g. `Slot`). Has a `Target` reference member.
- **`ValueAdd<T>`** (Operators): Adds two values. Has `A` and `B` reference inputs targeting `INodeValueOutput<T>`.
- **`ValueDisplay<T>`** (Core): Bridges ProtoFlux output to a data field. Has `Input` (reference to `INodeValueOutput<T>`) and `_value` (reference to `IField<T>`). This is how you read a computed result.
- **`ValueFieldDrive<T>`** (Core): Drives a field from a node output.
- Other operators: `ValueSub<T>`, `ValueMul<T>`, `ValueDiv<T>`, `ValueMod<T>`, `ValueLessThan<T>`, etc.
- Mixed-type operators: `Add_Float_Float2`, `Mul_Double3_Double`, etc.

**Flow/impulse nodes** (push-based, execute on trigger):
- **`Update`** (Actions): Fires an impulse every frame via `OnUpdate`. Use this as the primary impulse source for flow graphs that should run continuously.
- **`OnePerFrame`** (Actions): Accepts any number of incoming impulses per frame but only forwards the first one via `Next`. Use this to debounce — it does NOT generate impulses on its own.
- **`FireOnTrue`** (Flow): Fires an impulse when its `Condition` transitions from false to true (rising edge detector). Not a continuous trigger.
- **`If`** (Flow): Receives an impulse and routes to `OnTrue` or `OnFalse` based on `Condition` (a `INodeValueOutput<bool>`).
- **`WriteDynamicValueVariable<T>`** (Variables): Writes a value to a `DynamicValueVariable<T>` by name. Requires `Target` (slot ref), `Path` (variable name string), and `Value` (the value to write). Has `OnSuccess`/`OnFailed`/`OnNotFound` impulse outputs.

**Data components** (not ProtoFlux nodes, but used with them):
- **`DynamicVariableSpace`** (Data/Dynamic): Must be on a slot (or ancestor) for dynamic variables to work.
- **`DynamicValueVariable<T>`** (Data/Dynamic): Stores a named value. Has `VariableName` (string) and `Value` (T) fields. Readable directly via `get_component`.

#### Reading a Computed Result

ProtoFlux nodes don't expose their output values directly. To read a result:

1. Create a `ValueField<T>` component to hold the result
2. Create a `ValueDisplay<T>` node
3. Wire `ValueDisplay.input` -> the source node (by component ID or instance)
4. Wire `ValueDisplay.value` -> the **member ID** of the `Value` field inside the `ValueField` (NOT the component ID — use `result_field.get_member("Value").id`)
5. Wait briefly for the engine to evaluate
6. Read the `ValueField` back — it now contains the computed result

```python
# Create result field and add to server
result_field = FloatField()
await result_field.add_to_slot(resolink, slot_id)

# Get the member ID (not component ID) of the Value field
value_member = result_field.get_member("Value")

# Wire ValueDisplay: reads from source node, writes to result field
display = FloatDisplay(input=source_node.id, value=value_member.id)
await display.add_to_slot(resolink, slot_id)

# Read result after engine evaluates
time.sleep(0.5)
await result_field.refresh(resolink)
print(result_field.value)  # the computed value
```

#### Wiring Nodes Together

ProtoFlux nodes wire by setting reference members. You can pass component IDs (strings) or component instances directly — the type checker validates compatibility:

```python
# Wire ValueAdd inputs to ValueInput nodes (pass instances)
add1 = FloatAdd(a=input_10, b=input_20)  # type-checked!
await add1.add_to_slot(resolink, slot_id)

# Chain: wire to another ValueAdd's output
add2 = FloatAdd(a=add1, b=input_5)

# Also works with string IDs
add2 = FloatAdd(a=add1.id, b=input_5.id)
```

Any node that implements `INodeValueOutput<T>` can be used as a value input. This includes `ValueInput<T>`, `ValueAdd<T>`, and all other computation nodes. The type checker enforces this — passing an `AudioClipPlayer` where `INodeValueOutput[float32]` is expected is a mypy error.

For impulse/flow connections, the source node's output points to the target:

```python
# FireOnTrue.on_changed -> If node (impulse connection)
fire.on_changed = if_node.id  # ISyncNodeOperation reference
```

See `examples/protoflux_add.py` for a complete working example that builds `(10 + 20) + 5 = 35` and reads back the result.

#### Imperative Flow (If-Else with Dynamic Variables)

For procedural logic like `if (x < 3) z = x + 3; else z = x - 3;`, use impulse-driven flow nodes with `DynamicValueVariable` for storage:

1. Create a `DynamicVariableSpace` and `DynamicValueVariable<T>` on the slot
2. Use `Update` node as the impulse source (fires every frame)
3. Wire `Update.OnUpdate` -> `If.Condition` (via a comparison node)
4. Wire `If.OnTrue` / `If.OnFalse` -> `WriteDynamicValueVariable<T>` nodes
5. `WriteDynamicValueVariable` needs `Target` (a `RefObjectInput<Slot>` pointing at the slot), `Path` (a `ValueObjectInput<string>` with the variable name), and `Value` (the computed value)
6. Read the result by fetching the `DynamicValueVariable` component and reading its `Value` field

```python
# Update -> If -> WriteDynamicValueVariable (on each branch)
update_id = await add_node(resolink, slot_id, f"{PFX}.Actions.Update",
    OnUpdate=if_id)

if_id = await add_node(resolink, slot_id, f"{PFX}.If",
    Condition=less_than_id, OnTrue=write_true_id, OnFalse=write_false_id)

# Each WriteDynamicValueVariable needs slot ref + path + value
wt_id = await add_node(resolink, slot_id, WDVV_TYPE,
    Target=slot_ref_id, Path=path_id, Value=add_id)
```

See `examples/protoflux_if_else.py` for the complete working example.

## Known Issues

- First WebSocket connection fails with `ConnectionClosedError` on initial request. Workaround is implemented in the client (retry logic).
- On Git Bash (MSYS2), paths starting with `/` get mangled to Windows paths. Use `MSYS_NO_PATHCONV=1` when passing category paths like `/Data`.
- 18 `_types/` stubs are minimal placeholders because `GetTypeDefinition` fails for component types. These need a fallback to `GetComponentDefinition`. See memory file `type_stub_todo.md` for the full list.
- `cli/get_components.py` passes message objects to the convenience API methods instead of using keyword args (pre-existing, not yet fixed).

## Debugging Guidelines

### "Nothing Happens" Bugs in Data Processing

When code produces no output or skips all items silently:

- ALWAYS examine the actual input data structure FIRST, before reading code
- Trace the specific input through the code path to find where it's filtered/skipped
- Multiple layers may fail independently - fixing one issue doesn't guarantee success
- Test with the EXACT original command, not a variation

**General principle**: When data has inherent structure (hierarchies, nested types), preserve that structure through transformations rather than flattening early.

### Wire Format vs Python Names

Wire-format strings (`$type` values, `_register_type` first args) are protocol strings that MUST match exactly what the server sends. Python class names are independent. NEVER rename wire strings when renaming Python classes.

- `"float3"` is the wire name, `Float3` is the Python class
- `"color"` is the wire name, `Color` is the Python class
- `"Rect"` and `"BoundingBox"` happen to be PascalCase on the wire

### Component Definition vs Component Data

When generating code, ALWAYS prefer actual component data for member type resolution over the definition. The definition uses abstract `$type` values like `"field"` with nested `valueType`, while data uses concrete `$type` values like `"float3"`, `"int?"`, `"reference"` that map directly to field classes.

The definition is useful for:
- Identifying generic type parameters (`valueType.isGenericParameter == true`)
- Handling `Nullable<>` wrappers (unwrap to inner type + `?` suffix)
- Detecting array members (`$type = "array"` with `valueType`)
- Fallback when a component can't be instantiated (generic types with `<>`)

**ProtoFlux gotcha**: Generic ProtoFlux node definitions report input members as `$type: "field"` with generic valueType, but actual instantiated components have them as `$type: "reference"` targeting `INodeValueOutput<T>`. The `_is_generic_parameter` function MUST only return True for `"field"` members, not `"reference"` members whose target type contains a generic parameter.

### Resonite Type String Gotchas

- `<>` means "generic type definition" (no concrete args). ALWAYS strip `<>` before using as a base name or class name.
- `<,>` means "two type parameters, both unspecified". `_parse_target_type` must skip empty args.
- Assembly prefixes like `[FrooxEngine]` must be preserved in server communication but stripped for Python names.
- Non-generic `X` and generic `X<>` are SEPARATE types in Resonite. The generic inherits from the non-generic. In Python, merge them into one class.
- Self-referential constraints like `V: Foo<V>` should be dropped to plain TypeVars.
- `+` is the C# nested type separator (e.g. `Userspace+WorldRelation`). `_simple_class_name` takes the innermost name.
- Nullable types like `bool?` are primitives — `_is_primitive_wire_name` and `_primitive_python_name` strip the `?` suffix.
- Nested generics like `INodeObjectOutput<IAssetProvider<AudioClip>>` must be handled recursively by `_ref_type_annotation`.

### Snake Case and Known Abbreviations

`_to_snake_case` in `_generator.py` uses a known-abbreviations table (`_ABBREVIATIONS`) to keep compound tokens like `ColorX`, `Color32`, `UIX`, `HSV`, `HSL`, `RGB`, `URL` as atomic units:
- `ColorXToHexCode` → `colorx_to_hex_code`
- `HSVToColorX` → `hsv_to_colorx`
- `UIXButton` → `uix_button`
- `ActiveSessionURLs` → `active_session_urls`

ALWAYS add new abbreviations to `_ABBREVIATIONS` when Resonite types use compound acronyms that the generic regex splits incorrectly.

## Coding rules

Use import statements for packages and modules only, not for individual types, classes, or functions:

- Use import x for importing packages and modules.
- Use from x import y where x is the package prefix and y is the module name with no prefix.
- Use from x import y as z in any of the following circumstances:
  - Two modules named y are to be imported.
  - y conflicts with a top-level name defined in the current module.
  - y conflicts with a common parameter name that is part of the public API (e.g., features).
  - y is an inconveniently long name.
  - y is too generic in the context of your code (e.g., from storage.file_system import options as fs_options).
- Use import y as z only when z is a standard abbreviation (e.g., import numpy as np).

Exemptions from this rule:

- Symbols from the following modules are used to support static analysis and type checking:
  - typing module
  - collections.abc module
  - typing_extensions module

You must annotate Python code with type hints. Type-check the code at build time with mypy. In most cases, when feasible, type annotations are in source files. For third-party or extension modules, annotations can be in stub .pyi files.

You must add docstrings to all classes and functions using the Google style of docstrings.

You must add unit tests for new features and bug fixes.

You must update README.md when there is a new feature.
