"""Type mapping between Python types, Resonite C# type names, and field classes.

This is the single source of truth for the bidirectional mapping between:
- Python value types (e.g. ``bool``, ``np.float32``, ``primitives.Float3``)
- Resonite C# type name strings (e.g. ``"bool"``, ``"float"``, ``"float3"``)
- Field classes from ``pyresonitelink.data.fields`` (e.g. ``FieldBool``,
  ``FieldFloat``, ``FieldFloat3``)

Used by the generated component base to resolve generic type parameters
at runtime.
"""

from typing import Any

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives


class TypeInfo:
    """Holds the mapping tuple for a single value type.

    Attributes:
        python_type: The Python type used for the value.
        resonite_name: The Resonite C# type name string.
        field_class: The corresponding Field dataclass.
    """

    __slots__ = ("python_type", "resonite_name", "field_class")

    def __init__(
        self, python_type: type, resonite_name: str, field_class: type
    ) -> None:
        self.python_type = python_type
        self.resonite_name = resonite_name
        self.field_class = field_class


# All known value type mappings.
_TYPE_INFOS: list[TypeInfo] = [
    # Scalar numerics — canonical types first, then Python builtins as aliases
    TypeInfo(np.bool_, "bool", fields.FieldBool),
    TypeInfo(bool, "bool", fields.FieldBool),
    TypeInfo(np.uint8, "byte", fields.FieldByte),
    TypeInfo(np.int8, "sbyte", fields.FieldSbyte),
    TypeInfo(np.int16, "short", fields.FieldShort),
    TypeInfo(np.uint16, "ushort", fields.FieldUshort),
    TypeInfo(np.int32, "int", fields.FieldInt),
    TypeInfo(int, "int", fields.FieldInt),
    TypeInfo(np.uint32, "uint", fields.FieldUint),
    TypeInfo(np.int64, "long", fields.FieldLong),
    TypeInfo(np.uint64, "ulong", fields.FieldUlong),
    TypeInfo(np.float32, "float", fields.FieldFloat),
    TypeInfo(np.float64, "double", fields.FieldDouble),
    TypeInfo(float, "double", fields.FieldDouble),
    # String-like
    TypeInfo(str, "string", fields.FieldString),
    # Colors
    TypeInfo(primitives.Color, "color", fields.FieldColor),
    TypeInfo(primitives.ColorX, "colorX", fields.FieldColorX),
    TypeInfo(primitives.Color32, "color32", fields.FieldColor32),
    # 2D vectors
    TypeInfo(primitives.Float2, "float2", fields.FieldFloat2),
    TypeInfo(primitives.Double2, "double2", fields.FieldDouble2),
    TypeInfo(primitives.Int2, "int2", fields.FieldInt2),
    TypeInfo(primitives.UInt2, "uint2", fields.FieldUint2),
    TypeInfo(primitives.Long2, "long2", fields.FieldLong2),
    TypeInfo(primitives.ULong2, "ulong2", fields.FieldUlong2),
    TypeInfo(primitives.Short2, "short2", fields.FieldShort2),
    TypeInfo(primitives.UShort2, "ushort2", fields.FieldUshort2),
    TypeInfo(primitives.Byte2, "byte2", fields.FieldByte2),
    TypeInfo(primitives.SByte2, "sbyte2", fields.FieldSbyte2),
    TypeInfo(primitives.Bool2, "bool2", fields.FieldBool2),
    # 3D vectors
    TypeInfo(primitives.Float3, "float3", fields.FieldFloat3),
    TypeInfo(primitives.Double3, "double3", fields.FieldDouble3),
    TypeInfo(primitives.Int3, "int3", fields.FieldInt3),
    TypeInfo(primitives.UInt3, "uint3", fields.FieldUint3),
    TypeInfo(primitives.Long3, "long3", fields.FieldLong3),
    TypeInfo(primitives.ULong3, "ulong3", fields.FieldUlong3),
    TypeInfo(primitives.Short3, "short3", fields.FieldShort3),
    TypeInfo(primitives.UShort3, "ushort3", fields.FieldUshort3),
    TypeInfo(primitives.Byte3, "byte3", fields.FieldByte3),
    TypeInfo(primitives.SByte3, "sbyte3", fields.FieldSbyte3),
    TypeInfo(primitives.Bool3, "bool3", fields.FieldBool3),
    # 4D vectors
    TypeInfo(primitives.Float4, "float4", fields.FieldFloat4),
    TypeInfo(primitives.Double4, "double4", fields.FieldDouble4),
    TypeInfo(primitives.Int4, "int4", fields.FieldInt4),
    TypeInfo(primitives.UInt4, "uint4", fields.FieldUint4),
    TypeInfo(primitives.Long4, "long4", fields.FieldLong4),
    TypeInfo(primitives.ULong4, "ulong4", fields.FieldUlong4),
    TypeInfo(primitives.Short4, "short4", fields.FieldShort4),
    TypeInfo(primitives.UShort4, "ushort4", fields.FieldUshort4),
    TypeInfo(primitives.Byte4, "byte4", fields.FieldByte4),
    TypeInfo(primitives.SByte4, "sbyte4", fields.FieldSbyte4),
    TypeInfo(primitives.Bool4, "bool4", fields.FieldBool4),
    # Quaternions
    TypeInfo(primitives.FloatQ, "floatQ", fields.FieldFloatQ),
    TypeInfo(primitives.DoubleQ, "doubleQ", fields.FieldDoubleQ),
    # Matrices
    TypeInfo(primitives.Float2x2, "float2x2", fields.FieldFloat2x2),
    TypeInfo(primitives.Double2x2, "double2x2", fields.FieldDouble2x2),
    TypeInfo(primitives.Float3x3, "float3x3", fields.FieldFloat3x3),
    TypeInfo(primitives.Double3x3, "double3x3", fields.FieldDouble3x3),
    TypeInfo(primitives.Float4x4, "float4x4", fields.FieldFloat4x4),
    TypeInfo(primitives.Double4x4, "double4x4", fields.FieldDouble4x4),
]

# Lookup by Python type → TypeInfo (first match wins for duplicates)
_BY_PYTHON_TYPE: dict[type, TypeInfo] = {}
for _info in _TYPE_INFOS:
    if _info.python_type not in _BY_PYTHON_TYPE:
        _BY_PYTHON_TYPE[_info.python_type] = _info

# Lookup by Resonite name → TypeInfo (first match wins)
_BY_RESONITE_NAME: dict[str, TypeInfo] = {}
for _info in _TYPE_INFOS:
    if _info.resonite_name not in _BY_RESONITE_NAME:
        _BY_RESONITE_NAME[_info.resonite_name] = _info


def from_python_type(python_type: type) -> TypeInfo:
    """Look up type info by Python type.

    Args:
        python_type: A Python type like ``np.float32`` or ``bool``.

    Returns:
        The corresponding TypeInfo.

    Raises:
        KeyError: If the type is not a known value type.
    """
    info = _BY_PYTHON_TYPE.get(python_type)
    if info is None:
        raise KeyError(
            f"{python_type!r} is not a known Resonite value type"
        )
    return info


def from_resonite_name(name: str) -> TypeInfo:
    """Look up type info by Resonite C# type name.

    Args:
        name: A Resonite type name like ``"float"`` or ``"Float3"``.

    Returns:
        The corresponding TypeInfo.

    Raises:
        KeyError: If the name is not a known value type.
    """
    info = _BY_RESONITE_NAME.get(name)
    if info is None:
        raise KeyError(
            f"{name!r} is not a known Resonite value type name"
        )
    return info
