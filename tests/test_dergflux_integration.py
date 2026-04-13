"""Integration tests for the Dergflux DSL against a live Resonite server.

Each test builds a ProtoFlux graph via Dergflux, verifies that all
connections are wired correctly, waits for execution, and checks
results.

**Single-shot gate pattern**: every test declares ``ran`` (BoolModelVar,
initially False).  The flow only executes when ``ran`` is False, and
sets ``ran = True`` after one execution.  This ensures deterministic
single-shot evaluation without needing dynamic variables.

**E712 suppression**: ``s.ran == False`` triggers flake8 E712.  In
Dergflux ``==`` builds a ``ValueEquals<bool>`` ProtoFlux node — the
``is`` operator cannot be overridden, so ``==`` is correct.

All variables use ``*ModelVar`` (backed by ``DataModelValueFieldStore``)
to avoid dynamic variable binding delays.

Usage:
    pytest --port=<port> tests/test_dergflux_integration.py -v -s
"""

from __future__ import annotations

import asyncio
import time
from typing import Any

import pytest
import pytest_asyncio

from pyresonitelink import client
from pyresonitelink.data import messages
from pyresonitelink.dergflux import Graph, Outcome


# =========================================================================
# Helpers
# =========================================================================


async def verify_connections(
    resolink: client.Client, slot_id: str,
) -> list[str]:
    """Check all components on a slot for missing references.

    Returns a list of problems (empty = all OK).
    """
    optional = {
        "OnNotFound", "OnFailed", "OnFail", "OnFalse", "OnTrue",
        "UpdatingUser", "SkipIfNull", "OnlyForUser",
        "OnSuccess", "OnWritten",
    }
    problems: list[str] = []
    resp: Any = await resolink.request_json(
        messages.GetSlot(slotId=slot_id, depth=0),
    )
    for comp in resp.get("data", {}).get("components", []):
        cid: str = comp["id"]
        full: Any = await resolink.request_json(
            messages.GetComponent(componentId=cid),
        )
        data: Any = full.get("data") or {}
        ct: str = (data.get("componentType") or "?").rsplit(".", 1)[-1]
        members_dict: Any = data.get("members") or {}
        for mname, mval in members_dict.items():
            if not isinstance(mval, dict):
                continue
            dtype = mval.get("$type", "")
            tid = mval.get("targetId")
            if dtype == "reference" and tid is None and mname not in optional:
                problems.append(f"{cid} ({ct}): {mname} -> null")
    return problems


async def read_model_var(
    resolink: client.Client,
    parent_slot: Any,
    var_name: str,
    timeout: float = 5.0,
) -> Any:
    """Read a model variable's value from its +Store companion, with polling.
    
    Only returns non-None values. If after timeout it still hasn't found 
    a non-None value, it returns the last seen value (or None).
    """
    start_time = time.time()
    last_val = None
    while time.time() - start_time < timeout:
        # Search direct children only (depth=1) to avoid name collisions
        parent_resp: Any = await resolink.request_json(
            messages.GetSlot(slotId=parent_slot.id, depth=1),
        )
        child_id: str | None = None
        for child in parent_resp.get("data", {}).get("children", []):
            if child.get("name", {}).get("value") == var_name:
                child_id = child["id"]
                break
        
        if child_id is not None:
            resp: Any = await resolink.request_json(
                messages.GetSlot(slotId=child_id, depth=0),
            )
            for comp in resp.get("data", {}).get("components", []):
                ct: str = comp.get("componentType", "")
                if "+Store" not in ct:
                    continue
                full: Any = await resolink.request_json(
                    messages.GetComponent(componentId=comp["id"]),
                )
                val_info: Any = (
                    (full.get("data") or {}).get("members", {}).get("Value")
                )
                if val_info is not None:
                    val = val_info.get("value") if isinstance(val_info, dict) else getattr(val_info, "value", None)
                    if val is not None:
                        # If we're waiting for a non-zero value, keep polling
                        if val != 0 and val != False:
                            return val
                        last_val = val
        
        await asyncio.sleep(0.5)
    
    return last_val


