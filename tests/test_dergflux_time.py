"""Tests for Dergflux time, datetime, and timespan support."""

from __future__ import annotations

import pytest
from typing import Any

from pyresonitelink.dergflux import Graph, time, math
from pyresonitelink.data import primitives


def test_time_utc_now() -> None:
    g = Graph()
    now = time.utc_now()
    assert now._node._type == primitives.DateTime


def test_time_delta_time() -> None:
    g = Graph()
    dt = time.delta_time()
    assert dt._node._type == primitives.Float


def test_datetime_properties() -> None:
    g = Graph()
    now = time.utc_now()
    
    # Check property access inferred types
    assert now.year._node._type == primitives.Int
    assert now.hour._node._type == primitives.Int
    assert now.second._node._type == primitives.Int
    assert now.ticks._node._type == primitives.Int
    
    # from pyresonitelink.generated._enums.day_of_week import DayOfWeek
    # assert now.day_of_week._node._type == DayOfWeek
    assert now.day_of_week._node._type == primitives.Int


def test_timespan_factories() -> None:
    assert time.days(1)._node._type == primitives.TimeSpan
    assert time.hours(1)._node._type == primitives.TimeSpan
    assert time.minutes(1)._node._type == primitives.TimeSpan
    assert time.seconds(1)._node._type == primitives.TimeSpan
    assert time.milliseconds(1)._node._type == primitives.TimeSpan
    assert time.ticks(1)._node._type == primitives.TimeSpan


def test_timespan_properties() -> None:
    ts = time.hours(1)
    
    assert ts.hours._node._type == primitives.Int
    assert ts.total_hours._node._type == primitives.Double
    assert ts.total_seconds._node._type == primitives.Double


def test_datetime_arithmetic() -> None:
    now = time.utc_now()
    later = now + time.hours(1)
    
    assert later._node._type == primitives.DateTime
    
    # DateTime - DateTime = TimeSpan
    diff = later - now
    assert diff._node._type == primitives.TimeSpan


def test_unix_conversions() -> None:
    now = time.utc_now()
    
    unix_s = time.to_unix_seconds(now)
    assert unix_s._node._type == primitives.Double
    
    unix_ms = time.to_unix_milliseconds(now)
    assert unix_ms._node._type == primitives.Long
    
    dt_from_s = time.from_unix_seconds(unix_s)
    assert dt_from_s._node._type == primitives.DateTime
