"""Generated component: LegacySegmentCircleMenuController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_unlit_material import TextUnlitMaterial
from pyresonitelink.generated._types.legacy_circle_segment_mesh import LegacyCircleSegmentMesh
from pyresonitelink.generated._types.sync_list import SyncList
from pyresonitelink.generated._types.menu_segment import MenuSegment
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySegmentCircleMenuController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This is a Legacy item and should not be used.

    Just don't.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController"

    def __init__(self, default_font_material: str | TextUnlitMaterial | None = None, disabled_outline_color: primitives.ColorX | None = None, disabled_fill_color: primitives.ColorX | None = None, logo_circle: primitives.Bool | None = None, generate_colliders: primitives.Bool | None = None, highlight_radius_offset: primitives.Float | None = None, logo_menu_mesh: str | LegacyCircleSegmentMesh | None = None, overrides_drive: str | SyncList[MenuSegment] | None = None, independent_drive: str | SyncList[MenuSegment] | None = None, menu_items_slot: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_font_material: Initial value for DefaultFontMaterial.
            disabled_outline_color: Initial value for DisabledOutlineColor.
            disabled_fill_color: Initial value for DisabledFillColor.
            logo_circle: Initial value for LogoCircle.
            generate_colliders: Initial value for GenerateColliders.
            highlight_radius_offset: Initial value for HighlightRadiusOffset.
            logo_menu_mesh: Initial value for logoMenuMesh.
            overrides_drive: Initial value for _overridesDrive.
            independent_drive: Initial value for _independentDrive.
            menu_items_slot: Initial value for menuItemsSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_font_material is not None:
            self.default_font_material = default_font_material
        if disabled_outline_color is not None:
            self.disabled_outline_color = disabled_outline_color
        if disabled_fill_color is not None:
            self.disabled_fill_color = disabled_fill_color
        if logo_circle is not None:
            self.logo_circle = logo_circle
        if generate_colliders is not None:
            self.generate_colliders = generate_colliders
        if highlight_radius_offset is not None:
            self.highlight_radius_offset = highlight_radius_offset
        if logo_menu_mesh is not None:
            self.logo_menu_mesh = logo_menu_mesh
        if overrides_drive is not None:
            self.overrides_drive = overrides_drive
        if independent_drive is not None:
            self.independent_drive = independent_drive
        if menu_items_slot is not None:
            self.menu_items_slot = menu_items_slot

    @property
    def default_font_material(self) -> str | None:
        """The default font to use for menu items."""
        member = self.get_member("DefaultFontMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_font_material.setter
    def default_font_material(self, target: str | TextUnlitMaterial | None) -> None:
        """Set the DefaultFontMaterial reference by target ID or TextUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, TextUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("DefaultFontMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultFontMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextUnlitMaterial'),
            )

    @property
    def disabled_outline_color(self) -> primitives.ColorX | None:
        """The outline color menu items should have when disabled."""
        member = self.get_member("DisabledOutlineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disabled_outline_color.setter
    def disabled_outline_color(self, value: primitives.ColorX) -> None:
        """Set the DisabledOutlineColor field value."""
        member = self.get_member("DisabledOutlineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisabledOutlineColor", fields.FieldColorX(value=value)
            )

    @property
    def disabled_fill_color(self) -> primitives.ColorX | None:
        """The color menu items should have when disabled."""
        member = self.get_member("DisabledFillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disabled_fill_color.setter
    def disabled_fill_color(self, value: primitives.ColorX) -> None:
        """Set the DisabledFillColor field value."""
        member = self.get_member("DisabledFillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisabledFillColor", fields.FieldColorX(value=value)
            )

    @property
    def logo_circle(self) -> primitives.Bool | None:
        """Whether this is a logo Circle from a long dead platform. he who shall not be named on the holy land that is this wiki - @989onan."""
        member = self.get_member("LogoCircle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @logo_circle.setter
    def logo_circle(self, value: primitives.Bool) -> None:
        """Set the LogoCircle field value."""
        member = self.get_member("LogoCircle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LogoCircle", fields.FieldBool(value=value)
            )

    @property
    def generate_colliders(self) -> primitives.Bool | None:
        """Whether to generate colliders for menu items."""
        member = self.get_member("GenerateColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_colliders.setter
    def generate_colliders(self, value: primitives.Bool) -> None:
        """Set the GenerateColliders field value."""
        member = self.get_member("GenerateColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GenerateColliders", fields.FieldBool(value=value)
            )

    @property
    def highlight_radius_offset(self) -> primitives.Float | None:
        """The tolerance for highlighting menu items."""
        member = self.get_member("HighlightRadiusOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight_radius_offset.setter
    def highlight_radius_offset(self, value: primitives.Float) -> None:
        """Set the HighlightRadiusOffset field value."""
        member = self.get_member("HighlightRadiusOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighlightRadiusOffset", fields.FieldFloat(value=value)
            )

    @property
    def logo_menu_mesh(self) -> str | None:
        """The logo mesh from a long dead platform. he who shall not be named on the holy land that is this wiki - @989onan."""
        member = self.get_member("logoMenuMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @logo_menu_mesh.setter
    def logo_menu_mesh(self, target: str | LegacyCircleSegmentMesh | None) -> None:
        """Set the logoMenuMesh reference by target ID or LegacyCircleSegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, LegacyCircleSegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("logoMenuMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "logoMenuMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyCircleSegmentMesh'),
            )

    @property
    def circle_menu_items(self) -> members.SyncList | None:
        """The list of menu items this component is managing."""
        member = self.get_member("circleMenuItems")
        if isinstance(member, members.SyncList):
            return member
        return None

    @circle_menu_items.setter
    def circle_menu_items(self, value: members.SyncList) -> None:
        """Set circleMenuItems. The list of menu items this component is managing."""
        self.set_member("circleMenuItems", value)

    @property
    def independent_menu_items(self) -> members.SyncList | None:
        """The list of independent menu items this list is managing for other tools."""
        member = self.get_member("independentMenuItems")
        if isinstance(member, members.SyncList):
            return member
        return None

    @independent_menu_items.setter
    def independent_menu_items(self, value: members.SyncList) -> None:
        """Set independentMenuItems. The list of independent menu items this list is managing for other tools."""
        self.set_member("independentMenuItems", value)

    @property
    def items_arcs(self) -> members.SyncList | None:
        """The list of item arcs this component is managing."""
        member = self.get_member("itemsArcs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items_arcs.setter
    def items_arcs(self, value: members.SyncList) -> None:
        """Set itemsArcs. The list of item arcs this component is managing."""
        self.set_member("itemsArcs", value)

    @property
    def overrides_drive(self) -> str | None:
        """List of menu segments to use as overrides."""
        member = self.get_member("_overridesDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overrides_drive.setter
    def overrides_drive(self, target: str | SyncList[MenuSegment] | None) -> None:
        """Set the _overridesDrive reference by target ID or SyncList[MenuSegment] instance."""
        target_id: str | None = target.id if isinstance(target, SyncList) else target  # type: ignore[assignment]
        member = self.get_member("_overridesDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overridesDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncList<[FrooxEngine]FrooxEngine.LegacyCircleSegmentMesh+MenuSegment>'),
            )

    @property
    def independent_drive(self) -> str | None:
        """List of indepent drives of menu segments."""
        member = self.get_member("_independentDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @independent_drive.setter
    def independent_drive(self, target: str | SyncList[MenuSegment] | None) -> None:
        """Set the _independentDrive reference by target ID or SyncList[MenuSegment] instance."""
        target_id: str | None = target.id if isinstance(target, SyncList) else target  # type: ignore[assignment]
        member = self.get_member("_independentDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_independentDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncList<[FrooxEngine]FrooxEngine.LegacyCircleSegmentMesh+MenuSegment>'),
            )

    @property
    def menu_items_slot(self) -> str | None:
        """Where to generate and place menu items for this component."""
        member = self.get_member("menuItemsSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @menu_items_slot.setter
    def menu_items_slot(self, target: str | Slot | None) -> None:
        """Set the menuItemsSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("menuItemsSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "menuItemsSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

