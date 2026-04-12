"""Generated component: MaterialTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.asset_tool_replacement_mode import AssetToolReplacementMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """See Material Tool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, orb_slot: str | Slot | None = None, replacement_mode: AssetToolReplacementMode | str | None = None, area_radius: primitives.Float | None = None, area_indicator: str | Slot | None = None, area_indicator_radius: str | IField[primitives.Float] | None = None, area_indicator_offset: str | IField[primitives.Float3] | None = None, area_indicator_active: str | IField[primitives.Bool] | None = None, knob_control_active: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            orb_slot: Initial value for _orbSlot.
            replacement_mode: Initial value for ReplacementMode.
            area_radius: Initial value for AreaRadius.
            area_indicator: Initial value for _areaIndicator.
            area_indicator_radius: Initial value for _areaIndicatorRadius.
            area_indicator_offset: Initial value for _areaIndicatorOffset.
            area_indicator_active: Initial value for _areaIndicatorActive.
            knob_control_active: Initial value for _knobControlActive.
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
        if orb_slot is not None:
            self.orb_slot = orb_slot
        if replacement_mode is not None:
            self.replacement_mode = replacement_mode
        if area_radius is not None:
            self.area_radius = area_radius
        if area_indicator is not None:
            self.area_indicator = area_indicator
        if area_indicator_radius is not None:
            self.area_indicator_radius = area_indicator_radius
        if area_indicator_offset is not None:
            self.area_indicator_offset = area_indicator_offset
        if area_indicator_active is not None:
            self.area_indicator_active = area_indicator_active
        if knob_control_active is not None:
            self.knob_control_active = knob_control_active

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
    def orb_slot(self) -> str | None:
        """The slot to store the material orb when an orb is placed into the tool or picked from an object."""
        member = self.get_member("_orbSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orb_slot.setter
    def orb_slot(self, target: str | Slot | None) -> None:
        """Set the _orbSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_orbSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_orbSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def replacement_mode(self) -> AssetToolReplacementMode | None:
        """How to replace materials using the tool."""
        member = self.get_member("ReplacementMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AssetToolReplacementMode(member.value)
        return None

    @replacement_mode.setter
    def replacement_mode(self, value: AssetToolReplacementMode | str) -> None:
        """Set ReplacementMode. How to replace materials using the tool."""
        member = self.get_member("ReplacementMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ReplacementMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def area_radius(self) -> primitives.Float | None:
        """The radius to use when ``ReplacementMode`` is set to Area."""
        member = self.get_member("AreaRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @area_radius.setter
    def area_radius(self, value: primitives.Float) -> None:
        """Set the AreaRadius field value."""
        member = self.get_member("AreaRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AreaRadius", fields.FieldFloat(value=value)
            )

    @property
    def area_indicator(self) -> str | None:
        """The slot that is the root of the area indicator visual."""
        member = self.get_member("_areaIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @area_indicator.setter
    def area_indicator(self, target: str | Slot | None) -> None:
        """Set the _areaIndicator reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_areaIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_areaIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def area_indicator_radius(self) -> str | None:
        """The area indicator's radius field."""
        member = self.get_member("_areaIndicatorRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @area_indicator_radius.setter
    def area_indicator_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _areaIndicatorRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_areaIndicatorRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_areaIndicatorRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def area_indicator_offset(self) -> str | None:
        """The area indicator's offset field."""
        member = self.get_member("_areaIndicatorOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @area_indicator_offset.setter
    def area_indicator_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _areaIndicatorOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_areaIndicatorOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_areaIndicatorOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def area_indicator_active(self) -> str | None:
        """The area indicator's active field, used to disable the visual when ``ReplacementMode`` is not set to Area."""
        member = self.get_member("_areaIndicatorActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @area_indicator_active.setter
    def area_indicator_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _areaIndicatorActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_areaIndicatorActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_areaIndicatorActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def knob_control_active(self) -> str | None:
        """The active field of the knob control visual/control."""
        member = self.get_member("_knobControlActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @knob_control_active.setter
    def knob_control_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _knobControlActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_knobControlActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_knobControlActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

