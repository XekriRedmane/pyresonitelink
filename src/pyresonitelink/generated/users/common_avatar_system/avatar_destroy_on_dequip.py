"""Generated component: AvatarDestroyOnDequip."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarDestroyOnDequip(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarDestroyOnDequip.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarDestroyOnDequip"

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
        """Target ID of the DestroyRoot reference (targets Slot)."""
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

