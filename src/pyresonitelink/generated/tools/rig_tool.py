"""Generated component: RigTool."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot

if TYPE_CHECKING:
    from pyresonitelink.generated.interaction.handlers.interaction_handler import InteractionHandler
    from pyresonitelink.generated.rendering.rig import Rig
    from pyresonitelink.generated.transform.inverse_kinematics.fabrik_chain import FABRIK_Chain
    from pyresonitelink.generated.transform.inverse_kinematics.trigonometric_ik import TrigonometricIK
    from pyresonitelink.generated.hidden.rig_bone_proxy import RigBoneProxy
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RigTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """See: Rig Tool

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RigTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, current_rig: str | Rig | None = None, ik_chain: str | FABRIK_Chain | None = None, trig_ik: str | TrigonometricIK | None = None, selected_bone: str | RigBoneProxy | None = None, ik_effector_template: str | Slot | None = None, new_bone: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            current_rig: Initial value for CurrentRig.
            ik_chain: Initial value for IK_Chain.
            trig_ik: Initial value for TrigIK.
            selected_bone: Initial value for SelectedBone.
            ik_effector_template: Initial value for IK_EffectorTemplate.
            new_bone: Initial value for _newBone.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tip_reference is not None:
            self.tip_reference = tip_reference
        if block_grip_equip is not None:
            self.block_grip_equip = block_grip_equip
        if block_remote_equip is not None:
            self.block_remote_equip = block_remote_equip
        if equip_name is not None:
            self.equip_name = equip_name
        if override_active_tool is not None:
            self.override_active_tool = override_active_tool
        if grip_poses_generated is not None:
            self.grip_poses_generated = grip_poses_generated
        if current_rig is not None:
            self.current_rig = current_rig
        if ik_chain is not None:
            self.ik_chain = ik_chain
        if trig_ik is not None:
            self.trig_ik = trig_ik
        if selected_bone is not None:
            self.selected_bone = selected_bone
        if ik_effector_template is not None:
            self.ik_effector_template = ik_effector_template
        if new_bone is not None:
            self.new_bone = new_bone

    @property
    def equip_link(self) -> members.EmptyElement | None:
        """The _equipLink member."""
        member = self.get_member("_equipLink")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @equip_link.setter
    def equip_link(self, value: members.EmptyElement) -> None:
        """Set the _equipLink member."""
        self.set_member("_equipLink", value)

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
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def block_grip_equip(self) -> primitives.Bool | None:
        """The BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_grip_equip.setter
    def block_grip_equip(self, value: primitives.Bool) -> None:
        """Set the BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockGripEquip", fields.FieldBool(value=value)
            )

    @property
    def block_remote_equip(self) -> primitives.Bool | None:
        """The BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_remote_equip.setter
    def block_remote_equip(self, value: primitives.Bool) -> None:
        """Set the BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockRemoteEquip", fields.FieldBool(value=value)
            )

    @property
    def equip_name(self) -> primitives.String | None:
        """The EquipName field value."""
        member = self.get_member("EquipName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_name.setter
    def equip_name(self, value: primitives.String) -> None:
        """Set the EquipName field value."""
        member = self.get_member("EquipName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipName", fields.FieldString(value=value)
            )

    @property
    def override_active_tool(self) -> str | None:
        """Target ID of the _overrideActiveTool reference (targets InteractionHandler)."""
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_active_tool.setter
    def override_active_tool(self, target: str | InteractionHandler | None) -> None:
        """Set the _overrideActiveTool reference by target ID or InteractionHandler instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideActiveTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def grip_poses_generated(self) -> primitives.Bool | None:
        """The _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_poses_generated.setter
    def grip_poses_generated(self, value: primitives.Bool) -> None:
        """Set the _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gripPosesGenerated", fields.FieldBool(value=value)
            )

    @property
    def current_rig(self) -> str | None:
        """Target ID of the CurrentRig reference (targets Rig)."""
        member = self.get_member("CurrentRig")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_rig.setter
    def current_rig(self, target: str | Rig | None) -> None:
        """Set the CurrentRig reference by target ID or Rig instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("CurrentRig")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CurrentRig",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Rig'),
            )

    @property
    def ik_chain(self) -> str | None:
        """Target ID of the IK_Chain reference (targets FABRIK_Chain)."""
        member = self.get_member("IK_Chain")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ik_chain.setter
    def ik_chain(self, target: str | FABRIK_Chain | None) -> None:
        """Set the IK_Chain reference by target ID or FABRIK_Chain instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("IK_Chain")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IK_Chain",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FABRIK_Chain'),
            )

    @property
    def trig_ik(self) -> str | None:
        """Target ID of the TrigIK reference (targets TrigonometricIK)."""
        member = self.get_member("TrigIK")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trig_ik.setter
    def trig_ik(self, target: str | TrigonometricIK | None) -> None:
        """Set the TrigIK reference by target ID or TrigonometricIK instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("TrigIK")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrigIK",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TrigonometricIK'),
            )

    @property
    def selected_bone(self) -> str | None:
        """Target ID of the SelectedBone reference (targets RigBoneProxy)."""
        member = self.get_member("SelectedBone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_bone.setter
    def selected_bone(self, target: str | RigBoneProxy | None) -> None:
        """Set the SelectedBone reference by target ID or RigBoneProxy instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("SelectedBone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SelectedBone",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RigBoneProxy'),
            )

    @property
    def ik_effector_template(self) -> str | None:
        """Target ID of the IK_EffectorTemplate reference (targets Slot)."""
        member = self.get_member("IK_EffectorTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ik_effector_template.setter
    def ik_effector_template(self, target: str | Slot | None) -> None:
        """Set the IK_EffectorTemplate reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("IK_EffectorTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IK_EffectorTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def new_bone(self) -> str | None:
        """Target ID of the _newBone reference (targets Slot)."""
        member = self.get_member("_newBone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @new_bone.setter
    def new_bone(self, target: str | Slot | None) -> None:
        """Set the _newBone reference by target ID or Slot instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_newBone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_newBone",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

