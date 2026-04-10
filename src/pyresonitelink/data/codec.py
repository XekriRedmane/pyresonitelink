"""JSON encoding and decoding for ResoniteLink protocol.

This module provides functions to encode Python dataclass objects to JSON
and decode JSON back to Python dataclass objects, handling the $type
discriminator used in the ResoniteLink protocol.
"""

from dataclasses import asdict, fields, is_dataclass
from decimal import Decimal
import types
from typing import Any, cast, get_args, get_origin

import numpy as np

from .utils import JSON_IGNORE_KEY

from . import fields as field_types
from . import members as member_types
from . import messages as message_types
from . import primitives as primitive_types
from . import responses as response_types
from . import reflection as reflection_types
from . import workers as worker_types

# =============================================================================
# Type Definitions
# =============================================================================

type PrimitiveType = (
    primitive_types.Color
    | primitive_types.ColorX
    | primitive_types.Color32
    | primitive_types.Float2
    | primitive_types.Double2
    | primitive_types.Byte2
    | primitive_types.UShort2
    | primitive_types.UInt2
    | primitive_types.ULong2
    | primitive_types.SByte2
    | primitive_types.Short2
    | primitive_types.Int2
    | primitive_types.Long2
    | primitive_types.Bool2
    | primitive_types.Float3
    | primitive_types.Double3
    | primitive_types.Byte3
    | primitive_types.UShort3
    | primitive_types.UInt3
    | primitive_types.ULong3
    | primitive_types.SByte3
    | primitive_types.Short3
    | primitive_types.Int3
    | primitive_types.Long3
    | primitive_types.Bool3
    | primitive_types.Float4
    | primitive_types.Double4
    | primitive_types.Byte4
    | primitive_types.UShort4
    | primitive_types.UInt4
    | primitive_types.ULong4
    | primitive_types.SByte4
    | primitive_types.Short4
    | primitive_types.Int4
    | primitive_types.Long4
    | primitive_types.Bool4
    | primitive_types.FloatQ
    | primitive_types.DoubleQ
    | primitive_types.Float2x2
    | primitive_types.Double2x2
    | primitive_types.Float3x3
    | primitive_types.Double3x3
    | primitive_types.Float4x4
    | primitive_types.Double4x4
)

type MemberType = (
    member_types.Member
    | member_types.Reference
    | member_types.SyncList
    | member_types.SyncObject
    | member_types.EmptyElement
    | member_types.FieldEnum
)

