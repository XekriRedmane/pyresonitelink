"""Generated component: MeterTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.distance_meter import DistanceMeter
from pyresonitelink.generated._types.line_transform import LineTransform
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeterTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """See Meter Tool.

    Category: Tools

    See Meter Tool.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeterTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, indication_color: str | IField[primitives.ColorX] | None = None, meter_mode: Mode | str | None = None, measure_in_object_space: primitives.Bool | None = None, raycast_ignores_users: primitives.Bool | None = None, multi_point: primitives.Bool | None = None, last_point: str | Slot | None = None, current_meter: str | DistanceMeter | None = None, current_line_transform: str | LineTransform | None = None, format_number: primitives.String | None = None, format_unit: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            indication_color: Initial value for _indicationColor.
            meter_mode: Initial value for MeterMode.
            measure_in_object_space: Initial value for MeasureInObjectSpace.
            raycast_ignores_users: Initial value for RaycastIgnoresUsers.
            multi_point: Initial value for MultiPoint.
            last_point: Initial value for _lastPoint.
            current_meter: Initial value for _currentMeter.
            current_line_transform: Initial value for _currentLineTransform.
            format_number: Initial value for FormatNumber.
            format_unit: Initial value for FormatUnit.
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
        if indication_color is not None:
            self.indication_color = indication_color
        if meter_mode is not None:
            self.meter_mode = meter_mode
        if measure_in_object_space is not None:
            self.measure_in_object_space = measure_in_object_space
        if raycast_ignores_users is not None:
            self.raycast_ignores_users = raycast_ignores_users
        if multi_point is not None:
            self.multi_point = multi_point
        if last_point is not None:
            self.last_point = last_point
        if current_meter is not None:
            self.current_meter = current_meter
        if current_line_transform is not None:
            self.current_line_transform = current_line_transform
        if format_number is not None:
            self.format_number = format_number
        if format_unit is not None:
            self.format_unit = format_unit

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
    def indication_color(self) -> str | None:
        """The field to change the color value for when doing status indications."""
        member = self.get_member("_indicationColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @indication_color.setter
    def indication_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _indicationColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_indicationColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_indicationColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def meter_mode(self) -> Mode | None:
        """The mode the tool is currently in."""
        member = self.get_member("MeterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @meter_mode.setter
    def meter_mode(self, value: Mode | str) -> None:
        """Set MeterMode. The mode the tool is currently in."""
        member = self.get_member("MeterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MeterMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def measure_in_object_space(self) -> primitives.Bool | None:
        """If measurements should be done in global space or parent space."""
        member = self.get_member("MeasureInObjectSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @measure_in_object_space.setter
    def measure_in_object_space(self, value: primitives.Bool) -> None:
        """Set the MeasureInObjectSpace field value."""
        member = self.get_member("MeasureInObjectSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MeasureInObjectSpace", fields.FieldBool(value=value)
            )

    @property
    def raycast_ignores_users(self) -> primitives.Bool | None:
        """Whether the tool raycast ignores colliders with an active user."""
        member = self.get_member("RaycastIgnoresUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raycast_ignores_users.setter
    def raycast_ignores_users(self, value: primitives.Bool) -> None:
        """Set the RaycastIgnoresUsers field value."""
        member = self.get_member("RaycastIgnoresUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RaycastIgnoresUsers", fields.FieldBool(value=value)
            )

    @property
    def multi_point(self) -> primitives.Bool | None:
        """Measure between two points, or any amount of points."""
        member = self.get_member("MultiPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multi_point.setter
    def multi_point(self, value: primitives.Bool) -> None:
        """Set the MultiPoint field value."""
        member = self.get_member("MultiPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiPoint", fields.FieldBool(value=value)
            )

    @property
    def last_point(self) -> str | None:
        """The slot of the last point placed by the tool."""
        member = self.get_member("_lastPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_point.setter
    def last_point(self, target: str | Slot | None) -> None:
        """Set the _lastPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_lastPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def current_meter(self) -> str | None:
        """The current object displaying the distance between points."""
        member = self.get_member("_currentMeter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_meter.setter
    def current_meter(self, target: str | DistanceMeter | None) -> None:
        """Set the _currentMeter reference by target ID or DistanceMeter instance."""
        target_id: str | None = target.id if isinstance(target, DistanceMeter) else target  # type: ignore[assignment]
        member = self.get_member("_currentMeter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentMeter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DistanceMeter'),
            )

    @property
    def current_line_transform(self) -> str | None:
        """The current line transform object being used to display the distance between points"""
        member = self.get_member("_currentLineTransform")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_line_transform.setter
    def current_line_transform(self, target: str | LineTransform | None) -> None:
        """Set the _currentLineTransform reference by target ID or LineTransform instance."""
        target_id: str | None = target.id if isinstance(target, LineTransform) else target  # type: ignore[assignment]
        member = self.get_member("_currentLineTransform")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentLineTransform",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LineTransform'),
            )

    @property
    def format_number(self) -> primitives.String | None:
        """How to format the numbers."""
        member = self.get_member("FormatNumber")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_number.setter
    def format_number(self, value: primitives.String) -> None:
        """Set the FormatNumber field value."""
        member = self.get_member("FormatNumber")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormatNumber", fields.FieldString(value=value)
            )

    @property
    def format_unit(self) -> primitives.String | None:
        """How to format the units."""
        member = self.get_member("FormatUnit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_unit.setter
    def format_unit(self, value: primitives.String) -> None:
        """Set the FormatUnit field value."""
        member = self.get_member("FormatUnit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormatUnit", fields.FieldString(value=value)
            )

    async def filter_users(self, resolink: protocols.ResoniteLinkClient, collider: str, debug: bool = False) -> dict:
        """Call the FilterUsers sync method.

        Args:
            resolink: Connected ResoniteLink client.
            collider: The collider parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FilterUsers", {"collider": collider}, debug,
        )

