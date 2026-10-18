"""Generated component: WorldLoadProgress."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot

if TYPE_CHECKING:
    from pyresonitelink.generated.utility.entity_interfaces.world_loading_progress_interface import WorldLoadingProgressInterface
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLoadProgress(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The WorldLoadProgress component is the component that controls the WorldLoadingProgressInterface behavior.

    Category: Userspace

    Not used by the user.
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
        """The root slot for the progress indicator and visual."""
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | Slot | None) -> None:
        """Set the _visual reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """The loading indicator for this component."""
        member = self.get_member("ProgressIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_indicator.setter
    def progress_indicator(self, target: str | WorldLoadingProgressInterface | None) -> None:
        """Set the ProgressIndicator reference by target ID or WorldLoadingProgressInterface instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("ProgressIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProgressIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldLoadingProgressInterface'),
            )

