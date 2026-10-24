"""Integration tests for utils.recorder and the Dergflux slot, ray, variable, and async nodes.

Run as: pytest tests/test_recorder_integration.py [--port=<port>]

The graphs run in every engine update, and a Recorder logs what they see,
which the test reads back after the recording is done.
"""

# pylint: disable=missing-function-docstring,redefined-outer-name

from __future__ import annotations

import asyncio
import os
from typing import Any

import pytest

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import time
from pyresonitelink.dergflux import transform
from pyresonitelink.dergflux import variables
from pyresonitelink.generated.data.dynamic import dynamic_value_variable
from pyresonitelink.generated.data.dynamic import dynamic_variable_space
from pyresonitelink.generated.physics.colliders import box_collider
from pyresonitelink.utils import recorder

from tests.test_dergflux_integration import dergflux_slot  # noqa: F401  (fixture)

# Far below the world, so that the ray meets nothing but the test's box.
FLOOR_DEPTH = -50.0  # meters
FLOOR_THICKNESS = 0.1  # meters

# A clip 0.28 s long, which the golf example plays.
SHORT_CLIP = os.path.join(os.path.dirname(__file__), "..", "examples", "75205_golf_hit.wav")
SHORT_CLIP_LENGTH = 0.277  # seconds


class TestRecorder:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_records_one_line_per_update(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """A counter that goes up by one per update is logged without gaps."""
        g = Graph()
        s = g.Space(dergflux_slot, space_name="count")
        s.n = s.IntModelVar("n", value=0)
        rec = recorder.Recorder(g, s, "trace")
        with g.Under(dergflux_slot):
            s.n = s.n + 1
            rec.record(n=s.n)
        await g.build(resolink)

        await rec.start(resolink, lines=20)
        rows = await rec.read(resolink)
        assert len(rows) == 20
        counts = [row["n"] for row in rows]
        assert counts == [counts[0] + i for i in range(20)]
        times = [float(row["t"]) for row in rows]
        assert all(a < b for a, b in zip(times, times[1:]))

    @pytest.mark.asyncio(loop_scope="session")
    async def test_model_vars_read_and_write(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        g = Graph()
        s = g.Space(dergflux_slot, space_name="rw")
        s.v = s.Float3ModelVar("velocity")
        s.text = s.StringModelVar("text", value="")
        await g.build(resolink)

        await s.WriteModelVar(resolink, "v", primitives.Float3(1, 2, 3))
        await s.WriteModelVar(resolink, "text", "hello")
        v = await s.ReadModelVar(resolink, "v")
        assert (float(v.x), float(v.y), float(v.z)) == (1.0, 2.0, 3.0)
        assert await s.ReadModelVar(resolink, "text") == "hello"


class TestRayIntoASurface:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_hit_collider_slot_and_its_variable(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """A ray down onto a box finds the box's Physics/Friction, and the flow goes on after it."""
        floor = await resolink.add_slot(
            parent=dergflux_slot, name="Floor", position=(0, FLOOR_DEPTH, 0),
        )
        await box_collider.BoxCollider(
            size=primitives.Float3(1, FLOOR_THICKNESS, 1),
        ).add_to_slot(resolink, floor)
        await dynamic_variable_space.DynamicVariableSpace(
            space_name="Physics", only_direct_binding=False,
        ).add_to_slot(resolink, floor)
        await dynamic_value_variable.DynamicValueVariable[primitives.Float](
            variable_name="Physics/Friction", value=primitives.Float(0.7),
        ).add_to_slot(resolink, floor)

        g = Graph()
        s = g.Space(dergflux_slot, space_name="ray")
        rec = recorder.Recorder(g, s, "trace")
        floor_ref = slots.ref(floor)
        origin = transform.local_point_to_global(floor_ref, primitives.Float3(0, 1, 0))
        down = transform.local_direction_to_global(floor_ref, primitives.Float3(0, -1, 0))
        with g.Under(dergflux_slot):
            with g.RaycastOne(origin=origin, direction=dm.normalized(down),
                              max_distance=2.0) as hit:
                with hit.on_hit():
                    friction = variables.read(
                        slots.of_component(hit.hit_collider), "Physics/Friction",
                        primitives.Float,
                    )
                    rec.record(where="hit", d=hit.hit_distance,
                               f=friction.value, found=friction.found)
            rec.record(where="after")
        await g.build(resolink)

        await rec.start(resolink, lines=6)
        rows = await rec.read(resolink)
        hits = [row for row in rows if row["where"] == "hit"]
        afters = [row for row in rows if row["where"] == "after"]
        assert hits and afters
        # Each hit line is followed by the after line of the same update.
        for i, row in enumerate(rows[:-1]):
            if row["where"] == "hit":
                assert rows[i + 1]["where"] == "after"
                assert rows[i + 1]["t"] == row["t"]
        for row in hits:
            assert float(row["d"]) == pytest.approx(1 - FLOOR_THICKNESS / 2, abs=1e-3)
            assert float(row["f"]) == pytest.approx(0.7)
            assert row["found"] == 1.0

    @pytest.mark.asyncio(loop_scope="session")
    async def test_distances_are_in_lengths_of_the_direction(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """A ray whose direction is 2 m long reaches twice its maximum distance.

        The box's top is 0.95 m below the origin. A maximum distance of 0.6
        would stop short of it in meters, and reaches 1.2 m in lengths of
        the direction, where the hit is at 0.475 lengths. A maximum
        distance of 0.4 reaches 0.8 m and misses. The golf example's ball
        once found the ground early because its ray along the velocity
        wasn't normalized.
        """
        floor = await resolink.add_slot(
            parent=dergflux_slot, name="Floor", position=(0, FLOOR_DEPTH, 0),
        )
        await box_collider.BoxCollider(
            size=primitives.Float3(1, FLOOR_THICKNESS, 1),
        ).add_to_slot(resolink, floor)

        g = Graph()
        s = g.Space(dergflux_slot, space_name="units")
        rec = recorder.Recorder(g, s, "trace")
        floor_ref = slots.ref(floor)
        origin = transform.local_point_to_global(floor_ref, primitives.Float3(0, 1, 0))
        down = transform.local_direction_to_global(floor_ref, primitives.Float3(0, -2, 0))
        with g.Under(dergflux_slot):
            for name, reach in (("long", 0.6), ("short", 0.4)):
                with g.RaycastOne(origin=origin, direction=down, max_distance=reach) as hit:
                    with hit.on_hit():
                        rec.record(where=f"{name}_hit", d=hit.hit_distance)
                    with hit.on_miss():
                        rec.record(where=f"{name}_miss")
        await g.build(resolink)

        await rec.start(resolink, lines=6)
        rows = await rec.read(resolink)
        kinds = {str(row["where"]) for row in rows}
        assert kinds == {"long_hit", "short_miss"}
        for row in rows:
            if row["where"] == "long_hit":
                assert float(row["d"]) == pytest.approx((1 - FLOOR_THICKNESS / 2) / 2, abs=1e-3)


class TestAsyncContinuations:
    """The statements after an async action run when the action ends.

    Each flow runs once, when the test sets its "go" variable, and writes
    the world time at each step. The steps are plain writes, which the
    builder chains from one to the next. Two or more statements that
    branch, such as Recorder.record calls, are called from a Sequence
    instead, which would hide a missing continuation. Until Oct 2026 the
    Delay actions and PlayOneShotAndWait declared no continuations, so
    the statements after them were wired to a missing OnSuccess and never
    ran.
    """

    @staticmethod
    async def _times(resolink: client.Client, s: Any, names: list[str]) -> list[float]:
        """Waits until the flow has written its last time, and returns each one."""
        deadline = asyncio.get_running_loop().time() + 10
        while float(await s.ReadModelVar(resolink, names[-1])) == 0:
            assert asyncio.get_running_loop().time() < deadline, f"{names[-1]} was never written"
            await asyncio.sleep(0.1)
        return [float(await s.ReadModelVar(resolink, name)) for name in names]

    @pytest.mark.asyncio(loop_scope="session")
    async def test_delay_triggers_at_once_and_goes_on_after(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """OnTriggered runs as a Delay starts, and the next statement runs when it ends."""
        g = Graph()
        s = g.Space(dergflux_slot, space_name="delay")
        s.go = s.BoolModelVar("go", value=False)
        s.start = s.DoubleModelVar("start", value=0.0)
        s.triggered = s.DoubleModelVar("triggered", value=0.0)
        s.after = s.DoubleModelVar("after", value=0.0)
        with g.Under(dergflux_slot):
            with g.If(s.go):
                s.go = False
                s.start = time.world_time()
                with g.DelaySeconds(duration=0.5) as d:
                    with d.on_triggered():
                        s.triggered = time.world_time()
                s.after = time.world_time()
        await g.build(resolink)

        await s.WriteModelVar(resolink, "go", True)
        start, triggered, after = await self._times(resolink, s, ["start", "triggered", "after"])
        assert triggered == start
        assert after - start == pytest.approx(0.5, abs=0.1)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_statement_after_play_one_shot_and_wait_runs_when_the_clip_ends(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        g = Graph()
        s = g.Space(dergflux_slot, space_name="wait")
        s.go = s.BoolModelVar("go", value=False)
        s.start = s.DoubleModelVar("start", value=0.0)
        s.after = s.DoubleModelVar("after", value=0.0)
        clip = await resolink.create_audio_clip(dergflux_slot, SHORT_CLIP)
        with g.Under(dergflux_slot):
            with g.If(s.go):
                s.go = False
                s.start = time.world_time()
                with g.PlayOneShotAndWait(clip=clip, volume=0.2):
                    pass
                s.after = time.world_time()
        await g.build(resolink)

        await s.WriteModelVar(resolink, "go", True)
        start, after = await self._times(resolink, s, ["start", "after"])
        assert after - start == pytest.approx(SHORT_CLIP_LENGTH, abs=0.15)
