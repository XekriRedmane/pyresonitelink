"""Arithmetic on slot transforms.

A slot's position, rotation, and scale are relative to its parent slot. The
functions here convert between that local transform and the transform
relative to an ancestor, such as Root.

Terminology:

- A rotation is a unit quaternion (x, y, z, w). Rotating a vector v by q
  gives the vector part of q * (v, 0) * conjugate(q), where * is the
  Hamilton product.
- Resonite's axes are +X right, +Y up, and +Z forward. The coordinate
  system is left-handed, but the quaternion arithmetic is the same as in a
  right-handed one.

All arithmetic is done in float64, and the results are rounded to the
float32 components of Float3 and FloatQ.
"""

from dataclasses import dataclass, field

import numpy as np

from . import primitives


def _vector(v: primitives.Float3) -> np.ndarray:
    """Returns the components of a Float3 as a float64 array."""
    return np.array([v.x, v.y, v.z], dtype=np.float64)


def _quaternion(q: primitives.FloatQ) -> np.ndarray:
    """Returns the components of a FloatQ as a float64 (x, y, z, w) array."""
    return np.array([q.x, q.y, q.z, q.w], dtype=np.float64)


def _hamilton(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Returns the Hamilton product a * b of two (x, y, z, w) arrays."""
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return np.array([
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
        aw * bw - ax * bx - ay * by - az * bz,
    ])


def _rotate(q: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Returns the 3-element array v rotated by the unit quaternion array q."""
    conjugate = np.array([-q[0], -q[1], -q[2], q[3]])
    return _hamilton(_hamilton(q, np.append(v, 0.0)), conjugate)[:3]


def _inverse(q: np.ndarray) -> np.ndarray:
    """Returns the inverse of the quaternion array q.

    Raises:
        ValueError: q is the zero quaternion, which has no inverse.
    """
    norm_squared = float(np.dot(q, q))
    if norm_squared == 0.0:
        raise ValueError("The zero quaternion has no inverse.")
    return np.array([-q[0], -q[1], -q[2], q[3]]) / norm_squared


def _to_float3(v: np.ndarray) -> primitives.Float3:
    """Returns a 3-element array as a Float3."""
    return primitives.Float3(float(v[0]), float(v[1]), float(v[2]))


def _to_floatq(q: np.ndarray) -> primitives.FloatQ:
    """Returns an (x, y, z, w) array as a FloatQ."""
    return primitives.FloatQ(float(q[0]), float(q[1]), float(q[2]), float(q[3]))


def multiply(a: primitives.FloatQ, b: primitives.FloatQ) -> primitives.FloatQ:
    """Returns the rotation that applies b first and then a.

    That is, the Hamilton product a * b.
    """
    return _to_floatq(_hamilton(_quaternion(a), _quaternion(b)))


def inverse(q: primitives.FloatQ) -> primitives.FloatQ:
    """Returns the rotation that undoes q.

    Raises:
        ValueError: q is the zero quaternion, which has no inverse.
    """
    return _to_floatq(_inverse(_quaternion(q)))


def rotate(q: primitives.FloatQ, v: primitives.Float3) -> primitives.Float3:
    """Returns the vector v rotated by the unit quaternion q.

    For example, rotate(rotation, Float3(0, 0, 1)) is the forward direction
    of a slot with that rotation.
    """
    return _to_float3(_rotate(_quaternion(q), _vector(v)))


def twist_angle(q: primitives.FloatQ, axis: primitives.Float3) -> float:
    """Returns the angle in degrees by which a rotation turns about an axis.

    The rotation is split into a twist about the axis followed by a swing
    that tilts the axis, and the twist's angle is returned, from -180 to 180.
    For a rotation about the axis alone, such as a wheel's on its shaft,
    that is the rotation's own angle. That is, if q is the rotation by a
    degrees about axis, the result is a, wrapped to -180 to 180.

    The angle has the sign of a rotation built from the same axis and
    angle, e.g. by Resonite's floatQ.AxisAngle. In Resonite's left-handed
    coordinates, a positive angle looks counterclockwise to someone looking
    along the axis.

    Raises:
        ValueError: axis is the zero vector.
    """
    a = _vector(axis)
    length = float(np.linalg.norm(a))
    if length == 0.0:
        raise ValueError("The zero vector has no direction to turn about.")
    quaternion = _quaternion(q)
    # The twist is the quaternion's vector part projected onto the axis,
    # together with its scalar part.
    along = float(np.dot(quaternion[:3], a / length))
    angle = np.degrees(2 * np.arctan2(along, quaternion[3]))
    return float((angle + 180.0) % 360.0 - 180.0)


@dataclass
class Transform:
    """Represents a slot's position, rotation, and scale.

    The default is the identity transform.
    """

    position: primitives.Float3 = field(default_factory=primitives.Float3)
    rotation: primitives.FloatQ = field(default_factory=primitives.FloatQ)
    scale: primitives.Float3 = field(
        default_factory=lambda: primitives.Float3(1, 1, 1),
    )


def compose(parent: Transform, local: Transform) -> Transform:
    """Returns a child's transform in the space its parent is expressed in.

    A point at p in a slot's own space is at
    position + rotate(rotation, scale * p) in its parent's space, where *
    is the component-wise product. Composing applies the child's transform
    and then the parent's.

    The scale of the result is the component-wise product of the two
    scales. This is exact when the parent's scale is uniform or the child
    has no rotation. Otherwise the true result is sheared, and a Transform
    can't represent shear.

    Args:
        parent (Transform): The parent's transform.
        local (Transform): The child's transform relative to the parent.

    Returns:
        The child's transform relative to the parent's parent.
    """
    parent_rotation = _quaternion(parent.rotation)
    parent_scale = _vector(parent.scale)
    position = _vector(parent.position) + _rotate(
        parent_rotation, parent_scale * _vector(local.position),
    )
    rotation = _hamilton(parent_rotation, _quaternion(local.rotation))
    scale = parent_scale * _vector(local.scale)
    return Transform(_to_float3(position), _to_floatq(rotation), _to_float3(scale))


def relative_to(parent: Transform, transform: Transform) -> Transform:
    """Returns a transform re-expressed relative to a parent.

    This is the inverse of compose, so that
    compose(parent, relative_to(parent, t)) equals t up to rounding. Both
    arguments must be relative to the same space, such as Root. Use it to
    find the position, rotation, and scale to give a new child slot so that
    it ends up at a given place in the world.

    Args:
        parent (Transform): The parent's transform.
        transform (Transform): The transform to re-express.

    Returns:
        The transform relative to the parent.

    Raises:
        ValueError: A component of the parent's scale is zero, so the
            parent's space is degenerate and has no inverse.
    """
    parent_scale = _vector(parent.scale)
    if np.any(parent_scale == 0.0):
        raise ValueError(f"The parent's scale {parent.scale} has a zero component.")
    inverse_rotation = _inverse(_quaternion(parent.rotation))
    position = _rotate(
        inverse_rotation, _vector(transform.position) - _vector(parent.position),
    ) / parent_scale
    rotation = _hamilton(inverse_rotation, _quaternion(transform.rotation))
    scale = _vector(transform.scale) / parent_scale
    return Transform(_to_float3(position), _to_floatq(rotation), _to_float3(scale))
