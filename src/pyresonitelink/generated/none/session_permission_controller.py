"""Generated component: SessionPermissionController."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionPermissionController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SessionPermissionController.
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
        """Target ID of the _name reference (targets Text)."""
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
        """The _rolesButtons member."""
        member = self.get_member("_rolesButtons")
        if isinstance(member, members.SyncList):
            return member
        return None

    @roles_buttons.setter
    def roles_buttons(self, value: members.SyncList) -> None:
        """Set the _rolesButtons member."""
        self.set_member("_rolesButtons", value)

