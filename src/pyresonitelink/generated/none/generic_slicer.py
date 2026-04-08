"""Generated component: GenericSlicer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericSlicer(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GenericSlicer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GenericSlicer"

    def __init__(self, grabbed_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grabbed_visual: Initial value for _grabbedVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grabbed_visual is not None:
            self.grabbed_visual = grabbed_visual

    @property
    def targets(self) -> members.SyncList | None:
        """The Targets member."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the Targets member."""
        self.set_member("Targets", value)

    @property
    def space(self) -> members.SyncObject | None:
        """The Space member."""
        member = self.get_member("Space")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @space.setter
    def space(self, value: members.SyncObject) -> None:
        """Set the Space member."""
        self.set_member("Space", value)

    @property
    def grabbed_visual(self) -> str | None:
        """Target ID of the _grabbedVisual reference (targets Slot)."""
        member = self.get_member("_grabbedVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbed_visual.setter
    def grabbed_visual(self, target: str | Slot | None) -> None:
        """Set the _grabbedVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_grabbedVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabbedVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

