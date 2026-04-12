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
s.x ** 2         # power
-s.x             # negation
abs(s.x)         # absolute value

# Comparison (all return Bool)
s.x < 3          # less than
s.x <= 3         # less or equal
s.x > 3          # greater than
s.x >= 3         # greater or equal
s.x == 3         # equals
s.x != 3         # not equals

# Bitwise (for int types) / Boolean (for Bool)
s.a & s.b        # AND
s.a | s.b        # OR
s.a ^ s.b        # XOR
~s.a             # NOT / bitwise invert
s.n << 2         # left shift
s.n >> 2         # right shift

# Reflected operations
3 + s.x          # same as s.x + 3
10 - s.x         # literal on the left

# Chaining
(s.x + 3) * 2
```

**Boolean operators**: Python's `and`, `or`, `not` keywords cannot be overloaded. Use `&`, `|`, `~` instead for boolean logic on `Bool` variables. These map to `AND_Bool`, `OR_Bool`, `NOT_Bool` ProtoFlux nodes. On integer types, they perform bitwise operations (`AND_Int`, `OR_Int`, etc.).

**Safety**:
- `bool(proxy)` raises `TypeError` — use `g.If()` instead of Python `if`

**String is an object type**: Resonite treats ``string`` as an object
type, not a value type.  Dergflux handles this automatically — string
constants use ``ValueObjectInput<string>``, string variable reads use
``ReadDynamicObjectVariable<string>``, and string writes use
``WriteDynamicObjectVariable<string>``.  See
[Dynamic Variables: Value Types vs Object Types](dynamic_variables.md#value-types-vs-object-types)
for details.

### Math Functions

Import the math module for functions that don't have Python operators:

```python
from pyresonitelink.dergflux import math as dm
```

#### Trigonometric

```python
dm.sin(s.x)          # sine
dm.cos(s.x)          # cosine
dm.tan(s.x)          # tangent
dm.asin(s.x)         # arc sine
dm.acos(s.x)         # arc cosine
dm.atan(s.x)         # arc tangent
dm.atan2(s.y, s.x)   # two-argument arc tangent
```

#### Exponential / Logarithmic

```python
dm.exp(s.x)          # e^x
dm.log(s.x)          # natural log (ln)
dm.log10(s.x)        # base-10 log
dm.sqrt(s.x)         # square root
s.x ** s.y           # power (uses ** operator)
```

#### Rounding

```python
dm.ceil(s.x)         # ceiling (round up)
dm.floor(s.x)        # floor (round down)
dm.round_(s.x)       # round to nearest (note trailing _)
```

#### Sign / Value

```python
dm.sign(s.x)         # sign (-1, 0, or 1)
abs(s.x)             # absolute value (uses abs() builtin)
dm.clamp01(s.x)      # clamp to [0, 1]
dm.square(s.x)       # x^2 (generic ValueSquare<T>)
dm.cube(s.x)         # x^3 (generic ValueCube<T>)
dm.reciprocal(s.x)   # 1/x (generic ValueReciprocal<T>)
dm.one_minus(s.x)    # 1 - x (generic ValueOneMinus<T>)
```

#### Min / Max / Clamp

```python
dm.min_(s.x, s.y)          # minimum (note trailing _)
dm.max_(s.x, s.y)          # maximum (note trailing _)
dm.clamp(s.x, lo, hi)      # clamp to [lo, hi]
```

#### Interpolation

```python
dm.lerp(s.a, s.b, s.t)          # linear interpolation
dm.inverse_lerp(s.a, s.b, s.x)  # inverse lerp (find t)
dm.smoothstep(edge0, edge1, s.x) # Hermite smoothstep
```

#### Conditional

```python
dm.conditional(s.flag, s.a, s.b)  # if flag then a else b
```

This is a value-level conditional (like C's ternary `?:`) — it selects between two values based on a `Bool`, without creating an impulse flow.

### Flow Control

All flow control must be inside a `g.Under(slot)` block.  Multiple
flow statements inside a single `Under` block are chained via a
ProtoFlux `Sequence` node — each runs to completion before the next
starts.

#### If / Else

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3      # true branch
    with g.Else():
        s.z = s.x - 3      # false branch
```

Multiple writes per branch are supported. `g.Else()` is optional.

#### Continuation after If / Else

