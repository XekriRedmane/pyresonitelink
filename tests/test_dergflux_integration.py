"""Integration tests for the Dergflux DSL against a live Resonite server.

Each test builds a ProtoFlux graph via Dergflux, verifies that all
connections are wired correctly, then triggers execution and checks
results.

**Two-boolean gate pattern**: every test declares ``start`` (BoolVar,
initially False) and ``ran`` (BoolVar, initially False).  The flow
only executes when ``start`` is True and ``ran`` is False, and sets
``ran = True`` after one execution.  This ensures deterministic
single-shot evaluation.

**E712 suppression**: throughout this file, ``s.start == True`` and
``s.ran == False`` trigger flake8 E712 ("comparison to True/False
should be ``is``").  In Dergflux these are *not* Python boolean
checks — ``==`` invokes ``ExprProxy.__eq__`` to build a
``ValueEquals<bool>`` ProtoFlux node.  The ``is`` operator cannot
be overridden, so ``==`` is the correct and only option.

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

    Returns a list of problems (empty = all OK).  Optional outputs
    like OnNotFound, OnFailed, UpdatingUser, SkipIfNull, OnlyForUser
    are ignored.
    """
    optional = {
        "OnNotFound", "OnFailed", "OnFalse", "OnTrue",
        "UpdatingUser", "SkipIfNull", "OnlyForUser",
        "OnSuccess",  # last node in chain
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
        members: Any = data.get("members") or {}
        for mname, mval in members.items():
            if not isinstance(mval, dict):
                continue
            dtype = mval.get("$type", "")
            tid = mval.get("targetId")
            if dtype == "reference" and tid is None and mname not in optional:
                problems.append(f"{cid} ({ct}): {mname} -> null")
    return problems


async def trigger_and_wait(
    resolink: client.Client,
    start_var: Any,
    wait: float = 2.0,
) -> None:
    """Set start=True and wait for the graph to execute."""
    start_var.value = True
    await start_var.update(resolink)
    time.sleep(wait)


async def read_var(resolink: client.Client, var: Any) -> Any:
    """Refresh and return a variable's current value."""
    await var.refresh(resolink)
    return var.value


def _slot_id(slot: Any) -> str:
    """Extract slot ID with assertion for type safety."""
    sid: str | None = slot.id
    assert sid is not None, "Slot has no ID"
    return sid


# =========================================================================
# Fixtures
# =========================================================================


@pytest_asyncio.fixture(loop_scope="session")
async def dergflux_slot(
    resolink: client.Client,
) -> Any:
    """Create a parent slot for all dergflux integration tests."""
    old = await resolink.find_slot("Root", name="__dergflux_tests__")
    if old is not None:
        await resolink.remove_slot(slot=old)
        await asyncio.sleep(0.1)
    slot = await resolink.add_slot(name="__dergflux_tests__")
    await asyncio.sleep(0.1)
    yield slot
    # Cleanup temporarily disabled for inspection
    # await resolink.remove_slot(slot=slot)


# =========================================================================
# Tests
# =========================================================================


class TestBareWrite:
    """Test simple variable assignment: z = x + 3."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_bare_write(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Assign z = x + 3 where x=2, expect z=5."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="bare_write",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="bare_write")
        s.x = s.FloatVar("x", value=2.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x + 3
                    s.ran = True

        await g.build(resolink)

        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        print(f"\n  start type: {type(s.start).__name__}, id: {getattr(s.start, 'id', 'N/A')}")
        await trigger_and_wait(resolink, s.start)
        ran = await read_var(resolink, s.ran)
        z = await read_var(resolink, s.z)
        print(f"  z={z}, ran={ran}")
        assert z == pytest.approx(5.0), f"Expected z=5.0, got {z}"


class TestArithmetic:
    """Test arithmetic operators: +, -, *, /."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + y where x=3, y=4, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_add",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_add")
        s.x = s.FloatVar("x", value=3.0)
        s.y = s.FloatVar("y", value=4.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x + s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(7.0), f"Expected z=7.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_sub(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x - y where x=10, y=3, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_sub",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_sub")
        s.x = s.FloatVar("x", value=10.0)
        s.y = s.FloatVar("y", value=3.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x - s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(7.0), f"Expected z=7.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mul(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x * y where x=3, y=5, expect z=15."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_mul",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_mul")
        s.x = s.FloatVar("x", value=3.0)
        s.y = s.FloatVar("y", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x * s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(15.0), f"Expected z=15.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_div(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x / y where x=15, y=3, expect z=5."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_div",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_div")
        s.x = s.FloatVar("x", value=15.0)
        s.y = s.FloatVar("y", value=3.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x / s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(5.0), f"Expected z=5.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_mod(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x % y where x=17, y=5, expect z=2."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_mod",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_mod")
        s.x = s.FloatVar("x", value=17.0)
        s.y = s.FloatVar("y", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x % s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(2.0), f"Expected z=2.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_neg(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = -x where x=7, expect z=-7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_neg",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_neg")
        s.x = s.FloatVar("x", value=7.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = -s.x
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(-7.0), f"Expected z=-7.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_const_coercion(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + 10 where x=5.0 — int constant coerced to float."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_coerce",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_coerce")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x + 10
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(15.0), f"Expected z=15.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_chained_ops(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = (x + 3) * 2 where x=4, expect z=14."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="arith_chain",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="arith_chain")
        s.x = s.FloatVar("x", value=4.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = (s.x + 3) * 2
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(14.0), f"Expected z=14.0, got {z}"


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
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="if_true")
        s.x = s.FloatVar("x", value=1.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 3):
                        s.z = 1.0
                    with g.Else():
                        s.z = 2.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(1.0), f"Expected z=1.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_false_branch(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x < 3: z = 1, else: z = 2. x=5, expect z=2."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_false",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="if_false")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 3):
                        s.z = 1.0
                    with g.Else():
                        s.z = 2.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(2.0), f"Expected z=2.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_with_continuation(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """if x<3: tmp=x+3 else: tmp=x-3; z=tmp+1. x=2, expect z=6."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_cont",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="if_cont")
        s.x = s.FloatVar("x", value=2.0)
        s.z = s.FloatVar("z")
        s.tmp = s.FloatVar("tmp")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
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

        await trigger_and_wait(resolink, s.start, wait=2.0)
        z = await read_var(resolink, s.z)
        tmp = await read_var(resolink, s.tmp)
        print(f"\n  Slot: {slot.id}  z={z}  tmp={tmp}")
        assert z == pytest.approx(6.0), f"Expected z=6.0, got {z}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_if_without_else(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x<3: z=99. x=1, expect z=99. Then verify continuation."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="if_no_else",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="if_no_else")
        s.x = s.FloatVar("x", value=1.0)
        s.z = s.FloatVar("z")
        s.w = s.FloatVar("w")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 3):
                        s.z = 99.0
                    # w=1 runs after the If regardless of branch
                    s.w = 1.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        w = await read_var(resolink, s.w)
        assert z == pytest.approx(99.0), f"Expected z=99.0, got {z}"
        assert w == pytest.approx(1.0), f"Expected w=1.0, got {w}"


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
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="seq_writes")
        s.a = s.FloatVar("a")
        s.b = s.FloatVar("b")
        s.c = s.FloatVar("c")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.a = 1.0
                    s.b = 2.0
                    s.c = 3.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        a = await read_var(resolink, s.a)
        b = await read_var(resolink, s.b)
        c = await read_var(resolink, s.c)
        assert a == pytest.approx(1.0)
        assert b == pytest.approx(2.0)
        assert c == pytest.approx(3.0)


