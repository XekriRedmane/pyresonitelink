"""Math functions for Dergflux expressions.

Provides module-level functions that create AST nodes for ProtoFlux
math operations.  These map to typed ProtoFlux nodes (e.g. ``Sin_Float``,
``Sqrt_Double``) at build time.

Usage::

    from pyresonitelink.dergflux import math as dm

    s.y = dm.sin(s.x)
    s.z = dm.clamp(s.x, 0, 1)
    s.w = dm.lerp(s.a, s.b, s.t)
    s.d = dm.distance(s.p, s.q)  # Not yet implemented
"""

from __future__ import annotations

from typing import Any

from pyresonitelink.dergflux import _expr


def _math_call_1(func_name: str, x: Any) -> _expr.ExprProxy:
    """Create a unary math function call node."""
    xp = _expr._coerce(x)
    from pyresonitelink.dergflux import _types
    result_type = _types.infer_result_type(xp._node._type)
    return _expr.ExprProxy(
        _expr.MathCallNode(func_name, [xp._node], result_type),
    )


def _math_call_2(func_name: str, a: Any, b: Any) -> _expr.ExprProxy:
    """Create a binary math function call node.

    The arguments are widened to their common type first.
    """
    a_node, b_node, result_type = _expr.unify(
        _expr._coerce(a)._node, _expr._coerce(b)._node, func_name,
    )
    return _expr.ExprProxy(
        _expr.MathCallNode(func_name, [a_node, b_node], result_type),
    )


def _math_call_3(
    func_name: str, a: Any, b: Any, c: Any,
) -> _expr.ExprProxy:
    """Create a ternary math function call node.

    The first two arguments are widened to their common type first. The
    third can differ, as for the t of lerp(a, b, t).
    """
    a_node, b_node, result_type = _expr.unify(
        _expr._coerce(a)._node, _expr._coerce(b)._node, func_name,
    )
    cp = _expr._coerce(c)
    return _expr.ExprProxy(
        _expr.MathCallNode(
            func_name, [a_node, b_node, cp._node], result_type,
        ),
    )


# =========================================================================
# Conversions
# =========================================================================


def convert(x: Any, to: type) -> _expr.ExprProxy:
    """Converts a value to another type, narrowing it if needed.

    Widening, such as int to float, happens without this. Narrowing, such
    as float to int, needs it, and uses ProtoFlux's Cast node for the two
    types, e.g. Cast_float_To_int.

    Args:
        x: An expression or a Python literal.
        to: The type to convert to, e.g. primitives.Int.

    Returns:
        The converted expression.
    """
    return _expr.explicit(x, to)


def to_int(x: Any) -> _expr.ExprProxy:
    """Converts a value to an int (primitives.Int)."""
    from pyresonitelink.data import primitives
    return convert(x, primitives.Int)


def to_long(x: Any) -> _expr.ExprProxy:
    """Converts a value to a long (primitives.Long)."""
    from pyresonitelink.data import primitives
    return convert(x, primitives.Long)


def to_float(x: Any) -> _expr.ExprProxy:
    """Converts a value to a float (primitives.Float)."""
    from pyresonitelink.data import primitives
    return convert(x, primitives.Float)


def to_double(x: Any) -> _expr.ExprProxy:
    """Converts a value to a double (primitives.Double)."""
    from pyresonitelink.data import primitives
    return convert(x, primitives.Double)


# =========================================================================
# Trigonometric
# =========================================================================


def sin(x: Any) -> _expr.ExprProxy:
    """Sine function."""
    return _math_call_1("sin", x)


def cos(x: Any) -> _expr.ExprProxy:
    """Cosine function."""
    return _math_call_1("cos", x)


def tan(x: Any) -> _expr.ExprProxy:
    """Tangent function."""
    return _math_call_1("tan", x)


def asin(x: Any) -> _expr.ExprProxy:
    """Arc sine (inverse sine) function."""
    return _math_call_1("asin", x)


def acos(x: Any) -> _expr.ExprProxy:
    """Arc cosine (inverse cosine) function."""
    return _math_call_1("acos", x)


def atan(x: Any) -> _expr.ExprProxy:
    """Arc tangent (inverse tangent) function."""
    return _math_call_1("atan", x)


def atan2(y: Any, x: Any) -> _expr.ExprProxy:
    """Two-argument arc tangent."""
    return _math_call_2("atan2", y, x)


