"""Unit tests for pyresonitelink.utils.placement, against a fake client."""

import math

import pytest

from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.utils import placement
from tests import fake_scene


def _user(user_id: str, head_id: str = "head") -> workers.Slot:
    """Returns a user root slot whose children include a head."""
    return fake_scene.make_slot(
        user_id, "User", (placement.USER_ROOT_TYPE,),
        children=(fake_scene.make_slot("hands", "Hands"), fake_scene.make_slot(head_id, "Head")),
    )


class TestFindHead:
    async def test_returns_the_first_users_head(self) -> None:
        fake = fake_scene.FakeClient((fake_scene.make_slot("other", "Light", ("[FrooxEngine]FrooxEngine.Light",)),
                           _user("user1", "head1"), _user("user2", "head2")))
        assert await placement.find_head(fake) == "head1"  # type: ignore[arg-type]

    async def test_no_user_root(self) -> None:
        fake = fake_scene.FakeClient((fake_scene.make_slot("other", "Light"),))
        with pytest.raises(LookupError, match="UserRoot"):
            await placement.find_head(fake)  # type: ignore[arg-type]

    async def test_no_head(self) -> None:
        fake = fake_scene.FakeClient((fake_scene.make_slot("user", "User", (placement.USER_ROOT_TYPE,)),))
        with pytest.raises(LookupError, match="no Head"):
            await placement.find_head(fake)  # type: ignore[arg-type]


class TestInFrontOfHead:
    @pytest.fixture
    def fake(self) -> fake_scene.FakeClient:
        """A user whose head is at (1, 2, 3), turned 90 degrees about Y.

        That turn takes the head's forward axis, +Z, to +X.
        """
        fake = fake_scene.FakeClient((_user("user"),))
        s = math.sqrt(0.5)
        fake.world["head"] = transforms.Transform(
            primitives.Float3(1, 2, 3), primitives.FloatQ(0, s, 0, s),
        )
        return fake

    async def test_position_is_along_the_heads_forward_axis(self, fake: fake_scene.FakeClient) -> None:
        world = await placement.in_front_of_head(fake, 2.0)  # type: ignore[arg-type]
        assert fake_scene.close(world.position, (3, 2, 3))
        assert fake_scene.close(transforms.rotate(world.rotation, primitives.Float3(0, 0, 1)), (1, 0, 0))
        assert fake_scene.close(world.scale, (1, 1, 1))

    async def test_half_turn_faces_the_head(self, fake: fake_scene.FakeClient) -> None:
        world = await placement.in_front_of_head(
            fake, 2.0, turn=placement.HALF_TURN, scale=0.5,  # type: ignore[arg-type]
        )
        assert fake_scene.close(world.position, (3, 2, 3))
        # +Z now points from the transform back toward the head.
        assert fake_scene.close(transforms.rotate(world.rotation, primitives.Float3(0, 0, 1)), (-1, 0, 0))
        assert fake_scene.close(world.scale, (0.5, 0.5, 0.5))