Bare writes after a flow block are continuation statements — they run
after the preceding flow completes:

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3
    with g.Else():
        s.z = s.x - 3

    # Runs after either branch completes (via Sequence)
    s.z = s.z + 1
```

At build time, the `If` and the bare write become two entries in a
`Sequence` node.  The trigger drives the Sequence, which fires the
If first, waits for it to complete, then fires the bare write.

#### For

```python
with g.Under(slot):
    with g.For(10) as f:
        with f.OnStart():
            s.total = 0          # runs once before the loop
        with f.OnIterate() as i:
            s.total = s.total + i  # runs each iteration
```

`g.For(count)` yields a `ForProxy` with two context managers:

- **`f.OnStart()`** — statements go to `loop_start`, runs once before the first iteration.
- **`f.OnIterate()`** — yields an `ExprProxy` for the iteration index (Int), statements go to `loop_iteration`.

The count can be a literal or an expression.  Optional `reverse=True`
iterates in reverse order.

Code after the `with g.For()` block continues from `loop_end`:

```python
with g.Under(slot):
    with g.For(10) as f:
        with f.OnStart():
            s.total = 0
        with f.OnIterate() as i:
            s.total = s.total + i

    # Runs once after the loop finishes (via Sequence)
    with g.If(s.total > 30):
        s.total = s.total * 2
```

#### Range

```python
with g.Under(slot):
    with g.Range(0, 10, 2) as f:     # start=0, end=10, step=2
        with f.OnIterate() as i:
            s.total = s.total + i
```

Like Python's ``range()``, iterates from ``start`` to ``end`` with
``step`` increments.  Uses the same ``ForProxy`` as ``g.For()``, so
``f.OnStart()`` and ``f.OnIterate()`` work identically.  The step
defaults to 1 if omitted.

At build time, creates a ProtoFlux ``RangeLoopInt`` node.

#### While

```python
with g.Under(slot):
    with g.While(s.x > 0):
        s.x = s.x - 1
```

Repeats the body as long as `condition` is true. The condition is
re-evaluated each iteration. Statements go to `loop_iteration`.

Code after the `with g.While()` block continues from `loop_end`.

#### Action Nodes

Action nodes are ProtoFlux nodes triggered by an impulse that branch
into alternate flow paths and optionally produce value outputs.  They
are accessed as named methods on the Graph.

**RaycastOne** — cast a ray with hit/miss branches:

```python
with g.Under(slot):
    with g.RaycastOne(origin=s.pos, direction=s.dir, max_distance=100) as r:
        with r.on_hit():
            s.hit_pos = r.hit_point
            s.distance = r.hit_distance
        with r.on_miss():
            s.distance = -1
```

Value outputs: ``r.hit_point`` (Float3), ``r.hit_normal`` (Float3),
``r.hit_distance`` (Float), ``r.hit_triangle_index`` (Int).

**PlayOneShotAndWait** — play audio with start/finish callbacks:

```python
with g.Under(slot, trigger="play"):
    with g.PlayOneShotAndWait(clip=clip_ref, volume=1.0) as r:
        with r.on_started_playing():
            s.state = "playing"
        with r.on_finished_playing():
            s.state = "finished"
```

**PlayOneShot** — play audio (fire and forget):

```python
with g.Under(slot):
    with g.PlayOneShot(clip=clip_ref) as r:
        with r.on_started_playing():
            s.playing = True
```

#### Event Source Nodes

Some nodes fire impulses on their own when events occur, rather than
being triggered by an impulse.  These don't need an explicit trigger
(Update, DynamicImpulseReceiver) — the builder skips trigger creation
automatically.

**Lifecycle events** — fire once on specific lifecycle events:

```python
with g.Under(slot):
    with g.OnStart() as e:
        with e.trigger():
            s.log = "started"

    with g.OnActivated() as e:
        with e.trigger():
            s.log = "activated"

    with g.OnDeactivated() as e:
        with e.trigger():
            s.log = "deactivated"