# =========================================================================
# Exponential / logarithmic
# =========================================================================


def exp(x: Any) -> _expr.ExprProxy:
    """Exponential function (e^x)."""
    return _math_call_1("exp", x)


def log(x: Any) -> _expr.ExprProxy:
    """Natural logarithm (ln)."""
    return _math_call_1("log", x)


def log10(x: Any) -> _expr.ExprProxy:
    """Base-10 logarithm."""
    return _math_call_1("log10", x)


def sqrt(x: Any) -> _expr.ExprProxy:
    """Square root."""
    return _math_call_1("sqrt", x)


# =========================================================================
# Rounding
# =========================================================================


def ceil(x: Any) -> _expr.ExprProxy:
    """Ceiling (round up)."""
    return _math_call_1("ceil", x)


def floor(x: Any) -> _expr.ExprProxy:
    """Floor (round down)."""
    return _math_call_1("floor", x)


def round_(x: Any) -> _expr.ExprProxy:
    """Round to nearest integer.

    Named ``round_`` to avoid shadowing the Python builtin.
    """
    return _math_call_1("round", x)


# =========================================================================
# Sign / value
# =========================================================================


def sign(x: Any) -> _expr.ExprProxy:
    """Sign function (-1, 0, or 1)."""
    return _math_call_1("sign", x)


def clamp01(x: Any) -> _expr.ExprProxy:
    """Clamp to [0, 1] range."""
    return _math_call_1("clamp01", x)


def square(x: Any) -> _expr.ExprProxy:
    """Square (x^2).  Uses generic ``ValueSquare<T>``."""
    return _math_call_1("square", x)


def cube(x: Any) -> _expr.ExprProxy:
    """Cube (x^3).  Uses generic ``ValueCube<T>``."""
    return _math_call_1("cube", x)


def reciprocal(x: Any) -> _expr.ExprProxy:
    """Reciprocal (1/x).  Uses generic ``ValueReciprocal<T>``."""
    return _math_call_1("reciprocal", x)


def one_minus(x: Any) -> _expr.ExprProxy:
    """One minus x (1 - x).  Uses generic ``ValueOneMinus<T>``."""
    return _math_call_1("one_minus", x)


# =========================================================================
# Two-argument functions
# =========================================================================


def min_(a: Any, b: Any) -> _expr.ExprProxy:
    """Minimum of two values.  Uses generic ``ValueMin<T>``.

    Named ``min_`` to avoid shadowing the Python builtin.
    """
    return _math_call_2("min", a, b)


def max_(a: Any, b: Any) -> _expr.ExprProxy:
    """Maximum of two values.  Uses generic ``ValueMax<T>``.

    Named ``max_`` to avoid shadowing the Python builtin.
    """
    return _math_call_2("max", a, b)


# =========================================================================
# Three-argument functions
# =========================================================================


def clamp(value: Any, lo: Any, hi: Any) -> _expr.ExprProxy:
    """Clamp value to [lo, hi] range.  Uses generic ``ValueClamp<T>``."""
    return _math_call_3("clamp", value, lo, hi)


def _lerp(func_name: str, a: Any, b: Any, t: Any) -> _expr.ExprProxy:
    """Returns a call to the lerp node named func_name.

    The lerp nodes take their weight as a float, whatever the type of the
    values, so t is converted to a Float.
    """
    from pyresonitelink.data import primitives

    a_node, b_node, result_type = _expr.unify(
        _expr._coerce(a)._node, _expr._coerce(b)._node, func_name,
    )
    weight = _expr.implicit(t, primitives.Float, f"{func_name}'s t")
    return _expr.ExprProxy(
        _expr.MathCallNode(func_name, [a_node, b_node, weight._node], result_type),
    )


def lerp(a: Any, b: Any, t: Any) -> _expr.ExprProxy:
    """Returns a + (b - a) * t, with t clamped to [0, 1].

    Uses ``ValueLerp<T>``. a and b are widened to their common type, which
    is the result's type, and can be numbers or vectors. The node takes t
    as a Float, so a Double t raises TypeError until it's converted with
    ``to_float``.
    """
    return _lerp("lerp", a, b, t)


