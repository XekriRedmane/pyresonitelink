"""Response types for ResoniteLink communication.

This module contains response classes received from Resonite after sending messages.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

from . import reflection
from .members import DataReference, Member
from .workers import Component, Slot


@dataclass
class Response:
    """Base response from Resonite.

    Indicates success/failure of a request and may contain error information.
    """

    sourceMessageId: str | None = None
    success: bool = False
    errorInfo: str | None = None


@dataclass
class NewEntityId(Response):
    """Response containing the ID of a newly created entity.

    Returned by AddSlot and AddComponent.
    """

    entityId: str | None = None


@dataclass
class SlotData(Response):
    """Response containing slot data.

    Returned when requesting slot information.
    """

    depth: int = 0
    data: Slot | None = None


@dataclass
class ComponentData(Response):
    """Response containing component data.

    Returned when requesting component information.
    """

    data: Component | None = None


@dataclass
class AssetData(Response):
    """Response containing asset data.

    Returned after importing an asset (e.g., texture).

    Args:
        assetURL: URL of the imported asset. This can be assigned to static
            asset providers. Note: Usually this URL is valid only within the
            session. It is NOT recommended to persist it outside of the
            ResoniteLink session - static asset providers will automatically
            update the URL when the world/item is saved.
    """

    assetURL: str | None = None


@dataclass
class ComponentTypeList(Response):
    """Response containing a list of component types in a category.

    Returned when requesting available component types.

    Args:
        componentTypes: List of component type names in the requested category.
        subcategories: List of subcategory names in the requested category.
        totalComponentCount: Number of components in the requested category
            and all subcategories.
    """

    componentTypes: list[str] | None = None
    subcategories: list[str] | None = None
    totalComponentCount: int = 0


@dataclass
class ComponentDefinitionData(Response):
    """Response containing a component's type definition.

    Returned when requesting a component definition.

    Args:
        definition: The full definition of the requested component type.
    """

    definition: reflection.ComponentDefinition | None = None


@dataclass
class TypeDefinitionData(Response):
    """Response containing a type's definition.

    Returned by GetTypeDefinition and GetGenericTypeDefinition.

    Args:
        definition: The definition of the requested type.
    """

    definition: reflection.TypeDefinition | None = None


@dataclass
class EnumDefinitionData(Response):
    """Response containing an enum's definition.

    Returned by GetEnumDefinition.

    Args:
        definition: The definition of the requested enum.
    """

    definition: reflection.EnumDefinition | None = None


@dataclass
class SyncObjectDefinitionData(Response):
    """Response containing a sync object's definition.

    Returned by GetSyncObjectDefinition.

    Args:
        definition: The definition of the requested sync object type.
    """

    definition: reflection.SyncObjectDefinition | None = None


@dataclass
class SessionData(Response):
    """Response describing the ResoniteLink session.

    Returned by RequestSessionData.

    Args:
        resoniteVersion: The version of Resonite, e.g. "2026.9.18.82".
        resoniteLinkVersion: The version of the ResoniteLink library that
            Resonite uses, e.g. "0.13.1.0".
        uniqueSessionId: An ID unique to this ResoniteLink session for as
            long as the world runs. IDs generated with it as a prefix
            won't collide with those of another ResoniteLink session in
            the same world. It isn't unique across worlds or restarts.
    """

    resoniteVersion: str | None = None
    resoniteLinkVersion: str | None = None
    uniqueSessionId: str | None = None


@dataclass
class MethodResult(Response):
    """Response containing the value a sync method returned.

    Returned by CallSyncMethod and CallStaticSyncMethod.

    Args:
        result: The returned value, as the field class of its type, such
            as FieldInt, or a DataReference for a reference. None when the
            method returns nothing.
    """

    result: Member | DataReference | None = None


@dataclass
class BatchResponse(Response):
    """Response to a DataModelOperationBatch.

    success only means that the batch was processed. Each operation's own
    response says whether that operation succeeded.

    Args:
        responses: One response per operation, in order.
    """

    responses: list[Response] | None = None
