"""Generated component: Expander."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Expander(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The Expander component is an intractable UIX element that expands a section called the ``SectionRoot`` under itself. The ``SectionRoot``'s active state will toggle when that expander is triggered, expanding it under the Slot the expander is on. This can be seen on the Scene Inspector.

}}

    Category: UIX/Interaction

    This component is combined with the Button component to trigger this
    expander component. This component is also combined with the
    TextExpandIndicator component to drive the text and show the user that
    this expander has expanded, collapsed, or is empty.
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
        """The slot to expend with, by activating the slot that is referenced when toggled."""
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

