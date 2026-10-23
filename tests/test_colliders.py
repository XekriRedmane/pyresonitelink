"""Unit tests for pyresonitelink.utils.colliders, against a fake client."""

import numpy as np
import pytest

from pyresonitelink.data import fields
from pyresonitelink.utils import colliders
from pyresonitelink.utils import glb
from tests.test_rendering import FakeClient


def _mesh(positions: list[list[float]]) -> glb.Mesh:
    """Returns a mesh with the given vertices and no triangles."""
    array = np.array(positions, dtype=np.float32).reshape(-1, 3)
    return glb.Mesh(positions=array, normals=np.zeros_like(array))


class TestAddBoundingBox:
    async def test_centers_a_box_the_size_of_the_bounds(self) -> None:
        fake = FakeClient()
        m = _mesh([[1, 2, 3], [3, 2, 4], [2, 6, 3]])
        slot = await colliders.add_bounding_box(fake, "parent", m, name="Handle")  # type: ignore[arg-type]
        (added,) = fake.slots
        assert added["parent"] == "parent" and added["name"] == "Handle"
        np.testing.assert_allclose(added["position"], [2, 4, 3.5])
        (collider,) = fake.of_type("BoxCollider")
        assert fake.slot_of[collider.id or ""] == slot.id
        size = collider.members["Size"]
        assert isinstance(size, fields.FieldFloat3)
        np.testing.assert_allclose([size.value.x, size.value.y, size.value.z], [2, 4, 1])

    async def test_no_vertices(self) -> None:
        fake = FakeClient()
        with pytest.raises(ValueError, match="no vertices"):
            await colliders.add_bounding_box(fake, "parent", _mesh([]), name="Handle")  # type: ignore[arg-type]
        assert fake.slots == []
