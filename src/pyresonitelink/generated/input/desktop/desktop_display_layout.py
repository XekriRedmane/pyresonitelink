"""Generated component: DesktopDisplayLayout."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopDisplayLayout(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DesktopDisplayLayout component displays a list of display selection buttons for a user's monitor settup. It is used in the dash menu and only works in userspace.

    Category: Input/Desktop

    **DisplayItemHandler**: A Sync delegate of type Delegate&lt;Display display, Slot itemRoot&gt;
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopDisplayLayout"

    def __init__(self, display_template: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_template: Initial value for DisplayTemplate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_template is not None:
            self.display_template = display_template

    @property
    def user(self) -> members.SyncObject | None:
        """The user to get displays for."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The user to get displays for."""
        self.set_member("User", value)

    @property
    def display_template(self) -> str | None:
        """the template to use when generating display selection buttons."""
        member = self.get_member("DisplayTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_template.setter
    def display_template(self, target: str | Slot | None) -> None:
        """Set the DisplayTemplate reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DisplayTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DisplayTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

