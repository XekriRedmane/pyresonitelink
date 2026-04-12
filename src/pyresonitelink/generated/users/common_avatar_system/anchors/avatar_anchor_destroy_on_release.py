"""Generated component: AvatarAnchorDestroyOnRelease."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchorDestroyOnRelease(GeneratedComponent, IComponent, IWorldEventReceiver):
    """When a user is released from an anchor on the same slot as this component, ``DestroyRoot`` is destroyed.

    Category: Users/Common Avatar System/Anchors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchorDestroyOnRelease"

    def __init__(self, destroy_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            destroy_root: Initial value for DestroyRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if destroy_root is not None:
            self.destroy_root = destroy_root

    @property
    def destroy_root(self) -> str | None:
        """The slot to destroy when a user is released from an anchor on the same slot as this component."""
        member = self.get_member("DestroyRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destroy_root.setter
    def destroy_root(self, target: str | Slot | None) -> None:
        """Set the DestroyRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DestroyRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DestroyRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

