"""Field types for ResoniteLink data model.

This module contains Field and Array classes for all primitive types, mirroring
the auto-generated C# classes from the PrimitiveContainers.tt template.

Note: The C# BoxedValue and ValueType properties are marked [JsonIgnore] and
are not included in these dataclasses.
"""

from dataclasses import dataclass, field
from decimal import Decimal

import numpy as np

from .members import Member
from .primitives import (
    BoundingBox,
    Bool2,
    Bool3,
    Bool4,
    Byte2,
    Byte3,
    Byte4,
    Color,
    Color32,
    ColorX,
    Double2,
    Double2x2,
    Double3,
    Double3x3,
    Double4,
    Double4x4,
    DoubleQ,
    Float2,
    Float2x2,
    Float3,
    Float3x3,
    Float4,
    Float4x4,
    FloatQ,
    Int2,
    Int3,
    Int4,
    Long2,
    Long3,
    Long4,
    Rect,
    SByte2,
    SByte3,
    SByte4,
    Short2,
    Short3,
    Short4,
    UInt2,
    UInt3,
    UInt4,
    ULong2,
    ULong3,
    ULong4,
    UShort2,
    UShort3,
    UShort4,
)


# =============================================================================
# Standalone Primitive Fields
# =============================================================================


@dataclass
class FieldByte(Member):
    """Field containing a byte value."""

    value: np.uint8 = np.uint8(0)


@dataclass
class ArrayByte(Member):
    """Array of byte values."""

    values: list[np.uint8] = field(default_factory=list[np.uint8])


@dataclass
class FieldNullableByte(Member):
    """Field containing an optional byte value."""

    value: np.uint8 | None = None


@dataclass
class FieldUshort(Member):
    """Field containing an unsigned short value."""

    value: np.uint16 = np.uint16(0)


@dataclass
class ArrayUshort(Member):
    """Array of unsigned short values."""

    values: list[np.uint16] = field(default_factory=list[np.uint16])


@dataclass
class FieldNullableUshort(Member):
    """Field containing an optional unsigned short value."""

    value: np.uint16 | None = None


@dataclass
class FieldUint(Member):
    """Field containing an unsigned int value."""

    value: np.uint32 = np.uint32(0)


@dataclass
class ArrayUint(Member):
    """Array of unsigned int values."""

    values: list[np.uint32] = field(default_factory=list[np.uint32])


@dataclass
class FieldNullableUint(Member):
    """Field containing an optional unsigned int value."""

    value: np.uint32 | None = None


@dataclass
class FieldUlong(Member):
    """Field containing an unsigned long value."""

    value: np.uint64 = np.uint64(0)


@dataclass
class ArrayUlong(Member):
    """Array of unsigned long values."""

    values: list[np.uint64] = field(default_factory=list[np.uint64])


@dataclass
class FieldNullableUlong(Member):
    """Field containing an optional unsigned long value."""

    value: np.uint64 | None = None


@dataclass
class FieldSbyte(Member):
    """Field containing a signed byte value."""

    value: np.int8 = np.int8(0)


@dataclass
class ArraySbyte(Member):
    """Array of signed byte values."""

    values: list[np.int8] = field(default_factory=list[np.int8])


@dataclass
class FieldNullableSbyte(Member):
    """Field containing an optional signed byte value."""

    value: np.int8 | None = None


@dataclass
class FieldShort(Member):
    """Field containing a short value."""

    value: np.int16 = np.int16(0)


@dataclass
class ArrayShort(Member):
    """Array of short values."""

    values: list[np.int16] = field(default_factory=list[np.int16])


@dataclass
class FieldNullableShort(Member):
    """Field containing an optional short value."""

    value: np.int16 | None = None


@dataclass
class FieldInt(Member):
    """Field containing an int value."""

    value: np.int32 = np.int32(0)


@dataclass
class ArrayInt(Member):
    """Array of int values."""

    values: list[np.int32] = field(default_factory=list[np.int32])


@dataclass
class FieldNullableInt(Member):
    """Field containing an optional int value."""

    value: np.int32 | None = None


@dataclass
class FieldLong(Member):
    """Field containing a long value."""

    value: np.int64 = np.int64(0)


@dataclass
class ArrayLong(Member):
    """Array of long values."""

    values: list[np.int64] = field(default_factory=list[np.int64])


