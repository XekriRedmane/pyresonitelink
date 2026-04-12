"""Generated component: SessionPermissionController."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionPermissionController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SessionPermissionController component is used to change the roles or view the roles of a specific user in the current session.

    Not to be used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionPermissionController"

    def __init__(self, name: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            name: Initial value for _name.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if name is not None:
            self.name = name

    @property
    def name(self) -> str | None:
        """The text element showing the name of the user this belongs to."""
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | Text | None) -> None:
        """Set the _name reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def roles_buttons(self) -> members.SyncList | None:
        """A list of button elements used to assign the user this belongs to to a role."""
        member = self.get_member("_rolesButtons")
        if isinstance(member, members.SyncList):
            return member
        return None

    @roles_buttons.setter
    def roles_buttons(self, value: members.SyncList) -> None:
        """Set _rolesButtons. A list of button elements used to assign the user this belongs to to a role."""
        self.set_member("_rolesButtons", value)

