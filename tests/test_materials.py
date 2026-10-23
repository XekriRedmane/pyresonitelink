"""Unit tests for pyresonitelink.utils.materials, against a fake client."""

import numpy as np

from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.utils import materials


class FakeClient:
    """Records added components.

    Attributes:
        added (list[tuple[str, workers.Component]]): The slot ID and data of
            each add_component call.
    """

    def __init__(self) -> None:
        self.added: list[tuple[str, workers.Component]] = []

    async def add_component(
        self, containerSlotId: str, data: workers.Component, debug: bool = False,
    ) -> responses.NewEntityId:
        """Records the component and returns a new ID."""
        self.added.append((containerSlotId, data))
        return responses.NewEntityId(success=True, entityId=f"comp-{len(self.added)}")

    async def get_component(
        self, componentId: str, debug: bool = False,
    ) -> responses.ComponentData:
        """Returns the data the component was added with."""
        _, data = self.added[int(componentId.removeprefix("comp-")) - 1]
        return responses.ComponentData(
            success=True,
            data=workers.Component(
                id=componentId, componentType=data.componentType, members=dict(data.members),
            ),
        )


def _close(color: primitives.ColorX | None, rgba: tuple[float, ...]) -> bool:
    """Returns whether a color is linear and has the given components."""
    assert color is not None
    assert color.profile == "Linear"
    return bool(np.allclose([color.r, color.g, color.b, color.a], rgba))


class TestFinish:
    def test_material_has_the_settings(self) -> None:
        finish = materials.Finish(
            (0.25, 0.5, 0.75), metallic=0.3, smoothness=0.6, emissive=(0.1, 0.2, 0.3),
        )
        material = finish.material()
        assert material.id is None
        assert _close(material.albedo_color, (0.25, 0.5, 0.75, 1))
        assert _close(material.emissive_color, (0.1, 0.2, 0.3, 1))
        assert material.metallic == np.float32(0.3)
        assert material.smoothness == np.float32(0.6)

    def test_emissive_defaults_to_black(self) -> None:
        material = materials.Finish((1, 1, 1), metallic=0, smoothness=0).material()
        assert _close(material.emissive_color, (0, 0, 0, 1))


class TestAddMaterials:
    async def test_adds_one_material_per_entry(self) -> None:
        fake = FakeClient()
        table = {
            "Paint": materials.Finish((0.5, 0, 0), metallic=0.2, smoothness=0.4),
            "Chrome": materials.Finish((0.6, 0.6, 0.6), metallic=0.9, smoothness=0.8),
        }
        mats = await materials.add_materials(fake, "slot", table)  # type: ignore[arg-type]
        assert list(mats) == ["Paint", "Chrome"]
        assert [slot for slot, _ in fake.added] == ["slot", "slot"]
        assert [m.id for m in mats.values()] == ["comp-1", "comp-2"]
        assert mats["Chrome"].metallic == np.float32(0.9)
        assert _close(mats["Paint"].albedo_color, (0.5, 0, 0, 1))
