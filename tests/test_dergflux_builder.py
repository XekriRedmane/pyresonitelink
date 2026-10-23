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
    # For a field drive's Proxy, the drive node it belongs to.
    proxy_of: str | None = None


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
    "OnTrue", "OnFalse", "Axis", "Angle", "Angles", "Drive",
    "From", "To", "Lerp",
    # Outputs and inputs of the vector, transform, and physics nodes.
    "Z", "W", "V", "GlobalPosition", "GlobalRotation", "GlobalScale",
    "Instance", "Next", "FoundValue", "Component", "User", "Grabbable",
    "OnHit", "OnMiss", "HitCollider", "HitPoint", "HitNormal", "HitDistance",
    "Format", "FormatProvider",
]

# The slot fields that Bind() can drive. A mock slot's member ID for one
# is "<slot ID>-<field>".
_SLOT_FIELDS = ["position", "rotation", "scale", "isActive", "orderOffset"]


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

        if slotId is not None:
            sid = slotId
        elif isinstance(slot, str):
            sid = slot
        else:
            sid = slot.id if slot is not None else None
        comps: list[Any] = []
        for c in self.components.values():
            if c.slot_id != sid:
                continue
            if c.proxy_of is not None:
                # A real Component, so the builder can read its Node.
                comps.append(workers.Component(
                    id=c.id, componentType=c.component_type,
                    members={
                        "Node": members.Reference(targetId=c.proxy_of),
                        "Drive": members.Reference(targetId=None),
                    },
                ))
            else:
                comps.append(MagicMock(id=c.id, componentType=c.component_type))
        resp = MagicMock()
        resp.data = MagicMock()
        resp.data.components = comps
        resp.data.parent = None
        for name in _SLOT_FIELDS:
            setattr(resp.data, name, MagicMock(id=f"{sid}-{name}"))
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

        if "FieldDrive" in ct:
            # The server adds a Proxy beside each field drive node.
            proxy_cid = self._gen_id("proxy")
            proxy_rec = _ComponentRecord(
                id=proxy_cid,
                component_type="[FrooxEngine]FrooxEngine.ProtoFlux.CoreNodes.FieldDriveBase<T>+Proxy",
                slot_id=slot_id, proxy_of=cid,
            )
            self.components[proxy_cid] = proxy_rec
            self.component_list.append(proxy_rec)

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
    async def test_strings_compare_with_object_equals(self, mock_client: MockClient) -> None:
        """String == and != use ObjectEquals and ObjectNotEquals, since ValueEquals<string> doesn't exist."""
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cmp_str")
        s.name = s.StringModelVar("name", "")
        s.same = s.BoolModelVar("same")
        s.different = s.BoolModelVar("different")

        with g.Under(slot):
            s.same = s.name == "golf"
            s.different = s.name != "golf"

        await _build(mock_client, g)
        m = mock_client

        assert not m.find(r"ValueEquals<string>")
        assert not m.find(r"ValueNotEquals<string>")
        eq = m.find_one(r"ObjectEquals")
        assert eq.component_type.endswith("ObjectEquals<string>")
        ne = m.find_one(r"ObjectNotEquals")
        assert ne.component_type.endswith("ObjectNotEquals<string>")
        b_type = m.ref_target_type(eq, "B")
        assert b_type is not None and "ValueObjectInput" in b_type

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


class TestIsSlotOrChild:
    """Tests _is_slot_or_child with real Slot data instead of MagicMocks.

    A MagicMock answers any attribute, which once hid a read of a
    nonexistent ``Reference.target`` attribute.
    """

    class _HierarchyClient:
        """Serves get_slot from a child-to-parent map of slot IDs."""

        def __init__(self, parents: dict[str, str | None]) -> None:
            self.parents = parents

        async def get_slot(self, slot: Any, depth: int = 0) -> Any:
            from pyresonitelink.data import members, responses

            slot_id = slot.id if isinstance(slot, workers.Slot) else slot
            return responses.SlotData(
                success=True,
                data=workers.Slot(
                    id=slot_id,
                    parent=members.Reference(targetId=self.parents[slot_id]),
                ),
            )

    @pytest.mark.asyncio
    async def test_grandchild_is_under_parent(self) -> None:
        client = self._HierarchyClient(
            {"grandchild": "child", "child": "space", "space": "Root", "Root": None},
        )
        assert await _builder._is_slot_or_child(
            client,  # type: ignore[arg-type]
            workers.Slot(id="space"),
            workers.Slot(id="grandchild"),
        )

    @pytest.mark.asyncio
    async def test_sibling_is_not_under_parent(self) -> None:
        client = self._HierarchyClient(
            {"other": "Root", "space": "Root", "Root": None},
        )
        assert not await _builder._is_slot_or_child(
            client,  # type: ignore[arg-type]
            workers.Slot(id="space"),
            workers.Slot(id="other"),
        )