type FieldType = (
    field_types.FieldByte
    | field_types.ArrayByte
    | field_types.FieldNullableByte
    | field_types.FieldUshort
    | field_types.ArrayUshort
    | field_types.FieldNullableUshort
    | field_types.FieldUint
    | field_types.ArrayUint
    | field_types.FieldNullableUint
    | field_types.FieldUlong
    | field_types.ArrayUlong
    | field_types.FieldNullableUlong
    | field_types.FieldSbyte
    | field_types.ArraySbyte
    | field_types.FieldNullableSbyte
    | field_types.FieldShort
    | field_types.ArrayShort
    | field_types.FieldNullableShort
    | field_types.FieldInt
    | field_types.ArrayInt
    | field_types.FieldNullableInt
    | field_types.FieldLong
    | field_types.ArrayLong
    | field_types.FieldNullableLong
    | field_types.FieldFloat
    | field_types.ArrayFloat
    | field_types.FieldNullableFloat
    | field_types.FieldDouble
    | field_types.ArrayDouble
    | field_types.FieldNullableDouble
    | field_types.FieldDecimal
    | field_types.ArrayDecimal
    | field_types.FieldNullableDecimal
    | field_types.FieldBool
    | field_types.ArrayBool
    | field_types.FieldNullableBool
    | field_types.FieldChar
    | field_types.ArrayChar
    | field_types.FieldNullableChar
    | field_types.FieldString
    | field_types.ArrayString
    | field_types.FieldUri
    | field_types.ArrayUri
    | field_types.FieldTimeSpan
    | field_types.ArrayTimeSpan
    | field_types.FieldNullableTimeSpan
    | field_types.FieldDateTime
    | field_types.ArrayDateTime
    | field_types.FieldNullableDateTime
    | field_types.FieldColor
    | field_types.ArrayColor
    | field_types.FieldNullableColor
    | field_types.FieldColorX
    | field_types.ArrayColorX
    | field_types.FieldNullableColorX
    | field_types.FieldColor32
    | field_types.ArrayColor32
    | field_types.FieldNullableColor32
    | field_types.FieldFloat2
    | field_types.ArrayFloat2
    | field_types.FieldNullableFloat2
    | field_types.FieldDouble2
    | field_types.ArrayDouble2
    | field_types.FieldNullableDouble2
    | field_types.FieldByte2
    | field_types.ArrayByte2
    | field_types.FieldNullableByte2
    | field_types.FieldUshort2
    | field_types.ArrayUshort2
    | field_types.FieldNullableUshort2
    | field_types.FieldUint2
    | field_types.ArrayUint2
    | field_types.FieldNullableUint2
    | field_types.FieldUlong2
    | field_types.ArrayUlong2
    | field_types.FieldNullableUlong2
    | field_types.FieldSbyte2
    | field_types.ArraySbyte2
    | field_types.FieldNullableSbyte2
    | field_types.FieldShort2
    | field_types.ArrayShort2
    | field_types.FieldNullableShort2
    | field_types.FieldInt2
    | field_types.ArrayInt2
    | field_types.FieldNullableInt2
    | field_types.FieldLong2
    | field_types.ArrayLong2
    | field_types.FieldNullableLong2
    | field_types.FieldBool2
    | field_types.ArrayBool2
    | field_types.FieldNullableBool2
    | field_types.FieldFloat3
    | field_types.ArrayFloat3
    | field_types.FieldNullableFloat3
    | field_types.FieldDouble3
    | field_types.ArrayDouble3
    | field_types.FieldNullableDouble3
    | field_types.FieldByte3
    | field_types.ArrayByte3
    | field_types.FieldNullableByte3
    | field_types.FieldUshort3
    | field_types.ArrayUshort3
    | field_types.FieldNullableUshort3
    | field_types.FieldUint3
    | field_types.ArrayUint3
    | field_types.FieldNullableUint3
    | field_types.FieldUlong3
    | field_types.ArrayUlong3
    | field_types.FieldNullableUlong3
    | field_types.FieldSbyte3
    | field_types.ArraySbyte3
    | field_types.FieldNullableSbyte3
    | field_types.FieldShort3
    | field_types.ArrayShort3
    | field_types.FieldNullableShort3
    | field_types.FieldInt3
    | field_types.ArrayInt3
    | field_types.FieldNullableInt3
    | field_types.FieldLong3
    | field_types.ArrayLong3
    | field_types.FieldNullableLong3
    | field_types.FieldBool3
    | field_types.ArrayBool3
    | field_types.FieldNullableBool3
    | field_types.FieldFloat4
    | field_types.ArrayFloat4
    | field_types.FieldNullableFloat4
    | field_types.FieldDouble4
    | field_types.ArrayDouble4
    | field_types.FieldNullableDouble4
    | field_types.FieldByte4
    | field_types.ArrayByte4
    | field_types.FieldNullableByte4
    | field_types.FieldUshort4
    | field_types.ArrayUshort4
    | field_types.FieldNullableUshort4
    | field_types.FieldUint4
    | field_types.ArrayUint4
    | field_types.FieldNullableUint4
    | field_types.FieldUlong4
    | field_types.ArrayUlong4
    | field_types.FieldNullableUlong4
    | field_types.FieldSbyte4
    | field_types.ArraySbyte4
    | field_types.FieldNullableSbyte4
    | field_types.FieldShort4
    | field_types.ArrayShort4
    | field_types.FieldNullableShort4
    | field_types.FieldInt4
    | field_types.ArrayInt4
    | field_types.FieldNullableInt4
    | field_types.FieldLong4
    | field_types.ArrayLong4
    | field_types.FieldNullableLong4
    | field_types.FieldBool4
    | field_types.ArrayBool4
    | field_types.FieldNullableBool4
    | field_types.FieldFloatQ
    | field_types.ArrayFloatQ
    | field_types.FieldNullableFloatQ
    | field_types.FieldDoubleQ
    | field_types.ArrayDoubleQ
    | field_types.FieldNullableDoubleQ
    | field_types.FieldFloat2x2
    | field_types.ArrayFloat2x2
    | field_types.FieldNullableFloat2x2
    | field_types.FieldDouble2x2
    | field_types.ArrayDouble2x2
    | field_types.FieldNullableDouble2x2
    | field_types.FieldFloat3x3
    | field_types.ArrayFloat3x3
    | field_types.FieldNullableFloat3x3
    | field_types.FieldDouble3x3
    | field_types.ArrayDouble3x3
    | field_types.FieldNullableDouble3x3
    | field_types.FieldFloat4x4
    | field_types.ArrayFloat4x4
    | field_types.FieldNullableFloat4x4
    | field_types.FieldDouble4x4
    | field_types.ArrayDouble4x4
    | field_types.FieldNullableDouble4x4
)

type WorkerType = worker_types.Worker | worker_types.Slot | worker_types.Component

type MessageType = (
    message_types.Message
    | message_types.GetSlot
    | message_types.AddSlot
    | message_types.UpdateSlot
    | message_types.RemoveSlot
    | message_types.GetComponent
    | message_types.AddComponent
    | message_types.UpdateComponent
    | message_types.RemoveComponent
    | message_types.ImportTexture2DFile
    | message_types.ImportTexture2DRawData
    | message_types.ImportTexture2DRawDataHDR
    | message_types.ImportCubemapFiles
    | message_types.ImportCubemapFileWithRegions
    | message_types.ImportCubemapRawData
    | message_types.ImportCubemapRawDataHDR
    | message_types.ImportMeshJSON
    | message_types.ImportMeshRawData
    | message_types.ImportAudioClipFile
    | message_types.ImportAudioClipRawData
    | message_types.GetComponentTypeList
    | message_types.GetComponentDefinition
    | message_types.GetTypeDefinition
    | message_types.GetGenericTypeDefinition
    | message_types.GetEnumDefinition
    | message_types.GetSyncObjectDefinition
    | message_types.RequestSessionData
    | message_types.DataModelOperationBatch
    | message_types.CallSyncMethod
    | message_types.CallStaticSyncMethod
)