def lerp_unclamped(a: Any, b: Any, t: Any) -> _expr.ExprProxy:
    """Returns a + (b - a) * t, without clamping t.

    Uses ``ValueLerpUnclamped<T>``. The arguments are those of lerp.
    """
    return _lerp("lerp_unclamped", a, b, t)


def inverse_lerp(a: Any, b: Any, value: Any) -> _expr.ExprProxy:
    """Returns (value - a) / (b - a), the t for which lerp(a, b, t) is value.

    The result isn't clamped. The three arguments are widened to their
    common type. For numbers this is ``ValueInverseLerp<T>``, whose result
    is a Float even when the arguments are Doubles. For Float2 to Float4
    and Double2 to Double4 vectors it's ``InverseLerp_Float3`` and so on,
    which work per component and give a vector of the arguments' type.
    """
    from pyresonitelink.data import primitives
    from pyresonitelink.dergflux import _types

    nodes = [_expr._coerce(x)._node for x in (a, b, value)]
    # Literals take the type of the first typed argument where they can,
    # as in inverse_lerp(0, 10, x), so they need no cast nodes.
    context = next((n._type for n in nodes if n._type is not None), None)
    for node in nodes:
        if isinstance(node, _expr.ConstNode):
            _expr._type_literal(node, context)
    a_node, b_node, common = _expr.unify(nodes[0], nodes[1], "inverse_lerp")
    value_node = nodes[2]
    if common is not None:
        # Widen value to a and b's type, or a and b to value's.
        a_node, value_node, common = _expr.unify(a_node, value_node, "inverse_lerp")
        if common is not None and b_node._type != common:
            b_node = _expr.implicit(
                _expr.ExprProxy(b_node), common, "inverse_lerp",
            )._node
    result_type = common if common in _types._VECTORS else primitives.Float
    return _expr.ExprProxy(
        _expr.MathCallNode(
            "inverse_lerp", [a_node, b_node, value_node], result_type,
        ),
    )


def _float_type(*values: _expr.ExprProxy) -> type:
    """Returns Double if any of the values is a Double, and Float otherwise.

    The shaping nodes exist only for float and double.
    """
    from pyresonitelink.data import primitives

    if any(_type_of(v) == primitives.Double for v in values):
        return primitives.Double
    return primitives.Float


def _shape(func_name: str, args: tuple[Any, ...]) -> _expr.ExprProxy:
    """Returns smoothstep or smootherstep of one argument or three.

    With three arguments (edge0, edge1, x), x is first mapped to 0 at
    edge0 and 1 at edge1, and clamped to that range.
    """
    if len(args) not in (1, 3):
        raise TypeError(
            f"{func_name} takes x, or edge0, edge1, and x, but got "
            f"{len(args)} arguments."
        )
    proxies = [_expr._coerce(a) for a in args]
    t = _float_type(*proxies)
    converted = [_expr.implicit(p, t, func_name) for p in proxies]
    x = converted[-1]
    if len(converted) == 3:
        edge0, edge1 = converted[0], converted[1]
        x = clamp01((x - edge0) / (edge1 - edge0))
    return _expr.ExprProxy(_expr.MathCallNode(func_name, [x._node], t))


def smoothstep(*args: Any) -> _expr.ExprProxy:
    """Returns 3x² - 2x³, which eases from 0 at x = 0 to 1 at x = 1.

    Called as smoothstep(x), this is ProtoFlux's SmoothStep node, which
    doesn't clamp x, so the result leaves [0, 1] when x does. Called as
    smoothstep(edge0, edge1, x), as in GLSL, x is mapped to 0 at edge0 and
    1 at edge1 and clamped to that range first, so the result is 0 at or
    below edge0 and 1 at or above edge1.

    The result is a Double if any argument is, and a Float otherwise.
    """
    return _shape("smoothstep", args)


def smootherstep(*args: Any) -> _expr.ExprProxy:
    """Returns 6x⁵ - 15x⁴ + 10x³, a smoothstep with zero acceleration at the ends.

    The arguments are those of smoothstep, and so are the clamping and the
    result type.
    """
    return _shape("smootherstep", args)


# =========================================================================
# Rotations
# =========================================================================


def _type_of(proxy: _expr.ExprProxy) -> type | None:
    """Returns an expression's type, or an untyped literal's own type."""
    from pyresonitelink.dergflux import _types

    node = proxy._node
    if node._type is None and isinstance(node, _expr.ConstNode):
        return _types.literal_type(node.value)
    return node._type


