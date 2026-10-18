"""Tests for Dergflux time, datetime, and timespan support."""

from __future__ import annotations

import datetime

import pytest

from pyresonitelink.dergflux import _expr, time
from pyresonitelink.data import primitives


def test_time_utc_now() -> None:
    now = time.utc_now()
    assert now._node._type is primitives.DateTime
    assert isinstance(now._node, _expr.MathCallNode)
    assert now._node.func_name == "utc_now"


def test_delta_time_variants_are_distinct_calls() -> None:
    # Each must build its own node, not all DeltaTime.
    names = {
        f()._node.func_name  # type: ignore[attr-defined]
        for f in (time.delta_time, time.smooth_delta_time, time.raw_delta_time)
    }
    assert names == {"delta_time", "smooth_delta_time", "raw_delta_time"}
    assert time.delta_time()._node._type is primitives.Float


def test_datetime_properties() -> None:
    now = time.utc_now()
    assert now.year._node._type is primitives.Int
    assert now.hour._node._type is primitives.Int
    assert now.second._node._type is primitives.Int
    # DateTimeTicks is a DateTimeExtractor<long>.
    assert now.ticks._node._type is primitives.Long


def test_day_of_week_is_unsupported() -> None:
    with pytest.raises(AttributeError, match="DayOfWeek"):
        time.utc_now().day_of_week  # pylint: disable=expression-not-assigned


def test_timespan_factories() -> None:
    for factory in (time.days, time.hours, time.minutes, time.seconds, time.milliseconds):
        span = factory(1)
        assert span._node._type is primitives.TimeSpan
        # The TimeSpanFrom nodes take a double.
        assert span._node.args[0]._type is primitives.Double  # type: ignore[attr-defined]
    assert time.ticks(1)._node.args[0]._type is primitives.Long  # type: ignore[attr-defined]


def test_timespan_factory_widens_int_expression() -> None:
    index = _expr.ExprProxy(_expr.LoopIndexNode())
    arg = time.hours(index)._node.args[0]  # type: ignore[attr-defined]
    assert isinstance(arg, _expr.CastNode)
    assert arg._type is primitives.Double


def test_ticks_rejects_float() -> None:
    with pytest.raises(TypeError, match="time.ticks"):
        time.ticks(1.5)


def test_timespan_properties() -> None:
    span = time.hours(1)
    assert span.hours._node._type is primitives.Int
    assert span.ticks._node._type is primitives.Long
    assert span.total_hours._node._type is primitives.Double
    assert span.total_seconds._node._type is primitives.Double


def test_datetime_arithmetic() -> None:
    now = time.utc_now()
    later = now + time.hours(1)
    assert later._node._type is primitives.DateTime
    earlier = now - time.minutes(5)
    assert earlier._node._type is primitives.DateTime
    assert (later - now)._node._type is primitives.TimeSpan


def test_timespan_plus_datetime_puts_datetime_first() -> None:
    result = time.hours(1) + time.utc_now()
    assert result._node._type is primitives.DateTime
    assert result._node.left._type is primitives.DateTime  # type: ignore[attr-defined]


def test_datetime_literals() -> None:
    start = datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc)
    elapsed = time.utc_now() - start
    assert elapsed._node._type is primitives.TimeSpan
    assert elapsed._node.right._type is primitives.DateTime  # type: ignore[attr-defined]
    soon = time.utc_now() + datetime.timedelta(minutes=5)
    assert soon._node._type is primitives.DateTime


def test_unix_conversions() -> None:
    now = time.utc_now()
    # ToUnixSeconds and ToUnixMilliseconds are DateTimeConverter<long>.
    assert time.to_unix_seconds(now)._node._type is primitives.Long
    assert time.to_unix_milliseconds(now)._node._type is primitives.Long
    from_s = time.from_unix_seconds(time.to_unix_seconds(now))
    assert from_s._node._type is primitives.DateTime
    assert time.from_unix_milliseconds(1700000000000)._node._type is primitives.DateTime