@dataclass
class FieldNullableLong(Member):
    """Field containing an optional long value."""

    value: np.int64 | None = None


@dataclass
class FieldFloat(Member):
    """Field containing a float value."""

    value: np.float32 = np.float32(0.0)


@dataclass
class ArrayFloat(Member):
    """Array of float values."""

    values: list[np.float32] = field(default_factory=list[np.float32])


@dataclass
class FieldNullableFloat(Member):
    """Field containing an optional float value."""

    value: np.float32 | None = None


@dataclass
class FieldDouble(Member):
    """Field containing a double value."""

    value: np.float64 = np.float64(0.0)


@dataclass
class ArrayDouble(Member):
    """Array of double values."""

    values: list[np.float64] = field(default_factory=list[np.float64])


@dataclass
class FieldNullableDouble(Member):
    """Field containing an optional double value."""

    value: np.float64 | None = None


@dataclass
class FieldDecimal(Member):
    """Field containing a decimal value."""

    value: Decimal = Decimal(0)

    def __post_init__(self) -> None:
        """Coerce value to Decimal."""
        if not isinstance(self.value, Decimal):
            self.value = Decimal(str(self.value))


@dataclass
class ArrayDecimal(Member):
    """Array of decimal values."""

    values: list[Decimal] = field(default_factory=list[Decimal])


@dataclass
class FieldNullableDecimal(Member):
    """Field containing an optional decimal value."""

    value: Decimal | None = None

    def __post_init__(self) -> None:
        """Coerce value to Decimal if not None."""
        if self.value is not None and not isinstance(self.value, Decimal):
            self.value = Decimal(str(self.value))


@dataclass
class FieldBool(Member):
    """Field containing a boolean value."""

    value: bool = False


@dataclass
class ArrayBool(Member):
    """Array of boolean values."""

    values: list[bool] = field(default_factory=list[bool])


@dataclass
class FieldNullableBool(Member):
    """Field containing an optional boolean value."""

    value: bool | None = None


@dataclass
class FieldChar(Member):
    """Field containing a character value."""

    value: str = ""


@dataclass
class ArrayChar(Member):
    """Array of character values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldNullableChar(Member):
    """Field containing an optional character value."""

    value: str | None = None


@dataclass
class FieldString(Member):
    """Field containing a string value."""

    value: str | None = None


@dataclass
class ArrayString(Member):
    """Array of string values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldUri(Member):
    """Field containing a URI value."""

    value: str | None = None


@dataclass
class ArrayUri(Member):
    """Array of URI values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldTimeSpan(Member):
    """Field containing a TimeSpan value (serialized as string)."""

    value: str | None = None


@dataclass
class ArrayTimeSpan(Member):
    """Array of TimeSpan values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldNullableTimeSpan(Member):
    """Field containing an optional TimeSpan value."""

    value: str | None = None


@dataclass
class FieldDateTime(Member):
    """Field containing a DateTime value (serialized as string)."""

    value: str | None = None