# =========================================================================
# Tests: shaping, conditional, rotations, world time, and bindings
# =========================================================================


class TestMathBuild:
    """Test builder output for the shaping, conditional, and time nodes."""

    @pytest.mark.asyncio
    async def test_conditional_wiring(self, mock_client: MockClient) -> None:
        """r = conditional(flag, a, b) wires each argument to its own input."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="cond")
        s.flag = s.BoolModelVar("flag", value=True)
        s.a = s.FloatModelVar("a", value=1.0)
        s.b = s.FloatModelVar("b", value=2.0)
        s.r = s.FloatModelVar("r")
        with g.Under(slot):
            s.r = dm.conditional(s.flag, s.a, s.b)
        await _build(mock_client, g)
        m = mock_client

        cond = m.find_one(r"ValueConditional")
        condition = m.ref_target_type(cond, "Condition")
        assert condition is not None and _dmvfs_type_arg(condition) == "bool"
        on_true = m.ref_target_comp(cond, "OnTrue")
        on_false = m.ref_target_comp(cond, "OnFalse")
        assert on_true is not None and on_false is not None
        assert on_true.id != on_false.id
        assert _dmvfs_type_arg(on_true.component_type) == "float"
        assert _dmvfs_type_arg(on_false.component_type) == "float"

    @pytest.mark.asyncio
    async def test_smoothstep_one_argument(self, mock_client: MockClient) -> None:
        """smoothstep(x) is a SmoothStep_Float node reading x."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="shape")
        s.x = s.FloatModelVar("x", value=0.25)
        s.y = s.FloatModelVar("y")
        with g.Under(slot):
            s.y = dm.smoothstep(s.x)
        await _build(mock_client, g)
        m = mock_client

        node = m.find_one(_ct("SmoothStep_Float"))
        value = m.ref_target_type(node, "Value")
        assert value is not None and "DataModel" in value

    @pytest.mark.asyncio
    async def test_smootherstep_edges(self, mock_client: MockClient) -> None:
        """smootherstep(0, 2, x) clamps the mapped x before the node."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="shape3")
        s.x = s.DoubleModelVar("x", value=0.5)
        s.y = s.DoubleModelVar("y")
        with g.Under(slot):
            s.y = dm.smootherstep(0, 2, s.x)
        await _build(mock_client, g)
        m = mock_client

        node = m.find_one(_ct("SmootherStep_Double"))
        assert m.ref_target_type(node, "Value") is not None
        assert "Clamp01_Double" in (m.ref_target_type(node, "Value") or "")

    @pytest.mark.asyncio
    async def test_world_time(self, mock_client: MockClient) -> None:
        """time.world_time() is a WorldTimeDouble node."""
        from pyresonitelink.dergflux import time
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="wt")
        s.t = s.DoubleModelVar("t")
        with g.Under(slot):
            s.t = time.world_time()
        await _build(mock_client, g)
        assert mock_client.count(_ct("WorldTimeDouble")) == 1


class TestBindBuild:
    """Test builder output for g.Bind() with an expression."""

    @pytest.mark.asyncio
    async def test_expression_to_component(self, mock_client: MockClient) -> None:
        """The drive's Proxy, not the drive, references the bound field."""
        from pyresonitelink.data import fields
        from pyresonitelink.generated._base import GeneratedComponent
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="bind")
        s.x = s.FloatModelVar("x", value=1.0)
        comp = GeneratedComponent()
        comp._component.members["Value"] = fields.FieldFloat(id="field-member", value=0.0)
        g.Bind(s.x + 1, comp, "Value", slot=slot)
        await _build(mock_client, g)
        m = mock_client

        drive = m.find_one(r"ValueFieldDrive<float>")
        assert m.ref_target_type(drive, "Value") is not None
        proxy = m.find_one(r"\+Proxy")
        assert proxy.proxy_of == drive.id
        assert proxy.references["Drive"] == "field-member"

    @pytest.mark.asyncio
    async def test_axis_angle_to_slot_rotation(self, mock_client: MockClient) -> None:
        """A FloatQ expression drives the slot's Rotation field."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        wheel = workers.Slot(id="wheel")
        g = Graph()
        s = g.Space(slot, space_name="turn")
        s.angle = s.FloatModelVar("angle", value=30.0)
        g.Bind(dm.axis_angle(primitives.Float3(-1, 0, 0), s.angle), wheel, "Rotation", slot=slot)
        await _build(mock_client, g)
        m = mock_client

        axis_angle = m.find_one(_ct("AxisAngle_floatQ"))
        assert "ValueInput<float3>" in (m.ref_target_type(axis_angle, "Axis") or "")
        assert _dmvfs_type_arg(m.ref_target_type(axis_angle, "Angle") or "") == "float"
        drive = m.find_one(r"ValueFieldDrive<floatQ>")
        assert m.ref_target_comp(drive, "Value") == axis_angle
        proxy = m.find_one(r"\+Proxy")
        assert proxy.references["Drive"] == "wheel-rotation"

    @pytest.mark.asyncio
    async def test_binding_is_built_before_flows(self, mock_client: MockClient) -> None:
        """A binding that reads only variables exists before any flow node."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="early")
        s.angle = s.FloatModelVar("angle")
        with g.Under(slot):
            with g.If(s.angle == 0):
                s.angle = 30.0
        g.Bind(dm.axis_angle(primitives.Float3(0, 1, 0), s.angle), workers.Slot(id="w"), "Rotation", slot=slot)
        await _build(mock_client, g)
        m = mock_client

        order = [c.id for c in m.component_list]
        drive = m.find_one(r"ValueFieldDrive<floatQ>")
        if_node = m.find_one(_ct("If"))
        assert order.index(drive.id) < order.index(if_node.id)

    @pytest.mark.asyncio
    async def test_loop_index_binding_is_built_after_its_loop(
        self, mock_client: MockClient,
    ) -> None:
        """A binding that reads a loop index waits for the loop's node."""
        from pyresonitelink.data import fields
        from pyresonitelink.generated._base import GeneratedComponent
        slot = workers.Slot(id="test-slot")
        comp = GeneratedComponent()
        comp._component.members["Index"] = fields.FieldInt(id="index-member", value=0)
        g = Graph()
        with g.Under(slot):
            with g.For(3) as f:
                with f.OnIterate() as i:
                    g.Bind(i, comp, "Index")
        await _build(mock_client, g)
        m = mock_client

        order = [c.id for c in m.component_list]
        drive = m.find_one(r"ValueFieldDrive<int>")
        loop = m.find_one(_ct("For"))
        assert order.index(loop.id) < order.index(drive.id)
        assert m.ref_target_comp(drive, "Value") == loop


