"""Generated component: AvatarUserReferenceAssigner."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserReferenceAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarUserReferenceAssigner component is used to assign the user reference to a list of targets (depending on the ``AssignMode``). This component activates only when in the slot hierarchy of an Avatar and when a user equips it.

    Category: Users/Common Avatar System

    This is often used with assigning the user reference to nameplates, and
    the components within.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserReferenceAssigner"

    def __init__(self, assign_mode: Mode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            assign_mode: Initial value for AssignMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if assign_mode is not None:
            self.assign_mode = assign_mode

    @property
    def assign_mode(self) -> Mode | None:
        """How to use the list when assigning users to User storage fields."""
        member = self.get_member("AssignMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @assign_mode.setter
    def assign_mode(self, value: Mode | str) -> None:
        """Set AssignMode. How to use the list when assigning users to User storage fields."""
        member = self.get_member("AssignMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AssignMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def references(self) -> members.SyncList | None:
        """The references to scan through when assigning."""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set References. The references to scan through when assigning."""
        self.set_member("References", value)

