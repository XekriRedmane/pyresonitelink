"""Integration tests for Dergflux flow control features."""

from __future__ import annotations

import asyncio
import time
from typing import Any

import pytest
import pytest_asyncio

from pyresonitelink import client
from pyresonitelink.data import messages, workers, primitives, fields
from pyresonitelink.dergflux import Graph


# =========================================================================
# Helpers
# =========================================================================


async def read_model_var(
    resolink: client.Client,
    parent_slot: Any,
    var_name: str,
    timeout: float = 5.0,
) -> Any:
    """Read a model variable's value from its +Store companion, with polling."""
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
                        # If we're waiting for a non-zero/non-false value, keep polling
                        if val != 0 and val is not False and val != "unset":
                            return val
                        last_val = val
        
        await asyncio.sleep(0.5)
    
    return last_val


async def wait_for_ran(resolink: client.Client, slot: Any, timeout: float = 15.0) -> bool:
    """Poll the 'ran' variable until it becomes True."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        val = await read_model_var(resolink, slot, "ran", timeout=1.0)
        if val is True or val == 1:
            # Give the server plenty of time to finish writing 
            # other variables in the same impulse
            await asyncio.sleep(1.0)
            return True
        await asyncio.sleep(0.5)
    return False


async def trigger_go(resolink: client.Client, slot: Any):
    """Set the 'go' variable to True to trigger the FireOnTrue node."""
    go_slot = await resolink.find_slot(slot, name="go")
    assert go_slot is not None
    
    from pyresonitelink.dergflux._builder import _find_store_companion
    store_id, store_ct, val_id = await _find_store_companion(resolink, go_slot.id)
    
    update_member = fields.FieldBool(value=True)
    update_member.id = val_id
    await resolink.update_component(
        data=workers.Component(
            id=store_id,
            componentType=store_ct,
            members={"Value": update_member},
        ),
    )


# =========================================================================
# Fixtures
# =========================================================================


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def dergflux_slot(
    resolink: client.Client,
    request: pytest.FixtureRequest,
) -> Any:
    """Create a unique parent slot for each dergflux integration test."""
    name = f"__dergflux_flow_{request.node.name}__"
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

class TestLoops:
    """Test loop constructs: For, Range, While."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_for_loop(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test a simple For loop."""
        g = Graph()
        s = g.Space(dergflux_slot)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(dergflux_slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.For(5) as f:
                        with f.OnIterate() as i:
                            s.total = s.total + i
                    s.ran = True

        await g.build(resolink)
        await trigger_go(resolink, dergflux_slot)
        
        # 0 + 1 + 2 + 3 + 4 = 10
        assert await wait_for_ran(resolink, dergflux_slot)
        assert await read_model_var(resolink, dergflux_slot, "total") == 10

    @pytest.mark.asyncio(loop_scope="session")
    async def test_range_loop(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test a Range loop with step."""
        g = Graph()
        s = g.Space(dergflux_slot)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(dergflux_slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    # 2, 4, 6, 8 (stop at 10)
                    with g.Range(2, 10, 2) as f:
                        with f.OnIterate() as i:
                            s.total = s.total + i
                    s.ran = True

        await g.build(resolink)
        await trigger_go(resolink, dergflux_slot)
        
        # 2 + 4 + 6 + 8 + 10 = 30 (Resonite Range is inclusive)
        assert await wait_for_ran(resolink, dergflux_slot)
        assert await read_model_var(resolink, dergflux_slot, "total") == 30

    @pytest.mark.asyncio(loop_scope="session")
    async def test_while_loop(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test a While loop."""
        g = Graph()
        s = g.Space(dergflux_slot)
        s.counter = s.IntModelVar("counter", value=5)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(dergflux_slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.While(s.counter > 0):
                        s.total = s.total + s.counter
                        s.counter = s.counter - 1
                    s.ran = True

        await g.build(resolink)
        await trigger_go(resolink, dergflux_slot)
        
        # 5 + 4 + 3 + 2 + 1 = 15
        assert await wait_for_ran(resolink, dergflux_slot)
        assert await read_model_var(resolink, dergflux_slot, "total") == 15


class TestNestedFlow:
    """Test nested flow control."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_nested_if_in_for(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test an If statement nested inside a For loop."""
        g = Graph()
        s = g.Space(dergflux_slot)
        s.evens = s.IntModelVar("evens", value=0)
        s.odds = s.IntModelVar("odds", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(dergflux_slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.For(10) as f:
                        with f.OnIterate() as i:
                            # Check if i is even (i % 2 == 0)
                            with g.If((i % 2) == 0):
                                s.evens = s.evens + 1
                            with g.Else():
                                s.odds = s.odds + 1
                    s.ran = True

        await g.build(resolink)
        await trigger_go(resolink, dergflux_slot)
        
        # 0..9 has 5 evens (0,2,4,6,8) and 5 odds (1,3,5,7,9)
        assert await wait_for_ran(resolink, dergflux_slot)
        assert await read_model_var(resolink, dergflux_slot, "evens") == 5
        assert await read_model_var(resolink, dergflux_slot, "odds") == 5


class TestOutcome:
    """Test the Outcome high-level abstraction."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_outcome_basic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test basic Outcome setting and reaction."""
        g = Graph()
        s = g.Space(dergflux_slot)
        s.x = s.IntModelVar("x", value=5)
        s.log = s.StringModelVar("log", value="unset")
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)
        
        res = g.Outcome(s, "res")

        with g.Under(dergflux_slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.If(s.x > 3):
                        res.set("high")
                    with g.Else():
                        res.set("low")
            
            # Reactions fire via FireOnValueChange
            with res.on_changed() as label:
                with g.If(label == "high"):
                    s.log = "got high"
                with g.If(label == "low"):
                    s.log = "got low"
                s.ran = True

        await g.build(resolink)
        await trigger_go(resolink, dergflux_slot)
        
        # x=5 is > 3, so label should be "high" -> log "got high"
        assert await wait_for_ran(resolink, dergflux_slot)
        assert await read_model_var(resolink, dergflux_slot, "log") == "got high"
