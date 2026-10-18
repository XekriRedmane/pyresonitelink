"""Generated component: RigBoneProxy."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField

if TYPE_CHECKING:
    from pyresonitelink.generated.rendering.rig import Rig
    from pyresonitelink.generated.assets.materials.unlit.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RigBoneProxy(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RigBoneProxy.

    Category: Hidden
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RigBoneProxy"

    def __init__(self, rig: str | Rig | None = None, parent_bone: str | Slot | None = None, material: str | OverlayFresnelMaterial | None = None, self_visual_root: str | Slot | None = None, link_visual_root: str | Slot | None = None, self_radius: str | IField[primitives.Float] | None = None, link_width: str | IField[primitives.Float] | None = None, link_visual_active: str | IField[primitives.Bool] | None = None, link_visual_pos: str | IField[primitives.Float3] | None = None, link_visual_rot: str | IField[primitives.FloatQ] | None = None, link_visual_scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rig: Initial value for Rig.
            parent_bone: Initial value for ParentBone.
            material: Initial value for _material.
            self_visual_root: Initial value for _selfVisualRoot.
            link_visual_root: Initial value for _linkVisualRoot.
            self_radius: Initial value for _selfRadius.
            link_width: Initial value for _linkWidth.
            link_visual_active: Initial value for _linkVisualActive.
            link_visual_pos: Initial value for _linkVisualPos.
            link_visual_rot: Initial value for _linkVisualRot.
            link_visual_scale: Initial value for _linkVisualScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rig is not None:
            self.rig = rig
        if parent_bone is not None:
            self.parent_bone = parent_bone
        if material is not None:
            self.material = material
        if self_visual_root is not None:
            self.self_visual_root = self_visual_root
        if link_visual_root is not None:
            self.link_visual_root = link_visual_root
        if self_radius is not None:
            self.self_radius = self_radius
        if link_width is not None:
            self.link_width = link_width
        if link_visual_active is not None:
            self.link_visual_active = link_visual_active
        if link_visual_pos is not None:
            self.link_visual_pos = link_visual_pos
        if link_visual_rot is not None:
            self.link_visual_rot = link_visual_rot
        if link_visual_scale is not None:
            self.link_visual_scale = link_visual_scale

    @property
    def rig(self) -> str | None:
        """Target ID of the Rig reference (targets Rig)."""
        member = self.get_member("Rig")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rig.setter
    def rig(self, target: str | Rig | None) -> None:
        """Set the Rig reference by target ID or Rig instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Rig")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rig",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Rig'),
            )

    @property
    def parent_bone(self) -> str | None:
        """Target ID of the ParentBone reference (targets Slot)."""
        member = self.get_member("ParentBone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_bone.setter
    def parent_bone(self, target: str | Slot | None) -> None:
        """Set the ParentBone reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("ParentBone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentBone",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _material reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def self_visual_root(self) -> str | None:
        """Target ID of the _selfVisualRoot reference (targets Slot)."""
        member = self.get_member("_selfVisualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @self_visual_root.setter
    def self_visual_root(self, target: str | Slot | None) -> None:
        """Set the _selfVisualRoot reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_selfVisualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selfVisualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def link_visual_root(self) -> str | None:
        """Target ID of the _linkVisualRoot reference (targets Slot)."""
        member = self.get_member("_linkVisualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_visual_root.setter
    def link_visual_root(self, target: str | Slot | None) -> None:
        """Set the _linkVisualRoot reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkVisualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkVisualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def self_radius(self) -> str | None:
        """Target ID of the _selfRadius reference (targets IField[primitives.Float])."""
        member = self.get_member("_selfRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @self_radius.setter
    def self_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _selfRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_selfRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selfRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def link_width(self) -> str | None:
        """Target ID of the _linkWidth reference (targets IField[primitives.Float])."""
        member = self.get_member("_linkWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_width.setter
    def link_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _linkWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def link_visual_active(self) -> str | None:
        """Target ID of the _linkVisualActive reference (targets IField[primitives.Bool])."""
        member = self.get_member("_linkVisualActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_visual_active.setter
    def link_visual_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _linkVisualActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkVisualActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkVisualActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def link_visual_pos(self) -> str | None:
        """Target ID of the _linkVisualPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_linkVisualPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_visual_pos.setter
    def link_visual_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _linkVisualPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkVisualPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkVisualPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def link_visual_rot(self) -> str | None:
        """Target ID of the _linkVisualRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_linkVisualRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_visual_rot.setter
    def link_visual_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _linkVisualRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkVisualRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkVisualRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def link_visual_scale(self) -> str | None:
        """Target ID of the _linkVisualScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_linkVisualScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @link_visual_scale.setter
    def link_visual_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _linkVisualScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_linkVisualScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_linkVisualScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

