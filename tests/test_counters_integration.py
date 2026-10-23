"""Integration tests for pyresonitelink.utils.counters.

Run as: pytest tests/test_counters_integration.py [--port=<port>]

drum_turns is checked by a graph that runs once, gated by a "ran" model
variable. add_detents runs in every update, so its tests start the number
at a value and read the variables until they settle.
"""

# pylint: disable=missing-function-docstring,redefined-outer-name

from __future__ import annotations

from typing import Any

import pytest

from pyresonitelink import client
from pyresonitelink.dergflux import Graph
from pyresonitelink.utils import counters

from tests.test_dergflux_integration import (  # noqa: F401  (fixture)
    dergflux_slot,
    read_model_var,
    wait_for_ran,
)
from tests.test_dergflux_math_integration import poll


class TestDrumTurns:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_carries(self, resolink: client.Client, dergflux_slot: Any) -> None:
        """At 129.5 the units drum is halfway from 9 to 0, so the tens drum is halfway from 2 to 3."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="drums")
        g = Graph()
        s = g.Space(slot, space_name="drums")
        s.n = s.FloatModelVar("n", value=129.5)
        for place in (1, 10, 100, 1000):
            setattr(s, f"r{place}", s.FloatModelVar(f"r{place}"))
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                for place in (1, 10, 100, 1000):
                    setattr(s, f"r{place}", counters.drum_turns(s.n, place))
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        expected = {1: 9.5, 10: 2.5, 100: 1.0, 1000: 0.0}
        for place, turns in expected.items():
            assert await read_model_var(resolink, slot, f"r{place}") == pytest.approx(turns, abs=1e-4)


async def _detents(
    resolink: client.Client, parent: Any, name: str, value: float, held: bool | None,
) -> Any:
    """Builds a detent flow for a number that starts at value, in hundredths, and returns its slot."""
    slot = await resolink.add_slot(parent=parent, name=name)
    g = Graph()
    s = g.Space(slot, space_name=name)
    s.value = s.FloatModelVar("value", value=value)
    if held is not None:
        s.held = s.BoolModelVar("held", value=held)
    counters.add_detents(g, s, slot, "value", scale=100, held=None if held is None else s.held)
    await g.build(resolink)
    return slot


async def _settled(resolink: client.Client, slot: Any, var: str, expected: float) -> float:
    """Reads a variable until it is within 0.002 of expected, for up to 5 s, and returns it."""
    async def read() -> Any:
        return await read_model_var(resolink, slot, var, timeout=1.0)
    return await poll(read, lambda v: v is not None and abs(v - expected) < 0.002)


class TestAddDetents:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_leans_before_the_threshold(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """0.42 hundredths from the detent, the drums lean a quarter of the way and don't snap."""
        slot = await _detents(resolink, dergflux_slot, "lean", 0.0042, held=True)
        assert await _settled(resolink, slot, "detent_position", 0.105) == pytest.approx(0.105, abs=0.002)
        assert await read_model_var(resolink, slot, "detent") == pytest.approx(0.0)
        assert await read_model_var(resolink, slot, "value") == pytest.approx(0.0042, abs=1e-6)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_snaps_past_the_threshold(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """At 0.62 the detent moves to 1, and the drums lean back from it by a quarter of 0.38."""
        slot = await _detents(resolink, dergflux_slot, "snap", 0.0062, held=True)
        assert await _settled(resolink, slot, "detent_position", 0.905) == pytest.approx(0.905, abs=0.002)
        assert await read_model_var(resolink, slot, "detent") == pytest.approx(1.0)
        assert await read_model_var(resolink, slot, "value") == pytest.approx(0.0062, abs=1e-6)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_released_number_goes_to_the_detent(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        slot = await _detents(resolink, dergflux_slot, "release", 0.0062, held=False)
        assert await _settled(resolink, slot, "detent_position", 1.0) == pytest.approx(1.0, abs=0.002)
        assert await read_model_var(resolink, slot, "value") == pytest.approx(0.01, abs=1e-6)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_without_held_the_number_stays(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        slot = await _detents(resolink, dergflux_slot, "noheld", 0.0062, held=None)
        assert await _settled(resolink, slot, "detent_position", 0.905) == pytest.approx(0.905, abs=0.002)
        assert await read_model_var(resolink, slot, "value") == pytest.approx(0.0062, abs=1e-6)