type ResponseType = (
    response_types.Response
    | response_types.SlotData
    | response_types.ComponentData
    | response_types.AssetData
    | response_types.ComponentTypeList
    | response_types.ComponentDefinitionData
    | response_types.NewEntityId
)

type DataType = (
    PrimitiveType | MemberType | FieldType | WorkerType | MessageType | ResponseType
)

type JsonValue = (
    bool | int | float | str | list[JsonValue] | dict[str, JsonValue] | None
)

# =============================================================================
# Type Registry
# =============================================================================

# Maps $type string values to Python classes
_TYPE_REGISTRY: dict[str, type] = {}

# Maps Python classes to $type string values
_CLASS_TO_TYPE: dict[type, str] = {}


def _register_type(type_name: str, cls: type) -> None:
    """Register a type for encoding/decoding."""
    _TYPE_REGISTRY[type_name] = cls
    _CLASS_TO_TYPE[cls] = type_name


def _init_type_registry() -> None:
    """Initialize the type registry with all known types."""
    # Messages - $type is the message type in camelCase
    _register_type("getSlot", message_types.GetSlot)
    _register_type("addSlot", message_types.AddSlot)
    _register_type("updateSlot", message_types.UpdateSlot)
    _register_type("removeSlot", message_types.RemoveSlot)
    _register_type("getComponent", message_types.GetComponent)
    _register_type("addComponent", message_types.AddComponent)
    _register_type("updateComponent", message_types.UpdateComponent)
    _register_type("removeComponent", message_types.RemoveComponent)
    _register_type("importTexture2DFile", message_types.ImportTexture2DFile)
    _register_type("importTexture2DRawData", message_types.ImportTexture2DRawData)
    _register_type("importTexture2DRawDataHDR", message_types.ImportTexture2DRawDataHDR)
    _register_type("importCubemapFiles", message_types.ImportCubemapFiles)
    _register_type(
        "importCubemapFileWithRegions",
        message_types.ImportCubemapFileWithRegions,
    )
    _register_type("importCubemapRawData", message_types.ImportCubemapRawData)
    _register_type(
        "importCubemapRawDataHDR", message_types.ImportCubemapRawDataHDR,
    )
    _register_type("importMeshJSON", message_types.ImportMeshJSON)
    _register_type("importMeshRawData", message_types.ImportMeshRawData)
    _register_type("importAudioClipFile", message_types.ImportAudioClipFile)
    _register_type(
        "importAudioClipRawData", message_types.ImportAudioClipRawData,
    )
    _register_type("getComponentTypeList", message_types.GetComponentTypeList)
    _register_type("getComponentDefinition", message_types.GetComponentDefinition)
    _register_type("getTypeDefinition", message_types.GetTypeDefinition)
    _register_type(
        "getGenericTypeDefinition",
        message_types.GetGenericTypeDefinition,
    )
    _register_type("getEnumDefinition", message_types.GetEnumDefinition)
    _register_type(
        "getSyncObjectDefinition", message_types.GetSyncObjectDefinition,
    )
    _register_type("requestSessionData", message_types.RequestSessionData)
    _register_type(
        "dataModelOperationBatch",
        message_types.DataModelOperationBatch,
    )
    _register_type("callSyncMethod", message_types.CallSyncMethod)
    _register_type("callStaticSyncMethod", message_types.CallStaticSyncMethod)

    # Responses
    _register_type("response", response_types.Response)
    _register_type("newEntityId", response_types.NewEntityId)
    _register_type("slotData", response_types.SlotData)
    _register_type("componentData", response_types.ComponentData)
    _register_type("assetData", response_types.AssetData)
    _register_type("componentTypeList", response_types.ComponentTypeList)
    _register_type("componentDefinitionData", response_types.ComponentDefinitionData)

    # Workers
    _register_type("slot", worker_types.Slot)
    _register_type("component", worker_types.Component)

    # Members
    _register_type("reference", member_types.Reference)
    _register_type("list", member_types.SyncList)
    _register_type("syncObject", member_types.SyncObject)
    _register_type("emptyElement", member_types.EmptyElement)
    _register_type("empty", member_types.EmptyElement)
    _register_type("enum", member_types.FieldEnum)
    _register_type("enum?", member_types.FieldEnum)
    _register_type("playback", member_types.SyncPlayback)
    _register_type("dictionary<enum>", member_types.SyncDictionary)

    # Primitive Fields - standalone types
    _register_type("byte", field_types.FieldByte)
    _register_type("byte[]", field_types.ArrayByte)
    _register_type("byte?", field_types.FieldNullableByte)
    _register_type("ushort", field_types.FieldUshort)
    _register_type("ushort[]", field_types.ArrayUshort)
    _register_type("ushort?", field_types.FieldNullableUshort)
    _register_type("uint", field_types.FieldUint)
    _register_type("uint[]", field_types.ArrayUint)
    _register_type("uint?", field_types.FieldNullableUint)
    _register_type("ulong", field_types.FieldUlong)
    _register_type("ulong[]", field_types.ArrayUlong)
    _register_type("ulong?", field_types.FieldNullableUlong)
    _register_type("sbyte", field_types.FieldSbyte)
    _register_type("sbyte[]", field_types.ArraySbyte)
    _register_type("sbyte?", field_types.FieldNullableSbyte)
    _register_type("short", field_types.FieldShort)
    _register_type("short[]", field_types.ArrayShort)
    _register_type("short?", field_types.FieldNullableShort)
    _register_type("int", field_types.FieldInt)
    _register_type("int[]", field_types.ArrayInt)
    _register_type("int?", field_types.FieldNullableInt)
    _register_type("long", field_types.FieldLong)
    _register_type("long[]", field_types.ArrayLong)
    _register_type("long?", field_types.FieldNullableLong)
    _register_type("float", field_types.FieldFloat)
    _register_type("float[]", field_types.ArrayFloat)
    _register_type("float?", field_types.FieldNullableFloat)
    _register_type("double", field_types.FieldDouble)
    _register_type("double[]", field_types.ArrayDouble)
    _register_type("double?", field_types.FieldNullableDouble)
    _register_type("decimal", field_types.FieldDecimal)
    _register_type("decimal[]", field_types.ArrayDecimal)
    _register_type("decimal?", field_types.FieldNullableDecimal)
    _register_type("bool", field_types.FieldBool)
    _register_type("bool[]", field_types.ArrayBool)
    _register_type("bool?", field_types.FieldNullableBool)
    _register_type("char", field_types.FieldChar)
    _register_type("char[]", field_types.ArrayChar)
    _register_type("char?", field_types.FieldNullableChar)
    _register_type("string", field_types.FieldString)
    _register_type("string[]", field_types.ArrayString)
    _register_type("Uri", field_types.FieldUri)
    _register_type("Uri[]", field_types.ArrayUri)
    _register_type("TimeSpan", field_types.FieldTimeSpan)
    _register_type("TimeSpan[]", field_types.ArrayTimeSpan)
    _register_type("TimeSpan?", field_types.FieldNullableTimeSpan)
    _register_type("DateTime", field_types.FieldDateTime)
    _register_type("DateTime[]", field_types.ArrayDateTime)
    _register_type("DateTime?", field_types.FieldNullableDateTime)

    # Color fields
    _register_type("color", field_types.FieldColor)
    _register_type("color[]", field_types.ArrayColor)
    _register_type("color?", field_types.FieldNullableColor)
    _register_type("colorX", field_types.FieldColorX)
    _register_type("colorX[]", field_types.ArrayColorX)
    _register_type("colorX?", field_types.FieldNullableColorX)
    _register_type("color32", field_types.FieldColor32)
    _register_type("color32[]", field_types.ArrayColor32)
    _register_type("color32?", field_types.FieldNullableColor32)

    # 2D Vector fields
    _register_type("float2", field_types.FieldFloat2)
    _register_type("float2[]", field_types.ArrayFloat2)
    _register_type("float2?", field_types.FieldNullableFloat2)
    _register_type("double2", field_types.FieldDouble2)
    _register_type("double2[]", field_types.ArrayDouble2)
    _register_type("double2?", field_types.FieldNullableDouble2)
    _register_type("byte2", field_types.FieldByte2)
    _register_type("byte2[]", field_types.ArrayByte2)
    _register_type("byte2?", field_types.FieldNullableByte2)
    _register_type("ushort2", field_types.FieldUshort2)
    _register_type("ushort2[]", field_types.ArrayUshort2)
    _register_type("ushort2?", field_types.FieldNullableUshort2)
    _register_type("uint2", field_types.FieldUint2)
    _register_type("uint2[]", field_types.ArrayUint2)
    _register_type("uint2?", field_types.FieldNullableUint2)
    _register_type("ulong2", field_types.FieldUlong2)
    _register_type("ulong2[]", field_types.ArrayUlong2)
    _register_type("ulong2?", field_types.FieldNullableUlong2)
    _register_type("sbyte2", field_types.FieldSbyte2)
    _register_type("sbyte2[]", field_types.ArraySbyte2)
    _register_type("sbyte2?", field_types.FieldNullableSbyte2)
    _register_type("short2", field_types.FieldShort2)
    _register_type("short2[]", field_types.ArrayShort2)
    _register_type("short2?", field_types.FieldNullableShort2)
    _register_type("int2", field_types.FieldInt2)
    _register_type("int2[]", field_types.ArrayInt2)
    _register_type("int2?", field_types.FieldNullableInt2)
    _register_type("long2", field_types.FieldLong2)
    _register_type("long2[]", field_types.ArrayLong2)
    _register_type("long2?", field_types.FieldNullableLong2)
    _register_type("bool2", field_types.FieldBool2)
    _register_type("bool2[]", field_types.ArrayBool2)
    _register_type("bool2?", field_types.FieldNullableBool2)

    # 3D Vector fields
    _register_type("float3", field_types.FieldFloat3)
    _register_type("float3[]", field_types.ArrayFloat3)
    _register_type("float3?", field_types.FieldNullableFloat3)
    _register_type("double3", field_types.FieldDouble3)
    _register_type("double3[]", field_types.ArrayDouble3)
    _register_type("double3?", field_types.FieldNullableDouble3)
    _register_type("byte3", field_types.FieldByte3)
    _register_type("byte3[]", field_types.ArrayByte3)
    _register_type("byte3?", field_types.FieldNullableByte3)
    _register_type("ushort3", field_types.FieldUshort3)
    _register_type("ushort3[]", field_types.ArrayUshort3)
    _register_type("ushort3?", field_types.FieldNullableUshort3)
    _register_type("uint3", field_types.FieldUint3)
    _register_type("uint3[]", field_types.ArrayUint3)
    _register_type("uint3?", field_types.FieldNullableUint3)
    _register_type("ulong3", field_types.FieldUlong3)
    _register_type("ulong3[]", field_types.ArrayUlong3)
    _register_type("ulong3?", field_types.FieldNullableUlong3)
    _register_type("sbyte3", field_types.FieldSbyte3)
    _register_type("sbyte3[]", field_types.ArraySbyte3)
    _register_type("sbyte3?", field_types.FieldNullableSbyte3)
    _register_type("short3", field_types.FieldShort3)
    _register_type("short3[]", field_types.ArrayShort3)
    _register_type("short3?", field_types.FieldNullableShort3)
    _register_type("int3", field_types.FieldInt3)
    _register_type("int3[]", field_types.ArrayInt3)
    _register_type("int3?", field_types.FieldNullableInt3)
    _register_type("long3", field_types.FieldLong3)
    _register_type("long3[]", field_types.ArrayLong3)
    _register_type("long3?", field_types.FieldNullableLong3)
    _register_type("bool3", field_types.FieldBool3)
    _register_type("bool3[]", field_types.ArrayBool3)
    _register_type("bool3?", field_types.FieldNullableBool3)

    # 4D Vector fields
    _register_type("float4", field_types.FieldFloat4)
    _register_type("float4[]", field_types.ArrayFloat4)
    _register_type("float4?", field_types.FieldNullableFloat4)
    _register_type("double4", field_types.FieldDouble4)
    _register_type("double4[]", field_types.ArrayDouble4)
    _register_type("double4?", field_types.FieldNullableDouble4)
    _register_type("byte4", field_types.FieldByte4)
    _register_type("byte4[]", field_types.ArrayByte4)
    _register_type("byte4?", field_types.FieldNullableByte4)
    _register_type("ushort4", field_types.FieldUshort4)
    _register_type("ushort4[]", field_types.ArrayUshort4)
    _register_type("ushort4?", field_types.FieldNullableUshort4)
    _register_type("uint4", field_types.FieldUint4)
    _register_type("uint4[]", field_types.ArrayUint4)
    _register_type("uint4?", field_types.FieldNullableUint4)
    _register_type("ulong4", field_types.FieldUlong4)
    _register_type("ulong4[]", field_types.ArrayUlong4)
    _register_type("ulong4?", field_types.FieldNullableUlong4)
    _register_type("sbyte4", field_types.FieldSbyte4)
    _register_type("sbyte4[]", field_types.ArraySbyte4)
    _register_type("sbyte4?", field_types.FieldNullableSbyte4)
    _register_type("short4", field_types.FieldShort4)
    _register_type("short4[]", field_types.ArrayShort4)
    _register_type("short4?", field_types.FieldNullableShort4)
    _register_type("int4", field_types.FieldInt4)
    _register_type("int4[]", field_types.ArrayInt4)
    _register_type("int4?", field_types.FieldNullableInt4)
    _register_type("long4", field_types.FieldLong4)
    _register_type("long4[]", field_types.ArrayLong4)
    _register_type("long4?", field_types.FieldNullableLong4)
    _register_type("bool4", field_types.FieldBool4)
    _register_type("bool4[]", field_types.ArrayBool4)
    _register_type("bool4?", field_types.FieldNullableBool4)

    # Quaternion fields
    _register_type("floatQ", field_types.FieldFloatQ)
    _register_type("floatQ[]", field_types.ArrayFloatQ)
    _register_type("floatQ?", field_types.FieldNullableFloatQ)
    _register_type("doubleQ", field_types.FieldDoubleQ)
    _register_type("doubleQ[]", field_types.ArrayDoubleQ)
    _register_type("doubleQ?", field_types.FieldNullableDoubleQ)

    # Matrix fields
    _register_type("float2x2", field_types.FieldFloat2x2)
    _register_type("float2x2[]", field_types.ArrayFloat2x2)
    _register_type("float2x2?", field_types.FieldNullableFloat2x2)
    _register_type("double2x2", field_types.FieldDouble2x2)
    _register_type("double2x2[]", field_types.ArrayDouble2x2)
    _register_type("double2x2?", field_types.FieldNullableDouble2x2)
    _register_type("float3x3", field_types.FieldFloat3x3)
    _register_type("float3x3[]", field_types.ArrayFloat3x3)
    _register_type("float3x3?", field_types.FieldNullableFloat3x3)
    _register_type("double3x3", field_types.FieldDouble3x3)
    _register_type("double3x3[]", field_types.ArrayDouble3x3)
    _register_type("double3x3?", field_types.FieldNullableDouble3x3)
    _register_type("float4x4", field_types.FieldFloat4x4)
    _register_type("float4x4[]", field_types.ArrayFloat4x4)
    _register_type("float4x4?", field_types.FieldNullableFloat4x4)
    _register_type("double4x4", field_types.FieldDouble4x4)
    _register_type("double4x4[]", field_types.ArrayDouble4x4)
    _register_type("double4x4?", field_types.FieldNullableDouble4x4)

    # Geometry Fields
    _register_type("Rect", field_types.FieldRect)
    _register_type("BoundingBox", field_types.FieldBoundingBox)


