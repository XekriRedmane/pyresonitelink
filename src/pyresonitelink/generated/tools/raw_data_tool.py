"""Generated component: RawDataTool."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawDataTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RawDataTool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RawDataTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: bool | None = None, block_remote_equip: bool | None = None, equip_name: str | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: bool | None = None, local_tip_offset: primitives.Float3 | None = None, local_tip_reference: str | Slot | None = None, use_laser: bool | None = None, block_primary_when_touching: bool | None = None, use_secondary: bool | None = None, allow_use_when_holding: bool | None = None, equipped: bool | None = None, primary_strength_stream: str | ValueStream[np.float32] | None = None, secondary_axis_stream: str | ValueStream[primitives.Float2] | None = None, primary_stream: str | ValueStream[bool] | None = None, secondary_stream: str | ValueStream[bool] | None = None, raw_strength: np.float32 | None = None, raw_axis: primitives.Float2 | None = None, raw_primary: bool | None = None, raw_secondary: bool | None = None, primary_action_description: str | None = None, secondary_action_description: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            local_tip_offset: Initial value for LocalTipOffset.
            local_tip_reference: Initial value for LocalTipReference.
            use_laser: Initial value for UseLaser.
            block_primary_when_touching: Initial value for BlockPrimaryWhenTouching.
            use_secondary: Initial value for UseSecondary.
            allow_use_when_holding: Initial value for AllowUseWhenHolding.
            equipped: Initial value for Equipped.
            primary_strength_stream: Initial value for _primaryStrengthStream.
            secondary_axis_stream: Initial value for _secondaryAxisStream.
            primary_stream: Initial value for _primaryStream.
            secondary_stream: Initial value for _secondaryStream.
            raw_strength: Initial value for _rawStrength.
            raw_axis: Initial value for _rawAxis.
            raw_primary: Initial value for _rawPrimary.
            raw_secondary: Initial value for _rawSecondary.
            primary_action_description: Initial value for PrimaryActionDescription.
            secondary_action_description: Initial value for SecondaryActionDescription.
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
        if local_tip_offset is not None:
            self.local_tip_offset = local_tip_offset
        if local_tip_reference is not None:
            self.local_tip_reference = local_tip_reference
        if use_laser is not None:
            self.use_laser = use_laser
        if block_primary_when_touching is not None:
            self.block_primary_when_touching = block_primary_when_touching
        if use_secondary is not None:
            self.use_secondary = use_secondary
        if allow_use_when_holding is not None:
            self.allow_use_when_holding = allow_use_when_holding
        if equipped is not None:
            self.equipped = equipped
        if primary_strength_stream is not None:
            self.primary_strength_stream = primary_strength_stream
        if secondary_axis_stream is not None:
            self.secondary_axis_stream = secondary_axis_stream
        if primary_stream is not None:
            self.primary_stream = primary_stream
        if secondary_stream is not None:
            self.secondary_stream = secondary_stream
        if raw_strength is not None:
            self.raw_strength = raw_strength
        if raw_axis is not None:
            self.raw_axis = raw_axis
        if raw_primary is not None:
            self.raw_primary = raw_primary
        if raw_secondary is not None:
            self.raw_secondary = raw_secondary
        if primary_action_description is not None:
            self.primary_action_description = primary_action_description
        if secondary_action_description is not None:
            self.secondary_action_description = secondary_action_description

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
    def block_grip_equip(self) -> bool | None:
        """The BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_grip_equip.setter
    def block_grip_equip(self, value: bool) -> None:
        """Set the BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockGripEquip", fields.FieldBool(value=value)
            )

    @property
    def block_remote_equip(self) -> bool | None:
        """The BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_remote_equip.setter
    def block_remote_equip(self, value: bool) -> None:
        """Set the BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockRemoteEquip", fields.FieldBool(value=value)
            )

    @property
    def equip_name(self) -> str | None:
        """The EquipName field value."""
        member = self.get_member("EquipName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_name.setter
    def equip_name(self, value: str) -> None:
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
        target_id: str | None = target.id if isinstance(target, InteractionHandler) else target  # type: ignore[assignment]
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideActiveTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def grip_poses_generated(self) -> bool | None:
        """The _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_poses_generated.setter
    def grip_poses_generated(self, value: bool) -> None:
        """Set the _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gripPosesGenerated", fields.FieldBool(value=value)
            )

    @property
    def local_tip_offset(self) -> primitives.Float3 | None:
        """The LocalTipOffset field value."""
        member = self.get_member("LocalTipOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_tip_offset.setter
    def local_tip_offset(self, value: primitives.Float3) -> None:
        """Set the LocalTipOffset field value."""
        member = self.get_member("LocalTipOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalTipOffset", fields.FieldFloat3(value=value)
            )

    @property
    def local_tip_reference(self) -> str | None:
        """Target ID of the LocalTipReference reference (targets Slot)."""
        member = self.get_member("LocalTipReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_tip_reference.setter
    def local_tip_reference(self, target: str | Slot | None) -> None:
        """Set the LocalTipReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("LocalTipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalTipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def use_laser(self) -> bool | None:
        """The UseLaser field value."""
        member = self.get_member("UseLaser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_laser.setter
    def use_laser(self, value: bool) -> None:
        """Set the UseLaser field value."""
        member = self.get_member("UseLaser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLaser", fields.FieldBool(value=value)
            )

    @property
    def block_primary_when_touching(self) -> bool | None:
        """The BlockPrimaryWhenTouching field value."""
        member = self.get_member("BlockPrimaryWhenTouching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_primary_when_touching.setter
    def block_primary_when_touching(self, value: bool) -> None:
        """Set the BlockPrimaryWhenTouching field value."""
        member = self.get_member("BlockPrimaryWhenTouching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockPrimaryWhenTouching", fields.FieldBool(value=value)
            )

    @property
    def use_secondary(self) -> bool | None:
        """The UseSecondary field value."""
        member = self.get_member("UseSecondary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_secondary.setter
    def use_secondary(self, value: bool) -> None:
        """Set the UseSecondary field value."""
        member = self.get_member("UseSecondary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSecondary", fields.FieldBool(value=value)
            )

    @property
    def allow_use_when_holding(self) -> bool | None:
        """The AllowUseWhenHolding field value."""
        member = self.get_member("AllowUseWhenHolding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_use_when_holding.setter
    def allow_use_when_holding(self, value: bool) -> None:
        """Set the AllowUseWhenHolding field value."""
        member = self.get_member("AllowUseWhenHolding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowUseWhenHolding", fields.FieldBool(value=value)
            )

    @property
    def equipped(self) -> bool | None:
        """The Equipped field value."""
        member = self.get_member("Equipped")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equipped.setter
    def equipped(self, value: bool) -> None:
        """Set the Equipped field value."""
        member = self.get_member("Equipped")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Equipped", fields.FieldBool(value=value)
            )

    @property
    def controller_type(self) -> members.Member | None:
        """The ControllerType member."""
        member = self.get_member("ControllerType")
        if isinstance(member, members.Member):
            return member
        return None

    @controller_type.setter
    def controller_type(self, value: members.Member) -> None:
        """Set the ControllerType member."""
        self.set_member("ControllerType", value)

    @property
    def controller_side(self) -> members.FieldEnum | None:
        """The ControllerSide member."""
        member = self.get_member("ControllerSide")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @controller_side.setter
    def controller_side(self, value: members.FieldEnum) -> None:
        """Set the ControllerSide member."""
        self.set_member("ControllerSide", value)

    @property
    def primary_strength(self) -> members.EmptyElement | None:
        """The PrimaryStrength member."""
        member = self.get_member("PrimaryStrength")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary_strength.setter
    def primary_strength(self, value: members.EmptyElement) -> None:
        """Set the PrimaryStrength member."""
        self.set_member("PrimaryStrength", value)

    @property
    def secondary_axis(self) -> members.EmptyElement | None:
        """The SecondaryAxis member."""
        member = self.get_member("SecondaryAxis")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary_axis.setter
    def secondary_axis(self, value: members.EmptyElement) -> None:
        """Set the SecondaryAxis member."""
        self.set_member("SecondaryAxis", value)

    @property
    def primary(self) -> members.EmptyElement | None:
        """The Primary member."""
        member = self.get_member("Primary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary.setter
    def primary(self, value: members.EmptyElement) -> None:
        """Set the Primary member."""
        self.set_member("Primary", value)

    @property
    def secondary(self) -> members.EmptyElement | None:
        """The Secondary member."""
        member = self.get_member("Secondary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary.setter
    def secondary(self, value: members.EmptyElement) -> None:
        """Set the Secondary member."""
        self.set_member("Secondary", value)

    @property
    def primary_strength_stream(self) -> str | None:
        """Target ID of the _primaryStrengthStream reference (targets ValueStream[np.float32])."""
        member = self.get_member("_primaryStrengthStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_strength_stream.setter
    def primary_strength_stream(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the _primaryStrengthStream reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_primaryStrengthStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_primaryStrengthStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def secondary_axis_stream(self) -> str | None:
        """Target ID of the _secondaryAxisStream reference (targets ValueStream[primitives.Float2])."""
        member = self.get_member("_secondaryAxisStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_axis_stream.setter
    def secondary_axis_stream(self, target: str | ValueStream[primitives.Float2] | None) -> None:
        """Set the _secondaryAxisStream reference by target ID or ValueStream[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_secondaryAxisStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_secondaryAxisStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float2>'),
            )

    @property
    def primary_stream(self) -> str | None:
        """Target ID of the _primaryStream reference (targets ValueStream[bool])."""
        member = self.get_member("_primaryStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_stream.setter
    def primary_stream(self, target: str | ValueStream[bool] | None) -> None:
        """Set the _primaryStream reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_primaryStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_primaryStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def secondary_stream(self) -> str | None:
        """Target ID of the _secondaryStream reference (targets ValueStream[bool])."""
        member = self.get_member("_secondaryStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_stream.setter
    def secondary_stream(self, target: str | ValueStream[bool] | None) -> None:
        """Set the _secondaryStream reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_secondaryStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_secondaryStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def raw_strength(self) -> np.float32 | None:
        """The _rawStrength field value."""
        member = self.get_member("_rawStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_strength.setter
    def raw_strength(self, value: np.float32) -> None:
        """Set the _rawStrength field value."""
        member = self.get_member("_rawStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rawStrength", fields.FieldFloat(value=value)
            )

    @property
    def raw_axis(self) -> primitives.Float2 | None:
        """The _rawAxis field value."""
        member = self.get_member("_rawAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_axis.setter
    def raw_axis(self, value: primitives.Float2) -> None:
        """Set the _rawAxis field value."""
        member = self.get_member("_rawAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rawAxis", fields.FieldFloat2(value=value)
            )

    @property
    def raw_primary(self) -> bool | None:
        """The _rawPrimary field value."""
        member = self.get_member("_rawPrimary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_primary.setter
    def raw_primary(self, value: bool) -> None:
        """Set the _rawPrimary field value."""
        member = self.get_member("_rawPrimary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rawPrimary", fields.FieldBool(value=value)
            )

    @property
    def raw_secondary(self) -> bool | None:
        """The _rawSecondary field value."""
        member = self.get_member("_rawSecondary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_secondary.setter
    def raw_secondary(self, value: bool) -> None:
        """Set the _rawSecondary field value."""
        member = self.get_member("_rawSecondary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rawSecondary", fields.FieldBool(value=value)
            )

    @property
    def primary_action_description(self) -> str | None:
        """The PrimaryActionDescription field value."""
        member = self.get_member("PrimaryActionDescription")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @primary_action_description.setter
    def primary_action_description(self, value: str) -> None:
        """Set the PrimaryActionDescription field value."""
        member = self.get_member("PrimaryActionDescription")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PrimaryActionDescription", fields.FieldString(value=value)
            )

    @property
    def secondary_action_description(self) -> str | None:
        """The SecondaryActionDescription field value."""
        member = self.get_member("SecondaryActionDescription")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_action_description.setter
    def secondary_action_description(self, value: str) -> None:
        """Set the SecondaryActionDescription field value."""
        member = self.get_member("SecondaryActionDescription")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryActionDescription", fields.FieldString(value=value)
            )