class TestStringVariables:
    """Test string variable read/write."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_string_write(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Write a string constant to a StringVar."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="str_write",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="str_write")
        s.msg = s.StringVar("msg", value="initial")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.msg = "hello"
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        msg = await read_var(resolink, s.msg)
        assert msg == "hello", f"Expected 'hello', got {msg!r}"


class TestIntVariables:
    """Test integer variable operations."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_int_arithmetic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """z = x + y with IntVars. x=3, y=4, expect z=7."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="int_arith",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="int_arith")
        s.x = s.IntVar("x", value=3)
        s.y = s.IntVar("y", value=4)
        s.z = s.IntVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.z = s.x + s.y
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == 7, f"Expected z=7, got {z}"


class TestComparison:
    """Test comparison operators returning bool-like results."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_less_than_true(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x < 10 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_lt_true",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="cmp_lt_true")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 10):
                        s.z = 1.0
                    with g.Else():
                        s.z = 0.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(1.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_greater_than(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x > 3 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_gt",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="cmp_gt")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x > 3):
                        s.z = 1.0
                    with g.Else():
                        s.z = 0.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(1.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_equals(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x == 5 (x=5): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_eq",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="cmp_eq")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x == 5):
                        s.z = 1.0
                    with g.Else():
                        s.z = 0.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(1.0)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_not_equals(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """If x != 5 (x=3): z=1 else z=0. Expect z=1."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="cmp_ne",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="cmp_ne")
        s.x = s.FloatVar("x", value=3.0)
        s.z = s.FloatVar("z")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x != 5):
                        s.z = 1.0
                    with g.Else():
                        s.z = 0.0
                    s.ran = True

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start)
        z = await read_var(resolink, s.z)
        assert z == pytest.approx(1.0)