# Initialize the registry
_init_type_registry()


# =============================================================================
# Primitive Type Detection
# =============================================================================

# Set of primitive dataclass types that should be encoded as plain dicts
# (without $type) when nested inside a "value" field
_PRIMITIVE_TYPES: set[type] = {
    primitive_types.Color,
    primitive_types.ColorX,
    primitive_types.Color32,
    primitive_types.Float2,
    primitive_types.Double2,
    primitive_types.Byte2,
    primitive_types.UShort2,
    primitive_types.UInt2,
    primitive_types.ULong2,
    primitive_types.SByte2,
    primitive_types.Short2,
    primitive_types.Int2,
    primitive_types.Long2,
    primitive_types.Bool2,
    primitive_types.Float3,
    primitive_types.Double3,
    primitive_types.Byte3,
    primitive_types.UShort3,
    primitive_types.UInt3,
    primitive_types.ULong3,
    primitive_types.SByte3,
    primitive_types.Short3,
    primitive_types.Int3,
    primitive_types.Long3,
    primitive_types.Bool3,
    primitive_types.Float4,
    primitive_types.Double4,
    primitive_types.Byte4,
    primitive_types.UShort4,
    primitive_types.UInt4,
    primitive_types.ULong4,
    primitive_types.SByte4,
    primitive_types.Short4,
    primitive_types.Int4,
    primitive_types.Long4,
    primitive_types.Bool4,
    primitive_types.FloatQ,
    primitive_types.DoubleQ,
    primitive_types.Float2x2,
    primitive_types.Double2x2,
    primitive_types.Float3x3,
    primitive_types.Double3x3,
    primitive_types.Float4x4,
    primitive_types.Double4x4,
    primitive_types.Rect,
    primitive_types.BoundingBox,
}