def axis_angle(axis: Any, angle: Any) -> _expr.ExprProxy:
    """Returns the rotation by angle degrees about axis.

    Uses ProtoFlux's AxisAngle node, which normalizes the axis. The axis
    is a Float3 and the angle a Float, giving a FloatQ, unless either is
    a Double3 or Double, in which case both are widened and the result is
    a DoubleQ. A positive angle turns +Y toward +Z about +X, which in
    Resonite's left-handed coordinates is clockwise seen from the tip of
    the axis.
    """
    from pyresonitelink.data import primitives

    axis_p, angle_p = _expr._coerce(axis), _expr._coerce(angle)
    if (_type_of(axis_p) == primitives.Double3
            or _type_of(angle_p) == primitives.Double):
        vector, scalar, result = (
            primitives.Double3, primitives.Double, primitives.DoubleQ,
        )
    else:
        vector, scalar, result = (
            primitives.Float3, primitives.Float, primitives.FloatQ,
        )
    axis_p = _expr.implicit(axis_p, vector, "axis_angle's axis")
    angle_p = _expr.implicit(angle_p, scalar, "axis_angle's angle")
    return _expr.ExprProxy(
        _expr.MathCallNode("axis_angle", [axis_p._node, angle_p._node], result),
    )


def from_euler(angles: Any) -> _expr.ExprProxy:
    """Returns the rotation given by Euler angles in degrees.

    Uses ProtoFlux's FromEuler node. A Float3 gives a FloatQ and a Double3
    a DoubleQ.
    """
    from pyresonitelink.data import primitives

    angles_p = _expr._coerce(angles)
    if _type_of(angles_p) == primitives.Double3:
        vector, result = primitives.Double3, primitives.DoubleQ
    else:
        vector, result = primitives.Float3, primitives.FloatQ
    angles_p = _expr.implicit(angles_p, vector, "from_euler")
    return _expr.ExprProxy(
        _expr.MathCallNode("from_euler", [angles_p._node], result),
    )


# =========================================================================
# Vectors
# =========================================================================

# The modules of the vector nodes, relative to pyresonitelink.
_VECTORS_MODULE = "protoflux.operators.vectors"
_PACKING_MODULE = "protoflux.operators.packing"


def _float_vector(func_name: str, *args: Any) -> tuple[list[_expr.ExprNode], type]:
    """Widens vector arguments to their common type, which has float or double elements.

    Returns:
        The arguments' nodes and their common type.

    Raises:
        TypeError: The arguments aren't vectors of the same dimension, or
            their elements are integers, for which ProtoFlux has no such
            node.
    """
    from pyresonitelink.data import primitives
    from pyresonitelink.dergflux import _types

    nodes = [_expr._coerce(arg)._node for arg in args]
    vector_type = _type_of(_expr.ExprProxy(nodes[0]))
    for i in range(1, len(nodes)):
        nodes[0], nodes[i], vector_type = _expr.unify(nodes[0], nodes[i], func_name)
    if (vector_type not in _types._VECTORS
            or _types._VECTORS[vector_type][0] not in (primitives.Float, primitives.Double)):
        raise TypeError(
            f"{func_name} takes vectors of floats or doubles, not "
            f"{_types.type_name(vector_type)}."
        )
    # unify widened the first argument against each of the others, so the
    # earlier ones may still be narrower than the common type.
    nodes = [_expr.implicit(_expr.ExprProxy(n), vector_type, func_name)._node for n in nodes]
    return nodes, vector_type


def _vector_node(
    func_name: str, class_prefix: str, args: tuple[Any, ...], result: str,
) -> _expr.ExprProxy:
    """Builds a vector node such as Dot_Float3, whose inputs are A and B.

    Args:
        func_name: The Dergflux function, for error messages.
        class_prefix: The node's name before the type, e.g. "Dot".
        args: One or two vectors.
        result: "element" if the node returns a number of the vectors'
            element type, or "vector" if it returns a vector of their type.
    """
    from pyresonitelink.dergflux import _types

    nodes, vector_type = _float_vector(func_name, *args)
    element, _ = _types._VECTORS[vector_type]
    return _expr.node_output(
        {name: _expr.ExprProxy(n) for name, n in zip("AB", nodes)},
        element if result == "element" else vector_type,
        module=_VECTORS_MODULE,
        class_name=f"{class_prefix}_{_types.type_name(vector_type)}",
    )


