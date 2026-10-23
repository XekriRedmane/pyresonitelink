"""Unit tests for the transforms module."""

# pylint: disable=missing-function-docstring,missing-class-docstring

import math

import numpy as np
import pytest

from pyresonitelink.data import primitives
from pyresonitelink.data import transforms


def _axis_angle(axis: tuple[float, float, float], degrees: float) -> primitives.FloatQ:
    """Returns the rotation by the given angle around a unit axis."""
    half = math.radians(degrees) / 2
    s = math.sin(half)
    return primitives.FloatQ(axis[0] * s, axis[1] * s, axis[2] * s, math.cos(half))


def _assert_vector(actual: primitives.Float3, expected: tuple[float, float, float]) -> None:
    np.testing.assert_allclose([actual.x, actual.y, actual.z], expected, atol=1e-6)


def _assert_rotation(actual: primitives.FloatQ, expected: primitives.FloatQ) -> None:
    # q and -q are the same rotation.
    a = np.array([actual.x, actual.y, actual.z, actual.w])
    e = np.array([expected.x, expected.y, expected.z, expected.w])
    if np.dot(a, e) < 0:
        a = -a
    np.testing.assert_allclose(a, e, atol=1e-6)


FORWARD = primitives.Float3(0, 0, 1)
Y_90 = _axis_angle((0, 1, 0), 90)
X_90 = _axis_angle((1, 0, 0), 90)


class TestRotate:

    def test_identity(self) -> None:
        _assert_vector(transforms.rotate(primitives.FloatQ(), FORWARD), (0, 0, 1))

    def test_around_y(self) -> None:
        # Turning right by 90 degrees points forward along +X.
        _assert_vector(transforms.rotate(Y_90, FORWARD), (1, 0, 0))

    def test_around_x(self) -> None:
        # Pitching by 90 degrees around +X points forward down.
        _assert_vector(transforms.rotate(X_90, FORWARD), (0, -1, 0))


class TestTwistAngle:

    def test_rotation_about_the_axis(self) -> None:
        z = primitives.Float3(0, 0, 1)
        assert transforms.twist_angle(_axis_angle((0, 0, 1), 30), z) == pytest.approx(30, abs=1e-4)
        assert transforms.twist_angle(_axis_angle((0, 0, 1), -170), z) == pytest.approx(-170, abs=1e-4)

    def test_wraps_to_half_a_turn(self) -> None:
        z = primitives.Float3(0, 0, 1)
        assert transforms.twist_angle(_axis_angle((0, 0, 1), 190), z) == pytest.approx(-170, abs=1e-4)

    def test_opposite_axis_negates(self) -> None:
        minus_z = primitives.Float3(0, 0, -2)
        assert transforms.twist_angle(_axis_angle((0, 0, 1), 30), minus_z) == pytest.approx(-30, abs=1e-4)

    def test_ignores_a_swing_after_the_twist(self) -> None:
        # A tilt about X applied after a 40 degree turn about Z.
        q = transforms.multiply(_axis_angle((1, 0, 0), 25), _axis_angle((0, 0, 1), 40))
        assert transforms.twist_angle(q, primitives.Float3(0, 0, 1)) == pytest.approx(40, abs=1e-4)

    def test_zero_axis(self) -> None:
        with pytest.raises(ValueError, match="zero vector"):
            transforms.twist_angle(Y_90, primitives.Float3(0, 0, 0))


class TestMultiply:

    def test_identity(self) -> None:
        _assert_rotation(transforms.multiply(primitives.FloatQ(), Y_90), Y_90)

    def test_same_axis_adds_angles(self) -> None:
        _assert_rotation(transforms.multiply(Y_90, Y_90), _axis_angle((0, 1, 0), 180))

    def test_applies_right_operand_first(self) -> None:
        # X_90 points forward down, and then Y_90 leaves down unchanged.
        q = transforms.multiply(Y_90, X_90)
        _assert_vector(transforms.rotate(q, FORWARD), (0, -1, 0))
        # Y_90 points forward along +X, and then X_90 leaves +X unchanged.
        q = transforms.multiply(X_90, Y_90)
        _assert_vector(transforms.rotate(q, FORWARD), (1, 0, 0))


class TestInverse:

    def test_undoes_rotation(self) -> None:
        q = _axis_angle((0.6, 0.0, 0.8), 37)
        _assert_rotation(transforms.multiply(q, transforms.inverse(q)), primitives.FloatQ())

    def test_zero_quaternion(self) -> None:
        with pytest.raises(ValueError):
            transforms.inverse(primitives.FloatQ(0, 0, 0, 0))


class TestCompose:

    def test_identity_parent(self) -> None:
        local = transforms.Transform(primitives.Float3(1, 2, 3), Y_90, primitives.Float3(4, 5, 6))
        result = transforms.compose(transforms.Transform(), local)
        _assert_vector(result.position, (1, 2, 3))
        _assert_rotation(result.rotation, Y_90)
        _assert_vector(result.scale, (4, 5, 6))

    def test_parent_rotates_and_scales_child_position(self) -> None:
        parent = transforms.Transform(primitives.Float3(1, 2, 3), Y_90, primitives.Float3(2, 2, 2))
        local = transforms.Transform(primitives.Float3(0, 0, 1), X_90, primitives.Float3(1, 1, 1))
        result = transforms.compose(parent, local)
        # The child's offset of 1 along +Z is doubled and turned to +X.
        _assert_vector(result.position, (3, 2, 3))
        _assert_rotation(result.rotation, transforms.multiply(Y_90, X_90))
        _assert_vector(result.scale, (2, 2, 2))


class TestRelativeTo:

    def test_inverts_compose(self) -> None:
        rng = np.random.default_rng(1)
        for _ in range(20):
            q = rng.normal(size=4)
            q /= np.linalg.norm(q)
            parent = transforms.Transform(
                primitives.Float3(*rng.uniform(-10, 10, size=3)),
                primitives.FloatQ(*q),
                primitives.Float3(*([rng.uniform(0.5, 3)] * 3)),
            )
            q = rng.normal(size=4)
            q /= np.linalg.norm(q)
            world = transforms.Transform(
                primitives.Float3(*rng.uniform(-10, 10, size=3)),
                primitives.FloatQ(*q),
                primitives.Float3(*rng.uniform(0.5, 3, size=3)),
            )
            result = transforms.compose(parent, transforms.relative_to(parent, world))
            p = world.position
            s = world.scale
            np.testing.assert_allclose(
                [result.position.x, result.position.y, result.position.z],
                [p.x, p.y, p.z], atol=1e-4,
            )
            _assert_rotation(result.rotation, world.rotation)
            np.testing.assert_allclose(
                [result.scale.x, result.scale.y, result.scale.z],
                [s.x, s.y, s.z], atol=1e-5,
            )

    def test_zero_parent_scale(self) -> None:
        parent = transforms.Transform(scale=primitives.Float3(1, 0, 1))
        with pytest.raises(ValueError):
            transforms.relative_to(parent, transforms.Transform())
