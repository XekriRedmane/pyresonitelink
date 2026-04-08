"""Generated component: LightTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.item import Item
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LightTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LightTool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LightTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, color: primitives.ColorX | None = None, intensity: primitives.Float | None = None, shadow_strength: primitives.Float | None = None, range_: primitives.Float | None = None, spot_angle: primitives.Float | None = None, point_light_visual: str | Slot | None = None, spotlight_visual: str | Slot | None = None, directional_light_visual: str | Slot | None = None, show_gizmo: primitives.Bool | None = None, point_light_item: str | Item | None = None, spot_light_item: str | Item | None = None, directional_light_item: str | Item | None = None, shadows_item: str | Item | None = None, color_picker: str | ColorDialogInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            color: Initial value for Color.
            intensity: Initial value for Intensity.
            shadow_strength: Initial value for ShadowStrength.
            range_: Initial value for Range.
            spot_angle: Initial value for SpotAngle.
            point_light_visual: Initial value for PointLightVisual.
            spotlight_visual: Initial value for SpotlightVisual.
            directional_light_visual: Initial value for DirectionalLightVisual.
            show_gizmo: Initial value for ShowGizmo.
            point_light_item: Initial value for _pointLightItem.
            spot_light_item: Initial value for _spotLightItem.
            directional_light_item: Initial value for _directionalLightItem.
            shadows_item: Initial value for _shadowsItem.
            color_picker: Initial value for _colorPicker.
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
        if color is not None:
            self.color = color
        if intensity is not None:
            self.intensity = intensity
        if shadow_strength is not None:
            self.shadow_strength = shadow_strength
        if range_ is not None:
            self.range_ = range_
        if spot_angle is not None:
            self.spot_angle = spot_angle
        if point_light_visual is not None:
            self.point_light_visual = point_light_visual
        if spotlight_visual is not None:
            self.spotlight_visual = spotlight_visual
        if directional_light_visual is not None:
            self.directional_light_visual = directional_light_visual
        if show_gizmo is not None:
            self.show_gizmo = show_gizmo
        if point_light_item is not None:
            self.point_light_item = point_light_item
        if spot_light_item is not None:
            self.spot_light_item = spot_light_item
        if directional_light_item is not None:
            self.directional_light_item = directional_light_item
        if shadows_item is not None:
            self.shadows_item = shadows_item
        if color_picker is not None:
            self.color_picker = color_picker

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
    def light_mode(self) -> members.FieldEnum | None:
        """The LightMode member."""
        member = self.get_member("LightMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @light_mode.setter
    def light_mode(self, value: members.FieldEnum) -> None:
        """Set the LightMode member."""
        self.set_member("LightMode", value)

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def intensity(self) -> primitives.Float | None:
        """The Intensity field value."""
        member = self.get_member("Intensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity.setter
    def intensity(self, value: primitives.Float) -> None:
        """Set the Intensity field value."""
        member = self.get_member("Intensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Intensity", fields.FieldFloat(value=value)
            )

    @property
    def shadow_type(self) -> members.FieldEnum | None:
        """The ShadowType member."""
        member = self.get_member("ShadowType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shadow_type.setter
    def shadow_type(self, value: members.FieldEnum) -> None:
        """Set the ShadowType member."""
        self.set_member("ShadowType", value)

    @property
    def shadow_strength(self) -> primitives.Float | None:
        """The ShadowStrength field value."""
        member = self.get_member("ShadowStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_strength.setter
    def shadow_strength(self, value: primitives.Float) -> None:
        """Set the ShadowStrength field value."""
        member = self.get_member("ShadowStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowStrength", fields.FieldFloat(value=value)
            )

    @property
    def range_(self) -> primitives.Float | None:
        """The Range field value."""
        member = self.get_member("Range")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_.setter
    def range_(self, value: primitives.Float) -> None:
        """Set the Range field value."""
        member = self.get_member("Range")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Range", fields.FieldFloat(value=value)
            )

    @property
    def spot_angle(self) -> primitives.Float | None:
        """The SpotAngle field value."""
        member = self.get_member("SpotAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spot_angle.setter
    def spot_angle(self, value: primitives.Float) -> None:
        """Set the SpotAngle field value."""
        member = self.get_member("SpotAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpotAngle", fields.FieldFloat(value=value)
            )

    @property
    def point_light_visual(self) -> str | None:
        """Target ID of the PointLightVisual reference (targets Slot)."""
        member = self.get_member("PointLightVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_light_visual.setter
    def point_light_visual(self, target: str | Slot | None) -> None:
        """Set the PointLightVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PointLightVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PointLightVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def spotlight_visual(self) -> str | None:
        """Target ID of the SpotlightVisual reference (targets Slot)."""
        member = self.get_member("SpotlightVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spotlight_visual.setter
    def spotlight_visual(self, target: str | Slot | None) -> None:
        """Set the SpotlightVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SpotlightVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpotlightVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def directional_light_visual(self) -> str | None:
        """Target ID of the DirectionalLightVisual reference (targets Slot)."""
        member = self.get_member("DirectionalLightVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @directional_light_visual.setter
    def directional_light_visual(self, target: str | Slot | None) -> None:
        """Set the DirectionalLightVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DirectionalLightVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DirectionalLightVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def color_indicators(self) -> members.SyncList | None:
        """The ColorIndicators member."""
        member = self.get_member("ColorIndicators")
        if isinstance(member, members.SyncList):
            return member
        return None

    @color_indicators.setter
    def color_indicators(self, value: members.SyncList) -> None:
        """Set the ColorIndicators member."""
        self.set_member("ColorIndicators", value)

    @property
    def show_gizmo(self) -> primitives.Bool | None:
        """The ShowGizmo field value."""
        member = self.get_member("ShowGizmo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_gizmo.setter
    def show_gizmo(self, value: primitives.Bool) -> None:
        """Set the ShowGizmo field value."""
        member = self.get_member("ShowGizmo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowGizmo", fields.FieldBool(value=value)
            )

    @property
    def point_light_item(self) -> str | None:
        """Target ID of the _pointLightItem reference (targets Item)."""
        member = self.get_member("_pointLightItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_light_item.setter
    def point_light_item(self, target: str | Item | None) -> None:
        """Set the _pointLightItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_pointLightItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pointLightItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def spot_light_item(self) -> str | None:
        """Target ID of the _spotLightItem reference (targets Item)."""
        member = self.get_member("_spotLightItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spot_light_item.setter
    def spot_light_item(self, target: str | Item | None) -> None:
        """Set the _spotLightItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_spotLightItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spotLightItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def directional_light_item(self) -> str | None:
        """Target ID of the _directionalLightItem reference (targets Item)."""
        member = self.get_member("_directionalLightItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @directional_light_item.setter
    def directional_light_item(self, target: str | Item | None) -> None:
        """Set the _directionalLightItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_directionalLightItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_directionalLightItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def shadows_item(self) -> str | None:
        """Target ID of the _shadowsItem reference (targets Item)."""
        member = self.get_member("_shadowsItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shadows_item.setter
    def shadows_item(self, target: str | Item | None) -> None:
        """Set the _shadowsItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_shadowsItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shadowsItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def color_picker(self) -> str | None:
        """Target ID of the _colorPicker reference (targets ColorDialogInterface)."""
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_picker.setter
    def color_picker(self, target: str | ColorDialogInterface | None) -> None:
        """Set the _colorPicker reference by target ID or ColorDialogInterface instance."""
        target_id: str | None = target.id if isinstance(target, ColorDialogInterface) else target  # type: ignore[assignment]
        member = self.get_member("_colorPicker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorPicker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorDialogInterface'),
            )

