"""Message types for ResoniteLink communication.

This module contains message classes used to send commands to Resonite.
"""

# pylint: disable=invalid-name

import abc
from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np

from . import mesh
from .members import DataReference, Member
from .primitives import Rect
from .workers import Component, Slot
from .utils import json_ignore


@dataclass
class Message:
    """Base class for all messages/commands sent to Resonite."""

    messageId: str | None = None


# =============================================================================
# Slot Messages
# =============================================================================


@dataclass
class GetSlot(Message):
    """Request to fetch slot data.

    The response is a SlotData.

    Args:
        slotId: Unique ID of the slot to fetch. Use "Root" for the root slot.
        depth: How deep to fetch the hierarchy.
            0 = only the requested slot
            1 = include immediate children
            -1 = fetch everything
        includeComponentData: Whether to fetch full component data or just references.
    """

    slotId: str | None = None
    depth: int = 0
    includeComponentData: bool = False


@dataclass
class AddUpdateSlotData(Message):
    """Base for slot add/update messages."""

    data: Slot | None = None


@dataclass
class AddSlot(AddUpdateSlotData):
    """Request to add a new slot."""


@dataclass
class UpdateSlot(AddUpdateSlotData):
    """Request to update an existing slot."""


@dataclass
class RemoveSlot(Message):
    """Request to remove a slot.

    Args:
        slotId: The ID of the slot to remove.
    """

    slotId: str | None = None


# =============================================================================
# Component Messages
# =============================================================================


@dataclass
class GetComponent(Message):
    """Request to fetch component data.

    The response is a ComponentData.

    Args:
        componentId: The ID of the component to fetch.
    """

    componentId: str | None = None


@dataclass
class AddUpdateComponent(Message):
    """Base for component add/update messages."""

    data: Component | None = None


@dataclass
class AddComponent(AddUpdateComponent):
    """Request to add a new component to a slot.

    Args:
        containerSlotId: The ID of the slot to add the component to.
        data: The component data to add.
    """

    containerSlotId: str | None = None


@dataclass
class UpdateComponent(AddUpdateComponent):
    """Request to update an existing component."""


@dataclass
class RemoveComponent(Message):
    """Request to remove a component.

    Args:
        componentId: The ID of the component to remove.
    """

    componentId: str | None = None


@dataclass
class GetComponentTypeList(Message):
    """Request to fetch a list of component types.

    The response is a ComponentTypeList.

    Args:
        categoryPath: The category, such as "/Data". None or "/" is the
            root category, whose response lists its subcategories. The
            doc comment on CategoryPath, in ResoniteLink's
            ResoniteLink/Models/Messages/Reflection/GetComponentDefinitionList.cs,
            says that "*" lists every component, but as of Resonite
            2026.9.18.82 it returns nothing.
    """

    categoryPath: str | None = None


@dataclass
class GetComponentDefinition(Message):
    """Request to fetch a component's type definition.

    The response is a ComponentDefinitionData.

    Args:
        componentType: The fully qualified component type name. Must be a
            generic type definition for generic components.
        flattened: Whether to include inherited members from base classes.
            When True, all members are included. When False, only members
            declared directly on the type are returned.
    """

    componentType: str | None = None
    flattened: bool = True


@dataclass
class GetTypeDefinition(Message):
    """Request to fetch a type's definition.

    Unlike GetComponentDefinition, this works on any type -- interfaces,
    enums, value types, etc.

    Args:
        type: Full name of the type to fetch. Can be a generic type
            definition or a constructed generic type.
    """

    type: str | None = None


@dataclass
class GetSyncObjectDefinition(Message):
    """Request to fetch a sync object's definition.

    Returns member structure for sync objects (types that inherit from
    ``SyncObject``, like ``UserRef``).  Similar to
    ``GetComponentDefinition`` but for non-component sync object types.

    The response ``$type`` is ``syncObjectDefinitionData``.

    Args:
        syncObjectType: Full name of the sync object type.
        flattened: Whether to include inherited members from base classes.
    """

    syncObjectType: str | None = None
    flattened: bool = True


