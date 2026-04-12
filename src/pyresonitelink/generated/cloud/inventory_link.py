"""Generated component: InventoryLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InventoryLink(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component overrides the saving behavior of an item being saved to act as an inventory folder. The component will be overridden by another component if it is under another slot on an item with a different export behavior. (Ex: A Texture Exportable Component)

    Category: Cloud

    Attach to a slot and give the component a ``TargetName`` and a URI that
    links to a folder on the cloud for the ``Target`` saving an item with
    this component on it will make the item act like a folder link.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InventoryLink"

    def __init__(self, target_name: primitives.String | None = None, target: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_name: Initial value for TargetName.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_name is not None:
            self.target_name = target_name
        if target is not None:
            self.target = target

    @property
    def target_name(self) -> primitives.String | None:
        """The name of the folder this component is linking to. This will change the display name of the folder when saved, but if shared by the same user again from their inventory, this will become what the cloud says the folder's name is and not the custom name it was when saved."""
        member = self.get_member("TargetName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_name.setter
    def target_name(self, value: primitives.String) -> None:
        """Set the TargetName field value."""
        member = self.get_member("TargetName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetName", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """The folder URI link on the cloud that this component represents."""
        member = self.get_member("Target")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target.setter
    def target(self, value: str) -> None:
        """Set the Target field value."""
        member = self.get_member("Target")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Target", fields.FieldUri(value=value)
            )

