"""Time and date functions for Dergflux expressions.

DateTime and TimeSpan values are Python datetimes and timedeltas, so a
literal can be used directly::

    deadline = time.utc_now() + datetime.timedelta(minutes=5)
    s.waited = time.utc_now() - s.started    # a TimeSpan
    s.seconds = s.waited.total_seconds        # a Double

Each function maps to the ProtoFlux node of the same name under
TimeAndDate, and the result types are those of the nodes.
"""

from __future__ import annotations

from typing import Any

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr


def _call(
    func_name: str, args: list[_expr.ExprProxy], result_type: type,
) -> _expr.ExprProxy:
    """Returns a call to the node that the builder knows as func_name."""
    return _expr.ExprProxy(
        _expr.MathCallNode(func_name, [a._node for a in args], result_type),
    )


def utc_now() -> _expr.ExprProxy:
    """Returns the current UTC date and time, as a DateTime."""
    return _call("utc_now", [], primitives.DateTime)


def delta_time() -> _expr.ExprProxy:
    """Returns the seconds since the last frame, as a Float."""
    return _call("delta_time", [], primitives.Float)


def smooth_delta_time() -> _expr.ExprProxy:
    """Returns the smoothed seconds since the last frame, as a Float."""
    return _call("smooth_delta_time", [], primitives.Float)


def raw_delta_time() -> _expr.ExprProxy:
    """Returns the unprocessed seconds since the last frame, as a Float."""
    return _call("raw_delta_time", [], primitives.Float)


def inverted_delta_time() -> _expr.ExprProxy:
    """Returns 1 / delta_time(), as a Float."""
    return _call("inverted_delta_time", [], primitives.Float)


def inverted_smooth_delta_time() -> _expr.ExprProxy:
    """Returns 1 / smooth_delta_time(), as a Float."""
    return _call("inverted_smooth_delta_time", [], primitives.Float)


def inverted_raw_delta_time() -> _expr.ExprProxy:
    """Returns 1 / raw_delta_time(), as a Float."""
    return _call("inverted_raw_delta_time", [], primitives.Float)


# =========================================================================
# TimeSpan Factories
# =========================================================================


def _time_span_from(unit: str, n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n units. The TimeSpanFrom nodes take a double."""
    value = _expr.implicit(n, primitives.Double, f"time.{unit}")
    return _call(f"time_span_from_{unit}", [value], primitives.TimeSpan)


def days(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n days."""
    return _time_span_from("days", n)


def hours(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n hours."""
    return _time_span_from("hours", n)


def minutes(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n minutes."""
    return _time_span_from("minutes", n)


def seconds(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n seconds."""
    return _time_span_from("seconds", n)


def milliseconds(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n milliseconds."""
    return _time_span_from("milliseconds", n)


def ticks(n: Any) -> _expr.ExprProxy:
    """Returns a TimeSpan of n ticks, which are 100 nanoseconds each."""
    value = _expr.implicit(n, primitives.Long, "time.ticks")
    return _call("time_span_from_ticks", [value], primitives.TimeSpan)


# =========================================================================
# Unix Time
# =========================================================================


def from_unix_seconds(s: Any) -> _expr.ExprProxy:
    """Returns the UTC DateTime for a Unix time in seconds, given as a Long."""
    value = _expr.implicit(s, primitives.Long, "time.from_unix_seconds")
    return _call("from_unix_seconds", [value], primitives.DateTime)


def from_unix_milliseconds(ms: Any) -> _expr.ExprProxy:
    """Returns the UTC DateTime for a Unix time in milliseconds, given as a Long."""
    value = _expr.implicit(ms, primitives.Long, "time.from_unix_milliseconds")
    return _call("from_unix_milliseconds", [value], primitives.DateTime)


def to_unix_seconds(dt: Any) -> _expr.ExprProxy:
    """Returns a DateTime as a Unix time in whole seconds, as a Long."""
    value = _expr.implicit(dt, primitives.DateTime, "time.to_unix_seconds")
    return _call("to_unix_seconds", [value], primitives.Long)


def to_unix_milliseconds(dt: Any) -> _expr.ExprProxy:
    """Returns a DateTime as a Unix time in milliseconds, as a Long."""
    value = _expr.implicit(dt, primitives.DateTime, "time.to_unix_milliseconds")
    return _call("to_unix_milliseconds", [value], primitives.Long)
