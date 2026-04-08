"""Generated component: ProtoFluxTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.proto_flux_element_proxy import ProtoFluxElementProxy
from pyresonitelink.generated._types.proto_flux_node_visual import ProtoFluxNodeVisual
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxTool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, wire_point: str | Slot | None = None, max_connect_distance: primitives.Float | None = None, selection_progress: primitives.Float | None = None, hovering_element_name: primitives.String | None = None, hovering_element_color: primitives.ColorX | None = None, wire_point_position: str | IField[primitives.Float3] | None = None, text: str | TextRenderer | None = None, current_proxy: str | ProtoFluxElementProxy | None = None, current_temp_wire: str | Slot | None = None, current_cut_line: str | Slot | None = None, cut_line_scale: str | IField[primitives.Float3] | None = None, cut_line_orientation: str | IField[primitives.FloatQ] | None = None, current_highlighted_node: str | ProtoFluxNodeVisual | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            wire_point: Initial value for WirePoint.
            max_connect_distance: Initial value for MaxConnectDistance.
            selection_progress: Initial value for SelectionProgress.
            hovering_element_name: Initial value for HoveringElementName.
            hovering_element_color: Initial value for HoveringElementColor.
            wire_point_position: Initial value for _wirePointPosition.
            text: Initial value for _text.
            current_proxy: Initial value for _currentProxy.
            current_temp_wire: Initial value for _currentTempWire.
            current_cut_line: Initial value for _currentCutLine.
            cut_line_scale: Initial value for _cutLineScale.
            cut_line_orientation: Initial value for _cutLineOrientation.
            current_highlighted_node: Initial value for _currentHighlightedNode.
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
        if wire_point is not None:
            self.wire_point = wire_point
        if max_connect_distance is not None:
            self.max_connect_distance = max_connect_distance
        if selection_progress is not None:
            self.selection_progress = selection_progress
        if hovering_element_name is not None:
            self.hovering_element_name = hovering_element_name
        if hovering_element_color is not None:
            self.hovering_element_color = hovering_element_color
        if wire_point_position is not None:
            self.wire_point_position = wire_point_position
        if text is not None:
            self.text = text
        if current_proxy is not None:
            self.current_proxy = current_proxy
        if current_temp_wire is not None:
            self.current_temp_wire = current_temp_wire
        if current_cut_line is not None:
            self.current_cut_line = current_cut_line
        if cut_line_scale is not None:
            self.cut_line_scale = cut_line_scale
        if cut_line_orientation is not None:
            self.cut_line_orientation = cut_line_orientation
        if current_highlighted_node is not None:
            self.current_highlighted_node = current_highlighted_node

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
    def spawn_node_type(self) -> members.FieldEnum | None:
        """The SpawnNodeType member."""
        member = self.get_member("SpawnNodeType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @spawn_node_type.setter
    def spawn_node_type(self, value: members.FieldEnum) -> None:
        """Set the SpawnNodeType member."""
        self.set_member("SpawnNodeType", value)

    @property
    def wire_point(self) -> str | None:
        """Target ID of the WirePoint reference (targets Slot)."""
        member = self.get_member("WirePoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wire_point.setter
    def wire_point(self, target: str | Slot | None) -> None:
        """Set the WirePoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("WirePoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WirePoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def max_connect_distance(self) -> primitives.Float | None:
        """The MaxConnectDistance field value."""
        member = self.get_member("MaxConnectDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_connect_distance.setter
    def max_connect_distance(self, value: primitives.Float) -> None:
        """Set the MaxConnectDistance field value."""
        member = self.get_member("MaxConnectDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxConnectDistance", fields.FieldFloat(value=value)
            )

    @property
    def selection_progress(self) -> primitives.Float | None:
        """The SelectionProgress field value."""
        member = self.get_member("SelectionProgress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selection_progress.setter
    def selection_progress(self, value: primitives.Float) -> None:
        """Set the SelectionProgress field value."""
        member = self.get_member("SelectionProgress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectionProgress", fields.FieldFloat(value=value)
            )

    @property
    def hovering_element_name(self) -> primitives.String | None:
        """The HoveringElementName field value."""
        member = self.get_member("HoveringElementName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hovering_element_name.setter
    def hovering_element_name(self, value: primitives.String) -> None:
        """Set the HoveringElementName field value."""
        member = self.get_member("HoveringElementName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoveringElementName", fields.FieldString(value=value)
            )

    @property
    def hovering_element_content_type(self) -> members.FieldEnum | None:
        """The HoveringElementContentType member."""
        member = self.get_member("HoveringElementContentType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hovering_element_content_type.setter
    def hovering_element_content_type(self, value: members.FieldEnum) -> None:
        """Set the HoveringElementContentType member."""
        self.set_member("HoveringElementContentType", value)

    @property
    def hovering_element_color(self) -> primitives.ColorX | None:
        """The HoveringElementColor field value."""
        member = self.get_member("HoveringElementColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hovering_element_color.setter
    def hovering_element_color(self, value: primitives.ColorX) -> None:
        """Set the HoveringElementColor field value."""
        member = self.get_member("HoveringElementColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoveringElementColor", fields.FieldColorX(value=value)
            )

    @property
    def selected_nodes(self) -> members.SyncList | None:
        """The _selectedNodes member."""
        member = self.get_member("_selectedNodes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @selected_nodes.setter
    def selected_nodes(self, value: members.SyncList) -> None:
        """Set the _selectedNodes member."""
        self.set_member("_selectedNodes", value)

    @property
    def wire_point_position(self) -> str | None:
        """Target ID of the _wirePointPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_wirePointPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wire_point_position.setter
    def wire_point_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _wirePointPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_wirePointPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_wirePointPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def text(self) -> str | None:
        """Target ID of the _text reference (targets TextRenderer)."""
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | TextRenderer | None) -> None:
        """Set the _text reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def current_proxy(self) -> str | None:
        """Target ID of the _currentProxy reference (targets ProtoFluxElementProxy)."""
        member = self.get_member("_currentProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_proxy.setter
    def current_proxy(self, target: str | ProtoFluxElementProxy | None) -> None:
        """Set the _currentProxy reference by target ID or ProtoFluxElementProxy instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxElementProxy) else target  # type: ignore[assignment]
        member = self.get_member("_currentProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxElementProxy'),
            )

    @property
    def current_temp_wire(self) -> str | None:
        """Target ID of the _currentTempWire reference (targets Slot)."""
        member = self.get_member("_currentTempWire")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_temp_wire.setter
    def current_temp_wire(self, target: str | Slot | None) -> None:
        """Set the _currentTempWire reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_currentTempWire")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentTempWire",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def current_cut_line(self) -> str | None:
        """Target ID of the _currentCutLine reference (targets Slot)."""
        member = self.get_member("_currentCutLine")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_cut_line.setter
    def current_cut_line(self, target: str | Slot | None) -> None:
        """Set the _currentCutLine reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_currentCutLine")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentCutLine",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def cut_line_scale(self) -> str | None:
        """Target ID of the _cutLineScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_cutLineScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cut_line_scale.setter
    def cut_line_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cutLineScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cutLineScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cutLineScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def cut_line_orientation(self) -> str | None:
        """Target ID of the _cutLineOrientation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_cutLineOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cut_line_orientation.setter
    def cut_line_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _cutLineOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cutLineOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cutLineOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def current_highlighted_node(self) -> str | None:
        """Target ID of the _currentHighlightedNode reference (targets ProtoFluxNodeVisual)."""
        member = self.get_member("_currentHighlightedNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_highlighted_node.setter
    def current_highlighted_node(self, target: str | ProtoFluxNodeVisual | None) -> None:
        """Set the _currentHighlightedNode reference by target ID or ProtoFluxNodeVisual instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxNodeVisual) else target  # type: ignore[assignment]
        member = self.get_member("_currentHighlightedNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentHighlightedNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNodeVisual'),
            )

