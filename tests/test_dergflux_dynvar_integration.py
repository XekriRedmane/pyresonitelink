"""Integration tests for Dergflux dynamic variables (DynVars)."""

from __future__ import annotations

import asyncio
import time
from typing import Any

import pytest
import pytest_asyncio

from pyresonitelink import client
from pyresonitelink.data import messages, workers, members
from pyresonitelink.dergflux import Graph


# =========================================================================
# Helpers
# =========================================================================


async def read_dynvar(
    resolink: client.Client,
    slot: Any,
    var_name: str,
    timeout: float = 10.0,
    space_name: str | None = None,
) -> Any:
    """Read a dynamic variable's value by creating a temporary ReadDVV node."""
    from pyresonitelink.data import fields
    
    full_path = f"{space_name}/{var_name}" if space_name else var_name
    reader_slot = await resolink.add_slot(parent=slot, name=f"__reader_{var_name}__")
    
    async def add_comp_robust(ctype: str, refs: dict[str, str | members.Reference] | None = None) -> str:
        for _ in range(5):
            resp = await resolink.add_component(containerSlotId=reader_slot.id, componentType=ctype)
            if resp.entityId is not None:
                if refs:
                    await asyncio.sleep(0.1)
                    await resolink.update_references(componentId=resp.entityId, references=refs)
                return resp.entityId
            await asyncio.sleep(0.5)
        raise RuntimeError(f"Failed to add component {ctype}")

    # 1. SlotRef
    slot_ref_id = await add_comp_robust(
        f"[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.RefObjectInput<[FrooxEngine]FrooxEngine.Slot>",
        refs={"Target": slot.id}
    )

    # 2. Path
    path_field_id = await add_comp_robust(
        "[FrooxEngine]FrooxEngine.ValueField<[FrooxEngine]FrooxEngine.SyncString>"
    )
    # Get member ID for Value
    pf_mem_id = None
    for _ in range(10):
        pf_data = await resolink.get_component(componentId=path_field_id)
        if pf_data.data is not None and "Value" in pf_data.data.members:
            pf_mem_id = pf_data.data.members["Value"].id
            break
        await asyncio.sleep(0.2)
    assert pf_mem_id is not None
    
    update_mem = fields.FieldString(value=full_path)
    update_mem.id = pf_mem_id
    await resolink.update_component(data=workers.Component(
        id=path_field_id,
        componentType="[FrooxEngine]FrooxEngine.ValueField<[FrooxEngine]FrooxEngine.SyncString>",
        members={"Value": update_mem}
    ))

    # 3. Reader
    type_name = "System.Boolean" if "ran" in var_name else "System.Single"
    reader_type = f"[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ReadDynamicValueVariable<{type_name}>"
    reader_id = await add_comp_robust(
        reader_type,
        refs={
            "Source": slot_ref_id, 
            "Path": pf_mem_id
        }
    )
    
    # Direct binding must be false
    await resolink.update_component(data=workers.Component(
        id=reader_id,
        componentType=reader_type,
        members={"OnlyDirectBinding": fields.FieldBool(value=False)}
    ))
    
    # Poll
    start_time = time.time()
    last_val = None
    while time.time() - start_time < timeout:
        comp_resp = await resolink.get_component(componentId=reader_id)
        if comp_resp.data is not None:
            val_info = comp_resp.data.members.get("Value")
            if val_info is not None:
                val = val_info.get("value") if isinstance(val_info, dict) else getattr(val_info, "value", None)
                if val is not None:
                    last_val = val
                    if val != 0 and val is not False:
                        break
        await asyncio.sleep(0.5)
    
    await resolink.remove_slot(slot=reader_slot)
    return last_val


async def wait_for_dynvar_ran(resolink: client.Client, slot: Any, timeout: float = 20.0) -> bool:
    """Poll the 'ran' dynamic variable until it becomes True."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        val = await read_dynvar(resolink, slot, "ran", timeout=2.0, space_name=None)
        if val is True or val == 1:
            await asyncio.sleep(1.0)
            return True
        await asyncio.sleep(0.5)
    return False


# =========================================================================
# Fixtures
# =========================================================================


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def dergflux_slot(
    resolink: client.Client,
    request: pytest.FixtureRequest,
) -> Any:
    """Create a unique parent slot for each dergflux integration test."""
    name = f"__dergflux_dynvar_{request.node.name}__"
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

class TestDynVars:
    """Test dynamic variables (DynVars)."""

    @pytest.mark.xfail(reason="ReadDVV helper is sensitive to server assembly names")
    @pytest.mark.asyncio(loop_scope="session")
    async def test_bare_dynvar_write(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test a bare write to a dynamic variable."""
        g = Graph()
        s = g.Space(dergflux_slot, space_name=None)
        s.z = s.FloatDynVar("z", value=0.0)
        s.ran = s.BoolDynVar("ran", value=False)

        with g.Under(dergflux_slot):
            s.z = 5.0
            s.ran = True

        await g.build(resolink)
        
        assert await wait_for_dynvar_ran(resolink, dergflux_slot)
        assert await read_dynvar(resolink, dergflux_slot, "z", space_name=None) == pytest.approx(5.0)

    @pytest.mark.xfail(reason="ReadDVV helper is sensitive to server assembly names")
    @pytest.mark.asyncio(loop_scope="session")
    async def test_dynvar_arithmetic(
        self, resolink: client.Client, dergflux_slot: Any,
    ) -> None:
        """Test arithmetic using dynamic variables."""
        g = Graph()
        s = g.Space(dergflux_slot, space_name=None)
        s.x = s.FloatDynVar("x", value=2.0)
        s.y = s.FloatDynVar("y", value=3.0)
        s.z = s.FloatDynVar("z", value=0.0)
        s.ran = s.BoolDynVar("ran", value=False)

        with g.Under(dergflux_slot):
            s.z = s.x + s.y
            s.ran = True

        await g.build(resolink)
        
        assert await wait_for_dynvar_ran(resolink, dergflux_slot)
        assert await read_dynvar(resolink, dergflux_slot, "z", space_name=None) == pytest.approx(5.0)
