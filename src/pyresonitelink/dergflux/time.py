"""Time and Date functions for Dergflux expressions."""

from __future__ import annotations

from typing import Any

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr


def utc_now() -> _expr.ExprProxy:
    """Current UTC date and time."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.DateTime))


def delta_time() -> _expr.ExprProxy:
    """Time elapsed since the last frame (in seconds)."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


def smooth_delta_time() -> _expr.ExprProxy:
    """Smoothed time elapsed since the last frame."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


def raw_delta_time() -> _expr.ExprProxy:
    """Raw time elapsed since the last frame."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


def inverted_delta_time() -> _expr.ExprProxy:
    """1.0 / delta_time()."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


def inverted_smooth_delta_time() -> _expr.ExprProxy:
    """1.0 / smooth_delta_time()."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


def inverted_raw_delta_time() -> _expr.ExprProxy:
    """1.0 / raw_delta_time()."""
    return _expr.ExprProxy(_expr.ExprNode(primitives.Float))


# =========================================================================
# TimeSpan Factories
# =========================================================================


def days(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of days."""
    xp = _expr._coerce(float(n) if isinstance(n, (int, float)) else n)
    return _expr.ExprProxy(
        _expr.MathCallNode("time_span_from_days", [xp._node], primitives.TimeSpan),
    )


def hours(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of hours."""
    xp = _expr._coerce(float(n) if isinstance(n, (int, float)) else n)
    return _expr.ExprProxy(
        _expr.MathCallNode("time_span_from_hours", [xp._node], primitives.TimeSpan),
    )


def minutes(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of minutes."""
    xp = _expr._coerce(float(n) if isinstance(n, (int, float)) else n)
    return _expr.ExprProxy(
        _expr.MathCallNode("time_span_from_minutes", [xp._node], primitives.TimeSpan),
    )


def seconds(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of seconds."""
    xp = _expr._coerce(float(n) if isinstance(n, (int, float)) else n)
    return _expr.ExprProxy(
        _expr.MathCallNode("time_span_from_seconds", [xp._node], primitives.TimeSpan),
    )


def milliseconds(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of milliseconds."""
    xp = _expr._coerce(float(n) if isinstance(n, (int, float)) else n)
    return _expr.ExprProxy(
        _expr.MathCallNode(
            "time_span_from_milliseconds", [xp._node], primitives.TimeSpan,
        ),
    )


def ticks(n: Any) -> _expr.ExprProxy:
    """Create a TimeSpan from number of ticks (1 tick = 100ns)."""
    xp = _expr._coerce(n)
    return _expr.ExprProxy(
        _expr.MathCallNode("time_span_from_ticks", [xp._node], primitives.TimeSpan),
    )


# =========================================================================
# Unix Time
# =========================================================================


def from_unix_seconds(s: Any) -> _expr.ExprProxy:
    """Create a DateTime from Unix timestamp in seconds."""
    xp = _expr._coerce(s)
    return _expr.ExprProxy(
        _expr.MathCallNode("from_unix_seconds", [xp._node], primitives.DateTime),
    )


def from_unix_milliseconds(ms: Any) -> _expr.ExprProxy:
    """Create a DateTime from Unix timestamp in milliseconds."""
    xp = _expr._coerce(ms)
    return _expr.ExprProxy(
        _expr.MathCallNode("from_unix_milliseconds", [xp._node], primitives.DateTime),
    )


def to_unix_seconds(dt: Any) -> _expr.ExprProxy:
    """Convert DateTime to Unix timestamp in seconds."""
    xp = _expr._coerce(dt)
    return _expr.ExprProxy(
        _expr.MathCallNode("to_unix_seconds", [xp._node], primitives.Double),
    )


def to_unix_milliseconds(dt: Any) -> _expr.ExprProxy:
    """Convert DateTime to Unix timestamp in milliseconds."""
    xp = _expr._coerce(dt)
    return _expr.ExprProxy(
        _expr.MathCallNode("to_unix_milliseconds", [xp._node], primitives.Long),
    )
