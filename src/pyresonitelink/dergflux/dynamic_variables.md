# Dynamic Variables in Resonite

Dynamic variables (dynvars) are a scoped data storage system in Resonite.
They store named values under slot hierarchies, like an associative array.
This document covers how they work and how Dergflux uses them.

## Overview

Dynamic variables have two parts:

- **Dynamic variable spaces** — created by attaching a `DynamicVariableSpace`
  component to a slot.  The slot and all children become part of the named space.
- **Dynamic variables** — named values that live under a space.

## Variable Types

There are three component types for creating variables:

- **`DynamicValueVariable<T>`** — for value types (int, float, float3, etc.)
- **`DynamicReferenceVariable<T>`** — for reference types (Slot, User, etc.)
- **`DynamicTypeVariable`** — for the Type type

In Dergflux, `s.FloatDynVar("x")` creates a `DynamicValueVariable<float>`.

## Value Types vs Object Types

Resonite distinguishes **value types** from **object types** throughout
its type system, and this distinction is critical when working with
ProtoFlux nodes and dynamic variables.

**Value types** (numeric, composite primitives):
- `bool`, `int`, `float`, `double`, `long`, and their unsigned variants
- `float2`, `float3`, `float4`, `color`, `colorX`, and other composites
- Use: `ValueInput<T>`, `WriteDynamicValueVariable<T>`,
  `ReadDynamicValueVariable<T>`, `DynamicValueVariableDriver<T>`

**Object types** (reference and special types):
- **`string`** — this is the most common gotcha
- `Slot`, `User`, `Component`, `IAssetProvider<T>`, and all world elements
- Use: `ValueObjectInput<T>`, `WriteDynamicObjectVariable<T>`,
  `ReadDynamicObjectVariable<T>`, `DynamicReferenceVariableDriver<T>`

**`string` is an object type.** Even though it has a `FieldString` field
class and appears alongside value types in the data model, Resonite treats
`string` as an object type in ProtoFlux.  `ValueInput<string>` does not
exist — you must use `ValueObjectInput<string>`.  Similarly,
`WriteDynamicValueVariable<string>` does not exist — use
`WriteDynamicObjectVariable<string>`.

Using the wrong variant (e.g. `ValueInput<string>` instead of
`ValueObjectInput<string>`) causes a "Failed to resolve type" error at
component creation.

Dergflux handles this automatically — the builder detects object types
and uses the correct variants.

## Dynamic Fields

Existing component fields can be "transformed" into dynamic variables using:

- **`DynamicField<T>`** — for value type fields
- **`DynamicReference<T>`** — for reference type fields
- **`DynamicTypeField`** — for Type fields

This makes an existing field accessible by name through the dynamic variable
system, without creating a separate variable component.

## Naming

Variable and space names can contain letters, digits, period (`.`),
underscore (`_`), space (` `), and hyphen (`-`).  No other symbols or
punctuation.

Periods are conventionally used to namespace variables:
`User/Avatar.Systems.Flight.Drag`

## Binding

A dynamic variable traverses up the slot hierarchy looking for a compatible
space to bind to.  If no space is found, the variable is inaccessible
externally.

### Direct vs Indirect Binding

- **Indirect**: `VariableName` — binds to the first space that does not have
  `OnlyDirectBinding` set.
- **Direct**: `SpaceName/VariableName` — binds to the first space matching
  `SpaceName`.

Example hierarchy:

```
└─ Foo - Space "test"
   └─ Bar - Space "test2"
      └─ Baz - Variable "test/var"
```

- `test/var` binds to space `test` (direct)
- `var` binds to space `test2` (indirect, first non-direct space)
- `var` with `test2.OnlyDirectBinding=True` binds to `test`

### Binding in Dergflux

In Dergflux, when a Space has a name, variables use direct binding:

```python
s = g.Space(slot, name="Audio")
s.vol = s.FloatDynVar("vol")   # variable path: "Audio/vol"
```

Without a name, variables use indirect binding:

```python
s = g.Space(slot)
s.vol = s.FloatDynVar("vol")   # variable path: "vol"
```

## Driving Fields from Dynamic Variables

The `DynamicValueVariableDriver<T>` and `DynamicReferenceVariableDriver<T>`
components continuously drive a component field from a dynamic variable's
value.  This is the recommended way to connect dynvars to component fields.

- **`DynamicValueVariableDriver<T>`** — for value types (int, float, etc.)
- **`DynamicReferenceVariableDriver<T>`** — for reference types (Slot, etc.)

Both take a `VariableName` (the dynvar path) and a `Target` (the field to
drive).

### Driving in Dergflux

`g.Bind()` automatically selects the right driver:

```python
# Bind a dynvar to a field — uses DynamicValueVariableDriver<float>
g.Bind(s.volume, audio_output, "Volume", slot=slot)

# Bind a computed expression — uses ValueFieldDrive<int>
g.Bind(i, mux, "Index")
```

When the source is a bare dynamic variable read (`s.x`), Dergflux creates
a `DynamicValueVariableDriver` or `DynamicReferenceVariableDriver`.  When
the source is a computed expression (`s.x + 1`, loop index `i`, etc.),
Dergflux creates a `ValueFieldDrive` instead.

## Reading and Writing

### Reading (ProtoFlux)

- **`ReadDynamicValueVariable<T>`** — reads from any slot in the space
  hierarchy.  Takes a Source slot and Path.  Used when reading from outside
  the space or with dynamic paths.
- **`DynamicVariableInput<T>`** — more efficient, binds directly to spaces
  in its own slot hierarchy.  Preferred when the path is known at build time.

In Dergflux, reading a variable (`s.x` in an expression) creates a
`ReadDynamicValueVariable` at build time.

### Writing (ProtoFlux)

- **`WriteDynamicValueVariable<T>`** — writes a value to a named variable.
  Takes Target (slot), Path (variable name), and Value.
- **`WriteOrCreateDynamicVariable<T>`** — same, but creates the variable
  if it doesn't exist.

In Dergflux, `s.x = expr` inside a flow block creates a
`WriteDynamicValueVariable` at build time.

## Default Spaces

Three spaces exist by default in every world:

- **`World`** — under the Root slot, `OnlyDirectBinding`.  For global values.
- **`User`** — under each user's root slot, `OnlyDirectBinding`.  For per-user
  avatar systems.
- **`Dash`** — under the userspace dash slot.

## Caveats

- **Binding delay**: Creating, deleting, or renaming variables may require
  a 2-update delay before they bind correctly.
- **Driving caution**: If a dynvar is driven, all instances of the same
  variable must be driven by the same value, or clients will fight.
- **1-frame delay**: Driving a dynvar is a local write each frame, so
  there's a 1-frame propagation delay.
- **Single instance**: It's recommended to have only one instance of each
  named variable bound to a given space.

## Best Practices

- Use direct binding (`SpaceName/VarName`) for clarity.
- Use `OnlyDirectBinding` on spaces to prevent misbindings.
- Use periods for namespacing: `MySystem.Settings.Volume`.
- Prefer `DynamicVariableInput` over `ReadDynamicVariable` when the path
  is static and the node is in the same space.
