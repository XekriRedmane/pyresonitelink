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


class TestOnFloorInFrontOfHead:
    @pytest.fixture
    def fake(self) -> fake_scene.FakeClient:
        """A user standing at (1, 0.5, 3), whose head looks along +X and down.

        The head is turned 90 degrees about Y, which takes its forward axis
        to +X, and then pitched 30 degrees down about its own X axis.
        """
        fake = fake_scene.FakeClient((_user("user"),))
        s = math.sqrt(0.5)
        pitch = math.radians(30)
        fake.world["user"] = transforms.Transform(primitives.Float3(1, 0.5, 3))
        fake.world["head"] = transforms.Transform(
            primitives.Float3(1, 2.2, 3),
            transforms.multiply(
                primitives.FloatQ(0, s, 0, s),
                primitives.FloatQ(math.sin(pitch / 2), 0, 0, math.cos(pitch / 2)),
            ),
        )
        return fake

    async def test_is_at_the_feet_height_along_the_flattened_view(
        self, fake: fake_scene.FakeClient,
    ) -> None:
        world = await placement.on_floor_in_front_of_head(fake, 2.0)  # type: ignore[arg-type]
        assert fake_scene.close(world.position, (3, 0.5, 3))
        assert fake_scene.close(transforms.rotate(world.rotation, primitives.Float3(0, 0, 1)), (1, 0, 0))
        assert fake_scene.close(transforms.rotate(world.rotation, primitives.Float3(0, 1, 0)), (0, 1, 0))

    async def test_straight_down_raises(self, fake: fake_scene.FakeClient) -> None:
        s = math.sqrt(0.5)
        fake.world["head"] = transforms.Transform(
            primitives.Float3(1, 2.2, 3), primitives.FloatQ(s, 0, 0, s),
        )
        with pytest.raises(ValueError, match="straight up or down"):
            await placement.on_floor_in_front_of_head(fake, 2.0)  # type: ignore[arg-type]
