# Dergflux

Dergflux is a Pythonic domain-specific language for building ProtoFlux graphs in Resonite. Instead of manually creating and wiring dozens of components, you write Python expressions and control flow that get compiled into the equivalent ProtoFlux nodes.

## Quick Start

```python
from pyresonitelink import client
from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph

resolink = client.Client()
await resolink.connect(port)

slot = workers.Slot(id=slot_id)

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

This creates a ProtoFlux graph equivalent to: `if (x < 3) z = x + 3; else z = x - 3;`

## Core Concepts

### Graph

The `Graph` is the top-level object. It records all declarations and flow control, then materializes them on the server when you call `await g.build(resolink)`.

```python
g = Graph()
# ... declare spaces, variables, flows ...
await g.build(resolink)
```

### Under

`g.Under(slot)` is a context manager that sets the default slot for everything inside it. Flow control (`g.If`, `g.Else`) **must** be inside an `Under` block so Dergflux knows where to place the ProtoFlux nodes.

```python
with g.Under(slot):
    # Everything here uses `slot` for node placement
    ...
```

`Under` also controls **how the flow is triggered** via the `trigger` parameter. See [Triggers](#triggers) below.

### Space

A `Space` represents a `DynamicVariableSpace` component on a slot. You declare variables on it, then use them in expressions.

```python
s = g.Space(slot)               # explicit slot
s = g.Space(slot, name="MyVars") # named space
```

Inside an `Under` block, the slot is optional:

```python
with g.Under(slot):
    s = g.Space()          # inherits slot from Under
    s = g.Space(name="Vars")  # named, inherits slot
```

If a `DynamicVariableSpace` with the given name already exists on the slot, it is reused.

### Variables

Variables are declared on a `Space` using factory methods. Every primitive type in `pyresonitelink.data.primitives` has a corresponding method:

```python
s.x = s.FloatVar("x")         # float
s.n = s.IntVar("count")       # int
s.flag = s.BoolVar("active")  # bool
s.name = s.StringVar("label") # string
s.pos = s.Float3Var("pos")    # Float3 vector
s.col = s.ColorXVar("tint")   # ColorX
s.rot = s.FloatQVar("rot")    # quaternion
```

For the full list, see the `_VAR_TYPES` dict in `_space.py`. You can also use the generic `Var` method with an explicit type:

```python
from pyresonitelink.data import primitives
s.d = s.Var("d", primitives.Double)
```

#### Placing Variables on Child Slots

By default, the `DynamicValueVariable` component is created on the space's slot. You can place it on a child slot instead:

```python
s.x = s.FloatVar("x", slot=child_slot)
```

The slot must be equal to or a recursive child of the space's slot (validated at build time). Variables are only created if they don't already exist on the target slot.

### Expressions

Reading a declared variable returns an `ExprProxy` that supports Python operators:

```python
# Arithmetic
s.x + 3          # addition
s.x - 3          # subtraction
s.x * 2          # multiplication
s.x / 2          # division
s.x % 2          # modulo
-s.x             # negation

# Comparison (all return Bool)
s.x < 3          # less than
s.x <= 3         # less or equal
s.x > 3          # greater than
s.x >= 3         # greater or equal
s.x == 3         # equals
s.x != 3         # not equals

# Reflected operations
3 + s.x          # same as s.x + 3
10 - s.x         # literal on the left

# Chaining
(s.x + 3) * 2
```

**Safety**:
- `bool(proxy)` raises `TypeError` — use `g.If()` instead of Python `if`

### Flow Control

#### If / Else

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3      # true branch
    with g.Else():
        s.z = s.x - 3      # false branch
```

Both `g.If()` and `g.Else()` must be inside a `g.Under()` block. Writes (assignments to space variables) must be inside a flow block — writing outside `g.If()` raises an error.

Multiple writes per branch are supported:

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3
        s.y = s.x * 10
```

`g.Else()` is optional — you can have an `If` without it.

## Triggers

The `trigger` parameter on `g.Under()` controls what drives the impulse flow. There are three modes:

### Update (default) — fires every frame

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3
```

Creates an `Update` ProtoFlux node that fires the flow every engine frame.

### Named dynamic impulse — no argument

```python
with g.Under(slot, trigger="MyImpulse"):
    with g.If(s.x < 3):
        s.z = s.x + 3
```

Creates a `DynamicImpulseReceiver` that fires when a `DynamicImpulseTrigger` elsewhere sends an impulse with the tag `"MyImpulse"`.

### Named dynamic impulse — with typed value

```python
with g.Under(slot, trigger=("MyImpulse", primitives.Float)) as value:
    with g.If(value < 3):
        s.z = value + 3
    with g.Else():
        s.z = value - 3
```

Creates a `DynamicImpulseReceiverWithValue<Float>` that fires when triggered and provides the received value as an `ExprProxy`. Use the `as` clause to capture the value. It can be used in any expression, just like a variable read.

## Build Phase

Calling `await g.build(resolink)` materializes everything on the server:

1. **Spaces**: Creates `DynamicVariableSpace` components (skipped if already present).
2. **Variables**: Creates `DynamicValueVariable<T>` components (skipped if already present).
3. **Expressions**: Walks the AST bottom-up, creating `ValueInput<T>`, `ValueAdd<T>`, `ValueLessThan<T>`, etc.
4. **Writes**: Creates `WriteDynamicValueVariable<T>` chains (linked via `on_success`).
5. **Flow**: Creates `If` nodes wired to the condition and write chains.
6. **Trigger**: Creates `Update`, `DynamicImpulseReceiver`, or `DynamicImpulseReceiverWithValue<T>` to drive the impulse flow.

Shared sub-expressions are materialized only once (identity-cached).

## Operator Mapping

| Python operator | ProtoFlux node |
|---|---|
| `+` | `ValueAdd<T>` |
| `-` | `ValueSub<T>` |
| `*` | `ValueMul<T>` |
| `/` | `ValueDiv<T>` |
| `%` | `ValueMod<T>` |
| `<` | `ValueLessThan<T>` |
| `<=` | `ValueLessOrEqual<T>` |
| `>` | `ValueGreaterThan<T>` |
| `>=` | `ValueGreaterOrEqual<T>` |
| `==` | `ValueEquals<T>` |
| `!=` | `ValueNotEquals<T>` |
| unary `-` | `ValueSub<T>` (0 - operand) |

## Complete Example

See `examples/dergflux_if_else.py` for a working end-to-end example that builds an if-else graph and tests it with different input values.
