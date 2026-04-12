"""Generated component: SearchBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SearchBlock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Search Block component, slots tagged with this component can be used to prevent either:
- A user from grabbing an item from contacting certain colliders.
- A user from equipping an avatar when clicking on a limb or collider attached to it.
- A user from equipping a tool tip by clicking on a certain part of it.
- A user from clicking a physical button when clicking on a collider parented to the physical button further down the hierarchy, or any button type not just physical buttons.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SearchBlock"

    pass