class TestOutcome:
    """Test the Outcome API."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_outcome_high(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Outcome labels 'high' when x<3, reacts to set log."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="outcome_high",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="outcome_high")
        s.x = s.FloatVar("x", value=2.0)
        s.z = s.FloatVar("z")
        s.tmp = s.FloatVar("tmp")
        s.log = s.StringVar("log", value="none")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        outcome = g.Outcome(s, "result")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 3):
                        s.tmp = s.x + 3
                        outcome.set("high")
                    with g.Else():
                        s.tmp = s.x - 3
                        outcome.set("low")
                    s.z = s.tmp + 1
                    s.ran = True

            with outcome.on_changed() as oc:
                with g.If(oc == "high"):
                    s.log = "high path"
                with g.If(oc == "low"):
                    s.log = "low path"

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start, wait=1.0)
        z = await read_var(resolink, s.z)
        log = await read_var(resolink, s.log)
        assert z == pytest.approx(6.0), f"Expected z=6.0, got {z}"
        assert log == "high path", f"Expected 'high path', got {log!r}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_outcome_low(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Outcome labels 'low' when x>=3, reacts to set log."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="outcome_low",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="outcome_low")
        s.x = s.FloatVar("x", value=5.0)
        s.z = s.FloatVar("z")
        s.tmp = s.FloatVar("tmp")
        s.log = s.StringVar("log", value="none")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        outcome = g.Outcome(s, "result")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    with g.If(s.x < 3):
                        s.tmp = s.x + 3
                        outcome.set("high")
                    with g.Else():
                        s.tmp = s.x - 3
                        outcome.set("low")
                    s.z = s.tmp + 1
                    s.ran = True

            with outcome.on_changed() as oc:
                with g.If(oc == "high"):
                    s.log = "high path"
                with g.If(oc == "low"):
                    s.log = "low path"

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start, wait=1.0)
        z = await read_var(resolink, s.z)
        log = await read_var(resolink, s.log)
        assert z == pytest.approx(3.0), f"Expected z=3.0, got {z}"
        assert log == "low path", f"Expected 'low path', got {log!r}"


class TestFireOnValueChange:
    """Test FireOnValueChange event source."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_value_change(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnValueChange detects counter increment."""
        slot = await resolink.add_slot(
            parent=dergflux_slot, name="fire_on_change",
        )
        await asyncio.sleep(0.1)
        g = Graph()
        s = g.Space(slot, name="fire_on_change")
        s.counter = s.FloatVar("counter")
        s.detected = s.FloatVar("detected")
        s.start = s.BoolVar("start")
        s.ran = s.BoolVar("ran")

        with g.Under(slot):
            with g.If(s.start == True):  # noqa: E712
                with g.If(s.ran == False):  # noqa: E712
                    s.counter = s.counter + 1
                    s.ran = True

            with g.FireOnValueChange(value=s.counter) as e:
                with e.on_changed():
                    s.detected = s.detected + 1

        await g.build(resolink)
        problems = await verify_connections(resolink, _slot_id(slot))
        assert not problems, f"Missing connections: {problems}"

        await trigger_and_wait(resolink, s.start, wait=1.0)
        counter = await read_var(resolink, s.counter)
        detected = await read_var(resolink, s.detected)
        assert counter == pytest.approx(1.0), f"counter={counter}"
        assert detected == pytest.approx(1.0), (
            f"FireOnValueChange did not fire: detected={detected}"
        )
