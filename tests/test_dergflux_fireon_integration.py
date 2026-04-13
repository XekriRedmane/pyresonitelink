"""Integration tests for Dergflux FireOn event source nodes."""

from __future__ import annotations

import asyncio
import time
from typing import Any, cast

import pytest
import pytest_asyncio

from pyresonitelink import client
from pyresonitelink.data import messages, workers, fields
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux._builder import _find_store_companion


# =========================================================================
# Helpers
# =========================================================================


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


async def wait_for_value(
    resolink: client.Client, 
    slot: Any, 
    var_name: str, 
    expected: Any,
    timeout: float = 10.0,
) -> bool:
    """Poll a variable until it matches the expected value."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        val = await read_model_var(resolink, slot, var_name, timeout=1.0)
        if val == expected:
            return True
        await asyncio.sleep(0.5)
    return False


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
    name = f"__dergflux_fireon_{request.node.name}__"
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

class TestFireOn:
    """Test various FireOn event sources."""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_true(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnTrue fires when condition transitions False -> True."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_true")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=False)
        s.result = s.IntModelVar("result", value=0)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.trigger) as e:
                with e.on_changed():
                    s.result = 1

        await g.build(resolink)
        
        # Initial state check
        assert await read_model_var(resolink, slot, "result") == 0
        
        # Trigger the event
        # Find the trigger variable's +Store component
        var_slot = None
        for _ in range(10):
            var_slot = await resolink.find_slot(slot, name="trigger")
            if var_slot is not None:
                break
            await asyncio.sleep(0.5)
        assert var_slot is not None
        
        assert var_slot.id is not None
        store_id, store_ct, val_id = cast(tuple[str, str, str], await _find_store_companion(resolink, var_slot.id))
        assert store_id is not None
        assert val_id is not None
        assert store_ct is not None
        from pyresonitelink.data import fields
        update_member = fields.FieldBool(value=True)
        update_member.id = val_id
        await resolink.update_component(
            data=workers.Component(
                id=store_id,
                componentType=store_ct,
                members={"Value": update_member},
            ),
        )

        # Wait for reaction
        assert await wait_for_value(resolink, slot, "result", 1)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_false(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnFalse fires when condition transitions True -> False."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_false")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=True)
        s.result = s.IntModelVar("result", value=0)

        with g.Under(slot):
            with g.FireOnFalse(condition=s.trigger) as e:
                with e.on_changed():
                    s.result = 1

        await g.build(resolink)
        
        # Initial state check
        assert await read_model_var(resolink, slot, "result") == 0
        
        # Trigger the event
        var_slot = None
        for _ in range(10):
            var_slot = await resolink.find_slot(slot, name="trigger")
            if var_slot is not None:
                break
            await asyncio.sleep(0.5)
        assert var_slot is not None
        
        assert var_slot.id is not None
        store_id, store_ct, val_id = cast(tuple[str, str, str], await _find_store_companion(resolink, var_slot.id))
        assert store_id is not None
        assert val_id is not None
        assert store_ct is not None
        
        from pyresonitelink.data import fields
        update_member = fields.FieldBool(value=False)
        update_member.id = val_id
        await resolink.update_component(
            data=workers.Component(
                id=store_id,
                componentType=store_ct,
                members={"Value": update_member},
            ),
        )

        # Wait for reaction
        assert await wait_for_value(resolink, slot, "result", 1)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_value_change(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnValueChange fires whenever value changes."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_change")
        g = Graph()
        s = g.Space(slot)
        s.x = s.FloatModelVar("x", value=0.0)
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnValueChange(value=s.x) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await g.build(resolink)
        
        # Initial state check
        assert await read_model_var(resolink, slot, "counter") == 0
        
        # Helper to update x
        var_slot = None
        for _ in range(10):
            var_slot = await resolink.find_slot(slot, name="x")
            if var_slot is not None:
                break
            await asyncio.sleep(0.5)
        assert var_slot is not None
        
        assert var_slot.id is not None
        store_id, store_ct, val_id = cast(tuple[str, str, str], await _find_store_companion(resolink, var_slot.id))
        assert store_id is not None
        assert val_id is not None
        assert store_ct is not None
        
        from pyresonitelink.data import fields
        
        async def update_x(val: float):
            import numpy as np
            update_member = fields.FieldFloat(value=np.float32(val))
            update_member.id = val_id
            await resolink.update_component(
                data=workers.Component(
                    id=store_id,
                    componentType=store_ct,
                    members={"Value": update_member},
                ),
            )

        # First change
        await update_x(1.0)
        assert await wait_for_value(resolink, slot, "counter", 1)
        
        # Second change
        await update_x(2.0)
        assert await wait_for_value(resolink, slot, "counter", 2)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_object_value_change(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnObjectValueChange fires when string/object changes."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_obj_change")
        g = Graph()
        s = g.Space(slot)
        s.text = s.StringModelVar("text", value="initial")
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnObjectValueChange(value=s.text) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await g.build(resolink)
        
        # Initial state check
        assert await read_model_var(resolink, slot, "counter") == 0
        
        # Helper to update text
        var_slot = None
        for _ in range(10):
            var_slot = await resolink.find_slot(slot, name="text")
            if var_slot is not None:
                break
            await asyncio.sleep(0.5)
        assert var_slot is not None
        
        assert var_slot.id is not None
        store_id, store_ct, val_id = cast(tuple[str, str, str], await _find_store_companion(resolink, var_slot.id))
        assert store_id is not None
        assert val_id is not None
        assert store_ct is not None
        
        from pyresonitelink.data import fields
        
        async def update_text(val: str):
            update_member = fields.FieldString(value=val)
            update_member.id = val_id
            await resolink.update_component(
                data=workers.Component(
                    id=store_id,
                    componentType=store_ct,
                    members={"Value": update_member},
                ),
            )

        # First change
        await update_text("first")
        assert await wait_for_value(resolink, slot, "counter", 1)
        
        # Second change
        await update_text("second")
        assert await wait_for_value(resolink, slot, "counter", 2)

    @pytest.mark.xfail(reason="ReadDynamicObjectVariable resolution issues on server")
    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_ref_change(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnRefChange fires when a slot reference changes."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_ref")
        target1 = await resolink.add_slot(parent=slot, name="target1")
        target2 = await resolink.add_slot(parent=slot, name="target2")
        
        g = Graph()
        s = g.Space(slot)
        # Using RefDynVar for the monitored source
        s.ref = s.RefDynVar("ref", value=target1)
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnRefChange(value=s.ref) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await g.build(resolink)
        
        assert await read_model_var(resolink, slot, "counter") == 0
        
        # Helper to update ref. s.ref is a DynamicReferenceVariable<Slot>
        # after build, s.ref is the component instance.
        ref_comp = s.ref
        
        from pyresonitelink.data import members
        
        async def update_ref(target_slot: Any):
            ref_comp.value = target_slot.id
            await ref_comp.update(resolink)

        # Change ref to target2
        await update_ref(target2)
        assert await wait_for_value(resolink, slot, "counter", 1)
        
        # Change back to target1
        await update_ref(target1)
        assert await wait_for_value(resolink, slot, "counter", 2)

    @pytest.mark.xfail(reason="ReadDynamicObjectVariable resolution issues on server")
    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_on_type_change(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireOnTypeChange fires when a type field changes."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_on_type")
        
        g = Graph()
        s = g.Space(slot)
        # Using TypeDynVar for the monitored source
        s.type_var = s.TypeDynVar("type_var", value=float)
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnTypeChange(value=s.type_var) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await g.build(resolink)
        
        assert await read_model_var(resolink, slot, "counter") == 0
        
        # Helper to update type. s.type_var is a DynamicReferenceVariable<Type>
        type_comp = s.type_var
        
        async def update_type(t: type):
            from pyresonitelink.generated import _type_map
            t_name = _type_map.from_python_type(t).resonite_name
            type_comp.value = t_name
            await type_comp.update(resolink)

        # Change to int
        await update_type(int)
        assert await wait_for_value(resolink, slot, "counter", 1)
        
        # Change back to float
        await update_type(float)
        assert await wait_for_value(resolink, slot, "counter", 2)

    @pytest.mark.asyncio(loop_scope="session")
    async def test_fire_while_true(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """FireWhileTrue fires continuously while condition is True."""
        slot = await resolink.add_slot(parent=dergflux_slot, name="fire_while_true")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=False)
        s.counter = s.IntModelVar("counter", value=0)

        # Use Under(slot) to place the component on the slot
        with g.Under(slot):
            with g.FireWhileTrue(condition=s.trigger) as e:
                with e.on_update():
                    s.counter = s.counter + 1

        await g.build(resolink)
        
        # Initial state check
        assert await read_model_var(resolink, slot, "counter") == 0
        
        # Helper to update trigger
        var_slot = None
        for _ in range(10):
            var_slot = await resolink.find_slot(slot, name="trigger")
            if var_slot is not None:
                break
            await asyncio.sleep(0.5)
        assert var_slot is not None
        
        assert var_slot.id is not None
        store_id, store_ct, val_id = cast(tuple[str, str, str], await _find_store_companion(resolink, var_slot.id))
        assert store_id is not None
        assert val_id is not None
        assert store_ct is not None
        
        from pyresonitelink.data import fields
        
        async def set_trigger(val: bool):
            update_member = fields.FieldBool(value=val)
            update_member.id = val_id
            await resolink.update_component(
                data=workers.Component(
                    id=store_id,
                    componentType=store_ct,
                    members={"Value": update_member},
                ),
            )

        # Start firing
        await set_trigger(True)
        
        # Wait until counter is > 0
        start_time = time.time()
        success = False
        while time.time() - start_time < 5.0:
            val = await read_model_var(resolink, slot, "counter", timeout=1.0)
            if val is not None and val > 0:
                success = True
                break
            await asyncio.sleep(0.5)
        
        # Stop firing
        await set_trigger(False)
        
        assert success
        
        # Record value after stopping
        val_after_stop = await read_model_var(resolink, slot, "counter", timeout=1.0)
        
        # Wait a bit more and verify it hasn't changed much (or at all)
        await asyncio.sleep(1.0)
        val_later = await read_model_var(resolink, slot, "counter", timeout=1.0)
        
        # It might have fired a few more times before processing the False
        # but it shouldn't keep firing indefinitely.
        assert val_later is not None and val_after_stop is not None
        assert val_later - val_after_stop < 10 
