"""Unit tests for pyresonitelink.utils.rendering, against a fake client."""

from typing import Any

import numpy as np
import pytest

from pyresonitelink.data import members
from pyresonitelink.data import mesh
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.utils import glb
from pyresonitelink.utils import rendering


class FakeClient:
    """Records components, updates, and mesh imports.

    get_component returns the data a component was added with, plus an
    empty Materials list for a MeshRenderer, as the server does.

    Attributes:
        components (dict[str, workers.Component]): The added components,
            by ID.
        slot_of (dict[str, str]): The slot ID of each added component.
        updates (list[workers.Component]): The data of each
            update_component call.
        imports (list[dict[str, Any]]): The arguments of each
            import_mesh_raw_data call.
    """

    def __init__(self) -> None:
        self.components: dict[str, workers.Component] = {}
        self.slot_of: dict[str, str] = {}
        self.updates: list[workers.Component] = []
        self.imports: list[dict[str, Any]] = []

    async def add_component(
        self, containerSlotId: str, data: workers.Component, debug: bool = False,
    ) -> responses.NewEntityId:
        """Stores the component under a new ID."""
        component_id = f"comp-{len(self.components) + 1}"
        component_members = dict(data.members)
        if (data.componentType or "").endswith("MeshRenderer"):
            component_members["Materials"] = members.SyncList(id=f"{component_id}-materials")
        self.components[component_id] = workers.Component(
            id=component_id, componentType=data.componentType, members=component_members,
        )
        self.slot_of[component_id] = containerSlotId
        return responses.NewEntityId(success=True, entityId=component_id)

    async def get_component(
        self, componentId: str, debug: bool = False,
    ) -> responses.ComponentData:
        """Returns the stored component."""
        return responses.ComponentData(success=True, data=self.components[componentId])

    async def update_component(
        self, data: workers.Component, debug: bool = False,
    ) -> responses.Response:
        """Records the update."""
        self.updates.append(data)
        return responses.Response(success=True)

    async def import_mesh_raw_data(
        self, positions: np.ndarray, submeshes: list[mesh.RawTriangles], **kwargs: Any,
    ) -> responses.AssetData:
        """Records the import and returns an asset URL."""
        self.imports.append(dict(positions=positions, submeshes=submeshes, **kwargs))
        return responses.AssetData(success=True, assetURL=f"local://mesh-{len(self.imports)}")

    def of_type(self, suffix: str) -> list[workers.Component]:
        """Returns the added components whose type ends with suffix."""
        return [c for c in self.components.values() if (c.componentType or "").endswith(suffix)]


def _mesh(submesh_count: int, uvs: bool) -> glb.Mesh:
    """Returns a mesh of one triangle per submesh."""
    count = 3 * submesh_count
    return glb.Mesh(
        positions=np.arange(count * 3, dtype=np.float32).reshape(count, 3),
        normals=np.tile(np.array([0, 0, 1], dtype=np.float32), (count, 1)),
        uvs=np.zeros((count, 2), dtype=np.float32) if uvs else None,
        submeshes=[np.array([[3 * i, 3 * i + 1, 3 * i + 2]], dtype=np.int32)
                   for i in range(submesh_count)],
    )


async def _materials(fake: FakeClient, count: int) -> list[pbs_metallic.PBS_Metallic]:
    """Adds materials to a slot and returns them."""
    result = []
    for _ in range(count):
        material = pbs_metallic.PBS_Metallic()
        await material.add_to_slot(fake, "slot")  # type: ignore[arg-type]
        result.append(material)
    return result


def _material_targets(update: workers.Component) -> list[str | None]:
    """Returns the material IDs in a renderer update, in order."""
    materials = update.members["Materials"]
    assert isinstance(materials, members.SyncList)
    return [e.targetId for e in materials.elements if isinstance(e, members.Reference)]


class TestAddRenderer:
    async def test_sets_one_material_per_submesh_in_order(self) -> None:
        fake = FakeClient()
        box = box_mesh.BoxMesh()
        await box.add_to_slot(fake, "slot")  # type: ignore[arg-type]
        a, b = await _materials(fake, 2)
        renderer = await rendering.add_renderer(fake, "slot", box, [a, b, a])  # type: ignore[arg-type]
        (update,) = fake.updates
        assert update.id == renderer.id
        assert _material_targets(update) == [a.id, b.id, a.id]
        assert renderer.mesh == box.id
        assert fake.slot_of[renderer.id or ""] == "slot"

    async def test_no_materials_sends_no_update(self) -> None:
        fake = FakeClient()
        box = box_mesh.BoxMesh()
        await box.add_to_slot(fake, "slot")  # type: ignore[arg-type]
        await rendering.add_renderer(fake, "slot", box, [])  # type: ignore[arg-type]
        assert fake.updates == []

    async def test_material_not_added_yet(self) -> None:
        fake = FakeClient()
        box = box_mesh.BoxMesh()
        await box.add_to_slot(fake, "slot")  # type: ignore[arg-type]
        with pytest.raises(AssertionError, match="Add each material"):
            await rendering.add_renderer(
                fake, "slot", box, [pbs_metallic.PBS_Metallic()],  # type: ignore[arg-type]
            )


class TestAddMesh:
    async def test_imports_the_mesh_and_shows_it(self) -> None:
        fake = FakeClient()
        m = _mesh(2, uvs=True)
        a, b = await _materials(fake, 2)
        renderer = await rendering.add_mesh(fake, "slot", m, [a, b])  # type: ignore[arg-type]
        (imported,) = fake.imports
        assert imported["positions"] is m.positions
        assert imported["normals"] is m.normals
        assert len(imported["uvs"]) == 1 and imported["uvs"][0] is m.uvs
        assert [s.indices.tolist() for s in imported["submeshes"]] == [[[0, 1, 2]], [[3, 4, 5]]]
        (static,) = fake.of_type("StaticMesh")
        url = static.members["URL"]
        assert getattr(url, "value", None) == "local://mesh-1"
        assert renderer.mesh == static.id
        assert _material_targets(fake.updates[-1]) == [a.id, b.id]

    async def test_mesh_without_uvs(self) -> None:
        fake = FakeClient()
        (a,) = await _materials(fake, 1)
        await rendering.add_mesh(fake, "slot", _mesh(1, uvs=False), [a])  # type: ignore[arg-type]
        assert list(fake.imports[0]["uvs"]) == []

    async def test_material_count_must_match(self) -> None:
        fake = FakeClient()
        (a,) = await _materials(fake, 1)
        with pytest.raises(ValueError, match="1 materials for 2 submeshes"):
            await rendering.add_mesh(fake, "slot", _mesh(2, uvs=False), [a])  # type: ignore[arg-type]
        assert fake.imports == []