@dataclass
class GetGenericTypeDefinition(Message):
    """Get the generic type definition for a generic instance type.

    Given a constructed generic like ``MyComponent<int>``, returns
    the generic definition ``MyComponent<T>``.

    Args:
        genericInstanceType: The constructed generic type string.
    """

    genericInstanceType: str | None = None


@dataclass
class GetEnumDefinition(Message):
    """Get the definition of an enum type.

    Args:
        type: Full name of the enum type.
    """

    type: str | None = None


# =============================================================================
# Method Call Messages
# =============================================================================


@dataclass
class CallSyncMethod(Message):
    """Call a method on a component or sync member instance.

    Invokes the named method on the target identified by ``targetID``.
    Arguments are passed as a dict mapping parameter names to values.

    The response ``$type`` is ``methodResult`` with a ``result`` field.

    Args:
        targetID: ID of the component or sync member to call the method on.
        methodName: Name of the method to call.
        arguments: Named arguments to the method, mapping parameter
            name to value. The server only accepts values tagged with a
            ``$type``, so a primitive is passed as its field class, such as
            ``FieldInt(value=2)``, and a reference as a ``DataReference``.
            A bare value such as ``2`` fails with "The JSON value could
            not be converted to ResoniteLink.Data".
    """

    targetID: str | None = None
    methodName: str | None = None
    arguments: dict[str, Member | DataReference] | None = None


@dataclass
class CallStaticSyncMethod(Message):
    """Call a static method on a type.

    Invokes a static method by type name, without needing an instance.

    The response ``$type`` is ``methodResult`` with a ``result`` field.

    Args:
        targetType: Fully qualified type name.
        methodName: Name of the static method to call.
        arguments: Named arguments to the method, mapping parameter
            name to value, tagged as for ``CallSyncMethod``.
    """

    targetType: str | None = None
    methodName: str | None = None
    arguments: dict[str, Member | DataReference] | None = None


# =============================================================================
# Session Messages
# =============================================================================


@dataclass
class RequestSessionData(Message):
    """Request session data of the current ResoniteLink session.

    The response is a SessionData.
    """


# =============================================================================
# Batch Messages
# =============================================================================


@dataclass
class DataModelOperationBatch(Message):
    """Batch of data model operations processed atomically.

    All operations are guaranteed to be processed in sequence without
    any engine updates in between.  Only messages that derive from
    data model operations (slot/component CRUD) can be included.

    Args:
        operations: List of data model operation messages.
    """

    operations: list[Message] | None = None


@dataclass
class BinaryPayloadMessage(Message):
    """A message with a binary payload.

    The payload is sent as a separate binary WebSocket message right after
    the JSON message.
    """

    payload: bytearray | None = json_ignore(default=None)

    def expected_payload_size(self) -> int | None:
        """Returns the payload size in bytes that the server will expect.

        The server rejects a payload of any other size. None means that
        the size isn't known here.
        """
        return None


# =============================================================================
# Asset Import Messages — Texture 2D
# =============================================================================


@dataclass
class ImportTexture2DFile(Message):
    """Import a texture asset from a file on the local file system.

    Note that this must be a file format supported by Resonite, otherwise this
    will fail. If you are unsure if the file format is supported, send raw
    texture data instead.

    Args:
        filePath: Path of the texture file to import.
    """

    filePath: str | None = None


@dataclass
class ImportTexture2DRawDataBase(abc.ABC, BinaryPayloadMessage):
    """Base class for importing textures from raw color data.

    Args:
        width: Width of the texture in pixels.
        height: Height of the texture in pixels.
    """

    width: int = 0
    height: int = 0

    # Bytes per pixel: 4 for color32, 16 for color.
    _BYTES_PER_PIXEL = 4

    def expected_payload_size(self) -> int | None:
        """Returns width * height pixels of the subclass's pixel size."""
        return self.width * self.height * self._BYTES_PER_PIXEL

    def _access_raw_data(self, bytes_per_element: int) -> bytearray:
        """Returns, optionally creating, a bytearray for the data.

        Pixel (x, y) is at index x + y * width, so rows follow each other.

        Raises:
            ValueError: The width or height isn't positive, or an existing
                payload has the wrong size.
        """
        if self.width <= 0:
            raise ValueError("width must be greater than 0")
        if self.height <= 0:
            raise ValueError("height must be greater than 0")

        num_bytes = self.width * self.height * bytes_per_element
        if self.payload is None:
            self.payload = bytearray(num_bytes)
        elif len(self.payload) != num_bytes:
            raise ValueError(
                f"payload is {len(self.payload)} bytes, but {self.width}x"
                f"{self.height} pixels take {num_bytes}"
            )
        return self.payload

    @abc.abstractmethod
    def access_raw_data(self) -> bytearray:
        """Returns, optionally creating, a bytearray for the data."""


