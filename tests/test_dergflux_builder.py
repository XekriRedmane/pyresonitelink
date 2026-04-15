"""Unit tests for the Dergflux builder.

Each test constructs the same graph as the corresponding integration
test, runs ``build_graph`` against a mock client, and verifies that the
builder produces the expected set of components, wiring, and values.

No live server is required.
"""

from __future__ import annotations

import re
from collections.abc import Generator
from dataclasses import dataclass, field
from typing import Any

import pytest

from pyresonitelink.data import members, messages, primitives, workers
from pyresonitelink.dergflux import Graph, Outcome
from pyresonitelink.dergflux import _builder


# =========================================================================
# Mock infrastructure
# =========================================================================


@dataclass
class _ComponentRecord:
    """A component created during building."""

    id: str
    component_type: str
    slot_id: str
    member_ids: dict[str, str] = field(default_factory=dict)
    references: dict[str, str] = field(default_factory=dict)


@dataclass
class _SlotRecord:
    """A slot created during building."""

    id: str
    name: str
    parent_id: str | None = None


class MockResponse:
    """Mimics the response object from the client."""

    def __init__(
        self,
        success: bool = True,
        entity_id: str | None = None,
        data: Any = None,
        error_info: str | None = None,
    ) -> None:
        self.success = success
        self.entityId = entity_id
        self.data = data
        self.errorInfo = error_info


_COMMON_MEMBERS = [
    "Value", "A", "B", "N", "Condition",
    "OnTrue", "OnFalse", "OnSuccess", "OnFailed", "OnNotFound",
    "OnWritten", "OnChanged", "OnUpdate",
    "Target", "Path", "Source", "Variable",
    "LoopStart", "LoopIteration", "LoopEnd",
    "Iteration", "Current", "Count", "Reverse",
    "Start", "End", "StepSize",
    "Input", "_value", "Tag", "OnTriggered",
    "SpaceName", "OnlyDirectBinding", "VariableName",
    "Node", "Reference", "Shift", "Power",
    "Min", "Max", "Edge0", "Edge1", "X", "Y",
]


