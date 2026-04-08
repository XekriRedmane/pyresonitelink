"""Generated component: GripPoseReferenceEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.grip_pose_reference import GripPoseReference
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GripPoseReferenceEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GripPoseReferenceEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GripPoseReferenceEditor"

    def __init__(self, reference_root: str | Slot | None = None, item: str | Slot | None = None, slider: str | Slider | None = None, pose_reference: str | GripPoseReference | None = None, hide_visual_on_end: bool | None = None, root_position: primitives.Float3 | None = None, root_rotation: primitives.FloatQ | None = None, root_scale: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference_root: Initial value for ReferenceRoot.
            item: Initial value for Item.
            slider: Initial value for Slider.
            pose_reference: Initial value for PoseReference.
            hide_visual_on_end: Initial value for HideVisualOnEnd.
            root_position: Initial value for RootPosition.
            root_rotation: Initial value for RootRotation.
            root_scale: Initial value for RootScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference_root is not None:
            self.reference_root = reference_root
        if item is not None:
            self.item = item
        if slider is not None:
            self.slider = slider
        if pose_reference is not None:
            self.pose_reference = pose_reference
        if hide_visual_on_end is not None:
            self.hide_visual_on_end = hide_visual_on_end
        if root_position is not None:
            self.root_position = root_position
        if root_rotation is not None:
            self.root_rotation = root_rotation
        if root_scale is not None:
            self.root_scale = root_scale

    @property
    def reference_root(self) -> str | None:
        """Target ID of the ReferenceRoot reference (targets Slot)."""
        member = self.get_member("ReferenceRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_root.setter
    def reference_root(self, target: str | Slot | None) -> None:
        """Set the ReferenceRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ReferenceRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReferenceRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def item(self) -> str | None:
        """Target ID of the Item reference (targets Slot)."""
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item.setter
    def item(self, target: str | Slot | None) -> None:
        """Set the Item reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Item")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Item",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def slider(self) -> str | None:
        """Target ID of the Slider reference (targets Slider)."""
        member = self.get_member("Slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider | None) -> None:
        """Set the Slider reference by target ID or Slider instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("Slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slider'),
            )

    @property
    def pose_reference(self) -> str | None:
        """Target ID of the PoseReference reference (targets GripPoseReference)."""
        member = self.get_member("PoseReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pose_reference.setter
    def pose_reference(self, target: str | GripPoseReference | None) -> None:
        """Set the PoseReference reference by target ID or GripPoseReference instance."""
        target_id: str | None = target.id if isinstance(target, GripPoseReference) else target  # type: ignore[assignment]
        member = self.get_member("PoseReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PoseReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GripPoseReference'),
            )

    @property
    def hide_visual_on_end(self) -> bool | None:
        """The HideVisualOnEnd field value."""
        member = self.get_member("HideVisualOnEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_visual_on_end.setter
    def hide_visual_on_end(self, value: bool) -> None:
        """Set the HideVisualOnEnd field value."""
        member = self.get_member("HideVisualOnEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideVisualOnEnd", fields.FieldBool(value=value)
            )

    @property
    def root_position(self) -> primitives.Float3 | None:
        """The RootPosition field value."""
        member = self.get_member("RootPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_position.setter
    def root_position(self, value: primitives.Float3) -> None:
        """Set the RootPosition field value."""
        member = self.get_member("RootPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RootPosition", fields.FieldFloat3(value=value)
            )

    @property
    def root_rotation(self) -> primitives.FloatQ | None:
        """The RootRotation field value."""
        member = self.get_member("RootRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_rotation.setter
    def root_rotation(self, value: primitives.FloatQ) -> None:
        """Set the RootRotation field value."""
        member = self.get_member("RootRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RootRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def root_scale(self) -> primitives.Float3 | None:
        """The RootScale field value."""
        member = self.get_member("RootScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_scale.setter
    def root_scale(self, value: primitives.Float3) -> None:
        """Set the RootScale field value."""
        member = self.get_member("RootScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RootScale", fields.FieldFloat3(value=value)
            )

