"""Message types for ResoniteLink communication.

This module contains message classes used to send commands to Resonite.
"""

# pylint: disable=invalid-name

import abc
from dataclasses import dataclass

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
        categoryPath: Optional category path to filter component types.
            If None, returns all component types.
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
            name to value.
    """

    targetID: str | None = None
    methodName: str | None = None
    arguments: dict[str, object] | None = None


@dataclass
class CallStaticSyncMethod(Message):
    """Call a static method on a type.

    Invokes a static method by type name, without needing an instance.

    The response ``$type`` is ``methodResult`` with a ``result`` field.

    Args:
        targetType: Fully qualified type name.
        methodName: Name of the static method to call.
        arguments: Named arguments to the method, mapping parameter
            name to value.
    """

    targetType: str | None = None
    methodName: str | None = None
    arguments: dict[str, object] | None = None


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
    """A message with a binary payload."""

    payload: bytearray | None = json_ignore(default=None)


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

    def _access_raw_data(self, bytes_per_element: int) -> bytearray:
        """Returns, optionally creating, a bytearray for the data."""
        if self.width <= 0:
            raise ValueError("width must be greater than 0")
        if self.height <= 0:
            raise ValueError("height must be greater than 0")

        num_bytes = self.width * self.height * bytes_per_element
        if self.payload is None:
            self.payload = bytearray(num_bytes)
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


@dataclass
class ImportTexture2DRawDataHDR(ImportTexture2DRawDataBase):
    """Imports texture from raw floating point color data, allowing for HDR values.

    Resonite will take care of encoding the data into a file format.
    The binary payload should contain color data (RGBA, 4 float32s per pixel).

    Args:
        width: Width of the texture in pixels.
        height: Height of the texture in pixels.
    """

    def access_raw_data(self) -> bytearray:
        return super()._access_raw_data(bytes_per_element=4*4)


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

    Regions are in normalized coordinates (0..1).

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
    positiveXregion: dict[str, float] | None = None
    positiveYregion: dict[str, float] | None = None
    positiveZregion: dict[str, float] | None = None
    negativeXregion: dict[str, float] | None = None
    negativeYregion: dict[str, float] | None = None
    negativeZregion: dict[str, float] | None = None


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


@dataclass
class ImportCubemapRawDataHDR(BinaryPayloadMessage):
    """Import a cubemap from raw floating-point color data (HDR).

    Args:
        size: Size of each square face in pixels.
        mipMaps: Whether mipmap data is included.
    """

    size: int = 0
    mipMaps: bool = False


# =============================================================================
# Asset Import Messages — Mesh
# =============================================================================


@dataclass
class ImportMeshJSON(Message):
    """Import a mesh from a JSON definition.

    Verbose but convenient for small meshes. Use ImportMeshRawData for
    better efficiency with larger meshes.

    Args:
        vertices: List of vertex dicts.
        submeshes: List of submesh dicts.
        bones: List of bone dicts (for skinned meshes).
        blendshapes: List of blendshape dicts.
    """

    vertices: list[dict[str, object]] | None = None
    submeshes: list[dict[str, object]] | None = None
    bones: list[dict[str, object]] | None = None
    blendshapes: list[dict[str, object]] | None = None


@dataclass
class ImportMeshRawData(BinaryPayloadMessage):
    """Import a mesh from raw binary data.

    More efficient than ImportMeshJSON. Configure the structure metadata
    first, then set the binary payload.

    Args:
        vertexCount: Number of vertices.
        hasNormals: Whether vertices have normals.
        hasTangents: Whether vertices have tangents.
        hasColors: Whether vertices have colors.
        boneWeightCount: Bone weights per vertex (0 if unskinned).
        uvChannelDimensions: List of UV channel dimensions (2-4 each).
        submeshes: List of submesh metadata dicts.
        blendshapes: List of blendshape metadata dicts.
        bones: List of bone dicts.
    """

    vertexCount: int = 0
    hasNormals: bool = False
    hasTangents: bool = False
    hasColors: bool = False
    boneWeightCount: int = 0
    uvChannelDimensions: list[int] | None = None
    submeshes: list[dict[str, object]] | None = None
    blendshapes: list[dict[str, object]] | None = None
    bones: list[dict[str, object]] | None = None


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
