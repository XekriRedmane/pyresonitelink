"""Generated component: InspectorMemberActions."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_member import ISyncMember
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InspectorMemberActions(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InspectorMemberActions.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InspectorMemberActions"

    def __init__(self, member: str | ISyncMember | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            member: Initial value for Member.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if member is not None:
            self.member = member

    @property
    def member(self) -> str | None:
        """Target ID of the Member reference (targets ISyncMember)."""
        member = self.get_member("Member")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @member.setter
    def member(self, target: str | ISyncMember | None) -> None:
        """Set the Member reference by target ID or ISyncMember instance."""
        target_id: str | None = target.id if isinstance(target, ISyncMember) else target  # type: ignore[assignment]
        member = self.get_member("Member")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Member",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncMember'),
            )

