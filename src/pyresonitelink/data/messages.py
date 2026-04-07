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
class BinaryPayloadMessage(Message):
    """A message with a binary payload."""

    payload: bytearray | None = json_ignore(default=None)


# =============================================================================
# Asset Import Messages
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
