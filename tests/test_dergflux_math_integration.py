"""Integration tests for Dergflux shaping, rotations, world time, and Bind.

Run as: pytest tests/test_dergflux_math_integration.py [--port=<port>]

The math tests build a graph that runs once, gated by a "ran" model
variable, and read the results back from the model variables. The Bind
tests read the driven field until it has the expected value, since a
binding drives its field in every engine update.
"""

# pylint: disable=missing-function-docstring,redefined-outer-name

from __future__ import annotations

import asyncio
import math
from collections.abc import Awaitable, Callable
from typing import Any

import pytest

from pyresonitelink import client
from pyresonitelink.components.data import ValueField
from pyresonitelink.data import primitives
from pyresonitelink.dergflux import Graph, time
from pyresonitelink.dergflux import _math as dm

from tests.test_dergflux_integration import (  # noqa: F401  (fixture)
    dergflux_slot,
    read_model_var,
    wait_for_ran,
)


async def poll(read: Callable[[], Awaitable[Any]], check: Callable[[Any], bool]) -> Any:
    """Reads a value every 0.1 s until it passes the check, for up to 5 s.

    Returns:
        The last value read, whether or not it passed.
    """
    value = None
    for _ in range(50):
        value = await read()
        if check(value):
            break
        await asyncio.sleep(0.1)
    return value


