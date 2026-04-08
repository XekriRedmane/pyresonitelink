"""Generated component: InventoryLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InventoryLink(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InventoryLink.

    Category: Cloud
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
        """The TargetName field value."""
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
        """The Target field value."""
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

