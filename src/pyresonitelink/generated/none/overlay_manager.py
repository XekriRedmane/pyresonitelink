"""Generated component: OverlayManager."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OverlayManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The OverlayManager component is used to handle the Overlay for edit mode on userspace dash screens.

    Used internally.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OverlayManager"

    def __init__(self, overlay_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            overlay_root: Initial value for _overlayRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if overlay_root is not None:
            self.overlay_root = overlay_root

    @property
    def overlay_root(self) -> str | None:
        """The slot that has the Overlay visuals."""
        member = self.get_member("_overlayRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overlay_root.setter
    def overlay_root(self, target: str | Slot | None) -> None:
        """Set the _overlayRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_overlayRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overlayRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

