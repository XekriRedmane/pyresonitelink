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


def lerp(a: Any, b: Any, t: Any) -> _expr.ExprProxy:
    """Linear interpolation from a to b by t.

    Uses generic ``ValueLerp<T>`` (not the typed Lerp_* variants).
    """
    return _math_call_3("lerp", a, b, t)


def inverse_lerp(a: Any, b: Any, value: Any) -> _expr.ExprProxy:
    """Inverse linear interpolation.

    Returns the interpolation parameter t such that
    ``lerp(a, b, t) == value``.
    """
    return _math_call_3("inverse_lerp", a, b, value)


def smoothstep(edge0: Any, edge1: Any, x: Any) -> _expr.ExprProxy:
    """Hermite smoothstep interpolation."""
    return _math_call_3("smoothstep", edge0, edge1, x)


def conditional(
    condition: Any, on_true: Any, on_false: Any,
) -> _expr.ExprProxy:
    """Conditional (ternary) expression.

    Returns ``on_true`` if ``condition`` is true, else ``on_false``.
    Uses generic ``ValueConditional<T>``, where T is the common type of
    the two values. The condition must be a Bool.
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