```

Also: ``OnDestroy``, ``OnDestroying``, ``OnLoaded``, ``OnDuplicate``,
``OnPaste``, ``OnSaving``, ``OnPackageImported``.

``OnActivated``, ``OnDeactivated``, ``OnStart``, and ``OnDestroy``
accept an optional ``only_host=True`` to restrict to the host user.

**Condition-based event sources**:

```python
with g.Under(slot):
    # Fire once when condition becomes true (rising edge)
    with g.FireOnTrue(condition=s.flag) as e:
        with e.on_changed():
            s.count = s.count + 1

    # Fire once when condition becomes false (falling edge)
    with g.FireOnFalse(condition=s.flag) as e:
        with e.on_changed():
            s.result = s.x

    # Fire every frame while condition is true
    with g.FireWhileTrue(condition=s.active) as e:
        with e.on_update():
            s.elapsed = s.elapsed + 1
```

Local variants (``FireOnLocalTrue``, ``FireOnLocalFalse``,
``LocalFireWhileTrue``) only fire for the local user.

**Value-change event sources**:

```python
with g.Under(slot):
    with g.FireOnValueChange(value=s.x) as e:
        with e.on_changed():
            s.change_count = s.change_count + 1
```

Also: ``FireOnLocalValueChange``, ``FireOnObjectValueChange``,
``FireOnLocalObjectChange``, ``FireOnRefChange``, ``FireOnTypeChange``.

**Timer event sources**:

```python
with g.Under(slot):
    # Fire every 60 engine updates
    with g.UpdatesTimer(interval=60) as e:
        with e.on_update():
            s.tick = s.tick + 1

    # Fire every 1.0 seconds
    with g.SecondsTimer(interval=1.0) as e:
        with e.on_update():
            s.seconds = s.seconds + 1
```

**Delay** (async — suspends across frames):

```python
with g.Under(slot):
    # Delay by seconds
    with g.DelaySeconds(duration=2.0) as d:
        with d.next():
            s.state = "waiting"      # fires immediately
        with d.on_triggered():
            s.state = "delayed"      # fires after 2 seconds

    # Delay by engine updates
    with g.DelayUpdates(updates=2) as d:
        with d.on_triggered():
            s.state = "after 2 updates"

    # Delay by updates OR seconds (whichever first)
    with g.DelayUpdatesOrSeconds(updates=60, duration=1.0) as d:
        with d.on_triggered():
            s.state = "after 60 updates or 1 second"
```

**SlotChildrenEvents** — fires when children are added/removed:

```python
with g.Under(slot):
    with g.SlotChildrenEvents(instance=watched_slot) as e:
        with e.on_child_added():
            s.last_child = e.child
        with e.on_child_removed():
            s.removed_child = e.child
```

The ``instance`` input accepts a Slot instance directly — the builder
auto-creates a ``GlobalReference<Slot>`` bridge (since the node's
``Instance`` member requires ``IGlobalValueProxy<Slot>``).

Value output: ``e.child`` — the child Slot that was added or removed.

#### Data Source Nodes

Data source nodes are ProtoFlux nodes that provide value outputs
without any flow (no impulses, no triggers).  They compute values
on demand — other nodes pull from them.  Unlike action nodes (which
are context managers with flow branches), data sources are plain
calls that return a proxy with value output properties.

Data sources use the same ``ActionDef`` system as action nodes, but
with ``flow_outputs=[]``.  They're created with ``g.DataSource()``
or named shortcuts.

```python
ctrl = g.StandardController(user=user_ref, node=chirality, slot=slot)

# ctrl.primary, ctrl.grab, ctrl.axis etc. are ExprProxy values
# usable anywhere an expression is expected
with g.Under(slot):
    with g.FireOnTrue(condition=ctrl.primary) as e:
        with e.on_changed():
            s.log = "primary pressed"

    s.grip_value = ctrl.grab * 100
```

**Built-in controller data sources**:

- ``g.StandardController(user, node)`` — outputs: ``is_active``,
  ``primary``, ``secondary``, ``grab``, ``menu``, ``strength``,
  ``axis``, ``battery_level``, ``is_battery_charging``
- ``g.IndexController(user, node)`` — outputs: ``button_a``,
  ``button_b``, ``grip``, ``trigger``, ``thumbstick_x/y``,
  ``trackpad_x/y``, and touch/press variants
- ``g.TouchController(user, node)`` — similar to Index
- ``g.ViveController(user, node)`` — outputs: ``grip``, ``trigger``,
  ``trigger_hair``, ``trigger_click``, ``touchpad`` (float2),
  ``touchpad_touch``, ``touchpad_click``, ``app``

#### Defining Custom Data Sources

Any ProtoFlux value node can be wrapped as a data source using
``ActionDef`` with ``flow_outputs=[]``:

```python
from pyresonitelink.dergflux import ActionDef, InputDef, OutputDef
from pyresonitelink.data import primitives