@dataclass
class ArrayDateTime(Member):
    """Array of DateTime values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldNullableDateTime(Member):
    """Field containing an optional DateTime value."""

    value: str | None = None


# =============================================================================
# Color Fields
# =============================================================================


@dataclass
class FieldColor(Member):
    """Field containing a Color value."""

    value: Color | None = None


@dataclass
class ArrayColor(Member):
    """Array of Color values."""

    values: list[Color] = field(default_factory=list[Color])


@dataclass
class FieldNullableColor(Member):
    """Field containing an optional Color value."""

    value: Color | None = None


@dataclass
class FieldColorX(Member):
    """Field containing a ColorX value."""

    value: ColorX | None = None


@dataclass
class ArrayColorX(Member):
    """Array of ColorX values."""

    values: list[ColorX] = field(default_factory=list[ColorX])


@dataclass
class FieldNullableColorX(Member):
    """Field containing an optional ColorX value."""

    value: ColorX | None = None


@dataclass
class FieldColor32(Member):
    """Field containing a Color32 value."""

    value: Color32 | None = None


@dataclass
class ArrayColor32(Member):
    """Array of Color32 values."""

    values: list[Color32] = field(default_factory=list[Color32])


@dataclass
class FieldNullableColor32(Member):
    """Field containing an optional Color32 value."""

    value: Color32 | None = None


# =============================================================================
# 2D Vector Fields
# =============================================================================


@dataclass
class FieldFloat2(Member):
    """Field containing a Float2 value."""

    value: Float2 | None = None


@dataclass
class ArrayFloat2(Member):
    """Array of Float2 values."""

    values: list[Float2] = field(default_factory=list[Float2])


@dataclass
class FieldNullableFloat2(Member):
    """Field containing an optional Float2 value."""

    value: Float2 | None = None


@dataclass
class FieldDouble2(Member):
    """Field containing a Double2 value."""

    value: Double2 | None = None


@dataclass
class ArrayDouble2(Member):
    """Array of Double2 values."""

    values: list[Double2] = field(default_factory=list[Double2])


@dataclass
class FieldNullableDouble2(Member):
    """Field containing an optional Double2 value."""

    value: Double2 | None = None


@dataclass
class FieldByte2(Member):
    """Field containing a Byte2 value."""

    value: Byte2 | None = None


@dataclass
class ArrayByte2(Member):
    """Array of Byte2 values."""

    values: list[Byte2] = field(default_factory=list[Byte2])


@dataclass
class FieldNullableByte2(Member):
    """Field containing an optional Byte2 value."""

    value: Byte2 | None = None


@dataclass
class FieldUshort2(Member):
    """Field containing a UShort2 value."""

    value: UShort2 | None = None


@dataclass
class ArrayUshort2(Member):
    """Array of UShort2 values."""

    values: list[UShort2] = field(default_factory=list[UShort2])


@dataclass
class FieldNullableUshort2(Member):
    """Field containing an optional UShort2 value."""

    value: UShort2 | None = None


@dataclass
class FieldUint2(Member):
    """Field containing a UInt2 value."""

    value: UInt2 | None = None


@dataclass
class ArrayUint2(Member):
    """Array of UInt2 values."""

    values: list[UInt2] = field(default_factory=list[UInt2])


@dataclass
class FieldNullableUint2(Member):
    """Field containing an optional UInt2 value."""

    value: UInt2 | None = None


@dataclass
class FieldUlong2(Member):
    """Field containing a ULong2 value."""

    value: ULong2 | None = None


@dataclass
class ArrayUlong2(Member):
    """Array of ULong2 values."""

    values: list[ULong2] = field(default_factory=list[ULong2])


@dataclass
class FieldNullableUlong2(Member):
    """Field containing an optional ULong2 value."""

    value: ULong2 | None = None


@dataclass
class FieldSbyte2(Member):
    """Field containing a SByte2 value."""

    value: SByte2 | None = None


@dataclass
class ArraySbyte2(Member):
    """Array of SByte2 values."""

    values: list[SByte2] = field(default_factory=list[SByte2])


@dataclass
class FieldNullableSbyte2(Member):
    """Field containing an optional SByte2 value."""

    value: SByte2 | None = None


@dataclass
class FieldShort2(Member):
    """Field containing a Short2 value."""

    value: Short2 | None = None


@dataclass
class ArrayShort2(Member):
    """Array of Short2 values."""

    values: list[Short2] = field(default_factory=list[Short2])


@dataclass
class FieldNullableShort2(Member):
    """Field containing an optional Short2 value."""

    value: Short2 | None = None


@dataclass
class FieldInt2(Member):
    """Field containing an Int2 value."""

    value: Int2 | None = None


@dataclass
class ArrayInt2(Member):
    """Array of Int2 values."""

    values: list[Int2] = field(default_factory=list[Int2])


@dataclass
class FieldNullableInt2(Member):
    """Field containing an optional Int2 value."""

    value: Int2 | None = None


@dataclass
class FieldLong2(Member):
    """Field containing a Long2 value."""

    value: Long2 | None = None


@dataclass
class ArrayLong2(Member):
    """Array of Long2 values."""

    values: list[Long2] = field(default_factory=list[Long2])


@dataclass
class FieldNullableLong2(Member):
    """Field containing an optional Long2 value."""

    value: Long2 | None = None


@dataclass
class FieldBool2(Member):
    """Field containing a Bool2 value."""

    value: Bool2 | None = None


@dataclass
class ArrayBool2(Member):
    """Array of Bool2 values."""

    values: list[Bool2] = field(default_factory=list[Bool2])


@dataclass
class FieldNullableBool2(Member):
    """Field containing an optional Bool2 value."""

    value: Bool2 | None = None


# =============================================================================
# 3D Vector Fields
# =============================================================================


@dataclass
class FieldFloat3(Member):
    """Field containing a Float3 value."""

    value: Float3 | None = None


@dataclass
class ArrayFloat3(Member):
    """Array of Float3 values."""

    values: list[Float3] = field(default_factory=list[Float3])


@dataclass
class FieldNullableFloat3(Member):
    """Field containing an optional Float3 value."""

    value: Float3 | None = None


@dataclass
class FieldDouble3(Member):
    """Field containing a Double3 value."""

    value: Double3 | None = None


@dataclass
class ArrayDouble3(Member):
    """Array of Double3 values."""

    values: list[Double3] = field(default_factory=list[Double3])


@dataclass
class FieldNullableDouble3(Member):
    """Field containing an optional Double3 value."""

    value: Double3 | None = None


@dataclass
class FieldByte3(Member):
    """Field containing a Byte3 value."""

    value: Byte3 | None = None


@dataclass
class ArrayByte3(Member):
    """Array of Byte3 values."""

    values: list[Byte3] = field(default_factory=list[Byte3])


@dataclass
class FieldNullableByte3(Member):
    """Field containing an optional Byte3 value."""

    value: Byte3 | None = None


@dataclass
class FieldUshort3(Member):
    """Field containing a UShort3 value."""

    value: UShort3 | None = None


@dataclass
class ArrayUshort3(Member):
    """Array of UShort3 values."""

    values: list[UShort3] = field(default_factory=list[UShort3])


@dataclass
class FieldNullableUshort3(Member):
    """Field containing an optional UShort3 value."""

    value: UShort3 | None = None


@dataclass
class FieldUint3(Member):
    """Field containing a UInt3 value."""

    value: UInt3 | None = None


@dataclass
class ArrayUint3(Member):
    """Array of UInt3 values."""

    values: list[UInt3] = field(default_factory=list[UInt3])


@dataclass
class FieldNullableUint3(Member):
    """Field containing an optional UInt3 value."""

    value: UInt3 | None = None


@dataclass
class FieldUlong3(Member):
    """Field containing a ULong3 value."""

    value: ULong3 | None = None


@dataclass
class ArrayUlong3(Member):
    """Array of ULong3 values."""

    values: list[ULong3] = field(default_factory=list[ULong3])


@dataclass
class FieldNullableUlong3(Member):
    """Field containing an optional ULong3 value."""

    value: ULong3 | None = None


@dataclass
class FieldSbyte3(Member):
    """Field containing a SByte3 value."""

    value: SByte3 | None = None


@dataclass
class ArraySbyte3(Member):
    """Array of SByte3 values."""

    values: list[SByte3] = field(default_factory=list[SByte3])


@dataclass
class FieldNullableSbyte3(Member):
    """Field containing an optional SByte3 value."""

    value: SByte3 | None = None


@dataclass
class FieldShort3(Member):
    """Field containing a Short3 value."""

    value: Short3 | None = None


@dataclass
class ArrayShort3(Member):
    """Array of Short3 values."""

    values: list[Short3] = field(default_factory=list[Short3])


@dataclass
class FieldNullableShort3(Member):
    """Field containing an optional Short3 value."""

    value: Short3 | None = None


@dataclass
class FieldInt3(Member):
    """Field containing an Int3 value."""

    value: Int3 | None = None


@dataclass
class ArrayInt3(Member):
    """Array of Int3 values."""

    values: list[Int3] = field(default_factory=list[Int3])


@dataclass
class FieldNullableInt3(Member):
    """Field containing an optional Int3 value."""

    value: Int3 | None = None


@dataclass
class FieldLong3(Member):
    """Field containing a Long3 value."""

    value: Long3 | None = None


@dataclass
class ArrayLong3(Member):
    """Array of Long3 values."""

    values: list[Long3] = field(default_factory=list[Long3])


@dataclass
class FieldNullableLong3(Member):
    """Field containing an optional Long3 value."""

    value: Long3 | None = None


@dataclass
class FieldBool3(Member):
    """Field containing a Bool3 value."""

    value: Bool3 | None = None


@dataclass
class ArrayBool3(Member):
    """Array of Bool3 values."""

    values: list[Bool3] = field(default_factory=list[Bool3])


@dataclass
class FieldNullableBool3(Member):
    """Field containing an optional Bool3 value."""

    value: Bool3 | None = None


# =============================================================================
# 4D Vector Fields
# =============================================================================


@dataclass
class FieldFloat4(Member):
    """Field containing a Float4 value."""

    value: Float4 | None = None


@dataclass
class ArrayFloat4(Member):
    """Array of Float4 values."""

    values: list[Float4] = field(default_factory=list[Float4])


@dataclass
class FieldNullableFloat4(Member):
    """Field containing an optional Float4 value."""

    value: Float4 | None = None


@dataclass
class FieldDouble4(Member):
    """Field containing a Double4 value."""

    value: Double4 | None = None


@dataclass
class ArrayDouble4(Member):
    """Array of Double4 values."""

    values: list[Double4] = field(default_factory=list[Double4])


@dataclass
class FieldNullableDouble4(Member):
    """Field containing an optional Double4 value."""

    value: Double4 | None = None


@dataclass
class FieldByte4(Member):
    """Field containing a Byte4 value."""

    value: Byte4 | None = None


@dataclass
class ArrayByte4(Member):
    """Array of Byte4 values."""

    values: list[Byte4] = field(default_factory=list[Byte4])


@dataclass
class FieldNullableByte4(Member):
    """Field containing an optional Byte4 value."""

    value: Byte4 | None = None


@dataclass
class FieldUshort4(Member):
    """Field containing a UShort4 value."""

    value: UShort4 | None = None


@dataclass
class ArrayUshort4(Member):
    """Array of UShort4 values."""

    values: list[UShort4] = field(default_factory=list[UShort4])


@dataclass
class FieldNullableUshort4(Member):
    """Field containing an optional UShort4 value."""

    value: UShort4 | None = None


@dataclass
class FieldUint4(Member):
    """Field containing a UInt4 value."""

    value: UInt4 | None = None


@dataclass
class ArrayUint4(Member):
    """Array of UInt4 values."""

    values: list[UInt4] = field(default_factory=list[UInt4])


@dataclass
class FieldNullableUint4(Member):
    """Field containing an optional UInt4 value."""

    value: UInt4 | None = None


@dataclass
class FieldUlong4(Member):
    """Field containing a ULong4 value."""

    value: ULong4 | None = None


@dataclass
class ArrayUlong4(Member):
    """Array of ULong4 values."""

    values: list[ULong4] = field(default_factory=list[ULong4])


@dataclass
class FieldNullableUlong4(Member):
    """Field containing an optional ULong4 value."""

    value: ULong4 | None = None


@dataclass
class FieldSbyte4(Member):
    """Field containing a SByte4 value."""

    value: SByte4 | None = None


@dataclass
class ArraySbyte4(Member):
    """Array of SByte4 values."""

    values: list[SByte4] = field(default_factory=list[SByte4])


@dataclass
class FieldNullableSbyte4(Member):
    """Field containing an optional SByte4 value."""

    value: SByte4 | None = None


@dataclass
class FieldShort4(Member):
    """Field containing a Short4 value."""

    value: Short4 | None = None


@dataclass
class ArrayShort4(Member):
    """Array of Short4 values."""

    values: list[Short4] = field(default_factory=list[Short4])


@dataclass
class FieldNullableShort4(Member):
    """Field containing an optional Short4 value."""

    value: Short4 | None = None


@dataclass
class FieldInt4(Member):
    """Field containing an Int4 value."""

    value: Int4 | None = None


@dataclass
class ArrayInt4(Member):
    """Array of Int4 values."""

    values: list[Int4] = field(default_factory=list[Int4])


@dataclass
class FieldNullableInt4(Member):
    """Field containing an optional Int4 value."""

    value: Int4 | None = None


@dataclass
class FieldLong4(Member):
    """Field containing a Long4 value."""

    value: Long4 | None = None


@dataclass
class ArrayLong4(Member):
    """Array of Long4 values."""

    values: list[Long4] = field(default_factory=list[Long4])


@dataclass
class FieldNullableLong4(Member):
    """Field containing an optional Long4 value."""

    value: Long4 | None = None


@dataclass
class FieldBool4(Member):
    """Field containing a Bool4 value."""

    value: Bool4 | None = None


@dataclass
class ArrayBool4(Member):
    """Array of Bool4 values."""

    values: list[Bool4] = field(default_factory=list[Bool4])


@dataclass
class FieldNullableBool4(Member):
    """Field containing an optional Bool4 value."""

    value: Bool4 | None = None


# =============================================================================
# Quaternion Fields
# =============================================================================


@dataclass
class FieldFloatQ(Member):
    """Field containing a FloatQ (quaternion) value."""

    value: FloatQ | None = None


@dataclass
class ArrayFloatQ(Member):
    """Array of FloatQ values."""

    values: list[FloatQ] = field(default_factory=list[FloatQ])


@dataclass
class FieldNullableFloatQ(Member):
    """Field containing an optional FloatQ value."""

    value: FloatQ | None = None


@dataclass
class FieldDoubleQ(Member):
    """Field containing a DoubleQ (quaternion) value."""

    value: DoubleQ | None = None


@dataclass
class ArrayDoubleQ(Member):
    """Array of DoubleQ values."""

    values: list[DoubleQ] = field(default_factory=list[DoubleQ])


@dataclass
class FieldNullableDoubleQ(Member):
    """Field containing an optional DoubleQ value."""

    value: DoubleQ | None = None


# =============================================================================
# Matrix Fields
# =============================================================================


@dataclass
class FieldFloat2x2(Member):
    """Field containing a Float2x2 matrix value."""

    value: Float2x2 | None = None


@dataclass
class ArrayFloat2x2(Member):
    """Array of Float2x2 values."""

    values: list[Float2x2] = field(default_factory=list[Float2x2])


@dataclass
class FieldNullableFloat2x2(Member):
    """Field containing an optional Float2x2 value."""

    value: Float2x2 | None = None


@dataclass
class FieldDouble2x2(Member):
    """Field containing a Double2x2 matrix value."""

    value: Double2x2 | None = None


@dataclass
class ArrayDouble2x2(Member):
    """Array of Double2x2 values."""

    values: list[Double2x2] = field(default_factory=list[Double2x2])


@dataclass
class FieldNullableDouble2x2(Member):
    """Field containing an optional Double2x2 value."""

    value: Double2x2 | None = None


@dataclass
class FieldFloat3x3(Member):
    """Field containing a Float3x3 matrix value."""

    value: Float3x3 | None = None


@dataclass
class ArrayFloat3x3(Member):
    """Array of Float3x3 values."""

    values: list[Float3x3] = field(default_factory=list[Float3x3])


@dataclass
class FieldNullableFloat3x3(Member):
    """Field containing an optional Float3x3 value."""

    value: Float3x3 | None = None


@dataclass
class FieldDouble3x3(Member):
    """Field containing a Double3x3 matrix value."""

    value: Double3x3 | None = None


@dataclass
class ArrayDouble3x3(Member):
    """Array of Double3x3 values."""

    values: list[Double3x3] = field(default_factory=list[Double3x3])


@dataclass
class FieldNullableDouble3x3(Member):
    """Field containing an optional Double3x3 value."""

    value: Double3x3 | None = None


@dataclass
class FieldFloat4x4(Member):
    """Field containing a Float4x4 matrix value."""

    value: Float4x4 | None = None


@dataclass
class ArrayFloat4x4(Member):
    """Array of Float4x4 values."""

    values: list[Float4x4] = field(default_factory=list[Float4x4])


@dataclass
class FieldNullableFloat4x4(Member):
    """Field containing an optional Float4x4 value."""

    value: Float4x4 | None = None


@dataclass
class FieldDouble4x4(Member):
    """Field containing a Double4x4 matrix value."""

    value: Double4x4 | None = None


@dataclass
class ArrayDouble4x4(Member):
    """Array of Double4x4 values."""

    values: list[Double4x4] = field(default_factory=list[Double4x4])


@dataclass
class FieldNullableDouble4x4(Member):
    """Field containing an optional Double4x4 value."""

    value: Double4x4 | None = None


# =============================================================================
# Geometry Fields
# =============================================================================


@dataclass
class FieldRect(Member):
    """Field containing a Rect value."""

    value: Rect | None = None


@dataclass
class FieldBoundingBox(Member):
    """Field containing a BoundingBox value."""

    value: BoundingBox | None = None