def _slot_id(slot: Any) -> str:
    """Extract slot ID with assertion for type safety."""
    sid: str | None = slot.id
    assert sid is not None, "Slot has no ID"
    return sid


# =========================================================================
# Fixtures
# =========================================================================


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def dergflux_slot(
    resolink: client.Client,
    request: pytest.FixtureRequest,
) -> Any:
    """Create a unique parent slot for each dergflux integration test."""
    name = f"__dergflux_{request.node.name}__"
    old = await resolink.find_slot("Root", name=name)
    if old is not None:
        await resolink.remove_slot(slot=old)
        await asyncio.sleep(0.2)
    slot = await resolink.add_slot(name=name)
    yield slot
    await resolink.remove_slot(slot=slot)
    await asyncio.sleep(0.2)




# =========================================================================
# Tests
# =========================================================================

WAIT = 5.0  # seconds to wait for graph execution


async def wait_for_ran(resolink: client.Client, slot: Any, timeout: float = 20.0) -> bool:
    """Poll the 'ran' variable until it becomes True."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        val = await read_model_var(resolink, slot, "ran", timeout=1.0)
        if val is True or val == 1:
            # Give the server plenty of time to finish writing 
            # other variables in the same impulse
            await asyncio.sleep(3.0)
            return True
        await asyncio.sleep(0.2)
    return False


class TestBareWrite:
    """Test simple variable assignment: z = x + 3."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_bare_write(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + 3 where x=2, expect z=5."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="bare_write",
        )
        g = Graph()
        s = g.Space(slot, name="bare_write")
        s.x = s.FloatModelVar("x", value=2.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + 3
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(5.0)

class TestArithmetic:
    """Test arithmetic operators."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + y where x=3, y=4, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_add",
        )
        g = Graph()
        s = g.Space(slot, name="arith_add")
        s.x = s.FloatModelVar("x", value=3.0)
        s.y = s.FloatModelVar("y", value=4.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(7.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_sub(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x - y where x=10, y=3, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_sub",
        )
        g = Graph()
        s = g.Space(slot, name="arith_sub")
        s.x = s.FloatModelVar("x", value=10.0)
        s.y = s.FloatModelVar("y", value=3.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x - s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(7.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mul(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x * y where x=3, y=5, expect z=15."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_mul",
        )
        g = Graph()
        s = g.Space(slot, name="arith_mul")
        s.x = s.FloatModelVar("x", value=3.0)
        s.y = s.FloatModelVar("y", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x * s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(15.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_div(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x / y where x=15, y=3, expect z=5."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_div",
        )
        g = Graph()
        s = g.Space(slot, name="arith_div")
        s.x = s.FloatModelVar("x", value=15.0)
        s.y = s.FloatModelVar("y", value=3.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x / s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(5.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mod(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x % y where x=17, y=5, expect z=2."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_mod",
        )
        g = Graph()
        s = g.Space(slot, name="arith_mod")
        s.x = s.FloatModelVar("x", value=17.0)
        s.y = s.FloatModelVar("y", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x % s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(2.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_neg(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = -x where x=7, expect z=-7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_neg",
        )
        g = Graph()
        s = g.Space(slot, name="arith_neg")
        s.x = s.FloatModelVar("x", value=7.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = -s.x
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(-7.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_const_coercion(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + 10 where x=5.0 — int constant coerced to float."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_coerce",
        )
        g = Graph()
        s = g.Space(slot, name="arith_coerce")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + 10
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(15.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_chained_ops(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = (x + 3) * 2 where x=4, expect z=14."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_chain",
        )
        g = Graph()
        s = g.Space(slot, name="arith_chain")
        s.x = s.FloatModelVar("x", value=4.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = (s.x + 3) * 2
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(14.0)

        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

class TestIfElse:
    """Test If/Else flow control."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_true_branch(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x < 3: z = 1, else: z = 2. x=1, expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_true",
        )
        g = Graph()
        s = g.Space(slot, name="if_true")
        s.x = s.FloatModelVar("x", value=1.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x < 3):
                    s.z = 1.0
                with g.Else():
                    s.z = 2.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(1.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_false_branch(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x < 3: z = 1, else: z = 2. x=5, expect z=2."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_false",
        )
        g = Graph()
        s = g.Space(slot, name="if_false")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x < 3):
                    s.z = 1.0
                with g.Else():
                    s.z = 2.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(2.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_with_continuation(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """if x<3: tmp=x+3 else: tmp=x-3; z=tmp+1. x=2, expect z=6."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_cont",
        )
        g = Graph()
        s = g.Space(slot, name="if_cont")
        s.x = s.FloatModelVar("x", value=2.0)
        s.z = s.FloatModelVar("z")
        s.tmp = s.FloatModelVar("tmp")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x < 3):
                    s.tmp = s.x + 3
                with g.Else():
                    s.tmp = s.x - 3
                s.z = s.tmp + 1
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(6.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_without_else(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x<3: z=99. x=1. Continuation w=1 always runs."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_no_else",
        )
        g = Graph()
        s = g.Space(slot, name="if_no_else")
        s.x = s.FloatModelVar("x", value=1.0)
        s.z = s.FloatModelVar("z")
        s.w = s.FloatModelVar("w")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x < 3):
                    s.z = 99.0
                s.w = 1.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(99.0)
        assert await read_model_var(resolink, slot, "w") == pytest.approx(1.0)

        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

class TestMultipleWrites:
    """Test chaining multiple variable writes."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_sequential_writes(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """a=1, b=2, c=3 in sequence."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="seq_writes",
        )
        g = Graph()
        s = g.Space(slot, name="seq_writes")
        s.a = s.FloatModelVar("a")
        s.b = s.FloatModelVar("b")
        s.c = s.FloatModelVar("c")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.a = 1.0
                s.b = 2.0
                s.c = 3.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "a") == pytest.approx(1.0)
        assert await read_model_var(resolink, slot, "b") == pytest.approx(2.0)
        assert await read_model_var(resolink, slot, "c") == pytest.approx(3.0)

        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

