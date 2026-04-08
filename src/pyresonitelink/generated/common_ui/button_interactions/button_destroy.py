"""Generated component: ButtonDestroy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroyable import IDestroyable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonDestroy(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonDestroy.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonDestroy"

    def __init__(self, target: str | IDestroyable | None = None, find_object_root: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            find_object_root: Initial value for FindObjectRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if find_object_root is not None:
            self.find_object_root = find_object_root

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IDestroyable)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IDestroyable | None) -> None:
        """Set the Target reference by target ID or IDestroyable instance."""
        target_id: str | None = target.id if isinstance(target, IDestroyable) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IDestroyable'),
            )

    @property
    def find_object_root(self) -> bool | None:
        """The FindObjectRoot field value."""
        member = self.get_member("FindObjectRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @find_object_root.setter
    def find_object_root(self, value: bool) -> None:
        """Set the FindObjectRoot field value."""
        member = self.get_member("FindObjectRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FindObjectRoot", fields.FieldBool(value=value)
            )