@dataclass
class ImportTexture2DRawData(ImportTexture2DRawDataBase):
    """Imports texture from raw 8-bit color data.

    Resonite will take care of encoding the data into a file format.
    The binary payload should contain color32 data (RGBA, 4 bytes per pixel).

    Args:
        width: Width of the texture in pixels.
        height: Height of the texture in pixels.
        colorProfile: Color profile of the texture color data.
    """

    colorProfile: str | None = None

    def access_raw_data(self) -> bytearray:
        return super()._access_raw_data(bytes_per_element=4)

    @classmethod
    def from_pixels(
        cls, pixels: np.ndarray, colorProfile: str = "sRGB",
    ) -> "ImportTexture2DRawData":
        """Returns the message for an RGBA image.

        Args:
            pixels: The image, shaped (height, width, 4), as uint8. Row 0
                of the array is y = 0.
            colorProfile: The color profile of the data, e.g. "sRGB" or
                "Linear".
        """
        pixels = np.ascontiguousarray(pixels, dtype=np.uint8)
        if pixels.ndim != 3 or pixels.shape[2] != 4:
            raise ValueError(f"pixels must be (height, width, 4), not {pixels.shape}")
        height, width = pixels.shape[:2]
        return cls(
            width=width, height=height, colorProfile=colorProfile,
            payload=bytearray(pixels.tobytes()),
        )


@dataclass
class ImportTexture2DRawDataHDR(ImportTexture2DRawDataBase):
    """Imports texture from raw floating point color data, allowing for HDR values.

    Resonite will take care of encoding the data into a file format.
    The binary payload should contain color data (RGBA, 4 float32s per pixel).

    Args:
        width: Width of the texture in pixels.
        height: Height of the texture in pixels.
    """

    _BYTES_PER_PIXEL = 16

    def access_raw_data(self) -> bytearray:
        return super()._access_raw_data(bytes_per_element=4*4)

    @classmethod
    def from_pixels(cls, pixels: np.ndarray) -> "ImportTexture2DRawDataHDR":
        """Returns the message for a floating point RGBA image.

        Args:
            pixels: The image, shaped (height, width, 4), as float32. Row 0
                of the array is y = 0.
        """
        pixels = np.ascontiguousarray(pixels, dtype="<f4")
        if pixels.ndim != 3 or pixels.shape[2] != 4:
            raise ValueError(f"pixels must be (height, width, 4), not {pixels.shape}")
        height, width = pixels.shape[:2]
        return cls(width=width, height=height, payload=bytearray(pixels.tobytes()))


# =============================================================================
# Asset Import Messages — Cubemap
# =============================================================================


@dataclass
class ImportCubemapFiles(Message):
    """Import a cubemap from six face image files on the local file system.

    All files should ideally be the same format and size.

    Args:
        filePathPositiveX: Path to the +X face image.
        filePathPositiveY: Path to the +Y face image.
        filePathPositiveZ: Path to the +Z face image.
        filePathNegativeX: Path to the -X face image.
        filePathNegativeY: Path to the -Y face image.
        filePathNegativeZ: Path to the -Z face image.
    """

    filePathPositiveX: str | None = None
    filePathPositiveY: str | None = None
    filePathPositiveZ: str | None = None
    filePathNegativeX: str | None = None
    filePathNegativeY: str | None = None
    filePathNegativeZ: str | None = None