class TestIntVariables:
    """Test integer variable operations."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_int_arithmetic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + y with IntModelVars. x=3, y=4, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="int_arith",
        )
        g = Graph()
        s = g.Space(slot, name="int_arith")
        s.x = s.IntModelVar("x", value=3)
        s.y = s.IntModelVar("y", value=4)
        s.z = s.IntModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + s.y
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == 7

        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

class TestComparison:
    """Test comparison operators via If branching."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_less_than(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x < 10 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_lt",
        )
        g = Graph()
        s = g.Space(slot, name="cmp_lt")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x < 10):
                    s.z = 1.0
                with g.Else():
                    s.z = 0.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(1.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_greater_than(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x > 3 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_gt",
        )
        g = Graph()
        s = g.Space(slot, name="cmp_gt")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x > 3):
                    s.z = 1.0
                with g.Else():
                    s.z = 0.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(1.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_equals(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x == 5 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_eq",
        )
        g = Graph()
        s = g.Space(slot, name="cmp_eq")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x == 5):
                    s.z = 1.0
                with g.Else():
                    s.z = 0.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(1.0)
        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_not_equals(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x != 5 (x=3): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_ne",
        )
        g = Graph()
        s = g.Space(slot, name="cmp_ne")
        s.x = s.FloatModelVar("x", value=3.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                with g.If(s.x != 5):
                    s.z = 1.0
                with g.Else():
                    s.z = 0.0
                s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await wait_for_ran(resolink, slot)
        assert await read_model_var(resolink, slot, "z") == pytest.approx(1.0)

        await resolink.remove_slot(slot=slot)
        await asyncio.sleep(0.5)
