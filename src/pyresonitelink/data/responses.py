"""Response types for ResoniteLink communication.

This module contains response classes received from Resonite after sending messages.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

from . import reflection
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
