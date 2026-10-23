"""Unit tests for the methods of pyresonitelink.data.workers classes."""

from pyresonitelink.data import workers
from tests import fake_scene


class TestRemoveChildrenNamed:
    async def test_removes_only_direct_children_with_the_exact_name(self) -> None:
        fake = fake_scene.FakeClient((
            fake_scene.make_slot("a", "Example"),
            fake_scene.make_slot("b", "Example 2"),
            fake_scene.make_slot("c", "Other", children=(fake_scene.make_slot("d", "Example"),)),
            fake_scene.make_slot("e", "Example"),
        ))
        root = workers.Slot(id=workers.Slot.ROOT_SLOT_ID)
        removed = await root.remove_children_named(fake, "Example")  # type: ignore[arg-type]
        assert removed == ["a", "e"]
        assert fake.removed == ["a", "e"]

    async def test_no_match(self) -> None:
        fake = fake_scene.FakeClient((fake_scene.make_slot("a", "Other"),))
        root = workers.Slot(id=workers.Slot.ROOT_SLOT_ID)
        assert await root.remove_children_named(fake, "Example") == []  # type: ignore[arg-type]
        assert fake.removed == []

    async def test_uses_the_server_children_not_the_local_data(self) -> None:
        fake = fake_scene.FakeClient((fake_scene.make_slot("a", "Example"),))
        # The local data lists a different child, which isn't on the server.
        root = workers.Slot(
            id=workers.Slot.ROOT_SLOT_ID, children=[fake_scene.make_slot("stale", "Example")],
        )
        assert await root.remove_children_named(fake, "Example") == ["a"]  # type: ignore[arg-type]