class TestLerpBuild:
    """Test builder output for the lerp functions."""

    @pytest.mark.asyncio
    async def test_lerp(self, mock_client: MockClient) -> None:
        """lerp(a, b, t) is a ValueLerp<float> wired From, To, and Lerp."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="lerp")
        s.a = s.FloatModelVar("a", value=2.0)
        s.b = s.FloatModelVar("b", value=10.0)
        s.t = s.FloatModelVar("t", value=0.25)
        s.r = s.FloatModelVar("r")
        s.u = s.FloatModelVar("u")
        with g.Under(slot):
            s.r = dm.lerp(s.a, s.b, s.t)
            s.u = dm.lerp_unclamped(s.a, s.b, s.t)
        await _build(mock_client, g)
        m = mock_client

        for pattern in (r"\.ValueLerp<float>", r"\.ValueLerpUnclamped<float>"):
            node = m.find_one(pattern)
            sources = [m.ref_target_comp(node, name) for name in ("From", "To", "Lerp")]
            assert all(c is not None and _is_dmvfs(c.component_type) for c in sources)
            assert len({c.id for c in sources if c is not None}) == 3

    @pytest.mark.asyncio
    async def test_inverse_lerp_scalar_and_vector(self, mock_client: MockClient) -> None:
        """Doubles use ValueInverseLerp<double>, and Float3s InverseLerp_Float3."""
        from pyresonitelink.dergflux import math as dm
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="ilerp")
        s.x = s.DoubleModelVar("x", value=4.0)
        s.v = s.Float3ModelVar("v")
        s.r = s.FloatModelVar("r")
        s.rv = s.Float3ModelVar("rv")
        with g.Under(slot):
            s.r = dm.inverse_lerp(2, 10, s.x)
            s.rv = dm.inverse_lerp(primitives.Float3(0, 0, 0), primitives.Float3(2, 4, 8), s.v)
        await _build(mock_client, g)
        m = mock_client

        scalar = m.find_one(r"ValueInverseLerp<double>")
        assert _dmvfs_type_arg(m.ref_target_type(scalar, "Value") or "") == "double"
        vector = m.find_one(_ct("InverseLerp_Float3"))
        assert _dmvfs_type_arg(m.ref_target_type(vector, "Value") or "") == "float3"


# =========================================================================
# Tests: actions that continue the flow, and slots as values
# =========================================================================


class TestVariableNamesBuild:
    """A variable's attribute name and its path may differ."""

    @pytest.mark.asyncio
    async def test_read_of_a_renamed_model_variable(self, mock_client: MockClient) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="names")
        s.v = s.FloatModelVar("velocity")
        with g.Under(slot):
            s.v = s.v + 1
        await _build(mock_client, g)
        m = mock_client

        add = m.find_one(r"ValueAdd<float>")
        assert _is_dmvfs(m.ref_target_type(add, "A") or "")
        assert any(sl.name == "velocity" for sl in m.slots.values())

    @pytest.mark.asyncio
    async def test_read_of_a_renamed_dynamic_variable(self, mock_client: MockClient) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="names")
        s.v = s.FloatDynVar("velocity")
        s.w = s.FloatDynVar("other")
        with g.Under(slot):
            s.w = s.v + 1
        await _build(mock_client, g)

        read = mock_client.find_one(r"ReadDynamicValueVariable<float>")
        assert mock_client.ref_target_comp(read, "Path") is not None


