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
    """Create a binary math function call node."""
    ap = _expr._coerce(a)
    bp = _expr._coerce(b)
    from pyresonitelink.dergflux import _types
    result_type = _types.infer_result_type(ap._node._type, bp._node._type)
    return _expr.ExprProxy(
        _expr.MathCallNode(func_name, [ap._node, bp._node], result_type),
    )


def _math_call_3(
    func_name: str, a: Any, b: Any, c: Any,
) -> _expr.ExprProxy:
    """Create a ternary math function call node."""
    ap = _expr._coerce(a)
    bp = _expr._coerce(b)
    cp = _expr._coerce(c)
    from pyresonitelink.dergflux import _types
    result_type = _types.infer_result_type(ap._node._type, bp._node._type)
    return _expr.ExprProxy(
        _expr.MathCallNode(
            func_name, [ap._node, bp._node, cp._node], result_type,
        ),
    )


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
    Uses generic ``ValueConditional<T>``.
    """
    return _math_call_3("conditional", condition, on_true, on_false)
