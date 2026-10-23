# Dergflux

Dergflux is a Pythonic domain-specific language for building ProtoFlux graphs in Resonite. Instead of manually creating and wiring dozens of components, you write Python expressions and control flow that get compiled into the equivalent ProtoFlux nodes.

## Table of Contents

- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
  - [Graph](#graph)
  - [Under](#under)
  - [Space](#space)
  - [Variables](#variables)
  - [Model Variables](#model-variables)
  - [Expressions](#expressions)
  - [Math Functions](#math-functions)
  - [Type Conversions](#type-conversions)
  - [Time and Dates](#time-and-dates)
  - [Strings](#strings)
  - [Slots and Transforms](#slots-and-transforms)
  - [Variables on Other Slots](#variables-on-other-slots)
  - [Users and Grabbing](#users-and-grabbing)
  - [Mouse](#mouse)
- [Flow Control](#flow-control)
  - [If / Else](#if--else)
  - [Continuation](#continuation-after-if--else)
  - [For](#for), [Range](#range), [While](#while)
  - [Indexed Branch Nodes](#indexed-branch-nodes)
- [Bindings](#bindings)
- [Actions](#actions)
  - [Action Nodes](#action-nodes)
  - [Slot Actions](#slot-actions)
  - [Transform Setters](#transform-setters)
  - [Defining Custom Actions](#defining-custom-actions)
- [Data Sources](#data-sources)
  - [Data Source Nodes](#data-source-nodes)
  - [Defining Custom Data Sources](#defining-custom-data-sources)
- [Event Source Nodes](#event-source-nodes)
- [Triggers](#triggers)
  - [Update (default)](#update-default--fires-every-frame)
  - [Named dynamic impulse](#named-dynamic-impulse--no-argument)
  - [Named dynamic impulse with value](#named-dynamic-impulse--with-typed-value)
  - [Sync vs Async Flow](#sync-vs-async-flow)
- [Build Phase](#build-phase)
- [Operator Reference](#operator-reference)
- [Complete Example](#complete-example)

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
s.x = s.FloatDynVar("x")
s.z = s.FloatDynVar("z")

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
s = g.Space(slot, space_name="MyVars") # named space
```

Inside an `Under` block, the slot is optional:

```python
with g.Under(slot):
    s = g.Space()          # inherits slot from Under
    s = g.Space(space_name="Vars")  # named, inherits slot
```

If a `DynamicVariableSpace` with the given name already exists on the slot, it is reused.

### Variables

Variables are declared on a `Space` using factory methods. Every primitive type in `pyresonitelink.data.primitives` has a corresponding method:

```python
s.x = s.FloatDynVar("x")         # float
s.n = s.IntDynVar("count")       # int
s.flag = s.BoolDynVar("active")  # bool
s.name = s.StringDynVar("label") # string
s.pos = s.Float3DynVar("pos")    # Float3 vector
s.col = s.ColorXDynVar("tint")   # ColorX
s.rot = s.FloatQDynVar("rot")    # quaternion
```

For the full list, see the `_VAR_TYPES` dict in `_space.py`. You can also use the generic `Var` method with an explicit type:

```python
from pyresonitelink.data import primitives
s.d = s.Var("d", primitives.Double)
```

#### Placing Variables on Child Slots

By default, the `DynamicValueVariable` component is created on the space's slot. You can place it on a child slot instead:

```python
s.x = s.FloatDynVar("x", slot=child_slot)
```

The slot must be equal to or a recursive child of the space's slot (validated at build time). Variables are only created if they don't already exist on the target slot.

### Model Variables

Model variables use `DataModelValueFieldStore<T>` instead of dynamic variables. They avoid the [dynamic variable binding delay](https://wiki.resonite.com/Dynamic_variables#Binding) that requires 2+ update cycles after creating a `DynamicVariableSpace`. Model variables are:

- **Network-synchronized**: changes propagate to all users
- **Immediately available**: no binding delay after creation
- **Stored in the data model**: persist across sessions
- **Named by slot**: each variable lives on its own child slot for clarity

Declare model variables with `*ModelVar` methods:

```python
s.x = s.FloatModelVar("x")
s.n = s.IntModelVar("count")
s.flag = s.BoolModelVar("active")
s.name = s.StringModelVar("label")
s.owner = s.UserModelVar("owner")
```

A `UserModelVar` holds a reference to a user in a `DataModelUserRefStore`, which ProtoFlux writes with `ObjectWrite<FrooxEngineContext, User>`. It reads as null once the user has left the session, which `math.is_null` tests.

#### How Model Variables Work

Under the hood, each model variable creates:

1. A **child slot** named after the variable (e.g. `"x"`)
2. A `DataModelValueFieldStore<T>` component on that slot — this is both readable (`INodeValueOutput<T>`) and writable (`IVariable`)
3. An auto-generated `+Store` companion component with a `Value` field for the actual stored value

**Reading**: other ProtoFlux nodes reference the `DataModelValueFieldStore` component ID directly as `INodeValueOutput<T>`.

**Writing**: uses `ValueWrite<FrooxEngineContext, T>` (not `ValueWrite<T>`). The `FrooxEngineContext` type parameter makes the write compatible with the data model store's `IVariable` interface.

**Initial values**: set via the `+Store` companion's `Value` field.

#### Reading and Writing Model Variables from Python

After `g.build()`, `await s.ReadModelVar(resolink, "x")` reads a model variable's current value from its +Store component, and `await s.WriteModelVar(resolink, "x", value)` writes it. The name is the variable's attribute on the Space. A flow that writes the same variable in the same engine update may overwrite a written value.

`pyresonitelink.utils.recorder.Recorder` uses these to record values from inside a running flow, one line per `record()` call, for a script to read in one request afterwards. Polling the values through ResoniteLink instead would sample them at arbitrary points in an update and skip updates.

```python
rec = recorder.Recorder(g, s, "trace")
with g.Under(slot):
    ...
    rec.record(where="end", p=p, v=s.v)   # vectors become p.x, p.y, p.z
await g.build(resolink)
await rec.start(resolink, lines=300)
rows = await rec.read(resolink)            # [{"t": ..., "where": "end", "p.x": ...}, ...]
```

#### When to Use Model Variables vs Dynamic Variables

| Feature | Dynamic Variables | Model Variables |
|---------|------------------|-----------------|
| Binding delay | 2+ frames | None |
| Networking | Via DynamicVariableSpace | Built-in |
| ProtoFlux read | `ReadDynamicValueVariable` (member ID wiring) | Direct component ID reference |
| ProtoFlux write | `WriteDynamicValueVariable` | `ValueWrite<FrooxEngineContext, T>` |
| Variable path | `SpaceName/VarName` string | Named child slot |
| Suitable for | Existing dynamic variable systems | New Dergflux graphs |

**Recommendation**: prefer model variables (`*ModelVar`) for new Dergflux graphs. Use dynamic variables (`*Var`) only when interoperating with existing dynamic variable systems.

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
dm.lerp(s.a, s.b, s.t)            # a + (b - a) * t, with t clamped to [0, 1]
dm.lerp_unclamped(s.a, s.b, s.t)  # the same without the clamp
dm.inverse_lerp(s.a, s.b, s.x)    # (x - a) / (b - a), the t that lerp(a, b, t) maps to x
```

`a` and `b` can be numbers or vectors, and the result of `lerp` has their common type. The lerp nodes take `t` as a Float whatever the values' type, so a Double `t` raises `TypeError` until it's converted with `dm.to_float`. `inverse_lerp` isn't clamped. For numbers its result is a Float, even when the arguments are Doubles. For vectors from Float2 to Double4 it works per component and gives a vector of the arguments' type.

#### Shaping

```python
dm.smoothstep(s.x)                # 3x² - 2x³
dm.smoothstep(edge0, edge1, s.x)  # 0 at or below edge0, 1 at or above edge1, as in GLSL
dm.smootherstep(s.x)              # 6x⁵ - 15x⁴ + 10x³
dm.smootherstep(edge0, edge1, s.x)
```

ProtoFlux's SmoothStep and SmootherStep nodes don't clamp their input, so with one argument the result leaves [0, 1] when `x` does. The three-argument forms map `x` to 0 at `edge0` and 1 at `edge1`, and clamp it, before the node. The result is a Double if any argument is one, and a Float otherwise.

#### Rotations

```python
dm.axis_angle(primitives.Float3(0, 1, 0), s.degrees)  # a FloatQ
dm.from_euler(s.angles)                               # Euler angles, a Float3
```

Both take degrees, as the AxisAngle and FromEuler nodes do, and `axis_angle` normalizes the axis. Float arguments give a `FloatQ`. A `Double` or `Double3` argument gives a `DoubleQ`, and the other argument is widened to match. A positive angle turns +Y toward +Z about +X, which in Resonite's left-handed coordinates is clockwise seen from the tip of the axis.

#### Conditional

```python
dm.conditional(s.flag, s.a, s.b)  # if flag then a else b
```

This is a value-level conditional (like C's ternary `?:`) — it selects between two values based on a `Bool`, without creating an impulse flow.

#### Vectors

```python
dm.dot(s.a, s.b)         # a number of the vectors' element type
dm.cross(s.a, s.b)       # Float3 or Double3 only
dm.magnitude(s.v)        # a vector's length
dm.normalized(s.v)       # length 1, or the zero vector unchanged
dm.distance(s.p, s.q)    # between two points
dm.pack(s.x, 0, s.z)     # a Float3 from three numbers
s.v.x, s.v.y, s.v.z      # a vector's elements
s.v * s.f, s.f * s.v     # a vector times a number
s.v / s.f, s.f / s.v     # divided element by element
s.q * s.v                # a FloatQ rotating a Float3
```

These take vectors of floats or doubles, from Float2 to Double4, and raise `TypeError` for vectors of integers. Two vectors are widened to their common type first. The elements of one vector expression come from one Unpack node, such as `Unpack_Float3`, whose outputs are `X`, `Y`, `Z`, and `W`. A vector with a number uses the typed nodes such as `Mul_Float3_Float` and `Div_Float_Float3`, and the number is widened to the vector's element type, or the vector to a vector of the number's type. An int literal takes the element type without a Cast node, so `s.v * 2` is a `Mul_Float3_Float`. A `FloatQ` times a `Float3` uses `Mul_FloatQ_Float3`, and a `DoubleQ` times a `Double3` uses `Mul_DoubleQ_Double3`. Vector plus or minus vector still uses the generic `ValueAdd<T>` and `ValueSub<T>`.

### Type Conversions

Dergflux follows C#'s implicit numeric conversions, which only widen. When two operands of an operator differ in type, both are converted to the narrowest type they both widen to, and a `Cast_<from>_To_<to>` node is added for each one that changes:

```python
s.total = s.total + i     # float + int: i is widened to float
s.big = s.count + s.flags # int + uint: both are widened to long
s.v = s.ints3 + s.floats3 # int3 + float3: the int3 is widened to float3
```

The same applies to assignments, to the arguments of two-argument math functions such as `dm.min_`, to the two values of `dm.conditional`, and to the arguments of the `time` functions. An int literal takes the type of the other operand, but a float literal next to an int widens the int, so `s.count + 2.5` is a float rather than a truncated int. A literal of a `primitives` type, such as `primitives.Double(2.5)` or `primitives.Float3(0, 1, 0)`, has that type from the start.

Narrowing needs an explicit conversion, and Dergflux raises a `TypeError` at the line that would narrow:

```python
s.count = s.ratio * 10            # TypeError: Float doesn't convert to Int implicitly
s.count = dm.to_int(s.ratio * 10) # truncates toward zero, as C#'s (int) cast does
s.count = dm.convert(s.x, primitives.Int)  # the same, for any type
```

`dm.to_int`, `dm.to_long`, `dm.to_float`, and `dm.to_double` are shorthands for `dm.convert`. Types with no conversion between them, such as `Bool` and `Int`, raise a `TypeError` too.

### Time and Dates

`DateTime` and `TimeSpan` values are Python `datetime.datetime` and `datetime.timedelta` objects, so literals can be used directly. The `time` module provides the ProtoFlux time nodes:

```python
import datetime
from pyresonitelink.dergflux import time

s.started = s.DateTimeModelVar("started")
s.waited = s.TimeSpanModelVar("waited")

s.started = time.utc_now()
s.waited = time.utc_now() - s.started            # DateTime - DateTime is a TimeSpan
s.deadline = s.started + time.minutes(5)          # DateTime + TimeSpan is a DateTime
s.later = s.started + datetime.timedelta(hours=1) # literals work too
s.seconds = s.waited.total_seconds                # a Double
```

| Function or property | Result type | Node |
|---|---|---|
| `time.utc_now()` | DateTime | `UtcNow` |
| `time.world_time()` | Double | `WorldTimeDouble` |
| `time.delta_time()` and its `smooth_`, `raw_`, and `inverted_` variants | Float | `DeltaTime` etc. |
| `time.days(n)`, `hours`, `minutes`, `seconds`, `milliseconds` | TimeSpan | `TimeSpanFrom*`, which take a double |
| `time.ticks(n)` | TimeSpan | `TimeSpanFromTicks`, which takes a long |
| `time.from_unix_seconds(n)`, `from_unix_milliseconds(n)` | DateTime, in UTC | `FromUnix*`, which take a long |
| `time.to_unix_seconds(dt)`, `to_unix_milliseconds(dt)` | Long | `ToUnix*` |
| `dt.year`, `month`, `day`, `hour`, `minute`, `second`, `millisecond`, `day_of_year` | Int | `DateTime*` |
| `dt.ticks`, `span.ticks` | Long | `DateTimeTicks`, `TimeSpanTicks` |
| `span.days`, `hours`, `minutes`, `seconds`, `milliseconds` | Int | `TimeSpan*` |
| `span.total_days`, `total_hours`, `total_minutes`, `total_seconds`, `total_milliseconds` | Double | `TimeSpanTotal*` |

`time.world_time()` is the world's time in seconds. It starts at 0 when the session starts, and each user's copy follows the host's. To count from some moment, store the world time then and subtract it, as `examples/dergflux_number_wheel.py` does. ProtoFlux's Elapsed Time nodes return the same value as the world time until their Reset impulse sets a start time, and Dergflux can't send that impulse, so Dergflux has no elapsed time function.

`dt.day_of_week` isn't supported, because the `DateTimeDayOfWeek` node outputs a `System.DayOfWeek` enum, which Dergflux has no type for.

ResoniteLink sends both types as strings. A DateTime with a `Z` suffix becomes an aware `datetime` in UTC, and one without a suffix becomes a naive `datetime`. An aware `datetime` is sent as UTC. Python keeps microseconds, so the seventh fractional digit of a .NET time, which counts 100-nanosecond ticks, is lost when reading.

### Strings

```python
from pyresonitelink.dergflux import strings

s.log = s.log + "y=" + strings.to_string(p.y) + "\n"
```

Strings join with `+`, which uses ConcatenateString. `strings.to_string(x)` uses the ToString node of the value's type, such as `ToString_Float`, which formats with the invariant culture, so a float is written with a period and as few digits as read back to the same float. A number is never joined to a string implicitly, and `"y=" + p.y` raises `TypeError`.

`==` and `!=` on strings use ObjectEquals and ObjectNotEquals, because ProtoFlux has no ValueEquals for strings. The same goes for references. `math.conditional` with two strings uses ObjectConditional, and a binding of a string, such as a TextRenderer's `Text`, uses ObjectFieldDrive. `math.is_null(x)` is true for a null string or reference. A `StringModelVar` declared without a value starts as null, which isn't equal to `""`, so a variable that a flow compares with `""` should be declared with `""` as its value.

### Slots and Transforms

A graph that reads or moves a slot takes it as a reference. `slots.ref(slot)` makes one from a `workers.Slot` or a slot ID, and the builder holds it in a `RefObjectInput<Slot>` node, one per slot however often it is used. `slots.of_component(c)` is the slot that a component is on, through ProtoFlux's GetSlot node. It takes a component expression such as a raycast's `hit_collider`, or a component already added to a slot. GetSlot takes an `IComponent`, and ProtoFlux refuses a narrower type such as `ICollider` there, so a narrower component passes through an `ObjectCast<ICollider, IComponent>` node first.

```python
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import transform

ball = slots.ref(ball_slot)
head = slots.ref(club_head_slot)
p = transform.global_position(ball)
q = transform.global_point_to_local(head, p)   # the ball's center in the head's space
n = transform.local_direction_to_global(head, primitives.Float3(0, 0, 1))
```

| Function | Result | Node |
|---|---|---|
| `transform.global_position(slot)` | Float3 | `GlobalTransform.GlobalPosition` |
| `transform.global_rotation(slot)` | FloatQ | `GlobalTransform.GlobalRotation` |
| `transform.global_scale(slot)` | Float3 | `GlobalTransform.GlobalScale` |
| `transform.global_point_to_local(slot, p)` | Float3 | `GlobalPointToLocal` |
| `transform.local_point_to_global(slot, p)` | Float3 | `LocalPointToGlobal` |
| `transform.global_direction_to_local(slot, d)` | Float3 | `GlobalDirectionToLocal` |
| `transform.local_direction_to_global(slot, d)` | Float3 | `LocalDirectionToGlobal` |
| `slots.name(slot)` | String | `GetSlotName` |
| `slots.find_child(slot, name, depth=0)` | Slot, or null | `FindChildByName` |

`slots.find_child` turns off FindChildByName's substring match, which is on by default, so it finds only a child with exactly the name. A depth of 0 searches the direct children only, and -1 searches every descendant.

The three `global_*` outputs of one slot reference share one GlobalTransform node. A `workers.Slot` passed directly makes a new reference each time, so a graph that reads a slot more than once should make one reference with `slots.ref` and pass that. The nodes read the slot whenever the flow evaluates them, so a position read after `g.SetGlobalPosition` in the same impulse is the new one.

### Variables on Other Slots

A Space's variables are read from the Space's slot. `variables.read(source, path, type)` reads a dynamic variable from a slot that the graph computes, such as the slot of the collider that a raycast hit, so that each object can carry its own values. It returns the value and a Bool that says whether the variable was found. A variable that wasn't found reads as the type's default.

```python
from pyresonitelink.dergflux import variables

r = variables.read(slots.of_component(hit.hit_collider), "Physics/Friction", primitives.Float)
friction = dm.conditional(r.found, r.value, 0.5)
```

The path is `"space/name"`. ProtoFlux's ReadDynamicValueVariable looks for the nearest DynamicVariableSpace of that name on the slot or its ancestors, and then for the variable in that space (`DynamicVariableHelper.FindSpace`). A variable missing from the nearest such space isn't looked for in spaces further up. Value types are supported, and strings and references aren't.

### Users and Grabbing

```python
from pyresonitelink.dergflux import interaction
from pyresonitelink.dergflux import users

users.local_user()               # the User whose machine evaluates the node
users.is_host(users.local_user())
users.local_user_is_host()       # a Bool, true only on the host's machine
users.machine_id(u)              # a String, different for each user in the session
users.is_vr_active(u)            # a Bool, false in desktop mode
users.is_dash_open(u)            # a Bool, true while the user's dash is open
users.view_position()            # a Float3, the local user's view (the camera in desktop mode)
users.view_rotation()            # a FloatQ, which looks along its +Z
users.username(u)                # a String, or null for a null user
interaction.is_grabbed(grab)     # a Bool, true while a Grabbable or other IGrabbable is held
```

An Update node fires on every user's machine, and each machine writes what its own run computes. A flow that moves something, such as a simulated ball, should run on one machine, and `g.If(users.local_user_is_host())` makes it the host's.

A flow that acts on one user's input runs on that user's machine. A String model variable can hold that user's machine ID, and the flow can run only where it equals `users.machine_id(users.local_user())`. A drive is computed on each machine too, so a binding of a slot's `IsActive` to that comparison shows the slot only to that user.

```python
s.player = s.StringModelVar("player", "")
mine = s.player == users.machine_id(users.local_user())
with g.Under(slot):
    with g.If(mine):
        ...
g.Bind(mine, hud_slot, "IsActive", slot=slot)
```

`examples/dergflux_golf.py` uses this for desktop shots. The view nodes read the camera, which in desktop mode points a few degrees away from where the Head slot points.

### Mouse

```python
from pyresonitelink.dergflux import mouse

mouse.left_pressed()    # a Bool, true in the update in which the left button went down
mouse.left_held()       # a Bool, true while it is down
mouse.left_released()   # a Bool, true in the update in which it came up
mouse.right_pressed()   # and right_held, right_released
mouse.scroll_delta()    # a Float, positive for a turn of the wheel away from the user
```

These read the mouse of the machine that evaluates them, through ProtoFlux's mouse nodes, which read Resonite's input directly. They see every click, including one that the laser also delivers to whatever is under the crosshair, and one in the dash, so a flow should usually ignore them while `users.is_dash_open(users.local_user())` is true. In desktop mode Resonite itself presses and uses things with the left button, grabs with the right, and opens the context menu with the middle one. The cursor stays at the center of the screen except while the dash is open, so the crosshair is on the ray from `users.view_position()` along `users.view_rotation() * Float3(0, 0, 1)`.

The unit of `scroll_delta` isn't documented, so a flow that counts notches of the wheel should act in the update in which the scrolling starts.

## Flow Control

All flow control must be inside a `g.Under(slot)` block.  Multiple
flow statements inside a single `Under` block are chained via a
ProtoFlux `Sequence` node — each runs to completion before the next
starts.

### If / Else

```python
with g.Under(slot):
    with g.If(s.x < 3):
        s.z = s.x + 3      # true branch
    with g.Else():
        s.z = s.x - 3      # false branch
```

Multiple writes per branch are supported. `g.Else()` is optional.

### Continuation after If / Else

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

### For

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

### Range

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

### While

```python
with g.Under(slot):
    with g.While(s.x > 0):
        s.x = s.x - 1
```

Repeats the body as long as `condition` is true. The condition is
re-evaluated each iteration. Statements go to `loop_iteration`.

Code after the `with g.While()` block continues from `loop_end`.

### Indexed Branch Nodes

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

## Bindings

``g.Bind()`` permanently binds a value source to a field of a component
or of a slot. The field always reflects the source's current value.
**A field can only be bound once** — attempting to rebind raises
``RuntimeError``.

The binding mechanism depends on the source:

- **Dynamic variable** (e.g. ``s.x``): Creates a
  ``DynamicValueVariableDriver<T>`` (for value types like int, float,
  Float3) or ``DynamicReferenceVariableDriver<T>`` (for reference
  types like Slot).  The driver reads the named variable by path and
  continuously drives the target field.
- **General expression** (e.g. ``i``, ``s.x + 1``): Creates a
  ``ValueFieldDrive<T>`` whose ``Value`` input reads the expression. The
  field that it drives is the ``Drive`` reference of a
  ``FieldDriveBase<T>+Proxy`` component, which the server adds beside the
  node, and the builder sets it there.

```python
# Bind a loop counter to a field (uses ValueFieldDrive)
with g.Under(slot):
    with g.For(3) as f:
        with f.OnIterate() as i:
            g.Bind(i, mux, "Index")

# Bind a dynamic variable to a field (uses DynamicValueVariableDriver)
g.Bind(s.volume, audio_output, "Volume", slot=slot)

# Drive a slot's rotation
g.Bind(dm.axis_angle(primitives.Float3(0, 1, 0), s.angle), wheel, "Rotation", slot=slot)
```

A slot's fields that can be bound are ``"Position"``, ``"Rotation"``,
``"Scale"``, ``"IsActive"``, and ``"OrderOffset"``. Their types are known,
so the expression is widened to the field's type, and an expression that
would have to narrow raises ``TypeError`` at the ``Bind`` call. A slot's
``Name`` and ``Tag`` are strings, which ``ValueFieldDrive`` can't drive.

For named spaces, the variable path is automatically prefixed with
the space name (e.g. ``"Audio/vol"`` for a variable ``vol`` in space
``Audio``).

Arguments:

- ``expr`` — an ExprProxy or literal value to bind from
- ``target`` — the component (a generated component instance) or the
  slot (a ``workers.Slot``) whose field is bound
- ``member_name`` — the Resonite member name to bind to (e.g. ``"Index"``,
  or ``"Rotation"`` for a slot)
- ``slot`` — optional; defaults to the active ``Under()`` slot

## Actions

Action nodes are ProtoFlux nodes triggered by an impulse that branch
into alternate flow paths and optionally produce value outputs.  They
are accessed as named methods on the Graph, or via ``g.Action()`` with
a custom ``ActionDef``.

### Action Nodes

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

Value outputs: ``r.hit_collider`` (an ICollider), ``r.hit_point``
(Float3), ``r.hit_normal`` (Float3), ``r.hit_distance`` (Float),
``r.hit_triangle_index`` (Int). They are set only on a hit, so read them
in ``on_hit()``.

``max_distance`` and ``hit_distance`` are measured in lengths of
``direction``. ``MainPhysicsSimulation.RaycastOne`` passes the direction to
BEPU unnormalized, the ray ends at ``origin + direction * max_distance``,
and ``hit_distance`` is the multiple of the direction where it hit. A ray
along a velocity of 4 m/s with a ``max_distance`` of 0.1 reaches 0.4 m.
Pass ``dm.normalized(v)`` to work in meters.

``ignore_hierarchy`` takes a slot whose colliders, and its descendants',
the ray passes through, such as the collider of the object that casts
it. ``root`` takes a slot, and the origin, direction, and maximum distance
are then in its space. The hit outputs are in world space either way.

A statement after the raycast runs after whichever branch fired. The
node returns null instead of either branch when the direction is zero,
the maximum distance isn't positive, or the origin isn't a valid number,
and the flow ends there, so guard a ray whose direction can be zero with
``g.If``.

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

**Delay** (async — suspends across frames):

```python
with g.Under(slot):
    with g.DelaySeconds(duration=2.0) as d:
        with d.next():
            s.state = "waiting"      # fires immediately
        with d.on_triggered():
            s.state = "delayed"      # fires after 2 seconds

    with g.DelayUpdates(updates=2) as d:
        with d.on_triggered():
            s.state = "after 2 updates"

    with g.DelayUpdatesOrSeconds(updates=60, duration=1.0) as d:
        with d.on_triggered():
            s.state = "after 60 updates or 1 second"
```

**Prebuilt actions** in ``pyresonitelink.dergflux.actions``:

- ``actions.RaycastOne`` — ray cast with on_hit/on_miss
- ``actions.PlayOneShot`` / ``actions.PlayOneShotAndWait`` — audio
- ``actions.DelaySecondsFloat/Double/Int`` — time delay
- ``actions.DelayUpdates`` — update delay
- ``actions.DelayUpdatesOrSecondsFloat/Double/Int`` — combined delay

### Transform Setters

```python
with g.Under(slot):
    g.SetGlobalPosition(ball, transform.global_position(ball) + s.v * dt)
    g.SetLocalRotation(pivot, dm.axis_angle(primitives.Float3(1, 0, 0), s.angle))
    s.moved = True     # runs after both setters
```

``g.SetGlobalPosition``, ``g.SetGlobalRotation``,
``g.SetGlobalPositionRotation``, ``g.SetLocalPosition``, and
``g.SetLocalRotation`` are statements. Each sets a slot's transform when
the flow reaches it, and the flow then goes on to the next statement. The
slot is a ``workers.Slot`` or a slot expression from ``dergflux.slots``. A
null or removed slot ends the flow (``TransformSetter.Do``).

Unlike a binding, a setter leaves the slot undriven, so a user can still
grab it.

``g.Do(action_def, **inputs)`` records any action whose flow outputs all
continue the flow, as these do, as a statement.

### Slot Actions

```python
with g.Under(slot):
    with g.If(math.is_null(slots.find_child(players, users.machine_id(users.local_user())))):
        kit = g.DuplicateSlot(template, players)   # the duplicate, a slot expression
        g.SetSlotActiveSelf(kit, True)
        g.SetSlotName(kit, "Kit")
    g.DestroySlot(old_slot)
```

These are statements too. ``g.DuplicateSlot(template, parent)`` copies a
slot with everything under it and returns the copy, for the rest of the
flow to use. References between things inside the template point to
their copies in the duplicate, and references to things outside it are
kept, so a template can hold a whole Dergflux graph that reads the
course around it, and each duplicate runs a graph of its own.

The duplicate's components get their OnDuplicate event on the machine
that ran the flow only (``Slot.Duplicate`` calls ``RunDuplicate``
locally), so a graph in the template can claim the duplicate for that
machine's user with ``g.OnDuplicate``. ``examples/dergflux_golf.py`` gives
each player a kit this way.

A drive in an inactive slot computes, but an Update flow there doesn't
run (measured 23 Oct 2026, with a template kit whose flow ran only once
the kit was activated). A template that is inactive and has no owner
does nothing.

### Defining Custom Actions

Any ProtoFlux node with flow outputs can be wrapped as an action using
``ActionDef`` — no custom proxy or builder code needed:

```python
from pyresonitelink.dergflux import ActionDef, InputDef, OutputDef
from pyresonitelink.data import primitives

MyAction = ActionDef(
    import_path="protoflux.physics",
    class_name="RaycastOne",
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

- ``continuations=[...]`` — the flow outputs that continue the flow
  that ran the node, such as RaycastOne's ``on_hit`` and ``on_miss``,
  or a setter's ``next``. A statement after the action runs after
  whichever of them fires, and after its branch if it has one. Without
  them, the statement after the action is wired to the node's
  ``OnSuccess``.

- ``is_async=True`` — the node is async; enclosing flow uses async variants
  and ``StartAsyncTask`` bridge.
- ``is_event_source=True`` — the node fires its own impulses (no trigger
  created).  Use for event monitors like ``SlotChildrenEvents``.

## Data Sources

Data source nodes are ProtoFlux nodes that provide value outputs
without any flow (no impulses, no triggers).  They compute values
on demand — other nodes pull from them.  Unlike action nodes (which
are context managers with flow branches), data sources are plain
calls that return a proxy with value output properties.

Data sources use the same ``ActionDef`` system as action nodes, but
with ``flow_outputs=[]``.  They're created with ``g.DataSource()``
or named shortcuts.

### Data Source Nodes

```python
ctrl = g.StandardController(user=user_ref, node=chirality, slot=slot)

# ctrl.primary, ctrl.grab, ctrl.axis etc. are ExprProxy values
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

### Defining Custom Data Sources

Any ProtoFlux value node can be wrapped as a data source using
``ActionDef`` with ``flow_outputs=[]``:

```python
from pyresonitelink.dergflux import ActionDef, InputDef, OutputDef
from pyresonitelink.data import primitives

MyDataSource = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="StandardController",
    inputs={
        "user": InputDef("user"),
        "node": InputDef("node"),
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

## Event Source Nodes

Event source nodes fire impulses on their own when events occur,
rather than being triggered by an impulse.  The builder skips trigger
creation automatically.

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
    with g.FireOnTrue(condition=s.flag) as e:
        with e.on_changed():
            s.count = s.count + 1

    with g.FireOnFalse(condition=s.flag) as e:
        with e.on_changed():
            s.result = s.x

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
    with g.UpdatesTimer(interval=60) as e:
        with e.on_update():
            s.tick = s.tick + 1

    with g.SecondsTimer(interval=1.0) as e:
        with e.on_update():
            s.seconds = s.seconds + 1
```

**ButtonEvents** — fires on button press/release/hover:

```python
with g.Under(slot):
    with g.ButtonEvents(button=my_button) as e:
        with e.pressed():
            s.log = "pressed"
            s.press_point = e.global_point
        with e.released():
            s.log = "released"
```

Flow outputs: ``pressed()``, ``pressing()``, ``released()``,
``hover_enter()``, ``hover_stay()``, ``hover_leave()``.

Value outputs: ``e.global_point`` (Float3), ``e.local_point`` (Float3),
``e.normalized_point`` (Float2).

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
auto-creates a ``GlobalReference<Slot>`` bridge.

Value output: ``e.child`` — the child Slot that was added or removed.

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
2. **Variables**: Creates `DynamicValueVariable<T>` components (skipped if already present), and a child slot with a `DataModelValueFieldStore<T>` for each model variable.
3. **Bindings that read no flow state**: Creates their drivers and `ValueFieldDrive<T>` nodes, so a flow's first run happens with them already driving their fields.
4. **Expressions**: Walks the AST bottom-up, creating operator and math nodes.
5. **Writes**: Creates `WriteDynamicValueVariable<T>` chains (linked via `on_success`).
6. **Flow**: Creates `If` nodes wired to the condition and write chains.
7. **Trigger**: Creates `Update`, `DynamicImpulseReceiver`, or `DynamicImpulseReceiverWithValue<T>` to drive the impulse flow.
8. **Bindings that read flow state**: Creates the bindings whose expressions read a loop index, a trigger's value, or an action's output, which need the flow's nodes.

Shared sub-expressions are materialized only once (identity-cached).

A flow driven by `Update` starts running as soon as its trigger is wired, while the rest of the graph may still be building. Each node takes a round trip and a short pause, so a large graph takes seconds to build. A flow that records a start time therefore records it before any later part of the graph exists, and a value that should start counting when the whole graph is ready belongs in a binding, which is built first.

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
| `dm.smoothstep(x)`, `dm.smoothstep(e0, e1, x)` | `SmoothStep_Float`, `SmoothStep_Double` |
| `dm.smootherstep(x)`, `dm.smootherstep(e0, e1, x)` | `SmootherStep_Float`, `SmootherStep_Double` |
| `dm.axis_angle(axis, angle)` | `AxisAngle_floatQ`, `AxisAngle_doubleQ` |
| `dm.from_euler(angles)` | `FromEuler_floatQ`, `FromEuler_doubleQ` |

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
| `dm.lerp_unclamped(a, b, t)` | `ValueLerpUnclamped<T>` |
| `dm.inverse_lerp(a, b, v)` | `ValueInverseLerp<T>` for numbers, `InverseLerp_Float3` etc. for vectors |
| `dm.conditional(c, t, f)` | `ValueConditional<T>` |

## Complete Example

See `examples/dergflux_if_else.py` for a working end-to-end example that builds an if-else graph and tests it with different input values.
