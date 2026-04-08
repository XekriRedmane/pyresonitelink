"""Generated component: WorldLoadProgress."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.world_loading_progress_interface import WorldLoadingProgressInterface
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLoadProgress(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldLoadProgress.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldLoadProgress"

    def __init__(self, visual: str | Slot | None = None, progress_indicator: str | WorldLoadingProgressInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            visual: Initial value for _visual.
            progress_indicator: Initial value for ProgressIndicator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if visual is not None:
            self.visual = visual
        if progress_indicator is not None:
            self.progress_indicator = progress_indicator

    @property
    def visual(self) -> str | None:
        """Target ID of the _visual reference (targets Slot)."""
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | Slot | None) -> None:
        """Set the _visual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def progress_indicator(self) -> str | None:
        """Target ID of the ProgressIndicator reference (targets WorldLoadingProgressInterface)."""
        member = self.get_member("ProgressIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_indicator.setter
    def progress_indicator(self, target: str | WorldLoadingProgressInterface | None) -> None:
        """Set the ProgressIndicator reference by target ID or WorldLoadingProgressInterface instance."""
        target_id: str | None = target.id if isinstance(target, WorldLoadingProgressInterface) else target  # type: ignore[assignment]
        member = self.get_member("ProgressIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProgressIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldLoadingProgressInterface'),
            )

