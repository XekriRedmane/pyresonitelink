"""Primitive types for ResoniteLink data model.

This module contains vector, quaternion, matrix, and Color types that mirror
the C# structs used in ResoniteLink.

Scalar type aliases are provided so that code can use ``primitives.Float``
instead of ``np.float32``, keeping the namespace consistent with the
composite types (``primitives.Float3``, ``primitives.FloatQ``, etc.).
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

import numpy as np


# =============================================================================
# Scalar Type Aliases
# =============================================================================

Bool: type[np.bool_] = np.bool_
Byte: type[np.uint8] = np.uint8
SByte: type[np.int8] = np.int8
Short: type[np.int16] = np.int16
UShort: type[np.uint16] = np.uint16
Int: type[np.int32] = np.int32
UInt: type[np.uint32] = np.uint32
Long: type[np.int64] = np.int64
ULong: type[np.uint64] = np.uint64
Float: type[np.float32] = np.float32
Double: type[np.float64] = np.float64
String: type[str] = str
Char: type[str] = str


# =============================================================================
# Color Types
# =============================================================================


@dataclass
class Color:
    """RGBA Color with float components."""

    r: float = 0
    g: float = 0
    b: float = 0
    a: float = 1

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.r = np.float32(self.r)  # type: ignore[assignment]
        self.g = np.float32(self.g)  # type: ignore[assignment]
        self.b = np.float32(self.b)  # type: ignore[assignment]
        self.a = np.float32(self.a)  # type: ignore[assignment]


@dataclass
class ColorX:
    """RGBA Color with float components and Color profile."""

    r: float = 0
    g: float = 0
    b: float = 0
    a: float = 1
    profile: str = ""

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.r = np.float32(self.r)  # type: ignore[assignment]
        self.g = np.float32(self.g)  # type: ignore[assignment]
        self.b = np.float32(self.b)  # type: ignore[assignment]
        self.a = np.float32(self.a)  # type: ignore[assignment]


@dataclass
class Color32:
    """RGBA Color with byte components (0-255)."""

    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.r = np.uint8(self.r)  # type: ignore[assignment]
        self.g = np.uint8(self.g)  # type: ignore[assignment]
        self.b = np.uint8(self.b)  # type: ignore[assignment]
        self.a = np.uint8(self.a)  # type: ignore[assignment]


# =============================================================================
# 2D Vector Types
# =============================================================================


@dataclass
class Float2:
    """2D vector with float components."""

    x: float = 0.0
    y: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float32(self.x)  # type: ignore[assignment]
        self.y = np.float32(self.y)  # type: ignore[assignment]


@dataclass
class Double2:
    """2D vector with double components."""

    x: float = 0.0
    y: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float64(self.x)  # type: ignore[assignment]
        self.y = np.float64(self.y)  # type: ignore[assignment]


@dataclass
class Byte2:
    """2D vector with byte components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint8(self.x)  # type: ignore[assignment]
        self.y = np.uint8(self.y)  # type: ignore[assignment]


@dataclass
class UShort2:
    """2D vector with unsigned short components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint16(self.x)  # type: ignore[assignment]
        self.y = np.uint16(self.y)  # type: ignore[assignment]


@dataclass
class UInt2:
    """2D vector with unsigned int components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint32(self.x)  # type: ignore[assignment]
        self.y = np.uint32(self.y)  # type: ignore[assignment]


@dataclass
class ULong2:
    """2D vector with unsigned long components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint64(self.x)  # type: ignore[assignment]
        self.y = np.uint64(self.y)  # type: ignore[assignment]


@dataclass
class SByte2:
    """2D vector with signed byte components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int8(self.x)  # type: ignore[assignment]
        self.y = np.int8(self.y)  # type: ignore[assignment]


@dataclass
class Short2:
    """2D vector with short components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int16(self.x)  # type: ignore[assignment]
        self.y = np.int16(self.y)  # type: ignore[assignment]


@dataclass
class Int2:
    """2D vector with int components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int32(self.x)  # type: ignore[assignment]
        self.y = np.int32(self.y)  # type: ignore[assignment]


@dataclass
class Long2:
    """2D vector with long components."""

    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int64(self.x)  # type: ignore[assignment]
        self.y = np.int64(self.y)  # type: ignore[assignment]


@dataclass
class Bool2:
    """2D vector with bool components."""

    x: bool = False
    y: bool = False


# =============================================================================
# 3D Vector Types
# =============================================================================


