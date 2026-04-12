"""Generated component: ButtonHoverEventRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonHoverEventRelay(GeneratedComponent, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonHoverEventRelay component takes in a slot target, and if any IButton hover event happens with this component on a slot, will also send a signal to that target slot, and the components on that target slot will trigger with hover events (if applicable).

    Category: Common UI/Button Interactions

    Useful for sending multiple signals from one hover event.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonHoverEventRelay"

    def __init__(self, target: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target

    @property
    def target(self) -> str | None:
        """The slot to send the signal to."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