def dot(a: Any, b: Any) -> _expr.ExprProxy:
    """Returns the dot product of two vectors, a number of their element type.

    The vectors are Float2 to Double4, widened to their common type.
    """
    return _vector_node("dot", "Dot", (a, b), "element")


def cross(a: Any, b: Any) -> _expr.ExprProxy:
    """Returns the cross product of two Float3 or Double3 vectors.

    Resonite's coordinates are left-handed, so cross((1, 0, 0), (0, 1, 0))
    is (0, 0, 1), which is forward.
    """
    return _vector_node("cross", "Cross", (a, b), "vector")


def magnitude(v: Any) -> _expr.ExprProxy:
    """Returns a vector's length, a number of its element type."""
    return _vector_node("magnitude", "Magnitude", (v,), "element")


def normalized(v: Any) -> _expr.ExprProxy:
    """Returns a vector scaled to length 1, or the zero vector unchanged."""
    return _vector_node("normalized", "Normalized", (v,), "vector")


def distance(a: Any, b: Any) -> _expr.ExprProxy:
    """Returns the distance between two points, a number of their element type."""
    return _vector_node("distance", "Distance", (a, b), "element")


def pack(*elements: Any) -> _expr.ExprProxy:
    """Returns the vector with the given elements, such as a Float3 from x, y, and z.

    The elements are widened to their common type, and the vector's
    element type is that type, or Float for untyped literals. Uses
    ProtoFlux's Pack node, such as Pack_Float3.

    Raises:
        TypeError: There are fewer than 2 or more than 4 elements, or the
            elements have no common float or double type.
    """
    from pyresonitelink.data import primitives
    from pyresonitelink.dergflux import _types

    if not 2 <= len(elements) <= 4:
        raise TypeError(f"pack takes 2 to 4 elements, not {len(elements)}.")
    element_type: type | None = None
    for element in elements:
        node = _expr._coerce(element)._node
        own = _type_of(_expr.ExprProxy(node))
        if own is not None:
            element_type = own if element_type is None else _types.common_type(element_type, own)
    if element_type in (None, primitives.Int, primitives.Long):
        element_type = primitives.Float
    if element_type not in (primitives.Float, primitives.Double):
        raise TypeError("pack takes elements that convert to floats or doubles.")
    assert element_type is not None
    vector_type = _types._VECTOR_BY_PARTS[(element_type, len(elements))]
    return _expr.node_output(
        {
            name: _expr.implicit(element, element_type, "pack")
            for name, element in zip("XYZW", elements)
        },
        vector_type,
        module=_PACKING_MODULE,
        class_name=f"Pack_{_types.type_name(vector_type)}",
    )


def is_null(value: Any) -> _expr.ExprProxy:
    """Returns a Bool that is true if a string or a reference is null.

    Uses ProtoFlux's IsNull<T>. A user who has left the session, a slot
    that was destroyed, and a slot that a search didn't find are null.

    Args:
        value: An expression of a ProtoFlux object type, such as a String,
            a User, or a workers.Slot.

    Raises:
        TypeError: The value has no type.
    """
    from pyresonitelink.data import primitives

    node = _expr._coerce(value)._node
    if node._type is None:
        raise TypeError("is_null takes a value with a type.")
    return _expr.node_output(
        {"Instance": _expr.ExprProxy(node)}, primitives.Bool,
        module="protoflux.operators", class_name="IsNull", type_args=(node._type,),
    )


def conditional(
    condition: Any, on_true: Any, on_false: Any,
) -> _expr.ExprProxy:
    """Conditional (ternary) expression.

    Returns ``on_true`` if ``condition`` is true, else ``on_false``.
    Uses generic ``ValueConditional<T>``, where T is the common type of
    the two values, or ``ObjectConditional<T>`` for strings and
    references. The condition must be a Bool.
    """
    from pyresonitelink.data import primitives

    cond = _expr.implicit(condition, primitives.Bool, "conditional")
    true_node, false_node, result_type = _expr.unify(
        _expr._coerce(on_true)._node, _expr._coerce(on_false)._node,
        "conditional",
    )
    return _expr.ExprProxy(
        _expr.MathCallNode(
            "conditional", [cond._node, true_node, false_node], result_type,
        ),
    )