@dataclass
class ImportCubemapFileWithRegions(Message):
    """Import a cubemap from a single image file with face regions.

    Regions are in normalized coordinates (0..1), as Rects whose x and y
    are the region's corner.

    Args:
        filePath: Path to the image file.
        positiveXregion: Normalized region for the +X face.
        positiveYregion: Normalized region for the +Y face.
        positiveZregion: Normalized region for the +Z face.
        negativeXregion: Normalized region for the -X face.
        negativeYregion: Normalized region for the -Y face.
        negativeZregion: Normalized region for the -Z face.
    """

    filePath: str | None = None
    positiveXregion: Rect | None = None
    positiveYregion: Rect | None = None
    positiveZregion: Rect | None = None
    negativeXregion: Rect | None = None
    negativeYregion: Rect | None = None
    negativeZregion: Rect | None = None


def _cubemap_mip_count(size: int, mip_maps: bool) -> int:
    """Returns the number of mip levels in a cubemap payload.

    With mip maps, the levels halve the size until it reaches 1, so a
    size of 8 has levels of 8, 4, 2, and 1.
    """
    if not mip_maps:
        return 1
    count = 1
    while size > 1:
        size >>= 1
        count += 1
    return count


def _cubemap_payload_size(size: int, mip_maps: bool, bytes_per_pixel: int) -> int:
    """Returns the bytes in a cubemap payload: six faces per mip level."""
    return sum(
        6 * (size >> level) ** 2 * bytes_per_pixel
        for level in range(_cubemap_mip_count(size, mip_maps))
    )


def _cubemap_levels_payload(
    levels: Sequence[np.ndarray], dtype: str,
) -> tuple[int, bool, bytearray]:
    """Packs a cubemap's mip levels into a payload.

    The payload holds each mip level in turn, largest first, and within a
    level the faces +X, +Y, +Z, -X, -Y, -Z.

    Args:
        levels: The mip levels, each shaped (6, size, size, 4) in that face
            order. One level means no mip maps. More than one must be the
            whole chain down to 1x1.
        dtype: The element type, "u1" or "<f4".

    Returns:
        The face size, whether there are mip maps, and the payload.
    """
    if not levels:
        raise ValueError("A cubemap needs at least one mip level")
    arrays = [np.ascontiguousarray(level, dtype=dtype) for level in levels]
    size = arrays[0].shape[1]
    mip_maps = len(arrays) > 1
    expected = _cubemap_mip_count(size, mip_maps)
    if len(arrays) != expected:
        raise ValueError(
            f"A {size}x{size} cubemap with mip maps has {expected} levels, "
            f"not {len(arrays)}"
        )
    for level, array in enumerate(arrays):
        level_size = size >> level
        if array.shape != (6, level_size, level_size, 4):
            raise ValueError(
                f"Mip level {level} must be (6, {level_size}, {level_size}, 4), "
                f"not {array.shape}"
            )
    return size, mip_maps, bytearray(b"".join(a.tobytes() for a in arrays))


@dataclass
class ImportCubemapRawData(BinaryPayloadMessage):
    """Import a cubemap from raw 8-bit color data (color32, RGBA).

    Args:
        size: Size of each square face in pixels.
        mipMaps: Whether mipmap data is included.
        colorProfile: Color profile of the color data.
    """

    size: int = 0
    mipMaps: bool = False
    colorProfile: str | None = None

    def expected_payload_size(self) -> int | None:
        """Returns the size of every face of every mip level, 4 bytes a pixel."""
        return _cubemap_payload_size(self.size, self.mipMaps, 4)

    @classmethod
    def from_levels(
        cls, levels: Sequence[np.ndarray], colorProfile: str = "sRGB",
    ) -> "ImportCubemapRawData":
        """Returns the message for a cubemap of RGBA faces.

        Args:
            levels: The mip levels, each shaped (6, size, size, 4) as uint8,
                with the faces in the order +X, +Y, +Z, -X, -Y, -Z. One
                level means no mip maps. More than one must be the whole
                chain down to 1x1.
            colorProfile: The color profile of the data.
        """
        size, mip_maps, payload = _cubemap_levels_payload(levels, "u1")
        return cls(
            size=size, mipMaps=mip_maps, colorProfile=colorProfile,
            payload=payload,
        )


