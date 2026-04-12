"""Generated component: GripPoseReference."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GripPoseReference(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The GripPoseReference component is placed under Tools to tell them how they should be positioned when equipped.

    Category: Interaction

    To create a simple object using GripPoseReference, add the RawDataTool
    slot to the root of the object containing the mesh. This will
    automatically add the GripPoseReference slots. To edit the pose, enter
    UI Edit Mode with the Left or Right GripPoseReference slot selected in
    Scene Inspector then adjust the object pose in one hand's grip with your
    off hand. When the TipReference field is set, equipping the tool will
    align your tip reference (usually at the tip of your index finger) to
    the provided slot and ignore the transform of the grip pose. It is
    recommended to use this for custom tools which are supposed to have
    similar positioning to most of the default tools such as the Dev Tool.

    **Interaction with hand poser**: When grabbing or equipping a tool which defines a GripPoseReference without a set TipReference, the initial location from which the grip pose is applied is interpolated based on the location of the fingers and the HandRoot configured in the corresponding HandPoser.

For avatars with commonly-shaped hands with at least three fingers, this interpolated pose is usually close enough that, if you position the GripPoseReference correctly for one avatar, it should also be positioned decently well for most other avatars.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GripPoseReference"

    def __init__(self, hand_side: Chirality | str | None = None, root_pos: primitives.Float3 | None = None, tip_reference: str | Slot | None = None, show_visual: primitives.Bool | None = None, disable_slider: primitives.Bool | None = None, active_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hand_side: Initial value for HandSide.
            root_pos: Initial value for _rootPos.
            tip_reference: Initial value for TipReference.
            show_visual: Initial value for ShowVisual.
            disable_slider: Initial value for DisableSlider.
            active_visual: Initial value for _activeVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hand_side is not None:
            self.hand_side = hand_side
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
    def hand_side(self) -> Chirality | None:
        """The hand side this grip pose should"""
        member = self.get_member("HandSide")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @hand_side.setter
    def hand_side(self, value: Chirality | str) -> None:
        """Set HandSide. The hand side this grip pose should"""
        member = self.get_member("HandSide")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HandSide",
                members.FieldEnum(value=str(value)),
            )

    @property
    def root_pos(self) -> primitives.Float3 | None:
        """The root position of the tooltip."""
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
        """the slot for the tool tips tip in question."""
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
    def show_visual(self) -> primitives.Bool | None:
        """Whether to show the adjustment visual."""
        member = self.get_member("ShowVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_visual.setter
    def show_visual(self, value: primitives.Bool) -> None:
        """Set the ShowVisual field value."""
        member = self.get_member("ShowVisual")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowVisual", fields.FieldBool(value=value)
            )

    @property
    def disable_slider(self) -> primitives.Bool | None:
        """Whether to disable adjusting this grip pose."""
        member = self.get_member("DisableSlider")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_slider.setter
    def disable_slider(self, value: primitives.Bool) -> None:
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
        """The current adjustment visual."""
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