class TestContinuationBuild:
    """Statements after a raycast or a transform setter run after it."""

    @pytest.mark.asyncio
    async def test_statement_after_raycast_follows_both_branches(
        self, mock_client: MockClient,
    ) -> None:
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="ray")
        s.a = s.FloatModelVar("a")
        s.b = s.FloatModelVar("b")
        with g.Under(slot):
            with g.RaycastOne(origin=primitives.Float3(0, 1, 0),
                              direction=primitives.Float3(0, -1, 0)) as r:
                with r.on_hit():
                    s.a = r.hit_distance
            s.b = 2.0
        await _build(mock_client, g)
        m = mock_client

        ray = m.find_one(_ct("RaycastOne"))
        writes = m.find(r"ValueWrite<")
        write_a = m.ref_target_comp(ray, "OnHit")
        assert write_a is not None
        write_b = next(w for w in writes if w is not write_a)
        assert m.ref_target_comp(write_a, "OnWritten") is write_b
        assert m.ref_target_comp(ray, "OnMiss") is write_b

    @pytest.mark.asyncio
    async def test_set_global_position_is_a_statement(
        self, mock_client: MockClient,
    ) -> None:
        from pyresonitelink.dergflux import slots
        from pyresonitelink.dergflux import transform
        slot = workers.Slot(id="test-slot")
        ball = slots.ref(workers.Slot(id="ball"))
        g = Graph()
        s = g.Space(slot, space_name="move")
        s.done = s.BoolModelVar("done")
        with g.Under(slot):
            g.SetGlobalPosition(ball, transform.global_position(ball) + primitives.Float3(0, 1, 0))
            s.done = True
        await _build(mock_client, g)
        m = mock_client

        setter = m.find_one(_ct("SetGlobalPosition"))
        reference = m.find_one(r"RefObjectInput<\[FrooxEngine\]FrooxEngine\.Slot>")
        assert reference.references["Target"] == "ball"
        assert m.ref_target_comp(setter, "Instance") is reference
        assert m.ref_target_comp(setter, "Next") is m.find_one(r"ValueWrite<")
        # The GlobalTransform reads the same reference node.
        global_transform = m.find_one(_ct("GlobalTransform"))
        assert m.ref_target_comp(global_transform, "Instance") is reference

    @pytest.mark.asyncio
    async def test_slot_of_hit_collider(self, mock_client: MockClient) -> None:
        from pyresonitelink.dergflux import slots
        from pyresonitelink.dergflux import variables
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="hit")
        s.f = s.FloatModelVar("f")
        with g.Under(slot):
            with g.RaycastOne(origin=primitives.Float3(0, 1, 0),
                              direction=primitives.Float3(0, -1, 0),
                              ignore_hierarchy=workers.Slot(id="ball")) as r:
                with r.on_hit():
                    s.f = variables.read(
                        slots.of_component(r.hit_collider), "Physics/Friction",
                        primitives.Float,
                    ).value
        await _build(mock_client, g)
        m = mock_client

        ray = m.find_one(_ct("RaycastOne"))
        ignored = m.ref_target_comp(ray, "IgnoreHierarchy")
        assert ignored is not None and ignored.references["Target"] == "ball"
        cast = m.find_one(r"ObjectCast<")
        assert m.owner_of(cast.references["Input"]) == (ray.id, "HitCollider")
        get_slot = m.find_one(_ct("GetSlot"))
        assert m.ref_target_comp(get_slot, "Component") is cast
        read = m.find_one(r"ReadDynamicValueVariable<float>")
        assert m.ref_target_comp(read, "Source") is get_slot