@dataclass
class ImportCubemapRawDataHDR(BinaryPayloadMessage):
    """Import a cubemap from raw floating-point color data (HDR).

    Args:
        size: Size of each square face in pixels.
        mipMaps: Whether mipmap data is included.
    """

    size: int = 0
    mipMaps: bool = False

    def expected_payload_size(self) -> int | None:
        """Returns the size of every face of every mip level, 16 bytes a pixel."""
        return _cubemap_payload_size(self.size, self.mipMaps, 16)

    @classmethod
    def from_levels(cls, levels: Sequence[np.ndarray]) -> "ImportCubemapRawDataHDR":
        """Returns the message for a cubemap of floating point RGBA faces.

        Args:
            levels: The mip levels, each shaped (6, size, size, 4) as
                float32, as for ImportCubemapRawData.from_levels.
        """
        size, mip_maps, payload = _cubemap_levels_payload(levels, "<f4")
        return cls(size=size, mipMaps=mip_maps, payload=payload)


# =============================================================================
# Asset Import Messages — Mesh
# =============================================================================


@dataclass
class ImportMeshJSON(Message):
    """Import a mesh from a JSON definition.

    Verbose but convenient for small meshes. Use ImportMeshRawData for
    better efficiency with larger meshes.

    Args:
        vertices: The vertices.
        submeshes: The submeshes, which index into the vertices.
        bones: The bones, for a skinned mesh.
        blendshapes: The blendshapes.
    """

    vertices: list[mesh.Vertex] | None = None
    submeshes: (
        list[mesh.PointSubmesh | mesh.TriangleSubmesh | mesh.TriangleSubmeshFlat]
        | None
    ) = None
    bones: list[mesh.Bone] | None = None
    blendshapes: list[mesh.BlendShape] | None = None


