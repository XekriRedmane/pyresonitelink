"""Generated component: SlideSwapRegion."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlideSwapRegion(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SlideSwapRegion component takes in a RectTransform of a UIX element and uses it for a slide swap. This is an internal component used by the game engine to manage things like the inventory and tutorial pages to name a couple. This isn't usable by the player in any meaningful way because of this.

    Category: UIX/Utility

    Not used by the player. used by internal game elements.
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
        """Internal - The RectTransform to swap. This component acting as a controller for what this points to."""
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

