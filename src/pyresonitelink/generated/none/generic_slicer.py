"""Generated component: GenericSlicer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericSlicer(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """The GenericSlicer component is used to drive and handle the slicing of materials like volumes and PBS Slice.

    See Object Slicer Tool.
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
        """The Slicer Fields on materials to drive."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The Slicer Fields on materials to drive."""
        self.set_member("Targets", value)

    @property
    def space(self) -> members.SyncObject | None:
        """The transform space to do slicing in."""
        member = self.get_member("Space")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @space.setter
    def space(self, value: members.SyncObject) -> None:
        """Set Space. The transform space to do slicing in."""
        self.set_member("Space", value)

    @property
    def grabbed_visual(self) -> str | None:
        """The visual to show and hide when this Slicer is grabbed."""
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