@dataclass
class ImportMeshRawData(BinaryPayloadMessage):
    """Import a mesh from raw binary data.

    More efficient than ImportMeshJSON. The JSON message describes the
    structure, and the payload holds the data. from_arrays builds both
    from numpy arrays.

    With V vertices, the payload holds these segments in order, with no
    padding and little-endian values:

    1. Positions: V float3.
    2. Normals: V float3, if hasNormals.
    3. Tangents: V float4, if hasTangents.
    4. Colors: V color (four float32), if hasColors.
    5. Each UV channel in turn: V * dimensions float32.
    6. Bone weights: V * boneWeightCount entries of an int32 bone index
       followed by a float32 weight, each vertex's weights together.
    7. Each submesh's int32 indices in turn: pointCount for points, or
       triangleCount * 3 for triangles.
    8. Each blendshape frame in turn: V float3 position deltas, then V
       float3 normal deltas if hasNormalDeltas, then V float3 tangent
       deltas if hasTangentDeltas.

    The server rejects a payload of any other size.

    Args:
        vertexCount: Number of vertices.
        hasNormals: Whether vertices have normals.
        hasTangents: Whether vertices have tangents.
        hasColors: Whether vertices have colors.
        boneWeightCount: Bone weights per vertex (0 if unskinned).
        uvChannelDimensions: Each UV channel's dimensions (2 to 4).
        submeshes: The submeshes' structure.
        blendshapes: The blendshapes' structure.
        bones: The bones, for a skinned mesh.
    """

    vertexCount: int = 0
    hasNormals: bool = False
    hasTangents: bool = False
    hasColors: bool = False
    boneWeightCount: int = 0
    uvChannelDimensions: list[int] | None = None
    submeshes: (
        list[mesh.PointSubmeshRawData | mesh.TriangleSubmeshRawData] | None
    ) = None
    blendshapes: list[mesh.BlendShapeRawData] | None = None
    bones: list[mesh.Bone] | None = None

    def expected_payload_size(self) -> int | None:
        """Returns the payload size, following the segment list above."""
        v = self.vertexCount
        size = v * 12
        size += v * 12 if self.hasNormals else 0
        size += v * 16 if self.hasTangents else 0
        size += v * 16 if self.hasColors else 0
        size += sum(v * d * 4 for d in self.uvChannelDimensions or [])
        size += v * self.boneWeightCount * 8
        for submesh in self.submeshes or []:
            if isinstance(submesh, mesh.TriangleSubmeshRawData):
                size += submesh.triangleCount * 3 * 4
            else:
                size += submesh.pointCount * 4
        for blendshape in self.blendshapes or []:
            per_frame = v * 12 * (
                1 + blendshape.hasNormalDeltas + blendshape.hasTangentDeltas
            )
            size += per_frame * len(blendshape.frames or [])
        return size

    @classmethod
    def from_arrays(
        cls,
        positions: np.ndarray,
        submeshes: Sequence[mesh.RawTriangles | mesh.RawPoints],
        *,
        normals: np.ndarray | None = None,
        tangents: np.ndarray | None = None,
        colors: np.ndarray | None = None,
        uvs: Sequence[np.ndarray] = (),
        bone_indices: np.ndarray | None = None,
        bone_weights: np.ndarray | None = None,
        bones: Sequence[mesh.Bone] | None = None,
        blendshapes: Sequence[mesh.RawBlendShape] = (),
    ) -> "ImportMeshRawData":
        """Returns the message for a mesh given as numpy arrays.

        Args:
            positions: Vertex positions, shaped (V, 3).
            submeshes: The submeshes, each a RawTriangles or RawPoints.
            normals: Vertex normals, shaped (V, 3).
            tangents: Vertex tangents, shaped (V, 4), with the binormal
                sign in the fourth component.
            colors: Vertex colors, shaped (V, 4), as float32 RGBA.
            uvs: One array per UV channel, each shaped (V, 2), (V, 3), or
                (V, 4).
            bone_indices: The bones that move each vertex, shaped (V, K)
                as int32, for a skinned mesh.
            bone_weights: Their weights, shaped (V, K).
            bones: The bones, which bone_indices index into.
            blendshapes: The blendshapes.

        Returns:
            The message, with its payload.
        """
        def as_f4(array: np.ndarray, columns: int, name: str) -> np.ndarray:
            result = np.ascontiguousarray(array, dtype="<f4")
            if result.shape != (vertex_count, columns):
                raise ValueError(
                    f"{name} must be ({vertex_count}, {columns}), not {result.shape}"
                )
            return result

        positions = np.ascontiguousarray(positions, dtype="<f4")
        if positions.ndim != 2 or positions.shape[1] != 3:
            raise ValueError(f"positions must be (V, 3), not {positions.shape}")
        vertex_count = positions.shape[0]
        segments = [positions]
        if normals is not None:
            segments.append(as_f4(normals, 3, "normals"))
        if tangents is not None:
            segments.append(as_f4(tangents, 4, "tangents"))
        if colors is not None:
            segments.append(as_f4(colors, 4, "colors"))
        uv_dimensions = []
        for channel, uv in enumerate(uvs):
            uv_array = np.ascontiguousarray(uv, dtype="<f4")
            if uv_array.ndim != 2 or uv_array.shape[1] not in (2, 3, 4):
                raise ValueError(f"uvs[{channel}] must be (V, 2 to 4), not {uv_array.shape}")
            segments.append(as_f4(uv_array, uv_array.shape[1], f"uvs[{channel}]"))
            uv_dimensions.append(uv_array.shape[1])
        bone_weight_count = 0
        if bone_indices is not None or bone_weights is not None:
            if bone_indices is None or bone_weights is None:
                raise ValueError("bone_indices and bone_weights go together")
            indices = np.asarray(bone_indices)
            if indices.ndim != 2 or indices.shape[0] != vertex_count:
                raise ValueError(f"bone_indices must be (V, K), not {indices.shape}")
            bone_weight_count = indices.shape[1]
            weights = np.asarray(bone_weights)
            if weights.shape != indices.shape:
                raise ValueError("bone_indices and bone_weights must have the same shape")
            entries = np.empty(indices.shape, dtype=[("index", "<i4"), ("weight", "<f4")])
            entries["index"] = indices
            entries["weight"] = weights
            segments.append(entries)
        submesh_data: list[mesh.PointSubmeshRawData | mesh.TriangleSubmeshRawData] = []
        for submesh in submeshes:
            submesh_indices = np.ascontiguousarray(submesh.indices, dtype="<i4")
            if isinstance(submesh, mesh.RawTriangles):
                if submesh_indices.ndim != 2 or submesh_indices.shape[1] != 3:
                    raise ValueError(
                        f"Triangle indices must be (N, 3), not {submesh_indices.shape}"
                    )
                submesh_data.append(
                    mesh.TriangleSubmeshRawData(triangleCount=submesh_indices.shape[0])
                )
            else:
                submesh_indices = submesh_indices.reshape(-1)
                submesh_data.append(
                    mesh.PointSubmeshRawData(pointCount=submesh_indices.shape[0])
                )
            segments.append(submesh_indices)
        blendshape_data = []
        for blendshape in blendshapes:
            has_normals = any(f.normal_deltas is not None for f in blendshape.frames)
            has_tangents = any(f.tangent_deltas is not None for f in blendshape.frames)
            for frame in blendshape.frames:
                segments.append(as_f4(frame.position_deltas, 3, "position_deltas"))
                if has_normals:
                    if frame.normal_deltas is None:
                        raise ValueError(f"Every frame of {blendshape.name} needs normal deltas")
                    segments.append(as_f4(frame.normal_deltas, 3, "normal_deltas"))
                if has_tangents:
                    if frame.tangent_deltas is None:
                        raise ValueError(f"Every frame of {blendshape.name} needs tangent deltas")
                    segments.append(as_f4(frame.tangent_deltas, 3, "tangent_deltas"))
            blendshape_data.append(mesh.BlendShapeRawData(
                name=blendshape.name,
                hasNormalDeltas=has_normals,
                hasTangentDeltas=has_tangents,
                frames=[mesh.BlendShapeFrameRawData(position=f.position) for f in blendshape.frames],
            ))
        return cls(
            vertexCount=vertex_count,
            hasNormals=normals is not None,
            hasTangents=tangents is not None,
            hasColors=colors is not None,
            boneWeightCount=bone_weight_count,
            uvChannelDimensions=uv_dimensions or None,
            submeshes=submesh_data,
            blendshapes=blendshape_data or None,
            bones=list(bones) if bones else None,
            payload=bytearray(b"".join(segment.tobytes() for segment in segments)),
        )


