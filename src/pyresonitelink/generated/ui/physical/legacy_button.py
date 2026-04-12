"""Generated component: LegacyButton."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyButton(GeneratedComponent, IButton, ITouchable, IWorldEventReceiver):
    """The LegacyButton component is a leftover Component from content migrated from other platforms. It should not be used, and should be replaced whenever possible.

    Category: UI/Physical
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyButton"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, color: primitives.ColorX | None = None, width: primitives.Float | None = None, height: primitives.Float | None = None, thickness: primitives.Float | None = None, slant: primitives.Float | None = None, is_enabled: primitives.Bool | None = None, is_pressed: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, text_slot: str | Slot | None = None, text_renderer: str | TextRenderer | None = None, button_position: str | IField[primitives.Float3] | None = None, collider_size: str | IField[primitives.Float3] | None = None, collider_offset: str | IField[primitives.Float3] | None = None, text_position: str | IField[primitives.Float3] | None = None, text_bounds: str | IField[primitives.Float2] | None = None, holder_mesh: str | BevelStripeMesh | None = None, button_mesh: str | BevelStripeMesh | None = None, holder_material: str | PBS_RimMetallic | None = None, button_material: str | PBS_RimMetallic | None = None, press_depth: primitives.Float | None = None, flash_index: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            color: Initial value for Color.
            width: Initial value for Width.
            height: Initial value for Height.
            thickness: Initial value for Thickness.
            slant: Initial value for Slant.
            is_enabled: Initial value for IsEnabled.
            is_pressed: Initial value for IsPressed.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            text_slot: Initial value for _textSlot.
            text_renderer: Initial value for _textRenderer.
            button_position: Initial value for _buttonPosition.
            collider_size: Initial value for _colliderSize.
            collider_offset: Initial value for _colliderOffset.
            text_position: Initial value for _textPosition.
            text_bounds: Initial value for _textBounds.
            holder_mesh: Initial value for _holderMesh.
            button_mesh: Initial value for _buttonMesh.
            holder_material: Initial value for _holderMaterial.
            button_material: Initial value for _buttonMaterial.
            press_depth: Initial value for _pressDepth.
            flash_index: Initial value for _flashIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if color is not None:
            self.color = color
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if thickness is not None:
            self.thickness = thickness
        if slant is not None:
            self.slant = slant
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_pressed is not None:
            self.is_pressed = is_pressed
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if text_slot is not None:
            self.text_slot = text_slot
        if text_renderer is not None:
            self.text_renderer = text_renderer
        if button_position is not None:
            self.button_position = button_position
        if collider_size is not None:
            self.collider_size = collider_size
        if collider_offset is not None:
            self.collider_offset = collider_offset
        if text_position is not None:
            self.text_position = text_position
        if text_bounds is not None:
            self.text_bounds = text_bounds
        if holder_mesh is not None:
            self.holder_mesh = holder_mesh
        if button_mesh is not None:
            self.button_mesh = button_mesh
        if holder_material is not None:
            self.holder_material = holder_material
        if button_material is not None:
            self.button_material = button_material
        if press_depth is not None:
            self.press_depth = press_depth
        if flash_index is not None:
            self.flash_index = flash_index

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The color of the button."""
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
    def width(self) -> primitives.Float | None:
        """The width of the button."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def height(self) -> primitives.Float | None:
        """The height of the button."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> primitives.Float | None:
        """How thick the button is."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: primitives.Float) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def slant(self) -> primitives.Float | None:
        """How much Bevel the button should have."""
        member = self.get_member("Slant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant.setter
    def slant(self, value: primitives.Float) -> None:
        """Set the Slant field value."""
        member = self.get_member("Slant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Slant", fields.FieldFloat(value=value)
            )

    @property
    def is_enabled(self) -> primitives.Bool | None:
        """The IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled.setter
    def is_enabled(self, value: primitives.Bool) -> None:
        """Set the IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabled", fields.FieldBool(value=value)
            )

    @property
    def is_pressed(self) -> primitives.Bool | None:
        """Whether the button is being pressed currently."""
        member = self.get_member("IsPressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_pressed.setter
    def is_pressed(self, value: primitives.Bool) -> None:
        """Set the IsPressed field value."""
        member = self.get_member("IsPressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPressed", fields.FieldBool(value=value)
            )

    @property
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """Whether this button accepts interaction if the user isn't looking at it."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def text_slot(self) -> str | None:
        """The slot of the text visual for this button."""
        member = self.get_member("_textSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_slot.setter
    def text_slot(self, target: str | Slot | None) -> None:
        """Set the _textSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_textSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def text_renderer(self) -> str | None:
        """The text renderer for this button."""
        member = self.get_member("_textRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_renderer.setter
    def text_renderer(self, target: str | TextRenderer | None) -> None:
        """Set the _textRenderer reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_textRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def button_position(self) -> str | None:
        """The position field for this button for physical pressing."""
        member = self.get_member("_buttonPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button_position.setter
    def button_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _buttonPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_buttonPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_size(self) -> str | None:
        """The collider size field for this button's collider."""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_offset(self) -> str | None:
        """The collider offset field for this button's collider."""
        member = self.get_member("_colliderOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_offset.setter
    def collider_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def text_position(self) -> str | None:
        """The text position field for this button's text"""
        member = self.get_member("_textPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_position.setter
    def text_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _textPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def text_bounds(self) -> str | None:
        """The 2d bounds of this button's text"""
        member = self.get_member("_textBounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_bounds.setter
    def text_bounds(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _textBounds reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textBounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textBounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def holder_mesh(self) -> str | None:
        """The mesh that is containing this button (like a parent UI."""
        member = self.get_member("_holderMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @holder_mesh.setter
    def holder_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _holderMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_holderMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holderMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def button_mesh(self) -> str | None:
        """The Bevel mesh that makes up this button's visual."""
        member = self.get_member("_buttonMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button_mesh.setter
    def button_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _buttonMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_buttonMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def holder_material(self) -> str | None:
        """The material of the parent UI mesh."""
        member = self.get_member("_holderMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @holder_material.setter
    def holder_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _holderMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_holderMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holderMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def button_material(self) -> str | None:
        """The material of this button's mesh visual"""
        member = self.get_member("_buttonMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button_material.setter
    def button_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _buttonMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_buttonMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def press_depth(self) -> primitives.Float | None:
        """How far the user is currently pressing the button physically"""
        member = self.get_member("_pressDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @press_depth.setter
    def press_depth(self, value: primitives.Float) -> None:
        """Set the _pressDepth field value."""
        member = self.get_member("_pressDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_pressDepth", fields.FieldFloat(value=value)
            )

    @property
    def flash_index(self) -> primitives.Int | None:
        """How much to add to the emission of the holder material."""
        member = self.get_member("_flashIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flash_index.setter
    def flash_index(self, value: primitives.Int) -> None:
        """Set the _flashIndex field value."""
        member = self.get_member("_flashIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_flashIndex", fields.FieldInt(value=value)
            )