# =========================================================================
# Tests: every math and time function builds, with real member names
# =========================================================================


def _member_names(component_class: type) -> set[str]:
    """Returns the member names that a generated component class reads.

    A parameterized class such as ValueLerp[Float] is created at runtime,
    so its generated base classes are searched.
    """
    import inspect

    names: set[str] = set()
    for klass in component_class.__mro__:
        if not klass.__module__.startswith("pyresonitelink.generated."):
            continue
        try:
            source = inspect.getsource(klass)
        except (OSError, TypeError):
            continue
        names.update(re.findall(r'get_member\("(\w+)"\)', source))
    return names


def _calls() -> list[tuple[str, Any]]:
    """Returns (id, call) pairs, where call(s) builds an expression from s.

    The space s has the model variables f (Float), d (Double), b (Bool),
    and v (Float3).
    """
    from pyresonitelink.dergflux import interaction
    from pyresonitelink.dergflux import math as dm
    from pyresonitelink.dergflux import mouse
    from pyresonitelink.dergflux import slots
    from pyresonitelink.dergflux import strings
    from pyresonitelink.dergflux import time
    from pyresonitelink.dergflux import transform
    from pyresonitelink.dergflux import users
    from pyresonitelink.dergflux import variables
    from pyresonitelink.generated.transform.interaction import grabbable

    one = [
        "acos", "asin", "atan", "ceil", "clamp01", "cos", "cube", "exp",
        "floor", "log", "log10", "one_minus", "reciprocal", "round_", "sign",
        "sin", "smootherstep", "smoothstep", "sqrt", "square", "tan",
        "to_double", "to_float", "to_int", "to_long",
    ]
    calls: list[tuple[str, Any]] = [
        (name, lambda s, fn=getattr(dm, name): fn(s.f)) for name in one
    ]
    calls += [
        ("atan2", lambda s: dm.atan2(s.f, s.f)),
        ("min_", lambda s: dm.min_(s.f, s.f)),
        ("max_", lambda s: dm.max_(s.f, s.f)),
        ("clamp", lambda s: dm.clamp(s.f, 0, 1)),
        ("conditional", lambda s: dm.conditional(s.b, s.f, s.f)),
        ("convert", lambda s: dm.convert(s.f, primitives.Int)),
        ("axis_angle", lambda s: dm.axis_angle(s.v, s.f)),
        ("from_euler", lambda s: dm.from_euler(s.v)),
        ("lerp", lambda s: dm.lerp(s.f, s.f, s.f)),
        ("lerp_unclamped", lambda s: dm.lerp_unclamped(s.v, s.v, s.f)),
        ("inverse_lerp", lambda s: dm.inverse_lerp(s.d, s.d, s.d)),
        ("inverse_lerp_vector", lambda s: dm.inverse_lerp(s.v, s.v, s.v)),
        ("smoothstep_edges", lambda s: dm.smoothstep(0, 1, s.d)),
        ("smootherstep_edges", lambda s: dm.smootherstep(0, 1, s.f)),
        ("power", lambda s: s.f ** 2),
        ("abs", lambda s: abs(s.f)),
        ("world_time", lambda s: time.world_time()),
        ("utc_now", lambda s: time.utc_now()),
        ("delta_time", lambda s: time.delta_time()),
        ("smooth_delta_time", lambda s: time.smooth_delta_time()),
        ("raw_delta_time", lambda s: time.raw_delta_time()),
        ("inverted_delta_time", lambda s: time.inverted_delta_time()),
        ("inverted_smooth_delta_time", lambda s: time.inverted_smooth_delta_time()),
        ("inverted_raw_delta_time", lambda s: time.inverted_raw_delta_time()),
        ("dot", lambda s: dm.dot(s.v, s.v)),
        ("cross", lambda s: dm.cross(s.v, s.v)),
        ("magnitude", lambda s: dm.magnitude(s.v)),
        ("normalized", lambda s: dm.normalized(s.v)),
        ("distance", lambda s: dm.distance(s.v, s.v)),
        ("pack", lambda s: dm.pack(s.f, 0, s.f)),
        ("element", lambda s: s.v.y),
        ("vector_times_float", lambda s: s.v * s.f),
        ("float_times_vector", lambda s: s.f * s.v),
        ("vector_over_float", lambda s: s.v / s.f),
        ("rotate", lambda s: dm.axis_angle(s.v, s.f) * s.v),
        ("global_position", lambda s: transform.global_position(slots.ref("ball"))),
        ("global_rotation", lambda s: transform.global_rotation(slots.ref("ball"))),
        ("global_point_to_local", lambda s: transform.global_point_to_local("ball", s.v)),
        ("local_point_to_global", lambda s: transform.local_point_to_global("ball", s.v)),
        ("global_direction_to_local", lambda s: transform.global_direction_to_local("ball", s.v)),
        ("local_direction_to_global", lambda s: transform.local_direction_to_global("ball", s.v)),
        ("dynamic_read", lambda s: variables.read(slots.ref("ball"), "P/x", primitives.Float).value),
        ("local_user_is_host", lambda s: users.local_user_is_host()),
        ("machine_id", lambda s: users.machine_id(users.local_user())),
        ("is_vr_active", lambda s: users.is_vr_active(users.local_user())),
        ("is_dash_open", lambda s: users.is_dash_open(users.local_user())),
        ("view_position", lambda s: users.view_position()),
        ("view_rotation", lambda s: users.view_rotation()),
        ("string_equals", lambda s: users.machine_id(users.local_user()) == ""),
        ("string_not_equals", lambda s: users.machine_id(users.local_user()) != ""),
        ("is_grabbed", lambda s: interaction.is_grabbed(_added(grabbable.Grabbable()))),
        ("to_string", lambda s: strings.to_string(s.v)),
        ("concatenate", lambda s: "y=" + strings.to_string(s.f)),
        ("slot_of_component", lambda s: variables.read(
            slots.of_component(_added(grabbable.Grabbable())), "P/x", primitives.Float,
        ).found),
    ]
    calls += [
        (name, lambda s, fn=getattr(mouse, name): fn())
        for name in [
            "left_pressed", "left_held", "left_released",
            "right_pressed", "right_held", "right_released", "scroll_delta",
        ]
    ]
    return calls