# =============================================================================
# Asset Import Messages — Audio
# =============================================================================


@dataclass
class ImportAudioClipFile(Message):
    """Import an audio clip from a file on the local file system.

    Supported formats: WAV, OGG, FLAC.

    Args:
        filePath: Path of the audio clip file to import.
    """

    filePath: str | None = None


@dataclass
class ImportAudioClipRawData(BinaryPayloadMessage):
    """Import an audio clip from raw float32 PCM data.

    The binary payload should contain interleaved float32 samples.

    Args:
        sampleCount: Number of samples (same regardless of channel count).
        sampleRate: Sample rate in Hz.
        channelCount: Number of channels (1=mono, 2=stereo, 6=5.1).
    """

    sampleCount: int = 0
    sampleRate: int = 0
    channelCount: int = 0

    def expected_payload_size(self) -> int | None:
        """Returns sampleCount * channelCount float32 values."""
        return self.sampleCount * self.channelCount * 4

    @classmethod
    def from_samples(
        cls, samples: np.ndarray, sampleRate: int,
    ) -> "ImportAudioClipRawData":
        """Returns the message for PCM samples.

        Args:
            samples: The samples, from -1 to 1, shaped (sample count,) for
                mono or (sample count, channel count).
            sampleRate: The sample rate in Hz.
        """
        array = np.ascontiguousarray(samples, dtype="<f4")
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        if array.ndim != 2 or array.shape[0] == 0 or array.shape[1] == 0:
            raise ValueError(f"samples must be (count,) or (count, channels), not {array.shape}")
        # Row-major order interleaves the channels, as the server expects.
        return cls(
            sampleCount=array.shape[0], sampleRate=sampleRate,
            channelCount=array.shape[1], payload=bytearray(array.tobytes()),
        )