def _is_primitive_type(cls: type) -> bool:
    """Check if a class is a primitive type (vector, quaternion, matrix, Color)."""
    return cls in _PRIMITIVE_TYPES


def _json_safe(value: Any) -> Any:
    """Convert a value to a JSON-safe Python type.

    Numpy scalars become plain int/float so json.dumps can serialize them.
    """
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.bool_):
        return bool(value)
    return value


def _encode_primitive(value: Any) -> dict[str, Any]:
    """Encode a primitive value to a JSON-compatible dict.

    Handles special nested wire formats for Rect and BoundingBox.
    Other primitives use flat ``asdict()`` with numpy scalar conversion.
    """
    if isinstance(value, primitive_types.Rect):
        return {
            "position": {
                "x": _json_safe(value.x),
                "y": _json_safe(value.y),
            },
            "size": {
                "x": _json_safe(value.width),
                "y": _json_safe(value.height),
            },
        }
    if isinstance(value, primitive_types.BoundingBox):
        return {
            "min": {
                "x": _json_safe(value.min_x),
                "y": _json_safe(value.min_y),
                "z": _json_safe(value.min_z),
            },
            "max": {
                "x": _json_safe(value.max_x),
                "y": _json_safe(value.max_y),
                "z": _json_safe(value.max_z),
            },
        }
    return {k: _json_safe(v) for k, v in asdict(value).items() if v is not None}


