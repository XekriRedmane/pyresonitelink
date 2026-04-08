# ProtoFlux

> Summarized from the Resonite wiki:
> - https://wiki.resonite.com/ProtoFlux
> - https://wiki.resonite.com/Impulses
> - https://wiki.resonite.com/ProtoFlux:Local
> - https://wiki.resonite.com/ProtoFlux:Store
> - https://wiki.resonite.com/ProtoFlux:DataModelStore

ProtoFlux is Resonite's node-based visual programming language. It operates
in 3D space and supports real-time collaboration. This package provides
Python bindings for all ProtoFlux node types.

## Two Types of Chains

ProtoFlux has two fundamental chain types:

### Value Chains (Pull-Based)

Value nodes form continuous chains where downstream nodes pull values from
upstream nodes on demand. A node computes its output only when something
asks for it. These chains are **reactive** — they always reflect the
current state.

Examples: `ValueAdd<T>`, `ValueInput<T>`, `ValueLessThan<T>`

### Impulse Chains (Push-Based)

Impulse nodes execute discrete actions when triggered. An impulse pushes
execution along the chain, like imperative programming. Action nodes
receiving an impulse first **pull** all their non-impulse inputs, then
execute their action.

Examples: `Update`, `If`, `WriteDynamicValueVariable<T>`

## Impulse Sources

Impulses must originate from a trigger source:

- **`Update`** — fires every frame. Use this as the primary impulse
  source for continuously-running flow graphs.
- **`FireOnTrue` / `FireOnFalse`** — fires on a boolean rising/falling
  edge (transition detector, not continuous).
- **`CallInput`** — allows manual triggering from within Resonite
  (not callable via ResoniteLink API).
- **Dynamic Impulses** — triggered by name across ProtoFlux scripts.
- **Button/Touch Events** — triggered by user interaction.

## Impulse Flow: Sync vs Async

A **non-async** impulse chain runs entirely in one engine update. The
engine halts while it executes. Only the net difference at the end of the
update is synced across users — intermediate changes are not visible.

An **async** impulse chain can suspend and resume across multiple engine
updates (coroutines). Async flow preserves locals and action node outputs
across frames. Use `StartAsyncTask` to branch from a sync chain into an
async one. Async is useful for spreading heavy computation across multiple
frames to avoid framerate hitches.

## Execution Context

Every impulse chain runs within an execution context. The context carries:

- **Local variables** — scoped to the current impulse chain
- **Action node outputs** — results from previously-executed nodes

Context is preserved within a connected **node group** (all nodes
connected by wires or references). Context is lost when execution crosses
to a different node group (e.g. via dynamic impulses to an unconnected
group).

## Variable Types

ProtoFlux has three variable scoping levels:

### Local (`LocalValue<T>`, `LocalObject<T>`)

- Scoped to the current impulse context
- Initialized to the type's default value at the start of each context
- Discarded when the context completes
- Similar to a local variable inside a function
- **Cannot be read outside a context** — returns the default value
- Use for temporary computation within an impulse chain

### Store (`StoredValue<T>`, `StoredObject<T>`)

- Global, mutable variable scoped to the user
- **Not networked** — each user has their own independent value
- Persists across contexts and impulse chains
- Similar to a global variable in conventional programming
- Requires a `ContinuousRelay` to detect changes for driving
- Written to via the `Write` node

### Data Model Store (`DataModelValueFieldStore<T>`)

- Global, mutable variable that is **network-synchronized**
- When any user writes to it, the value propagates to all users
- Persists across contexts, sessions, and is saved with the item
- If written multiple times in one impulse, only the final value
  is synced
- Use for values that all users need to see (scores, states, etc.)
- Can also be read/written via `DynamicValueVariable` components
  on slots

## Using ProtoFlux from Python

### Value Graph Example

```python
from pyresonitelink.protoflux.core import ValueInput
from pyresonitelink.protoflux.operators import ValueAdd

FloatInput = ValueInput[primitives.Float]
FloatAdd = ValueAdd[primitives.Float]

input_a = FloatInput(primitives.Float(10.0))
input_b = FloatInput(primitives.Float(20.0))
await input_a.add_to_slot(resolink, slot)
await input_b.add_to_slot(resolink, slot)

add = FloatAdd(a=input_a, b=input_b)
await add.add_to_slot(resolink, slot)
```

### Impulse Graph Example

```python
from pyresonitelink.protoflux.flow import Update, If
from pyresonitelink.protoflux.operators import ValueLessThan

# Update fires every frame -> If branches based on condition
update = Update(on_update=if_node.id)
if_node = If(condition=less_than.id, on_true=write_a.id, on_false=write_b.id)
```

### Writing to Dynamic Variables

Use `DynamicVariableSpace` + `DynamicValueVariable<T>` on a slot for
storage, and `WriteDynamicValueVariable<T>` ProtoFlux nodes to write:

```python
from pyresonitelink.components.data.dynamic import (
    DynamicValueVariable, DynamicVariableSpace,
)
from pyresonitelink.protoflux.variables.dynamic import WriteDynamicValueVariable

space = DynamicVariableSpace()
z_var = DynamicValueVariable[primitives.Float](variable_name="z")
write = WriteDynamicValueVariable[primitives.Float](
    target=slot_ref.id, path=path.id, value=computed_value.id,
)
```

See `examples/protoflux_add.py` and `examples/protoflux_if_else.py` for
complete working examples.
