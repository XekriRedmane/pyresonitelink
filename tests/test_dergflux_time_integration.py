"""Integration tests for Dergflux conversions and time support.

Run as: pytest tests/test_dergflux_time_integration.py [--port=<port>]

Each test builds a graph that runs once, gated by a "ran" model variable,
and reads the results back from the model variables.
"""

# pylint: disable=missing-function-docstring,redefined-outer-name

from __future__ import annotations

import datetime
from typing import Any

import pytest

from pyresonitelink import client
from pyresonitelink.data import timeformats
from pyresonitelink.dergflux import Graph, time
from pyresonitelink.dergflux import _math as dm

from tests.test_dergflux_integration import (  # noqa: F401  (fixture)
    dergflux_slot,
    read_model_var,
    wait_for_ran,
)


class TestConversions:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_float_accumulates_int_loop_index(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """total (float) += i (int) widens i, so 0 + 1 + 2 + 3 + 4 = 10."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="widen")
        g = Graph()
        s = g.Space(slot, space_name="widen")
        s.total = s.FloatModelVar("total", value=0.0)
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.For(5) as f:
                    with f.OnIterate() as i:
                        s.total = s.total + i
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "total") == pytest.approx(10.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_explicit_narrowing_truncates(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """to_int(2.7) uses Cast_float_To_int, which truncates as C# does."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="narrow")
        g = Graph()
        s = g.Space(slot, space_name="narrow")
        s.x = s.FloatModelVar("x", value=2.7)
        s.n = s.IntModelVar("n")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.n = dm.to_int(s.x)
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "n") == 2


class TestTime:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_timespan_arithmetic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """hours(2) + minutes(30) is 2.5 hours, or 9000 seconds."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="span")
        g = Graph()
        s = g.Space(slot, space_name="span")
        s.span = s.TimeSpanModelVar("span")
        s.total_seconds = s.DoubleModelVar("total_seconds")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.span = time.hours(2) + time.minutes(30)
                s.total_seconds = s.span.total_seconds
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        span = await read_model_var(resolink, slot, "span")
        assert timeformats.parse_timespan(span) == datetime.timedelta(hours=2.5)
        assert await read_model_var(resolink, slot, "total_seconds") == pytest.approx(9000.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_unix_time_and_datetime_arithmetic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Unix time 1700000000 is 2023-11-14T22:13:20Z, and a day later is the 15th."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="unix")
        g = Graph()
        s = g.Space(slot, space_name="unix")
        s.moment = s.DateTimeModelVar("moment")
        s.next_day = s.DateTimeModelVar("next_day")
        s.year = s.IntModelVar("year")
        s.unix = s.LongModelVar("unix")
        s.gap = s.TimeSpanModelVar("gap")
        s.ran = s.BoolModelVar("ran")
        start = datetime.datetime(2023, 11, 14, 22, 13, 20, tzinfo=datetime.timezone.utc)
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.moment = time.from_unix_seconds(1700000000)
                s.next_day = s.moment + time.days(1)
                s.year = s.moment.year
                s.unix = time.to_unix_seconds(s.next_day)
                s.gap = s.next_day - start
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        moment = timeformats.parse_datetime(await read_model_var(resolink, slot, "moment"))
        assert moment == start
        next_day = timeformats.parse_datetime(await read_model_var(resolink, slot, "next_day"))
        assert next_day == start + datetime.timedelta(days=1)
        assert await read_model_var(resolink, slot, "year") == 2023
        assert await read_model_var(resolink, slot, "unix") == 1700000000 + 86400
        gap = timeformats.parse_timespan(await read_model_var(resolink, slot, "gap"))
        assert gap == datetime.timedelta(days=1)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_utc_now_is_current(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        slot = await resolink.add_slot(parent=dergflux_slot, name="now")
        g = Graph()
        s = g.Space(slot, space_name="now")
        s.now = s.DateTimeModelVar("now")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.now = time.utc_now()
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        now = timeformats.parse_datetime(await read_model_var(resolink, slot, "now"))
        delta = abs(datetime.datetime.now(datetime.timezone.utc) - now)
        assert delta < datetime.timedelta(minutes=1)
