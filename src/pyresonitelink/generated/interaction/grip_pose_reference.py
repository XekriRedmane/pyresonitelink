"""Generated component: GripPoseReference."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GripPoseReference(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GripPoseReference.

    Category: Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GripPoseReference"

    def __init__(self, root_pos: primitives.Float3 | None = None, tip_reference: str | Slot | None = None, show_visual: bool | None = None, disable_slider: bool | None = None, active_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root_pos: Initial value for _rootPos.
            tip_reference: Initial value for TipReference.
            show_visual: Initial value for ShowVisual.
            disable_slider: Initial value for DisableSlider.
            active_visual: Initial value for _activeVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root_pos is not None:
            self.root_pos = root_pos
        if tip_reference is not None:
            self.tip_reference = tip_reference
        if show_visual is not None:
            self.show_visual = show_visual
        if disable_slider is not None:
            self.disable_slider = disable_slider
        if active_visual is not None:
            self.active_visual = active_visual

    @property
    def hand_side(self) -> members.FieldEnum | None:
        """The HandSide member."""
        member = self.get_member("HandSide")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hand_side.setter
    def hand_side(self, value: members.FieldEnum) -> None:
        """Set the HandSide member."""
        self.set_member("HandSide", value)

    @property
    def root_pos(self) -> primitives.Float3 | None:
        """The _rootPos field value."""
        member = self.get_member("_rootPos")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_pos.setter
    def root_pos(self, value: primitives.Float3) -> None:
        """Set the _rootPos field value."""
        member = self.get_member("_rootPos")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rootPos", fields.FieldFloat3(value=value)
            )

    @property
    def tip_reference(self) -> str | None:
        """Target ID of the TipReference reference (targets Slot)."""
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_reference.setter
    def tip_reference(self, target: str | Slot | None) -> None:
        """Set the TipReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def show_visual(self) -> bool | None:
        """The ShowVisual field value."""
        member = self.get_member("ShowVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_visual.setter
    def show_visual(self, value: bool) -> None:
        """Set the ShowVisual field value."""
        member = self.get_member("ShowVisual")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowVisual", fields.FieldBool(value=value)
            )

    @property
    def disable_slider(self) -> bool | None:
        """The DisableSlider field value."""
        member = self.get_member("DisableSlider")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_slider.setter
    def disable_slider(self, value: bool) -> None:
        """Set the DisableSlider field value."""
        member = self.get_member("DisableSlider")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableSlider", fields.FieldBool(value=value)
            )

    @property
    def active_visual(self) -> str | None:
        """Target ID of the _activeVisual reference (targets Slot)."""
        member = self.get_member("_activeVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_visual.setter
    def active_visual(self, target: str | Slot | None) -> None:
        """Set the _activeVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_activeVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

