"""Generated component: Expander."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Expander(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Expander.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Expander"

    def __init__(self, section_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            section_root: Initial value for SectionRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if section_root is not None:
            self.section_root = section_root

    @property
    def section_root(self) -> str | None:
        """Target ID of the SectionRoot reference (targets Slot)."""
        member = self.get_member("SectionRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @section_root.setter
    def section_root(self, target: str | Slot | None) -> None:
        """Set the SectionRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SectionRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SectionRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