def _added(component: Any) -> Any:
    """Gives a component an ID, as if it had been added to a slot."""
    component._component.id = "added-component"
    return component


class TestFunctionAudit:
    """Each Dergflux math and time function builds, and wires real members.

    A function with no builder entry raises TypeError when built, and a
    reference to a member the node class doesn't have fails the check in
    _create_and_wire. The server ignores a reference to an unknown member,
    so neither mistake shows up otherwise.
    """

    @pytest.mark.asyncio
    @pytest.mark.parametrize("call", [c for _, c in _calls()], ids=[n for n, _ in _calls()])
    async def test_builds_with_real_members(
        self, mock_client: MockClient, monkeypatch: pytest.MonkeyPatch, call: Any,
    ) -> None:
        from pyresonitelink.dergflux import _types

        original = _builder._create_and_wire

        async def checked(
            resolink: Any, slot: Any, component_class: Any,
            references: dict[str, str], debug: bool = False,
        ) -> Any:
            unknown = set(references) - _member_names(component_class)
            assert not unknown, (
                f"{component_class.__name__} has no member {sorted(unknown)}"
            )
            return await original(resolink, slot, component_class, references, debug=debug)

        monkeypatch.setattr(_builder, "_create_and_wire", checked)
        slot = workers.Slot(id="test-slot")
        g = Graph()
        s = g.Space(slot, space_name="audit")
        s.f = s.FloatModelVar("f", value=0.5)
        s.d = s.DoubleModelVar("d", value=0.5)
        s.b = s.BoolModelVar("b", value=True)
        s.v = s.Float3ModelVar("v")
        result = call(s)
        type_name = _types.type_name(result._node._type)
        s.r = getattr(s, f"{type_name}ModelVar")("r")
        with g.Under(slot):
            s.r = result
        await _build(mock_client, g)