@dataclass
class Float3:
    """3D vector with float components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float32(self.x)  # type: ignore[assignment]
        self.y = np.float32(self.y)  # type: ignore[assignment]
        self.z = np.float32(self.z)  # type: ignore[assignment]


@dataclass
class Double3:
    """3D vector with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float64(self.x)  # type: ignore[assignment]
        self.y = np.float64(self.y)  # type: ignore[assignment]
        self.z = np.float64(self.z)  # type: ignore[assignment]


@dataclass
class Byte3:
    """3D vector with byte components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint8(self.x)  # type: ignore[assignment]
        self.y = np.uint8(self.y)  # type: ignore[assignment]
        self.z = np.uint8(self.z)  # type: ignore[assignment]


@dataclass
class UShort3:
    """3D vector with unsigned short components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint16(self.x)  # type: ignore[assignment]
        self.y = np.uint16(self.y)  # type: ignore[assignment]
        self.z = np.uint16(self.z)  # type: ignore[assignment]


@dataclass
class UInt3:
    """3D vector with unsigned int components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint32(self.x)  # type: ignore[assignment]
        self.y = np.uint32(self.y)  # type: ignore[assignment]
        self.z = np.uint32(self.z)  # type: ignore[assignment]


@dataclass
class ULong3:
    """3D vector with unsigned long components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint64(self.x)  # type: ignore[assignment]
        self.y = np.uint64(self.y)  # type: ignore[assignment]
        self.z = np.uint64(self.z)  # type: ignore[assignment]


@dataclass
class SByte3:
    """3D vector with signed byte components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int8(self.x)  # type: ignore[assignment]
        self.y = np.int8(self.y)  # type: ignore[assignment]
        self.z = np.int8(self.z)  # type: ignore[assignment]


@dataclass
class Short3:
    """3D vector with short components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int16(self.x)  # type: ignore[assignment]
        self.y = np.int16(self.y)  # type: ignore[assignment]
        self.z = np.int16(self.z)  # type: ignore[assignment]


@dataclass
class Int3:
    """3D vector with int components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int32(self.x)  # type: ignore[assignment]
        self.y = np.int32(self.y)  # type: ignore[assignment]
        self.z = np.int32(self.z)  # type: ignore[assignment]


@dataclass
class Long3:
    """3D vector with long components."""

    x: int = 0
    y: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int64(self.x)  # type: ignore[assignment]
        self.y = np.int64(self.y)  # type: ignore[assignment]
        self.z = np.int64(self.z)  # type: ignore[assignment]


@dataclass
class Bool3:
    """3D vector with bool components."""

    x: bool = False
    y: bool = False
    z: bool = False


# =============================================================================
# 4D Vector Types
# =============================================================================


@dataclass
class Float4:
    """4D vector with float components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float32(self.x)  # type: ignore[assignment]
        self.y = np.float32(self.y)  # type: ignore[assignment]
        self.z = np.float32(self.z)  # type: ignore[assignment]
        self.w = np.float32(self.w)  # type: ignore[assignment]


@dataclass
class Double4:
    """4D vector with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float64(self.x)  # type: ignore[assignment]
        self.y = np.float64(self.y)  # type: ignore[assignment]
        self.z = np.float64(self.z)  # type: ignore[assignment]
        self.w = np.float64(self.w)  # type: ignore[assignment]


@dataclass
class Byte4:
    """4D vector with byte components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint8(self.x)  # type: ignore[assignment]
        self.y = np.uint8(self.y)  # type: ignore[assignment]
        self.z = np.uint8(self.z)  # type: ignore[assignment]
        self.w = np.uint8(self.w)  # type: ignore[assignment]


@dataclass
class UShort4:
    """4D vector with unsigned short components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint16(self.x)  # type: ignore[assignment]
        self.y = np.uint16(self.y)  # type: ignore[assignment]
        self.z = np.uint16(self.z)  # type: ignore[assignment]
        self.w = np.uint16(self.w)  # type: ignore[assignment]


@dataclass
class UInt4:
    """4D vector with unsigned int components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint32(self.x)  # type: ignore[assignment]
        self.y = np.uint32(self.y)  # type: ignore[assignment]
        self.z = np.uint32(self.z)  # type: ignore[assignment]
        self.w = np.uint32(self.w)  # type: ignore[assignment]


