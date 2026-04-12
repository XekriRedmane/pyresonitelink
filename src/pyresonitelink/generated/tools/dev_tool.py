"""Generated component: DevTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.selection import Selection
from pyresonitelink.generated._enums.interaction import Interaction
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.point_anchor import PointAnchor
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DevTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Detailed information can be located at Dev Tool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DevTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, selection_mode: Selection | str | None = None, interaction_mode: Interaction | str | None = None, selected_anchor: str | PointAnchor | None = None, selected_anchor_highlight: str | Slot | None = None, material: str | OverlayFresnelMaterial | None = None, current_gizmo: str | Slot | None = None, previous_gizmo: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            selection_mode: Initial value for SelectionMode.
            interaction_mode: Initial value for InteractionMode.
            selected_anchor: Initial value for _selectedAnchor.
            selected_anchor_highlight: Initial value for _selectedAnchorHighlight.
            material: Initial value for _material.
            current_gizmo: Initial value for _currentGizmo.
            previous_gizmo: Initial value for _previousGizmo.
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
        if selection_mode is not None:
            self.selection_mode = selection_mode
        if interaction_mode is not None:
            self.interaction_mode = interaction_mode
        if selected_anchor is not None:
            self.selected_anchor = selected_anchor
        if selected_anchor_highlight is not None:
            self.selected_anchor_highlight = selected_anchor_highlight
        if material is not None:
            self.material = material
        if current_gizmo is not None:
            self.current_gizmo = current_gizmo
        if previous_gizmo is not None:
            self.previous_gizmo = previous_gizmo

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
    def selection_mode(self) -> Selection | None:
        """See Selection section."""
        member = self.get_member("SelectionMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Selection(member.value)
        return None

    @selection_mode.setter
    def selection_mode(self, value: Selection | str) -> None:
        """Set SelectionMode. See Selection section."""
        member = self.get_member("SelectionMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SelectionMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def interaction_mode(self) -> Interaction | None:
        """See Interaction section."""
        member = self.get_member("InteractionMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Interaction(member.value)
        return None

    @interaction_mode.setter
    def interaction_mode(self, value: Interaction | str) -> None:
        """Set InteractionMode. See Interaction section."""
        member = self.get_member("InteractionMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "InteractionMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def selected_anchor(self) -> str | None:
        """The point anchor which is part of a gizmo this tool is moving currently."""
        member = self.get_member("_selectedAnchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_anchor.setter
    def selected_anchor(self, target: str | PointAnchor | None) -> None:
        """Set the _selectedAnchor reference by target ID or PointAnchor instance."""
        target_id: str | None = target.id if isinstance(target, PointAnchor) else target  # type: ignore[assignment]
        member = self.get_member("_selectedAnchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectedAnchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PointAnchor'),
            )

    @property
    def selected_anchor_highlight(self) -> str | None:
        """The slot being used to indicate what gizmo is currently being moved. Is an icosphere."""
        member = self.get_member("_selectedAnchorHighlight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_anchor_highlight.setter
    def selected_anchor_highlight(self, target: str | Slot | None) -> None:
        """Set the _selectedAnchorHighlight reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_selectedAnchorHighlight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectedAnchorHighlight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def material(self) -> str | None:
        """The visual material used for the default cone mesh."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _material reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def current_gizmo(self) -> str | None:
        """The gizmo that the dev tool is currently targeting for gizmo options."""
        member = self.get_member("_currentGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_gizmo.setter
    def current_gizmo(self, target: str | Slot | None) -> None:
        """Set the _currentGizmo reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_currentGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def previous_gizmo(self) -> str | None:
        """The previous gizmo that the dev tool targeted for gizmo options."""
        member = self.get_member("_previousGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @previous_gizmo.setter
    def previous_gizmo(self, target: str | Slot | None) -> None:
        """Set the _previousGizmo reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_previousGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previousGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    async def select_parent(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """See Dev Tool.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SelectParent", {}, debug,
        )

    async def toggle_space(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """See Dev Tool.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ToggleSpace", {}, debug,
        )

    async def set_translation(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """See Dev Tool.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetTranslation", {}, debug,
        )

    async def set_rotation(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """See Dev Tool.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetRotation", {}, debug,
        )

    async def set_scale(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """See Dev Tool.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetScale", {}, debug,
        )