class MockClient:
    """Captures all builder operations without touching a real server.

    Generates sequential fake IDs for slots, components, and members.
    Tracks every component creation and reference wiring for later
    assertion.  Member IDs are cached per component so repeated
    ``get_component`` calls return stable IDs.
    """

    def __init__(self) -> None:
        self._next_id = 1
        self.slots: dict[str, _SlotRecord] = {}
        self.components: dict[str, _ComponentRecord] = {}
        self.component_list: list[_ComponentRecord] = []
        # Reverse map: member_id -> (component_id, member_name)
        self._member_owner: dict[str, tuple[str, str]] = {}

    def _gen_id(self, prefix: str = "mock") -> str:
        """Generate a unique fake ID."""
        fid = f"{prefix}-{self._next_id}"
        self._next_id += 1
        return fid

    def _ensure_member_ids(self, comp_id: str) -> dict[str, str]:
        """Return cached member IDs for a component, creating them on first call."""
        rec = self.components.get(comp_id)
        if rec is None:
            return {}
        if not rec.member_ids:
            for mname in _COMMON_MEMBERS:
                mid = self._gen_id("mem")
                rec.member_ids[mname] = mid
                self._member_owner[mid] = (comp_id, mname)
        return rec.member_ids

    # -- Slot operations ---------------------------------------------------

    async def add_slot(
        self, parent: Any = None, name: str = "", **kwargs: Any,
    ) -> workers.Slot:
        """Create a fake slot and return it."""
        sid = self._gen_id("slot")
        parent_id = None
        if parent is not None:
            parent_id = parent.id if hasattr(parent, "id") else str(parent)
        self.slots[sid] = _SlotRecord(id=sid, name=name, parent_id=parent_id)
        return workers.Slot(id=sid)

    async def find_slot(
        self, parent: Any = None, name: str = "", **kwargs: Any,
    ) -> workers.Slot | None:
        """Find a previously created slot by name."""
        parent_id = None
        if parent is not None:
            parent_id = parent.id if hasattr(parent, "id") else str(parent)
        for s in self.slots.values():
            if s.name == name and (parent_id is None or s.parent_id == parent_id):
                return workers.Slot(id=s.id)
        return None

    async def get_slot(
        self, slot: Any = None, slotId: str | None = None, depth: int = 0,
        **kwargs: Any,
    ) -> Any:
        """Return a mock slot response with components and children."""
        from unittest.mock import MagicMock

        sid = slotId or (slot.id if slot is not None else None)
        comps = [
            MagicMock(id=c.id, componentType=c.component_type)
            for c in self.components.values()
            if c.slot_id == sid
        ]
        resp = MagicMock()
        resp.data = MagicMock()
        resp.data.components = comps
        resp.data.parent = None
        return resp

    async def remove_slot(self, **kw: Any) -> Any:
        """No-op for tests."""
        return MockResponse(success=True)

    # -- Component operations ----------------------------------------------

    async def add_component(
        self,
        containerSlotId: Any = None,
        componentType: str = "",
        data: Any = None,
        references: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> MockResponse:
        """Create a component by type string."""
        cid = self._gen_id("comp")
        slot_id = containerSlotId
        if hasattr(containerSlotId, "id"):
            slot_id = containerSlotId.id
        ct = componentType
        if data is not None:
            ct = getattr(data, "componentType", ct) or ct
        rec = _ComponentRecord(
            id=cid, component_type=ct, slot_id=str(slot_id) if slot_id else "",
        )
        self.components[cid] = rec
        self.component_list.append(rec)
        self._ensure_member_ids(cid)
        if references:
            rec.references.update(references)
        return MockResponse(entity_id=cid)

    async def get_component(
        self, componentId: str, **kwargs: Any,
    ) -> Any:
        """Return mock component data with stable member IDs."""
        rec = self.components.get(componentId)
        ct = rec.component_type if rec else "Unknown"
        mids = self._ensure_member_ids(componentId) if rec else {}

        member_dict: dict[str, Any] = {}
        for mname, mid in mids.items():
            ref: members.Reference = members.Reference(targetId=None)
            ref.id = mid
            member_dict[mname] = ref

        comp_data = workers.Component(
            id=componentId, componentType=ct, members=member_dict,
        )
        from unittest.mock import MagicMock

        resp = MagicMock()
        resp.data = comp_data
        return resp

    async def update_component(self, data: Any = None, **kwargs: Any) -> MockResponse:
        """Record a component update."""
        return MockResponse(success=True)

    async def update_references(
        self, componentId: str, references: dict[str, Any], **kwargs: Any,
    ) -> MockResponse:
        """Record a reference wiring operation."""
        resolved: dict[str, str] = {}
        for k, v in references.items():
            if isinstance(v, members.Reference):
                resolved[k] = v.targetId or ""
            elif hasattr(v, "id"):
                resolved[k] = v.id
            elif isinstance(v, str):
                resolved[k] = v
            else:
                resolved[k] = str(v)
        rec = self.components.get(componentId)
        if rec is not None:
            rec.references.update(resolved)
        return MockResponse(success=True)

    async def request_json(self, msg: Any, **kwargs: Any) -> dict[str, Any]:
        """Handle raw JSON requests."""
        if isinstance(msg, messages.GetSlot):
            sid = msg.slotId
            children = [
                {"id": s.id, "name": {"value": s.name}}
                for s in self.slots.values() if s.parent_id == sid
            ]
            comps = [
                {"id": c.id, "componentType": c.component_type}
                for c in self.components.values() if c.slot_id == sid
            ]
            return {"data": {"children": children, "components": comps}}
        if isinstance(msg, messages.GetComponent):
            cid = msg.componentId or ""
            rec = self.components.get(cid)
            if rec is None:
                return {"data": None}
            mids = self._ensure_member_ids(cid)
            mems: dict[str, Any] = {}
            for mname, mid in mids.items():
                mems[mname] = {"id": mid, "$type": "field", "value": None}
            return {
                "data": {"componentType": rec.component_type, "members": mems},
            }
        return {}

    def _register_component(self, comp: Any, slot: Any, ct: str) -> str:
        """Register a component created via add_to_slot.

        Automatically creates a +Store companion for DataModel*FieldStore.
        """
        cid = self._gen_id("comp")
        slot_id = slot.id if hasattr(slot, "id") else str(slot)
        rec = _ComponentRecord(id=cid, component_type=ct, slot_id=slot_id)
        self.components[cid] = rec
        self.component_list.append(rec)
        self._ensure_member_ids(cid)

        if "DataModel" in ct and "FieldStore" in ct:
            store_cid = self._gen_id("store")
            store_ct = ct.replace("FieldStore", "FieldStore+Store")
            store_rec = _ComponentRecord(
                id=store_cid, component_type=store_ct, slot_id=slot_id,
            )
            self.components[store_cid] = store_rec
            self.component_list.append(store_rec)
            self._ensure_member_ids(store_cid)
        return cid

    # -- Graph query helpers -----------------------------------------------

    def find(self, pattern: str) -> list[_ComponentRecord]:
        """Find all components whose type matches a regex pattern."""
        return [c for c in self.component_list if re.search(pattern, c.component_type)]

    def find_one(self, pattern: str) -> _ComponentRecord:
        """Find exactly one component matching the pattern, or fail."""
        matches = self.find(pattern)
        assert len(matches) == 1, (
            f"Expected 1 component matching /{pattern}/, "
            f"got {len(matches)}: {[c.component_type for c in matches]}"
        )
        return matches[0]

    def count(self, pattern: str) -> int:
        """Count components matching the pattern."""
        return len(self.find(pattern))

    def owner_of(self, target_id: str) -> tuple[str, str] | None:
        """Resolve a target ID to (component_id, member_name).

        If the target is a member ID, returns the owning component.
        If the target is a component ID, returns (component_id, "").
        """
        if target_id in self._member_owner:
            return self._member_owner[target_id]
        if target_id in self.components:
            return (target_id, "")
        return None

    def ref_target_type(self, comp: _ComponentRecord, ref_name: str) -> str | None:
        """Get the component type that a reference points to.

        Resolves through member IDs to the owning component.
        """
        tid = comp.references.get(ref_name)
        if not tid:
            return None
        owner = self.owner_of(tid)
        if owner is None:
            return None
        return self.components[owner[0]].component_type

    def ref_target_comp(self, comp: _ComponentRecord, ref_name: str) -> _ComponentRecord | None:
        """Get the component record that a reference points to."""
        tid = comp.references.get(ref_name)
        if not tid:
            return None
        owner = self.owner_of(tid)
        if owner is None:
            return None
        return self.components[owner[0]]

    def ref_chain(
        self, comp: _ComponentRecord, ref_name: str,
    ) -> list[tuple[str, _ComponentRecord]]:
        """Follow a chain of references, returning [(ref_name, comp), ...]."""
        chain: list[tuple[str, _ComponentRecord]] = []
        current = self.ref_target_comp(comp, ref_name)
        while current is not None:
            chain.append((ref_name, current))
            # Follow OnSuccess/OnWritten/OnTrue chains
            for next_ref in ("OnSuccess", "OnWritten", "OnTrue"):
                nxt = self.ref_target_comp(current, next_ref)
                if nxt is not None:
                    ref_name = next_ref
                    current = nxt
                    break
            else:
                break
        return chain

    def types(self) -> list[str]:
        """Return all component types in creation order (excluding +Store)."""
        return [
            c.component_type for c in self.component_list
            if "+Store" not in c.component_type
        ]

    def short(self, ct: str) -> str:
        """Extract the short class name from a Resonite type string."""
        name = ct.rsplit(".", 1)[-1] if "." in ct else ct
        return name


def _ct(pattern: str) -> str:
    """Make a regex that matches a component type by its short name."""
    return rf"\.{pattern}$|\.{pattern}<"


def _patch_add_to_slot(mock_client: MockClient) -> Any:
    """Monkey-patch GeneratedComponent.add_to_slot to use mock_client.

    Returns the original method to restore later.
    """
    from pyresonitelink.generated import _base

    original = _base.GeneratedComponent.add_to_slot

    async def _mock_add_to_slot(  # type: ignore[no-untyped-def]
        self: Any,
        client: Any,
        slot: Any,
        debug: bool = False,
        **kwargs: Any,
    ) -> None:
        ct = getattr(type(self), "COMPONENT_TYPE", type(self).__name__)
        # Capture constructor-set references before they get overwritten.
        # Generated __init__ sets members like condition=<id> on
        # self._component.members as Reference(targetId=<id>).
        ctor_refs: dict[str, str] = {}
        for mname, mval in self._component.members.items():
            if isinstance(mval, members.Reference) and mval.targetId:
                ctor_refs[mname] = mval.targetId
        cid = mock_client._register_component(self, slot, ct)
        self._component.id = cid
        get_resp = await mock_client.get_component(componentId=cid)
        if get_resp.data:
            self._component = get_resp.data
        # Re-apply constructor refs and record them in the mock
        if ctor_refs:
            rec = mock_client.components.get(cid)
            if rec is not None:
                rec.references.update(ctor_refs)

    _base.GeneratedComponent.add_to_slot = _mock_add_to_slot  # type: ignore[assignment]
    return original


def _unpatch_add_to_slot(original: Any) -> None:
    """Restore the original add_to_slot method."""
    from pyresonitelink.generated import _base

    _base.GeneratedComponent.add_to_slot = original  # type: ignore[method-assign]


@pytest.fixture
def mock_client() -> Generator[MockClient, None, None]:
    """Create a MockClient and patch add_to_slot for the test."""
    client = MockClient()
    orig = _patch_add_to_slot(client)
    yield client
    _unpatch_add_to_slot(orig)


async def _build(mock: MockClient, g: Graph) -> None:
    """Run build_graph with the mock client."""
    await _builder.build_graph(g, mock)  # type: ignore[arg-type]


def _is_dmvfs(ct: str) -> bool:
    """Check if a component type is a DataModel*FieldStore (not +Store)."""
    return "DataModel" in ct and "FieldStore" in ct and "+Store" not in ct


def _dmvfs_type_arg(ct: str) -> str:
    """Extract the type argument from a DMVFS type string.

    ``"...DataModelValueFieldStore<float>"`` -> ``"float"``
    """
    m = re.search(r"<([^>]+)>$", ct)
    return m.group(1) if m else ""


# =========================================================================
# Tests: Bare Write (from test_dergflux_integration.py TestBareWrite)
# =========================================================================


class TestBareWriteBuild:
    """Test builder output for z = x + 3 where x=2."""

    @pytest.mark.asyncio
    async def test_bare_write(self, mock_client: MockClient) -> None:
        """Verify exact components and wiring for z = x + 3."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="bare_write")
        s.x = s.FloatModelVar("x", value=2.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + 3
                s.ran = True

        await _build(mock_client, g)

        m = mock_client

        # -- Model variables: 3 DMVFS (x:float, z:float, ran:bool) --------
        dmvfs = [c for c in m.component_list if _is_dmvfs(c.component_type)]
        assert len(dmvfs) == 3
        dmvfs_types = sorted(_dmvfs_type_arg(c.component_type) for c in dmvfs)
        assert dmvfs_types == ["bool", "float", "float"]

        # Each DMVFS has a named child slot
        child_names = {
            s.name for s in m.slots.values() if s.parent_id == "test-slot"
        }
        assert {"x", "z", "ran"} <= child_names

        # -- Gate condition: ValueEquals<bool>(ran, False) ------------------
        equals_comps = m.find(r"ValueEquals")
        assert len(equals_comps) == 1
        eq = equals_comps[0]
        # A input -> DMVFS(ran)
        eq_a_target = m.ref_target_type(eq, "A")
        assert eq_a_target is not None and "DataModel" in eq_a_target and "bool" in eq_a_target
        # B input -> ValueInput<bool> for the False constant
        eq_b_target = m.ref_target_type(eq, "B")
        assert eq_b_target is not None and "ValueInput" in eq_b_target

        # -- Expression: ValueAdd<float>(x, 3) ----------------------------
        add_comps = m.find(r"ValueAdd")
        assert len(add_comps) == 1
        add = add_comps[0]
        # A input -> DMVFS(x), which is float
        add_a_target = m.ref_target_type(add, "A")
        assert add_a_target is not None and "DataModel" in add_a_target and "float" in add_a_target
        # B input -> ValueInput<float> for the constant 3
        add_b_target = m.ref_target_type(add, "B")
        assert add_b_target is not None and "ValueInput" in add_b_target and "float" in add_b_target

        # -- ValueInput constants: False (bool) and 3 (float) and True ----
        value_inputs = m.find(r"ValueInput<")
        # At least: False, 3, True
        assert len(value_inputs) >= 3

        # -- Write nodes: ValueWrite for z and ran -------------------------
        writes = m.find(r"ValueWrite")
        assert len(writes) == 2
        # Each write has Variable and Value wired
        for w in writes:
            assert w.references.get("Variable"), (
                f"ValueWrite {w.id} missing Variable ref"
            )
            assert w.references.get("Value"), (
                f"ValueWrite {w.id} missing Value ref"
            )

        # -- Flow: If node -------------------------------------------------
        if_nodes = m.find(_ct("If"))
        assert len(if_nodes) == 1
        if_node = if_nodes[0]
        # Condition -> ValueEquals
        if_cond_target = m.ref_target_comp(if_node, "Condition")
        assert if_cond_target is not None
        assert "ValueEquals" in if_cond_target.component_type
        # OnTrue -> first write node in the chain
        assert if_node.references.get("OnTrue"), "If.OnTrue not wired"

        # -- Trigger: Update node ------------------------------------------
        updates = m.find(_ct("Update"))
        assert len(updates) == 1
        update = updates[0]
        # OnUpdate -> If node
        update_target = m.ref_target_comp(update, "OnUpdate")
        assert update_target is not None
        assert update_target.id == if_node.id


# =========================================================================
# Tests: Arithmetic (from test_dergflux_integration.py TestArithmetic)
# =========================================================================


class TestArithmeticBuild:
    """Test builder output for arithmetic operators."""

    @pytest.mark.asyncio
    async def test_add(self, mock_client: MockClient) -> None:
        """z = x + y: ValueAdd wired to both DMVFS inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_add")
        s.x = s.FloatModelVar("x", value=3.0)
        s.y = s.FloatModelVar("y", value=4.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        add = m.find_one(r"ValueAdd")
        # Both inputs should reference DMVFS<float> components (x and y)
        a_type = m.ref_target_type(add, "A")
        b_type = m.ref_target_type(add, "B")
        assert a_type is not None and "DataModel" in a_type and "float" in a_type
        assert b_type is not None and "DataModel" in b_type and "float" in b_type
        # A and B should point to different DMVFS components (x vs y)
        a_comp = m.ref_target_comp(add, "A")
        b_comp = m.ref_target_comp(add, "B")
        assert a_comp is not None and b_comp is not None
        assert a_comp.id != b_comp.id

        # Write node for z should get its Value from the ValueAdd
        writes = m.find(r"ValueWrite")
        z_write = None
        for w in writes:
            val_target = m.ref_target_comp(w, "Value")
            if val_target is not None and val_target.id == add.id:
                z_write = w
                break
        assert z_write is not None, "No ValueWrite with Value -> ValueAdd"

    @pytest.mark.asyncio
    async def test_sub(self, mock_client: MockClient) -> None:
        """z = x - y: ValueSub wired to both DMVFS inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_sub")
        s.x = s.FloatModelVar("x", value=10.0)
        s.y = s.FloatModelVar("y", value=3.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x - s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        sub = m.find_one(r"ValueSub")
        a_type = m.ref_target_type(sub, "A")
        b_type = m.ref_target_type(sub, "B")
        assert a_type is not None and "DataModel" in a_type
        assert b_type is not None and "DataModel" in b_type
        assert m.ref_target_comp(sub, "A") != m.ref_target_comp(sub, "B")

    @pytest.mark.asyncio
    async def test_mul(self, mock_client: MockClient) -> None:
        """z = x * y: ValueMul wired to both DMVFS inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_mul")
        s.x = s.FloatModelVar("x", value=3.0)
        s.y = s.FloatModelVar("y", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x * s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        mul = m.find_one(r"ValueMul")
        assert m.ref_target_type(mul, "A") is not None
        assert m.ref_target_type(mul, "B") is not None
        assert m.ref_target_comp(mul, "A") != m.ref_target_comp(mul, "B")

    @pytest.mark.asyncio
    async def test_div(self, mock_client: MockClient) -> None:
        """z = x / y: ValueDiv wired to both DMVFS inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_div")
        s.x = s.FloatModelVar("x", value=15.0)
        s.y = s.FloatModelVar("y", value=3.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x / s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        div = m.find_one(r"ValueDiv")
        assert m.ref_target_type(div, "A") is not None
        assert m.ref_target_type(div, "B") is not None
        assert m.ref_target_comp(div, "A") != m.ref_target_comp(div, "B")

    @pytest.mark.asyncio
    async def test_mod(self, mock_client: MockClient) -> None:
        """z = x %% y: ValueMod wired to both DMVFS inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_mod")
        s.x = s.FloatModelVar("x", value=17.0)
        s.y = s.FloatModelVar("y", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x % s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        mod = m.find_one(r"ValueMod")
        assert m.ref_target_type(mod, "A") is not None
        assert m.ref_target_type(mod, "B") is not None

    @pytest.mark.asyncio
    async def test_neg(self, mock_client: MockClient) -> None:
        """z = -x: ValueNegate with N wired to DMVFS(x)."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_neg")
        s.x = s.FloatModelVar("x", value=7.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = -s.x
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        neg = m.find_one(r"ValueNegate")
        # N input -> DMVFS(x)
        n_type = m.ref_target_type(neg, "N")
        assert n_type is not None and "DataModel" in n_type and "float" in n_type

    @pytest.mark.asyncio
    async def test_const_coercion(self, mock_client: MockClient) -> None:
        """z = x + 10: int constant coerced to float ValueInput."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_coerce")
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + 10
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        add = m.find_one(r"ValueAdd")
        # A -> DMVFS(x)
        a_type = m.ref_target_type(add, "A")
        assert a_type is not None and "DataModel" in a_type
        # B -> ValueInput<float> (constant 10 coerced to float)
        b_type = m.ref_target_type(add, "B")
        assert b_type is not None and "ValueInput" in b_type
        # The ValueInput should be float-typed (not int) due to coercion
        assert "float" in b_type

    @pytest.mark.asyncio
    async def test_chained_ops(self, mock_client: MockClient) -> None:
        """z = (x + 3) * 2: ValueAdd feeds into ValueMul."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="arith_chain")
        s.x = s.FloatModelVar("x", value=4.0)
        s.z = s.FloatModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = (s.x + 3) * 2
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        add = m.find_one(r"ValueAdd")
        mul = m.find_one(r"ValueMul")
        # ValueMul.A should reference the ValueAdd (chained)
        mul_a = m.ref_target_comp(mul, "A")
        assert mul_a is not None and mul_a.id == add.id
        # ValueMul.B -> ValueInput (constant 2)
        mul_b_type = m.ref_target_type(mul, "B")
        assert mul_b_type is not None and "ValueInput" in mul_b_type
        # ValueAdd.A -> DMVFS(x)
        add_a_type = m.ref_target_type(add, "A")
        assert add_a_type is not None and "DataModel" in add_a_type
        # ValueAdd.B -> ValueInput (constant 3)
        add_b_type = m.ref_target_type(add, "B")
        assert add_b_type is not None and "ValueInput" in add_b_type


# =========================================================================
# Tests: If/Else (from test_dergflux_integration.py TestIfElse)
# =========================================================================


class TestIfElseBuild:
    """Test builder output for If/Else flow control."""

    @pytest.mark.asyncio
    async def test_if_true_branch(self, mock_client: MockClient) -> None:
        """If x<3: z=1, else: z=2. Two If nodes, ValueLessThan, 3 writes."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="if_true")
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

        await _build(mock_client, g)
        m = mock_client

        # Two If nodes: outer gate (ran==False) and inner (x<3)
        if_nodes = m.find(_ct("If"))
        assert len(if_nodes) == 2

        # ValueLessThan for x < 3
        lt = m.find_one(r"ValueLessThan")
        # A -> DMVFS(x)
        lt_a = m.ref_target_type(lt, "A")
        assert lt_a is not None and "DataModel" in lt_a and "float" in lt_a
        # B -> ValueInput<float> (constant 3)
        lt_b = m.ref_target_type(lt, "B")
        assert lt_b is not None and "ValueInput" in lt_b

        # Inner If.Condition -> ValueLessThan
        # Find the If whose Condition points to the LessThan
        inner_if = None
        for ifn in if_nodes:
            cond_comp = m.ref_target_comp(ifn, "Condition")
            if cond_comp is not None and cond_comp.id == lt.id:
                inner_if = ifn
                break
        assert inner_if is not None, "No If node with Condition -> ValueLessThan"

        # Inner If should have both OnTrue and OnFalse wired (both branches)
        assert inner_if.references.get("OnTrue"), "Inner If.OnTrue not wired"
        assert inner_if.references.get("OnFalse"), "Inner If.OnFalse not wired"

        # 3 write nodes: z=1.0 (true), z=2.0 (false), ran=True
        writes = m.find(r"ValueWrite")
        assert len(writes) == 3

    @pytest.mark.asyncio
    async def test_if_with_continuation(self, mock_client: MockClient) -> None:
        """if x<3: tmp=x+3 else: tmp=x-3; z=tmp+1."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="if_cont")
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

        await _build(mock_client, g)
        m = mock_client

        # ValueAdd for x+3, ValueSub for x-3, ValueAdd for tmp+1
        adds = m.find(r"ValueAdd")
        assert len(adds) == 2, f"Expected 2 ValueAdd, got {len(adds)}"
        subs = m.find(r"ValueSub")
        assert len(subs) == 1

        # 4 writes: tmp (true branch), tmp (false branch), z, ran
        writes = m.find(r"ValueWrite")
        assert len(writes) == 4

        # The continuation writes (z, ran) should be reachable from
        # both If branches — verify the inner If has OnTrue and OnFalse
        lt = m.find_one(r"ValueLessThan")
        inner_if = None
        for ifn in m.find(_ct("If")):
            cc = m.ref_target_comp(ifn, "Condition")
            if cc is not None and cc.id == lt.id:
                inner_if = ifn
                break
        assert inner_if is not None
        assert inner_if.references.get("OnTrue")
        assert inner_if.references.get("OnFalse")

    @pytest.mark.asyncio
    async def test_if_without_else(self, mock_client: MockClient) -> None:
        """If x<3: z=99. Continuation w=1 always runs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="if_no_else")
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

        await _build(mock_client, g)
        m = mock_client

        # Inner If has OnTrue (z=99) but OnFalse should be wired to
        # the continuation (w=1) since there's no else branch.
        lt = m.find_one(r"ValueLessThan")
        inner_if = None
        for ifn in m.find(_ct("If")):
            cc = m.ref_target_comp(ifn, "Condition")
            if cc is not None and cc.id == lt.id:
                inner_if = ifn
                break
        assert inner_if is not None
        assert inner_if.references.get("OnTrue"), "If.OnTrue not wired"
        # OnFalse should also be wired (to continuation)
        assert inner_if.references.get("OnFalse"), (
            "If.OnFalse should be wired to continuation w=1"
        )

        # 3 writes: z=99, w=1, ran=True
        writes = m.find(r"ValueWrite")
        assert len(writes) == 3


# =========================================================================
# Tests: Multiple Writes (from TestMultipleWrites)
# =========================================================================


class TestMultipleWritesBuild:
    """Test builder output for sequential writes."""

    @pytest.mark.asyncio
    async def test_sequential_writes(self, mock_client: MockClient) -> None:
        """a=1, b=2, c=3 creates 4 writes chained by OnWritten."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="seq_writes")
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

        await _build(mock_client, g)
        m = mock_client

        # 4 DMVFS (a, b, c, ran)
        dmvfs = [c for c in m.component_list if _is_dmvfs(c.component_type)]
        assert len(dmvfs) == 4

        # 4 writes (a, b, c, ran) each with Variable + Value wired
        writes = m.find(r"ValueWrite")
        assert len(writes) == 4
        for w in writes:
            assert w.references.get("Variable"), f"Write {w.id} missing Variable"
            assert w.references.get("Value"), f"Write {w.id} missing Value"

        # Writes should be chained: first.OnWritten -> second, etc.
        # At least some writes should have OnWritten pointing to another write
        chained = 0
        for w in writes:
            target = m.ref_target_comp(w, "OnWritten")
            if target is not None and "ValueWrite" in target.component_type:
                chained += 1
        assert chained >= 2, (
            f"Expected at least 2 chained OnWritten links, got {chained}"
        )


# =========================================================================
# Tests: Int Variables (from TestIntVariables)
# =========================================================================


class TestIntVariablesBuild:
    """Test builder output for integer arithmetic."""

    @pytest.mark.asyncio
    async def test_int_arithmetic(self, mock_client: MockClient) -> None:
        """z = x + y with IntModelVars uses int-typed DMVFS and ValueAdd."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="int_arith")
        s.x = s.IntModelVar("x", value=3)
        s.y = s.IntModelVar("y", value=4)
        s.z = s.IntModelVar("z")
        s.ran = s.BoolModelVar("ran")

        with g.Under(slot):
            with g.If(s.ran == False):  # noqa: E712
                s.z = s.x + s.y
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        # 3 DMVFS<int> + 1 DMVFS<bool>
        dmvfs = [c for c in m.component_list if _is_dmvfs(c.component_type)]
        type_args = sorted(_dmvfs_type_arg(c.component_type) for c in dmvfs)
        assert type_args == ["bool", "int", "int", "int"]

        # ValueAdd should be int-parameterized
        add = m.find_one(r"ValueAdd")
        assert "int" in add.component_type, (
            f"Expected int-typed ValueAdd, got {add.component_type}"
        )


# =========================================================================
# Tests: Comparison (from TestComparison)
# =========================================================================


class TestComparisonBuild:
    """Test builder output for comparison operators."""

    @pytest.mark.asyncio
    async def test_less_than(self, mock_client: MockClient) -> None:
        """If x < 10 creates ValueLessThan with DMVFS and constant inputs."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cmp_lt")
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

        await _build(mock_client, g)
        m = mock_client

        lt = m.find_one(r"ValueLessThan")
        # A -> DMVFS(x, float)
        assert m.ref_target_type(lt, "A") is not None
        assert "DataModel" in m.ref_target_type(lt, "A")  # type: ignore[operator]
        # B -> ValueInput<float> (constant 10)
        b_type = m.ref_target_type(lt, "B")
        assert b_type is not None and "ValueInput" in b_type

        # The comparison feeds into an If node
        found_if = False
        for ifn in m.find(_ct("If")):
            cc = m.ref_target_comp(ifn, "Condition")
            if cc is not None and cc.id == lt.id:
                found_if = True
                break
        assert found_if, "No If node with Condition -> ValueLessThan"

    @pytest.mark.asyncio
    async def test_greater_than(self, mock_client: MockClient) -> None:
        """If x > 3 creates ValueGreaterThan."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cmp_gt")
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

        await _build(mock_client, g)
        m = mock_client

        gt = m.find_one(r"ValueGreaterThan")
        assert m.ref_target_type(gt, "A") is not None
        assert m.ref_target_type(gt, "B") is not None

    @pytest.mark.asyncio
    async def test_equals(self, mock_client: MockClient) -> None:
        """If x == 5 creates 2 ValueEquals (gate + inner comparison)."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cmp_eq")
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

        await _build(mock_client, g)
        m = mock_client

        equals = m.find(r"ValueEquals")
        assert len(equals) == 2, f"Expected 2 ValueEquals, got {len(equals)}"
        # One should compare bool (gate), one should compare float (x==5)
        bool_eq = [e for e in equals if "bool" in e.component_type]
        float_eq = [e for e in equals if "float" in e.component_type]
        assert len(bool_eq) == 1, "Expected 1 bool ValueEquals (gate)"
        assert len(float_eq) == 1, "Expected 1 float ValueEquals (x==5)"

    @pytest.mark.asyncio
    async def test_not_equals(self, mock_client: MockClient) -> None:
        """If x != 5 creates ValueNotEquals + ValueEquals (gate)."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cmp_ne")
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

        await _build(mock_client, g)
        m = mock_client

        ne = m.find_one(r"ValueNotEquals")
        assert "float" in ne.component_type
        # A -> DMVFS(x)
        a_type = m.ref_target_type(ne, "A")
        assert a_type is not None and "DataModel" in a_type
        # B -> ValueInput<float>
        b_type = m.ref_target_type(ne, "B")
        assert b_type is not None and "ValueInput" in b_type