MyDataSource = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="StandardController",
    inputs={
        "user": InputDef("user"),          # reference input
        "node": InputDef("node"),          # reference input
    },
    flow_outputs=[],                        # no flow — data source only
    value_outputs={
        "primary": OutputDef("Primary", primitives.Bool),
        "grab": OutputDef("Grab", primitives.Float),
    },
)
```

Use it with ``g.DataSource()``:

```python
src = g.DataSource(MyDataSource, user=user_ref, node=chirality, slot=slot)
# src.primary and src.grab are ExprProxy values
```

The key difference from action nodes:
- **Action nodes** (``flow_outputs`` is non-empty): used as context
  managers inside ``g.Under()``, with flow branch context managers.
- **Data source nodes** (``flow_outputs=[]``): used as plain calls,
  return a proxy with value output properties.  Can be created inside
  or outside ``g.Under()`` (with an explicit ``slot`` parameter).

#### Indexed Branch Nodes

Some nodes route impulses to one of N indexed outputs (via SyncList).
Use ``proxy[i]`` as context managers to record statements for each
branch.

**PulseRandom** — randomly fire one of N branches:

```python
with g.Under(slot):
    with g.PulseRandom(3) as pr:
        with pr[0]:
            s.log = "zero"
        with pr[1]:
            s.log = "one"
        with pr[2]:
            s.log = "two"
```

**ImpulseMultiplexer** — route to branch selected by index:

```python
with g.Under(slot):
    with g.ImpulseMultiplexer(3, index=s.idx) as mux:
        with mux[0]:
            s.log = "route 0"
        with mux[1]:
            s.log = "route 1"
        with mux[2]:
            s.log = "route 2"
```

**ImpulseDemultiplexer** — N indexed inputs, fires with which triggered:

```python
with g.Under(slot):
    with g.ImpulseDemultiplexer(3) as demux:
        with demux.on_triggered():
            s.last_input = demux.index  # Int: which input fired
```

The indexed inputs can be wired from external impulse sources.

#### Defining Custom Actions

Any ProtoFlux node with flow outputs can be wrapped as an action using
``ActionDef`` — no custom proxy or builder code needed:

```python
from pyresonitelink.dergflux import ActionDef, InputDef, OutputDef
from pyresonitelink.data import primitives

MyAction = ActionDef(
    import_path="protoflux.physics",      # module under pyresonitelink
    class_name="RaycastOne",              # class to import
    inputs={
        "origin": InputDef("origin", primitives.Float3),
        "direction": InputDef("direction", primitives.Float3),
    },
    flow_outputs=["on_hit", "on_miss"],   # become context managers
    value_outputs={                        # become ExprProxy properties
        "hit_distance": OutputDef("HitDistance", primitives.Float),
    },
)
```

Use it with ``g.Action()``:

```python
with g.Action(MyAction, origin=s.pos, direction=s.dir) as r:
    with r.on_hit():
        s.distance = r.hit_distance
```

Or add a named shortcut method on Graph that delegates to ``g.Action()``.

**InputDef options** for reference inputs:

- ``ref_type="..."`` — auto-creates ``RefObjectInput<type>`` when a
  component is passed.  Used for ``INodeObjectOutput`` inputs.
- ``global_type="..."`` — auto-creates ``GlobalReference<type>`` when a
  component/slot is passed.  Used for ``IGlobalValueProxy`` inputs.

**ActionDef flags**:

- ``is_async=True`` — the node is async; enclosing flow uses async variants
  and ``StartAsyncTask`` bridge.
- ``is_event_source=True`` — the node fires its own impulses (no trigger
  created).  Use for event monitors like ``SlotChildrenEvents``.

### Generic Action Nodes

Many ProtoFlux nodes follow a common pattern: they take value inputs,
have multiple flow outputs (branches), and optionally produce value
outputs.  Instead of implementing each one as a custom DSL construct,
define them once with ``ActionDef`` and use them with ``g.Action()``.

#### Defining an action

```python
from pyresonitelink.dergflux import ActionDef, InputDef, OutputDef
from pyresonitelink.data import primitives

