"""Generated component: AvatarGroup."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarGroup(GeneratedComponent, IComponent, IWorldEventReceiver):
    """For detailed information on how this functions for mix and match body parts. Please also see Equipping Multiple Avatars.

AvatarGroup is a component commonly found on the root of an avatar. It mostly controls where the avatar should be parented back to when dequipped, and is set by a user's Avatar Manager.

    Category: Users/Common Avatar System

    **Behavior**: This component is currently not entirely functioning. see Issue 3076
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarGroup"

    def __init__(self, original_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            original_parent: Initial value for OriginalParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if original_parent is not None:
            self.original_parent = original_parent

    @property
    def original_parent(self) -> str | None:
        """The slot that this avatar was parented under before being equipped."""
        member = self.get_member("OriginalParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_parent.setter
    def original_parent(self, target: str | Slot | None) -> None:
        """Set the OriginalParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OriginalParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OriginalParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