@dataclass
class ULong4:
    """4D vector with unsigned long components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.uint64(self.x)  # type: ignore[assignment]
        self.y = np.uint64(self.y)  # type: ignore[assignment]
        self.z = np.uint64(self.z)  # type: ignore[assignment]
        self.w = np.uint64(self.w)  # type: ignore[assignment]


@dataclass
class SByte4:
    """4D vector with signed byte components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int8(self.x)  # type: ignore[assignment]
        self.y = np.int8(self.y)  # type: ignore[assignment]
        self.z = np.int8(self.z)  # type: ignore[assignment]
        self.w = np.int8(self.w)  # type: ignore[assignment]


@dataclass
class Short4:
    """4D vector with short components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int16(self.x)  # type: ignore[assignment]
        self.y = np.int16(self.y)  # type: ignore[assignment]
        self.z = np.int16(self.z)  # type: ignore[assignment]
        self.w = np.int16(self.w)  # type: ignore[assignment]


@dataclass
class Int4:
    """4D vector with int components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int32(self.x)  # type: ignore[assignment]
        self.y = np.int32(self.y)  # type: ignore[assignment]
        self.z = np.int32(self.z)  # type: ignore[assignment]
        self.w = np.int32(self.w)  # type: ignore[assignment]


@dataclass
class Long4:
    """4D vector with long components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.int64(self.x)  # type: ignore[assignment]
        self.y = np.int64(self.y)  # type: ignore[assignment]
        self.z = np.int64(self.z)  # type: ignore[assignment]
        self.w = np.int64(self.w)  # type: ignore[assignment]


@dataclass
class Bool4:
    """4D vector with bool components."""

    x: bool = False
    y: bool = False
    z: bool = False
    w: bool = False


# =============================================================================
# Quaternion Types
# =============================================================================


@dataclass
class FloatQ:
    """Quaternion with float components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float32(self.x)  # type: ignore[assignment]
        self.y = np.float32(self.y)  # type: ignore[assignment]
        self.z = np.float32(self.z)  # type: ignore[assignment]
        self.w = np.float32(self.w)  # type: ignore[assignment]


@dataclass
class DoubleQ:
    """Quaternion with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float64(self.x)  # type: ignore[assignment]
        self.y = np.float64(self.y)  # type: ignore[assignment]
        self.z = np.float64(self.z)  # type: ignore[assignment]
        self.w = np.float64(self.w)  # type: ignore[assignment]


# =============================================================================
# 2x2 Matrix Types
# =============================================================================


@dataclass
class Float2x2:
    """2x2 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m10: float = 0.0
    m11: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float32(self.m00)  # type: ignore[assignment]
        self.m01 = np.float32(self.m01)  # type: ignore[assignment]
        self.m10 = np.float32(self.m10)  # type: ignore[assignment]
        self.m11 = np.float32(self.m11)  # type: ignore[assignment]


@dataclass
class Double2x2:
    """2x2 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m10: float = 0.0
    m11: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float64(self.m00)  # type: ignore[assignment]
        self.m01 = np.float64(self.m01)  # type: ignore[assignment]
        self.m10 = np.float64(self.m10)  # type: ignore[assignment]
        self.m11 = np.float64(self.m11)  # type: ignore[assignment]


# =============================================================================
# 3x3 Matrix Types
# =============================================================================


@dataclass
class Float3x3:
    """3x3 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float32(self.m00)  # type: ignore[assignment]
        self.m01 = np.float32(self.m01)  # type: ignore[assignment]
        self.m02 = np.float32(self.m02)  # type: ignore[assignment]
        self.m10 = np.float32(self.m10)  # type: ignore[assignment]
        self.m11 = np.float32(self.m11)  # type: ignore[assignment]
        self.m12 = np.float32(self.m12)  # type: ignore[assignment]
        self.m20 = np.float32(self.m20)  # type: ignore[assignment]
        self.m21 = np.float32(self.m21)  # type: ignore[assignment]
        self.m22 = np.float32(self.m22)  # type: ignore[assignment]