MyAction = ActionDef(
    import_path="protoflux.physics",      # module under pyresonitelink
    class_name="RaycastOne",              # class to import
    inputs={
        "origin": InputDef("origin", primitives.Float3),
        "direction": InputDef("direction", primitives.Float3),
        "max_distance": InputDef("max_distance", primitives.Float),
    },
    flow_outputs=["on_hit", "on_miss"],   # become context managers
    value_outputs={                        # become ExprProxy properties
        "hit_point": OutputDef("HitPoint", primitives.Float3),
        "hit_distance": OutputDef("HitDistance", primitives.Float),
    },
)
```

#### Using an action

```python
with g.Under(slot):
    with g.Action(MyAction, origin=s.pos, direction=s.dir) as r:
        with r.on_hit():
            s.distance = r.hit_distance
        with r.on_miss():
            s.distance = -1
```

- Flow outputs (``on_hit``, ``on_miss``) are context managers on the proxy.
- Value outputs (``hit_distance``, ``hit_point``) are ``ExprProxy`` properties.
- Inputs are passed as keyword arguments matching the keys in ``inputs``.

#### Prebuilt actions

``pyresonitelink.dergflux.actions`` provides ready-to-use definitions:

- **``actions.RaycastOne``** — ray cast with on_hit/on_miss and hit result outputs
- **``actions.PlayOneShot``** — play audio with on_started_playing
- **``actions.PlayOneShotAndWait``** — play audio with on_started_playing/on_finished_playing

```python
from pyresonitelink.dergflux import actions

with g.Under(slot):
    with g.Action(actions.RaycastOne, origin=s.pos, direction=s.dir) as r:
        with r.on_hit():
            s.hit_pos = r.hit_point
```

### Bindings

``g.Bind()`` permanently binds a value source to a component field.
The field always reflects the source's current value.  **A field can
only be bound once** — attempting to rebind raises ``RuntimeError``.

The binding mechanism depends on the source:

- **Dynamic variable** (e.g. ``s.x``): Creates a
  ``DynamicValueVariableDriver<T>`` (for value types like int, float,
  Float3) or ``DynamicReferenceVariableDriver<T>`` (for reference
  types like Slot).  The driver reads the named variable by path and
  continuously drives the target field.
- **General expression** (e.g. ``i``, ``s.x + 1``): Creates a
  ``ValueFieldDrive<T>`` driven by the ProtoFlux expression.

```python
# Bind a loop counter to a field (uses ValueFieldDrive)
with g.Under(slot):
    with g.For(3) as f:
        with f.OnIterate() as i:
            g.Bind(i, mux, "Index")

