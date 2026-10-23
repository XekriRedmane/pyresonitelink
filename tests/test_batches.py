"""Tests for utils.batches."""

import math
from typing import Any

import pytest

from pyresonitelink.data import messages
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import transforms
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.utils import batches


class FakeClient:
    """Records the batches it is sent, and refuses operations whose index is in fail."""

    def __init__(self, fail: set[int] | None = None) -> None:
        self.batches: list[list[messages.Message]] = []
        self.fail = fail or set()

    async def data_model_operation_batch(self, operations: list[Any]) -> Any:
        offset = sum(len(b) for b in self.batches)
        self.batches.append(list(operations))
        return responses.BatchResponse(success=True, responses=[
            responses.Response(success=(offset + i) not in self.fail, errorInfo="no")
            for i in range(len(operations))
        ])


class TestSceneBatch:

    @pytest.mark.asyncio
    async def test_later_additions_refer_to_earlier_ones(self) -> None:
        fake = FakeClient()
        batch = batches.SceneBatch(fake)  # type: ignore[arg-type]
        slot = batch.add_slot("Root", "Box", position=(1, 2, 3))
        mesh = batch.add_component(slot, box_mesh.BoxMesh(size=primitives.Float3(1, 1, 1)))
        renderer = batch.add_renderer(slot, mesh, ["material"])
        await batch.flush()

        add_slot, add_mesh, add_renderer = fake.batches[0]
        assert isinstance(add_slot, messages.AddSlot)
        assert add_slot.data.id == slot
        assert add_slot.data.parent.targetId == "Root"
        assert isinstance(add_mesh, messages.AddComponent)
        assert add_mesh.containerSlotId == slot and add_mesh.data.id == mesh
        assert isinstance(add_renderer, messages.AddComponent)
        assert add_renderer.data.id == renderer
        assert add_renderer.data.members["Mesh"].targetId == mesh
        assert [e.targetId for e in add_renderer.data.members["Materials"].elements] == ["material"]
        assert batch.operations == []

    @pytest.mark.asyncio
    async def test_splits_into_messages(self) -> None:
        fake = FakeClient()
        batch = batches.SceneBatch(fake)  # type: ignore[arg-type]
        for i in range(batches.MAX_OPERATIONS + 1):
            batch.add_slot("Root", f"S{i}")
        await batch.flush()
        assert [len(b) for b in fake.batches] == [batches.MAX_OPERATIONS, 1]

    @pytest.mark.asyncio
    async def test_failure_raises(self) -> None:
        fake = FakeClient(fail={1})
        batch = batches.SceneBatch(fake)  # type: ignore[arg-type]
        batch.add_slot("Root", "A")
        batch.add_slot("Root", "B")
        with pytest.raises(RuntimeError, match="1 of 2"):
            await batch.flush()


class TestEuler:

    def test_single_axes_match_axis_rotations(self) -> None:
        q = batches.euler(y=90)
        v = transforms.rotate(q, primitives.Float3(0, 0, 1))
        assert math.isclose(float(v.x), 1, abs_tol=1e-6) and math.isclose(float(v.z), 0, abs_tol=1e-6)

    def test_matches_floatq_euler(self) -> None:
        # floatQ.EulerRad, from the decompiled Elements.Core.
        x, y, z = 30.0, -70.0, 115.0
        hx, hy, hz = (math.radians(a) / 2 for a in (x, y, z))
        sx, sy, sz = math.sin(hx), math.sin(hy), math.sin(hz)
        cx, cy, cz = math.cos(hx), math.cos(hy), math.cos(hz)
        expected = (cy * sx * cz + sy * cx * sz, sy * cx * cz - cy * sx * sz,
                    cy * cx * sz - sy * sx * cz, cy * cx * cz + sy * sx * sz)
        q = batches.euler(x, y, z)
        for got, want in zip((q.x, q.y, q.z, q.w), expected):
            assert math.isclose(float(got), want, abs_tol=1e-6)
