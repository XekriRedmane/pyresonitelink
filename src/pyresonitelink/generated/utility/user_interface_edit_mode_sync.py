"""Generated component: UserInterfaceEditModeSync."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInterfaceEditModeSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserInterfaceEditModeSync component allows a world to tell if a user is currently in UI Edit Mode.

    Category: Utility

    Attach to a slot and fill in the ``TargetUser`` to check UI Edit Mode
    for.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInterfaceEditModeSync"

    def __init__(self, edit_mode_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            edit_mode_active: Initial value for EditModeActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if edit_mode_active is not None:
            self.edit_mode_active = edit_mode_active

    @property
    def target_user(self) -> members.SyncObject | None:
        """The user to check UI edit mode for."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set TargetUser. The user to check UI edit mode for."""
        self.set_member("TargetUser", value)

    @property
    def edit_mode_active(self) -> primitives.Bool | None:
        """Whether ``TargetUser`` is in UI edit mode."""
        member = self.get_member("EditModeActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_active.setter
    def edit_mode_active(self, value: primitives.Bool) -> None:
        """Set the EditModeActive field value."""
        member = self.get_member("EditModeActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeActive", fields.FieldBool(value=value)
            )