# Bind a dynamic variable to a field (uses DynamicValueVariableDriver)
g.Bind(s.volume, audio_output, "Volume", slot=slot)
```

For named spaces, the variable path is automatically prefixed with
the space name (e.g. ``"Audio/vol"`` for a variable ``vol`` in space
``Audio``).

Arguments:

- ``expr`` — an ExprProxy or literal value to bind from
- ``component`` — the target component (a generated component instance)
- ``member_name`` — the Resonite member name to bind to (e.g. ``"Index"``)
- ``slot`` — optional; defaults to the active ``Under()`` slot

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

### Sync vs Async Flow

ProtoFlux distinguishes sync and async impulse flow. Operations like
`PlayOneShotAndWait` are async — they suspend across frames. When an
`Under` block contains async actions, Dergflux automatically uses
async flow node variants (`AsyncFor`, `AsyncSequence`,
`AsyncDynamicImpulseReceiver`). Sync operations like variable writes
and `If` work in both contexts because `ISyncNodeOperation` extends
`INodeOperation`.

See [Sync vs Async Flow](async_flow.md) for the full technical details.

## Build Phase

Calling `await g.build(resolink)` materializes everything on the server:

1. **Spaces**: Creates `DynamicVariableSpace` components (skipped if already present).
2. **Variables**: Creates `DynamicValueVariable<T>` components (skipped if already present).
3. **Expressions**: Walks the AST bottom-up, creating operator and math nodes.
4. **Writes**: Creates `WriteDynamicValueVariable<T>` chains (linked via `on_success`).
5. **Flow**: Creates `If` nodes wired to the condition and write chains.
6. **Trigger**: Creates `Update`, `DynamicImpulseReceiver`, or `DynamicImpulseReceiverWithValue<T>` to drive the impulse flow.

Shared sub-expressions are materialized only once (identity-cached).

## Operator Reference

### Arithmetic (generic `Value*<T>` nodes)

| Python | ProtoFlux node |
|---|---|
| `+` | `ValueAdd<T>` |
| `-` | `ValueSub<T>` |
| `*` | `ValueMul<T>` |
| `/` | `ValueDiv<T>` |
| `%` | `ValueMod<T>` |
| unary `-` | `ValueNegate<T>` |
| `abs()` | `ValueAbs<T>` |

### Power (typed `Pow_*` nodes)

| Python | ProtoFlux node |
|---|---|
| `**` | `Pow_Float`, `Pow_Double`, etc. |

### Comparison (generic `Value*<T>` nodes, result is `Bool`)

| Python | ProtoFlux node |
|---|---|
| `<` | `ValueLessThan<T>` |
| `<=` | `ValueLessOrEqual<T>` |
| `>` | `ValueGreaterThan<T>` |
| `>=` | `ValueGreaterOrEqual<T>` |
| `==` | `ValueEquals<T>` |
| `!=` | `ValueNotEquals<T>` |

### Bitwise / Boolean (typed `*_Bool`, `*_Int`, etc.)

| Python | Bool type | Int types |
|---|---|---|
| `&` | `AND_Bool` | `AND_Int`, `AND_Long`, etc. |
| `\|` | `OR_Bool` | `OR_Int`, `OR_Long`, etc. |
| `^` | `XOR_Bool` | `XOR_Int`, `XOR_Long`, etc. |
| `~` | `NOT_Bool` | `NOT_Int`, `NOT_Long`, etc. |
| `<<` | — | `ShiftLeft_Int`, `ShiftLeft_Long`, etc. |
| `>>` | — | `ShiftRight_Int`, `ShiftRight_Long`, etc. |

### Math Functions (typed `*_Float`, `*_Double`, etc.)

| Function | ProtoFlux node |
|---|---|
| `dm.sin(x)` | `Sin_Float`, `Sin_Double`, etc. |
| `dm.cos(x)` | `Cos_Float`, `Cos_Double`, etc. |
| `dm.tan(x)` | `Tan_Float`, `Tan_Double`, etc. |
| `dm.asin(x)` | `Asin_Float`, etc. |
| `dm.acos(x)` | `Acos_Float`, etc. |
| `dm.atan(x)` | `Atan_Float`, etc. |
| `dm.atan2(y, x)` | `Atan2_Float`, etc. |
| `dm.exp(x)` | `Exp_Float`, etc. |
| `dm.log(x)` | `Log_Float`, etc. |
| `dm.log10(x)` | `Log10_Float`, etc. |
| `dm.sqrt(x)` | `Sqrt_Float`, etc. |
| `dm.ceil(x)` | `Ceil_Float`, etc. |
| `dm.floor(x)` | `Floor_Float`, etc. |
| `dm.round_(x)` | `Round_Float`, etc. |
| `dm.sign(x)` | `Sign_Float`, `Sign_Int`, etc. |
| `dm.clamp01(x)` | `Clamp01_Float`, etc. |
| `dm.smoothstep(e0, e1, x)` | `SmoothStep_Float`, etc. |

### Math Functions (generic `Value*<T>` nodes)

| Function | ProtoFlux node |
|---|---|
| `dm.square(x)` | `ValueSquare<T>` |
| `dm.cube(x)` | `ValueCube<T>` |
| `dm.reciprocal(x)` | `ValueReciprocal<T>` |
| `dm.one_minus(x)` | `ValueOneMinus<T>` |
| `dm.min_(a, b)` | `ValueMin<T>` |
| `dm.max_(a, b)` | `ValueMax<T>` |
| `dm.clamp(v, lo, hi)` | `ValueClamp<T>` |
| `dm.lerp(a, b, t)` | `ValueLerp<T>` |
| `dm.inverse_lerp(a, b, v)` | `ValueInverseLerp<T>` |
| `dm.conditional(c, t, f)` | `ValueConditional<T>` |

## Complete Example

See `examples/dergflux_if_else.py` for a working end-to-end example that builds an if-else graph and tests it with different input values.
