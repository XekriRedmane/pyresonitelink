"""Generated component: SelfFootstepEventRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifootstep_event_receiver import IFootstepEventReceiver
from pyresonitelink.generated._types.ifootstep_event_relay import IFootstepEventRelay
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SelfFootstepEventRelay(GeneratedComponent, IFootstepEventReceiver, IFootstepEventRelay, IWorldEventReceiver):
    """The SelfFootstepEventRelay can be put on a user's feet to recieve foot step events and send them to other slots.

    Category: Locomotion/Footsteps

    Used to recieve and relay foot step events.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SelfFootstepEventRelay"

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
        """The slot to relay foot step events to."""
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