@dataclass
class Double3x3:
    """3x3 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float64(self.m00)  # type: ignore[assignment]
        self.m01 = np.float64(self.m01)  # type: ignore[assignment]
        self.m02 = np.float64(self.m02)  # type: ignore[assignment]
        self.m10 = np.float64(self.m10)  # type: ignore[assignment]
        self.m11 = np.float64(self.m11)  # type: ignore[assignment]
        self.m12 = np.float64(self.m12)  # type: ignore[assignment]
        self.m20 = np.float64(self.m20)  # type: ignore[assignment]
        self.m21 = np.float64(self.m21)  # type: ignore[assignment]
        self.m22 = np.float64(self.m22)  # type: ignore[assignment]


# =============================================================================
# 4x4 Matrix Types
# =============================================================================


@dataclass
class Float4x4:
    """4x4 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m03: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m13: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0
    m23: float = 0.0
    m30: float = 0.0
    m31: float = 0.0
    m32: float = 0.0
    m33: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float32(self.m00)  # type: ignore[assignment]
        self.m01 = np.float32(self.m01)  # type: ignore[assignment]
        self.m02 = np.float32(self.m02)  # type: ignore[assignment]
        self.m03 = np.float32(self.m03)  # type: ignore[assignment]
        self.m10 = np.float32(self.m10)  # type: ignore[assignment]
        self.m11 = np.float32(self.m11)  # type: ignore[assignment]
        self.m12 = np.float32(self.m12)  # type: ignore[assignment]
        self.m13 = np.float32(self.m13)  # type: ignore[assignment]
        self.m20 = np.float32(self.m20)  # type: ignore[assignment]
        self.m21 = np.float32(self.m21)  # type: ignore[assignment]
        self.m22 = np.float32(self.m22)  # type: ignore[assignment]
        self.m23 = np.float32(self.m23)  # type: ignore[assignment]
        self.m30 = np.float32(self.m30)  # type: ignore[assignment]
        self.m31 = np.float32(self.m31)  # type: ignore[assignment]
        self.m32 = np.float32(self.m32)  # type: ignore[assignment]
        self.m33 = np.float32(self.m33)  # type: ignore[assignment]


@dataclass
class Double4x4:
    """4x4 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m03: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m13: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0
    m23: float = 0.0
    m30: float = 0.0
    m31: float = 0.0
    m32: float = 0.0
    m33: float = 0.0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.m00 = np.float64(self.m00)  # type: ignore[assignment]
        self.m01 = np.float64(self.m01)  # type: ignore[assignment]
        self.m02 = np.float64(self.m02)  # type: ignore[assignment]
        self.m03 = np.float64(self.m03)  # type: ignore[assignment]
        self.m10 = np.float64(self.m10)  # type: ignore[assignment]
        self.m11 = np.float64(self.m11)  # type: ignore[assignment]
        self.m12 = np.float64(self.m12)  # type: ignore[assignment]
        self.m13 = np.float64(self.m13)  # type: ignore[assignment]
        self.m20 = np.float64(self.m20)  # type: ignore[assignment]
        self.m21 = np.float64(self.m21)  # type: ignore[assignment]
        self.m22 = np.float64(self.m22)  # type: ignore[assignment]
        self.m23 = np.float64(self.m23)  # type: ignore[assignment]
        self.m30 = np.float64(self.m30)  # type: ignore[assignment]
        self.m31 = np.float64(self.m31)  # type: ignore[assignment]
        self.m32 = np.float64(self.m32)  # type: ignore[assignment]
        self.m33 = np.float64(self.m33)  # type: ignore[assignment]


# =============================================================================
# Geometry Types
# =============================================================================


@dataclass
class Rect:
    """2D rectangle with position and size (float components).

    Matches the C# Rect struct used in Resonite. The wire format nests
    ``position`` and ``size`` as sub-objects with ``x``/``y`` fields.
    """

    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.x = np.float32(self.x)  # type: ignore[assignment]
        self.y = np.float32(self.y)  # type: ignore[assignment]
        self.width = np.float32(self.width)  # type: ignore[assignment]
        self.height = np.float32(self.height)  # type: ignore[assignment]


@dataclass
class BoundingBox:
    """Axis-aligned bounding box with min and max corners (float components).

    Matches the C# BoundingBox struct used in Resonite. The wire format
    nests ``min`` and ``max`` as sub-objects with ``x``/``y``/``z`` fields.
    """

    min_x: float = 0
    min_y: float = 0
    min_z: float = 0
    max_x: float = 0
    max_y: float = 0
    max_z: float = 0

    def __post_init__(self) -> None:
        """Coerce fields to exact numpy types."""
        self.min_x = np.float32(self.min_x)  # type: ignore[assignment]
        self.min_y = np.float32(self.min_y)  # type: ignore[assignment]
        self.min_z = np.float32(self.min_z)  # type: ignore[assignment]
        self.max_x = np.float32(self.max_x)  # type: ignore[assignment]
        self.max_y = np.float32(self.max_y)  # type: ignore[assignment]
        self.max_z = np.float32(self.max_z)  # type: ignore[assignment]