# =============================================================================
# Encoding
# =============================================================================

type EncodableType = (
    bool
    | int
    | float
    | str
    | list[EncodableType]
    | dict[str, EncodableType]
    | DataType
    | None
)


def _encode_value(value: EncodableType) -> Any:
    """Encode a single value to JSON-compatible format.

    Args:
        value: Any Python value to encode.

    Returns:
        A JSON-compatible value (dict, list, or primitive).

    Raises:
        ValueError: If value is not an encodable type.
    """
    if value is None:
        return None

    if isinstance(value, (bool, int, float, str)):
        return value

    if isinstance(value, np.integer):
        return int(value)

    if isinstance(value, np.floating):
        return float(value)

    if isinstance(value, Decimal):
        return str(value)

    if isinstance(value, list):
        return [_encode_value(item) for item in value]

    if isinstance(value, dict):
        return {k: _encode_value(v) for k, v in value.items() if v is not None}

    if is_dataclass(value) and not isinstance(value, type):
        cls = type(value)
        if cls in _CLASS_TO_TYPE or cls in _PRIMITIVE_TYPES:
            return _encode_dataclass(value)

    raise ValueError(f"Cannot encode value of type {type(value).__name__}: {value!r}")


def _encode_dataclass(obj: DataType) -> dict[str, EncodableType]:
    """Encode a dataclass instance to a JSON-compatible dict.

    Args:
        obj: A dataclass instance of one of the ResoniteLink data types.

    Returns:
        A dictionary with $type and encoded fields.
    """
    cls: type = type(obj)
    result: dict[str, EncodableType] = {}

    # Add $type if this class is registered (not for primitives)
    if cls in _CLASS_TO_TYPE:
        result["$type"] = _CLASS_TO_TYPE[cls]

    # Encode each field
    for f in fields(obj):
        # Skip fields marked with json_ignore
        if f.metadata.get(JSON_IGNORE_KEY):
            continue

        value: EncodableType = getattr(obj, f.name)

        # Skip None values (sparse serialization)
        if value is None:
            continue

        # Skip empty lists/dicts
        if isinstance(value, (list, dict)) and len(value) == 0:
            continue

        # Encode the value
        encoded = _encode_value(value)

        # For primitive types nested in "value" field, just use the dict
        # without $type
        if is_dataclass(value) and _is_primitive_type(type(value)):
            encoded = _encode_primitive(value)

        result[f.name] = encoded

    return result