class TestConditional:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_selects_by_condition(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """conditional(true, 1, 2) is 1 and conditional(false, 1, 2) is 2."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="cond")
        g = Graph()
        s = g.Space(slot, space_name="cond")
        s.yes = s.BoolModelVar("yes", value=True)
        s.no = s.BoolModelVar("no", value=False)
        s.a = s.FloatModelVar("a", value=1.0)
        s.b = s.FloatModelVar("b", value=2.0)
        s.r_yes = s.FloatModelVar("r_yes")
        s.r_no = s.FloatModelVar("r_no")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.r_yes = dm.conditional(s.yes, s.a, s.b)
                s.r_no = dm.conditional(s.no, s.a, s.b)
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "r_yes") == pytest.approx(1.0)
        assert await read_model_var(resolink, slot, "r_no") == pytest.approx(2.0)


class TestShaping:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_smoothstep_and_smootherstep(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """The one- and three-argument forms, including a clamped x."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="shape")
        g = Graph()
        s = g.Space(slot, space_name="shape")
        s.x = s.FloatModelVar("x", value=0.25)
        s.e = s.FloatModelVar("e", value=1.5)
        s.over = s.FloatModelVar("over", value=3.0)
        s.step = s.FloatModelVar("step")
        s.edges = s.FloatModelVar("edges")
        s.clamped = s.FloatModelVar("clamped")
        s.smoother = s.FloatModelVar("smoother")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.step = dm.smoothstep(s.x)
                s.edges = dm.smoothstep(0, 2, s.e)
                s.clamped = dm.smoothstep(0, 2, s.over)
                s.smoother = dm.smootherstep(s.x)
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        # 3x² - 2x³ at 0.25, and at 1.5 / 2 = 0.75.
        assert await read_model_var(resolink, slot, "step") == pytest.approx(0.15625)
        assert await read_model_var(resolink, slot, "edges") == pytest.approx(0.84375)
        assert await read_model_var(resolink, slot, "clamped") == pytest.approx(1.0)
        # 6x⁵ - 15x⁴ + 10x³ at 0.25.
        assert await read_model_var(resolink, slot, "smoother") == pytest.approx(0.103515625)


class TestLerp:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_lerp_and_inverse_lerp(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """lerp clamps t, lerp_unclamped doesn't, and inverse_lerp undoes lerp."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="lerp")
        g = Graph()
        s = g.Space(slot, space_name="lerp")
        s.t = s.FloatModelVar("t", value=0.25)
        s.over = s.FloatModelVar("over", value=1.5)
        s.x = s.DoubleModelVar("x", value=4.0)
        s.v = s.Float3ModelVar("v", value=primitives.Float3(1, 1, 1))
        s.mid = s.FloatModelVar("mid")
        s.clamped = s.FloatModelVar("clamped")
        s.unclamped = s.FloatModelVar("unclamped")
        s.inverse = s.FloatModelVar("inverse")
        s.inverse_v = s.Float3ModelVar("inverse_v")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.mid = dm.lerp(2, 10, s.t)
                s.clamped = dm.lerp(2, 10, s.over)
                s.unclamped = dm.lerp_unclamped(2, 10, s.over)
                s.inverse = dm.inverse_lerp(2, 10, s.x)
                s.inverse_v = dm.inverse_lerp(
                    primitives.Float3(0, 0, 0), primitives.Float3(2, 4, 8), s.v,
                )
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "mid") == pytest.approx(4.0)
        assert await read_model_var(resolink, slot, "clamped") == pytest.approx(10.0)
        assert await read_model_var(resolink, slot, "unclamped") == pytest.approx(14.0)
        assert await read_model_var(resolink, slot, "inverse") == pytest.approx(0.25)
        v = await read_model_var(resolink, slot, "inverse_v")
        assert [v["x"], v["y"], v["z"]] == pytest.approx([0.5, 0.25, 0.125])


class TestRotationsAndTime:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_axis_angle_and_from_euler(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """90 degrees about Y, both ways, is (0, sin 45°, 0, cos 45°)."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="rot")
        g = Graph()
        s = g.Space(slot, space_name="rot")
        s.q = s.FloatQModelVar("q")
        s.e = s.FloatQModelVar("e")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.q = dm.axis_angle(primitives.Float3(0, 1, 0), 90.0)
                s.e = dm.from_euler(primitives.Float3(0, 90, 0))
                s.ran = True
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        half = math.sqrt(0.5)
        for name in ("q", "e"):
            q = await read_model_var(resolink, slot, name)
            assert [q["x"], q["y"], q["z"], q["w"]] == pytest.approx(
                [0, half, 0, half], abs=1e-6,
            ), name

    @pytest.mark.asyncio(loop_scope="session")
    async def test_world_time_advances(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """world_time() is positive, and later than a stored earlier value."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="wtime")
        g = Graph()
        s = g.Space(slot, space_name="wtime")
        s.t = s.DoubleModelVar("t")
        s.later = s.BoolModelVar("later")
        s.ran = s.BoolModelVar("ran")
        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.t = time.world_time()
                s.ran = True
            # The bare write runs on every update after the If.
            s.later = time.world_time() > s.t
        await g.build(resolink)
        assert await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "t") > 0
        assert await read_model_var(resolink, slot, "later") is True


class TestBind:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_expression_drives_component_field(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Binding x * 2, with x = 3, drives a ValueField<float> to 6."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="bind")
        field = ValueField[primitives.Float](primitives.Float(1.0))
        await field.add_to_slot(resolink, slot)
        g = Graph()
        s = g.Space(slot, space_name="bind")
        s.x = s.FloatModelVar("x", value=3.0)
        g.Bind(s.x * 2, field, "Value", slot=slot)
        await g.build(resolink)

        async def read() -> Any:
            await field.refresh(resolink)
            return field.value

        assert await poll(read, lambda v: v == 6.0) == pytest.approx(6.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_axis_angle_drives_slot_rotation(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Binding axis_angle(+Y, 90) to a slot's Rotation turns the slot."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="turn")
        wheel = await resolink.add_slot(parent=slot, name="wheel")
        g = Graph()
        s = g.Space(slot, space_name="turn")
        s.angle = s.FloatModelVar("angle", value=90.0)
        g.Bind(dm.axis_angle(primitives.Float3(0, 1, 0), s.angle), wheel, "Rotation", slot=slot)
        await g.build(resolink)

        async def read() -> Any:
            data = (await resolink.get_slot(wheel)).data
            assert data is not None and data.rotation is not None
            return data.rotation.value

        half = math.sqrt(0.5)
        rotation = await poll(read, lambda q: abs(q.y - half) < 1e-5)
        assert [rotation.x, rotation.y, rotation.z, rotation.w] == pytest.approx(
            [0, half, 0, half], abs=1e-5,
        )