# =========================================================================
# Tests: FireOn (from test_dergflux_fireon_integration.py TestFireOn)
# =========================================================================


class TestFireOnBuild:
    """Test builder output for FireOn event source nodes."""

    @pytest.mark.asyncio
    async def test_fire_on_true(self, mock_client: MockClient) -> None:
        """FireOnTrue: event source + write, no Update trigger."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=False)
        s.result = s.IntModelVar("result", value=0)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.trigger) as e:
                with e.on_changed():
                    s.result = 1

        await _build(mock_client, g)
        m = mock_client

        # FireOnTrue component exists
        fot = m.find_one(r"FireOnTrue")
        # Condition input -> DMVFS(trigger, bool)
        cond_type = m.ref_target_type(fot, "Condition")
        assert cond_type is not None and "DataModel" in cond_type and "bool" in cond_type
        # OnChanged -> write node
        on_changed_target = m.ref_target_comp(fot, "OnChanged")
        assert on_changed_target is not None
        assert "ValueWrite" in on_changed_target.component_type

        # No Update node (event source)
        assert m.count(_ct("Update")) == 0

        # Write for result=1
        writes = m.find(r"ValueWrite")
        assert len(writes) == 1
        w = writes[0]
        assert w.references.get("Variable")
        assert w.references.get("Value")

    @pytest.mark.asyncio
    async def test_fire_on_false(self, mock_client: MockClient) -> None:
        """FireOnFalse: Condition wired to DMVFS(trigger)."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=True)
        s.result = s.IntModelVar("result", value=0)

        with g.Under(slot):
            with g.FireOnFalse(condition=s.trigger) as e:
                with e.on_changed():
                    s.result = 1

        await _build(mock_client, g)
        m = mock_client

        fof = m.find_one(r"FireOnFalse")
        cond_type = m.ref_target_type(fof, "Condition")
        assert cond_type is not None and "bool" in cond_type
        assert m.count(_ct("Update")) == 0

    @pytest.mark.asyncio
    async def test_fire_on_value_change(self, mock_client: MockClient) -> None:
        """FireOnValueChange: input wired to DMVFS(x), body has ValueAdd."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.x = s.FloatModelVar("x", value=0.0)
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnValueChange(value=s.x) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await _build(mock_client, g)
        m = mock_client

        fovc = m.find_one(r"FireOnValueChange")
        # Value input -> DMVFS(x, float)
        val_type = m.ref_target_type(fovc, "Value")
        assert val_type is not None and "DataModel" in val_type

        # counter + 1 creates ValueAdd<int>
        add = m.find_one(r"ValueAdd")
        assert "int" in add.component_type
        # A -> DMVFS(counter, int)
        add_a = m.ref_target_type(add, "A")
        assert add_a is not None and "DataModel" in add_a

        # OnChanged -> write node
        assert fovc.references.get("OnChanged")

    @pytest.mark.asyncio
    async def test_fire_on_object_value_change(self, mock_client: MockClient) -> None:
        """FireOnObjectValueChange for a string model var."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.text = s.StringModelVar("text", value="initial")
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireOnObjectValueChange(value=s.text) as e:
                with e.on_changed():
                    s.counter = s.counter + 1

        await _build(mock_client, g)
        m = mock_client

        foovc = m.find_one(r"FireOnObjectValueChange")
        # String model var uses DataModelObjectFieldStore
        val_type = m.ref_target_type(foovc, "Value")
        assert val_type is not None and "DataModel" in val_type

    @pytest.mark.asyncio
    async def test_fire_while_true(self, mock_client: MockClient) -> None:
        """FireWhileTrue: Condition wired, OnUpdate wired to write."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.trigger = s.BoolModelVar("trigger", value=False)
        s.counter = s.IntModelVar("counter", value=0)

        with g.Under(slot):
            with g.FireWhileTrue(condition=s.trigger) as e:
                with e.on_update():
                    s.counter = s.counter + 1

        await _build(mock_client, g)
        m = mock_client

        fwt = m.find_one(r"FireWhileTrue")
        cond_type = m.ref_target_type(fwt, "Condition")
        assert cond_type is not None and "bool" in cond_type
        # OnUpdate -> write chain
        assert fwt.references.get("OnUpdate")
        assert m.count(_ct("Update")) == 0


# =========================================================================
# Tests: Loops (from test_dergflux_flow_integration.py TestLoops)
# =========================================================================


class TestLoopsBuild:
    """Test builder output for loop constructs."""

    @pytest.mark.asyncio
    async def test_for_loop(self, mock_client: MockClient) -> None:
        """For(5): For node with Count wired, LoopIteration -> write."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.For(5) as f:
                        with f.OnIterate() as i:
                            s.total = s.total + i
                    s.ran = True

        await _build(mock_client, g)
        m = mock_client

        # FireOnTrue event source
        fot = m.find_one(r"FireOnTrue")
        assert m.count(_ct("Update")) == 0

        # For node exists
        for_node = m.find_one(_ct("For"))
        # Count should be wired to a ValueInput<int> (constant 5)
        count_type = m.ref_target_type(for_node, "Count")
        assert count_type is not None and "ValueInput" in count_type
        # LoopIteration -> write chain
        assert for_node.references.get("LoopIteration")

        # ValueAdd for total + i
        add = m.find_one(r"ValueAdd")
        assert "int" in add.component_type

        # LoopEnd -> write for ran=True
        assert for_node.references.get("LoopEnd")

    @pytest.mark.asyncio
    async def test_range_loop(self, mock_client: MockClient) -> None:
        """Range(2, 10, 2): RangeLoopInt with Start/End/StepSize wired."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.Range(2, 10, 2) as f:
                        with f.OnIterate() as i:
                            s.total = s.total + i
                    s.ran = True

        await _build(mock_client, g)
        m = mock_client

        rl = m.find_one(r"RangeLoopInt")
        # Start, End, StepSize all wired to ValueInput<int> constants
        for ref_name in ("Start", "End", "StepSize"):
            ref_type = m.ref_target_type(rl, ref_name)
            assert ref_type is not None and "ValueInput" in ref_type, (
                f"RangeLoopInt.{ref_name} should be wired to ValueInput, "
                f"got {ref_type}"
            )
        # LoopIteration -> write chain
        assert rl.references.get("LoopIteration")

    @pytest.mark.asyncio
    async def test_while_loop(self, mock_client: MockClient) -> None:
        """While(counter > 0): While node with Condition and LoopIteration."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.counter = s.IntModelVar("counter", value=5)
        s.total = s.IntModelVar("total", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.While(s.counter > 0):
                        s.total = s.total + s.counter
                        s.counter = s.counter - 1
                    s.ran = True

        await _build(mock_client, g)
        m = mock_client

        while_node = m.find_one(_ct("While"))
        # Condition -> ValueGreaterThan
        cond_comp = m.ref_target_comp(while_node, "Condition")
        assert cond_comp is not None
        assert "ValueGreaterThan" in cond_comp.component_type
        # LoopIteration -> first write in body
        assert while_node.references.get("LoopIteration")

        # ValueGreaterThan: A -> DMVFS(counter), B -> ValueInput(0)
        gt = cond_comp
        gt_a = m.ref_target_type(gt, "A")
        assert gt_a is not None and "DataModel" in gt_a
        gt_b = m.ref_target_type(gt, "B")
        assert gt_b is not None and "ValueInput" in gt_b

        # Body: ValueAdd (total+counter) and ValueSub (counter-1)
        assert m.count(r"ValueAdd") >= 1
        assert m.count(r"ValueSub") >= 1


# =========================================================================
# Tests: Nested Flow (from TestNestedFlow)
# =========================================================================


class TestNestedFlowBuild:
    """Test builder output for nested flow control."""

    @pytest.mark.asyncio
    async def test_nested_if_in_for(self, mock_client: MockClient) -> None:
        """For(10) with If(i%%2==0) inside: For + If + Mod + Equals."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.evens = s.IntModelVar("evens", value=0)
        s.odds = s.IntModelVar("odds", value=0)
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.For(10) as f:
                        with f.OnIterate() as i:
                            with g.If((i % 2) == 0):
                                s.evens = s.evens + 1
                            with g.Else():
                                s.odds = s.odds + 1
                    s.ran = True

        await _build(mock_client, g)
        m = mock_client

        # For node
        for_node = m.find_one(_ct("For"))
        assert for_node.references.get("LoopIteration")

        # ValueMod for i % 2
        mod = m.find_one(r"ValueMod")
        assert "int" in mod.component_type

        # ValueEquals for (i%2) == 0
        # There will be multiple ValueEquals; find the int one
        int_eq = [e for e in m.find(r"ValueEquals") if "int" in e.component_type]
        assert len(int_eq) == 1
        eq = int_eq[0]
        # A -> ValueMod output
        eq_a = m.ref_target_comp(eq, "A")
        assert eq_a is not None and eq_a.id == mod.id

        # If node with Condition -> the int ValueEquals
        inner_if = None
        for ifn in m.find(_ct("If")):
            cc = m.ref_target_comp(ifn, "Condition")
            if cc is not None and cc.id == eq.id:
                inner_if = ifn
                break
        assert inner_if is not None
        assert inner_if.references.get("OnTrue")
        assert inner_if.references.get("OnFalse")

        # 2 ValueAdd: evens+1 and odds+1
        adds = m.find(r"ValueAdd")
        int_adds = [a for a in adds if "int" in a.component_type]
        assert len(int_adds) == 2


# =========================================================================
# Tests: Outcome (from TestOutcome)
# =========================================================================


class TestOutcomeBuild:
    """Test builder output for Outcome abstraction."""

    @pytest.mark.asyncio
    async def test_outcome_basic(self, mock_client: MockClient) -> None:
        """Outcome: model var + FireOnValueChange reaction + If branches."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.x = s.IntModelVar("x", value=5)
        s.log = s.StringModelVar("log", value="unset")
        s.ran = s.BoolModelVar("ran", value=False)
        s.go = s.BoolModelVar("go", value=False)

        res = g.Outcome(s, "res")

        with g.Under(slot):
            with g.FireOnTrue(condition=s.go) as e:
                with e.on_changed():
                    with g.If(s.x > 3):
                        res.set("high")
                    with g.Else():
                        res.set("low")

            with res.on_changed() as label:
                with g.If(label == "high"):
                    s.log = "got high"
                with g.If(label == "low"):
                    s.log = "got low"
                s.ran = True

        await _build(mock_client, g)
        m = mock_client

        # FireOnTrue for go trigger
        m.find_one(r"FireOnTrue")

        # FireOnValueChange for outcome reaction
        fovc = m.find_one(r"FireOnValueChange")
        # Its value input -> DMVFS(res, int) (outcome uses int internally)
        val_type = m.ref_target_type(fovc, "Value")
        assert val_type is not None and "DataModel" in val_type

        # ValueGreaterThan for x > 3
        m.find_one(r"ValueGreaterThan")

        # Multiple ValueEquals: gate label comparisons (high=1, low=2)
        equals = m.find(r"ValueEquals")
        assert len(equals) >= 2

        # Writes for setting the outcome int + writing "got high"/"got low"
        writes = m.find(r"ValueWrite|ObjectWrite")
        assert len(writes) >= 4  # res="high", res="low", log, ran


# =========================================================================
# Tests: Structural properties
# =========================================================================


class TestStructuralProperties:
    """Test general structural properties of the builder output."""

    @pytest.mark.asyncio
    async def test_no_trigger_uses_update(self, mock_client: MockClient) -> None:
        """Under without trigger: Update.OnUpdate -> first write node."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="notrigger")
        s.x = s.FloatModelVar("x", value=1.0)
        s.z = s.FloatModelVar("z")

        with g.Under(slot):
            s.z = s.x + 1

        await _build(mock_client, g)
        m = mock_client

        update = m.find_one(_ct("Update"))
        # OnUpdate should be wired
        assert update.references.get("OnUpdate"), "Update.OnUpdate not wired"
        target = m.ref_target_comp(update, "OnUpdate")
        assert target is not None

    @pytest.mark.asyncio
    async def test_model_vars_create_child_slots(self, mock_client: MockClient) -> None:
        """Each ModelVar creates a named child slot with DMVFS on it."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.a = s.FloatModelVar("a", value=1.0)
        s.b = s.IntModelVar("b", value=2)

        with g.Under(slot):
            s.a = s.a + 1

        await _build(mock_client, g)
        m = mock_client

        child_names = {
            sr.name for sr in m.slots.values() if sr.parent_id == "test-slot"
        }
        assert "a" in child_names
        assert "b" in child_names

        # DMVFS components live on the child slots, not the parent
        for c in m.component_list:
            if _is_dmvfs(c.component_type):
                assert c.slot_id != "test-slot", (
                    f"DMVFS {c.id} should be on a child slot, "
                    f"not the parent"
                )

    @pytest.mark.asyncio
    async def test_event_source_no_update_node(self, mock_client: MockClient) -> None:
        """Event sources don't create an Update trigger."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.flag = s.BoolModelVar("flag", value=False)
        s.z = s.IntModelVar("z", value=0)

        with g.Under(slot):
            with g.FireOnTrue(condition=s.flag) as e:
                with e.on_changed():
                    s.z = 1

        await _build(mock_client, g)
        assert mock_client.count(_ct("Update")) == 0

    @pytest.mark.asyncio
    async def test_all_write_nodes_fully_wired(self, mock_client: MockClient) -> None:
        """Every ValueWrite node has both Variable and Value references."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="wiring")
        s.x = s.FloatModelVar("x", value=1.0)
        s.y = s.FloatModelVar("y")
        s.z = s.FloatModelVar("z")

        with g.Under(slot):
            s.y = s.x + 1
            s.z = s.x * 2

        await _build(mock_client, g)
        m = mock_client

        writes = m.find(r"ValueWrite")
        assert len(writes) == 2
        for w in writes:
            assert w.references.get("Variable"), (
                f"ValueWrite {w.id} missing Variable"
            )
            assert w.references.get("Value"), (
                f"ValueWrite {w.id} missing Value"
            )
            # Variable should point to a DMVFS
            var_type = m.ref_target_type(w, "Variable")
            assert var_type is not None and "DataModel" in var_type

    @pytest.mark.asyncio
    async def test_if_condition_points_to_bool_expr(
        self, mock_client: MockClient,
    ) -> None:
        """Every If node's Condition points to a bool-producing component."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot)
        s.x = s.FloatModelVar("x", value=5.0)
        s.z = s.FloatModelVar("z")

        with g.Under(slot):
            with g.If(s.x > 3):
                s.z = 1.0

        await _build(mock_client, g)
        m = mock_client

        if_node = m.find_one(_ct("If"))
        cond_comp = m.ref_target_comp(if_node, "Condition")
        assert cond_comp is not None
        # Condition should be a comparison node (ValueGreaterThan)
        assert "ValueGreaterThan" in cond_comp.component_type
