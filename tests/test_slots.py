"""Unit tests for pyresonitelink.utils.slots, against a fake client."""

from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.utils import slots
from tests import fake_scene


class TestAddSlotAt:
    async def test_converts_to_the_parents_space(self) -> None:
        parent = fake_scene.make_slot("parent", "Parent")
        fake = fake_scene.FakeClient((parent,))
        fake.world["parent"] = transforms.Transform(
            primitives.Float3(10, 0, 0), scale=primitives.Float3(2, 2, 2),
        )
        world = transforms.Transform(primitives.Float3(12, 4, 0), scale=primitives.Float3(2, 2, 2))
        slot = await slots.add_slot_at(fake, world, name="Thing", parent=parent)  # type: ignore[arg-type]
        assert slot.id == "new-1"
        (added,) = fake.added
        assert added["parent"] is parent
        assert added["name"] == "Thing"
        assert fake_scene.close(added["position"], (1, 2, 0))
        assert fake_scene.close(added["scale"], (1, 1, 1))

    async def test_parent_defaults_to_root(self) -> None:
        fake = fake_scene.FakeClient()
        await slots.add_slot_at(fake, transforms.Transform(), name="Thing")  # type: ignore[arg-type]
        assert fake.added[0]["parent"] == workers.Slot.ROOT_SLOT_ID