def encode(obj: DataType) -> dict[str, Any]:
    """Encode a message or response object to JSON-compatible dict.

    Args:
        obj: A dataclass instance of one of the ResoniteLink data types.

    Returns:
        A dictionary ready for JSON serialization.

    Example:
        >>> msg = AddSlot(
        ...     data=Slot(
        ...         id="MySDK_0",
        ...         parent=Reference(targetId="Root"),
        ...         name=FieldString(value="Hello from MySDK!"),
        ...         position=FieldFloat3(value=Float3(x=0, y=1.5, z=10))
        ...     )
        ... )
        >>> json_dict = encode(msg)
    """
    return _encode_dataclass(obj)


# =============================================================================
# Decoding
# =============================================================================


def _get_field_types(cls: type) -> dict[str, Any]:
    """Get a mapping of field names to their types for a dataclass.

    Returns the full generic type (e.g., list[Slot]) to preserve element type info.
    """
    result: dict[str, Any] = {}
    for field in fields(cls):
        # Get the actual type, handling Optional types
        field_type = field.type

        # Handle X | None (Python 3.10+ union syntax)
        if isinstance(field_type, types.UnionType):
            args = field_type.__args__
            for arg in args:
                if arg is not type(None):
                    field_type = arg
                    break
        elif get_origin(field_type) is not None:
            origin = get_origin(field_type)
            args = get_args(field_type)

            # Handle Optional[X] which is Union[X, None]
            if origin is type(None) or str(origin).startswith("typing.Union"):
                args = getattr(field_type, "__args__", ())
                for arg in args:
                    if arg is not type(None):
                        field_type = arg
                        break
            # For list[X] and dict[K, V], keep the full generic type
            # so we can extract element types later
        result[field.name] = field_type
    return result


def _decode_primitive(data: dict[str, Any], cls: type) -> Any:
    """Decode a primitive type (vector, matrix, Color, quaternion).

    Handles special nested wire formats for Rect and BoundingBox.

    Args:
        data: Dictionary with primitive fields.
        cls: The primitive dataclass type.

    Returns:
        An instance of the primitive type.
    """
    if cls is primitive_types.Rect:
        pos = data.get("position", {})
        size = data.get("size", {})
        return primitive_types.Rect(
            x=pos.get("x", 0), y=pos.get("y", 0),
            width=size.get("x", 0), height=size.get("y", 0),
        )
    if cls is primitive_types.BoundingBox:
        mn = data.get("min", {})
        mx = data.get("max", {})
        return primitive_types.BoundingBox(
            min_x=mn.get("x", 0), min_y=mn.get("y", 0), min_z=mn.get("z", 0),
            max_x=mx.get("x", 0), max_y=mx.get("y", 0), max_z=mx.get("z", 0),
        )
    kwargs = {}
    for field in fields(cls):
        if field.name in data:
            kwargs[field.name] = data[field.name]
    return cls(**kwargs)


