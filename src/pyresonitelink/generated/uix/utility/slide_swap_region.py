"""Generated component: SlideSwapRegion."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlideSwapRegion(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.SlideSwapRegion.

    Category: UIX/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion"

    def __init__(self, current: str | RectTransform | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            current: Initial value for _current.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if current is not None:
            self.current = current

    @property
    def current(self) -> str | None:
        """Target ID of the _current reference (targets RectTransform)."""
        member = self.get_member("_current")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current.setter
    def current(self, target: str | RectTransform | None) -> None:
        """Set the _current reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_current")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_current",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