def _decode_value(data: JsonValue, expected_type: type | None = None) -> Any:
    """Decode a JSON value to a Python object.

    Args:
        data: The JSON data (dict, list, or primitive).
        expected_type: Optional type hint for the expected result.

    Returns:
        A Python object (dataclass instance, list, or primitive).
    """
    if data is None:
        return None

    if isinstance(data, (bool, int, float, str)):
        return data

    if isinstance(data, list):
        # For lists, try to decode each item
        return [_decode_value(item) for item in data]

    assert isinstance(data, dict)

    # Check for $type discriminator
    type_name = data.get("$type")

    if type_name and type_name in _TYPE_REGISTRY:
        assert isinstance(type_name, str), f"Invalid type for $type: {type(type_name)}"
        cls = _TYPE_REGISTRY[type_name]
        return _decode_dataclass(data, cls)

    # If expected_type is a primitive, decode as primitive
    if expected_type and _is_primitive_type(expected_type):
        return _decode_primitive(data, expected_type)

    # If expected_type is a registered type, decode as that type
    if expected_type and expected_type in _CLASS_TO_TYPE:
        return _decode_dataclass(data, expected_type)

    # If expected_type is a dataclass (like Slot), decode as that type
    if expected_type and is_dataclass(expected_type):
        return _decode_dataclass(data, expected_type)

    # Return as plain dict if we can't determine the type
    return data


def _decode_dataclass(data: dict[str, Any], cls: type) -> Any:
    """Decode a dictionary to a dataclass instance.

    Args:
        data: Dictionary with field data.
        cls: The dataclass type to instantiate.

    Returns:
        An instance of the dataclass.
    """
    _field_types = _get_field_types(cls)
    kwargs = {}

    for f in fields(cls):
        # Skip fields marked with json_ignore
        if f.metadata.get(JSON_IGNORE_KEY):
            continue

        if f.name not in data or f.name == "$type":
            continue

        value = data[f.name]
        field_type = _field_types.get(f.name)

        # Handle nested dataclasses
        if isinstance(value, dict):
            value = cast(dict[str, JsonValue], value)
            # Check if value has $type
            if "$type" in value:
                kwargs[f.name] = _decode_value(value)
            elif field_type and isinstance(field_type, type) and is_dataclass(field_type):
                # Decode using expected type
                if _is_primitive_type(field_type):
                    kwargs[f.name] = _decode_primitive(value, field_type)
                else:
                    kwargs[f.name] = _decode_dataclass(value, field_type)
            else:
                # Handle dict fields (like members in Component)
                origin = get_origin(field_type) if field_type else None
                if field_type is dict or (origin is not None and origin is dict):
                    # Decode each value in the dict
                    kwargs[f.name] = {k: _decode_value(v) for k, v in value.items()}
                else:
                    kwargs[f.name] = value
        elif isinstance(value, list):
            value = cast(list[JsonValue], value)
            # Handle list fields - try to get the element type from the type hint
            element_type = None
            if field_type is not None:
                origin = get_origin(field_type)
                if origin is list:
                    args = get_args(field_type)
                    if args:
                        element_type = args[0]
                        # Handle forward references like "Slot"
                        if isinstance(element_type, str):
                            element_type = _TYPE_REGISTRY.get(element_type.lower())
            kwargs[f.name] = [_decode_value(item, element_type) for item in value]
        else:
            kwargs[f.name] = value

    return cls(**kwargs)


def decode(data: dict[str, JsonValue]) -> Any:
    """Decode a JSON dictionary to a Python dataclass instance.

    Args:
        data: A dictionary from JSON parsing.

    Returns:
        A dataclass instance (typically a Message or Response subclass).

    Raises:
        ValueError: If $type is missing or unknown.

    Example:
        >>> json_data = {
        ...     "$type": "slotData",
        ...     "success": True,
        ...     "data": {
        ...         "id": "Reso_123",
        ...         "name": {"$type": "string", "value": "MySlot"}
        ...     }
        ... }
        >>> response = decode(json_data)
    """
    type_name = data.get("$type")
    if not type_name:
        raise ValueError("Missing $type field in JSON data")
    assert isinstance(type_name, str), f"Invalid type for $type: {type(type_name)}"

    if type_name not in _TYPE_REGISTRY:
        raise ValueError(f"Unknown type: {type_name}")

    cls = _TYPE_REGISTRY[type_name]
    return _decode_dataclass(data, cls)


def decode_response(data: dict[str, JsonValue]) -> response_types.Response:
    """Decode a JSON dictionary to a Response object.

    This is a convenience wrapper around decode() that provides
    type hints for the return value.

    Args:
        data: A dictionary from JSON parsing.

    Returns:
        A Response subclass instance.
    """
    result = decode(data)
    if not isinstance(result, response_types.Response):
        raise TypeError(f"Expected Response, got {type(result)}")
    return result


def decode_message(data: dict[str, JsonValue]) -> message_types.Message:
    """Decode a JSON dictionary to a Message object.

    This is a convenience wrapper around decode() that provides
    type hints for the return value.

    Args:
        data: A dictionary from JSON parsing.

    Returns:
        A Message subclass instance.
    """
    result = decode(data)
    if not isinstance(result, message_types.Message):
        raise TypeError(f"Expected Message, got {type(result)}")
    return result
