"""Generated component: LegacyTextField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itext_field import ITextField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyTextField(GeneratedComponent, ITextField, ITouchable, IWorldEventReceiver):
    """The LegacyTextField component was used to edit text in old content migrated from other platforms. This component should not be used in new content, and should be replaced whenever possible.

    Category: UI/Physical

    Just dont.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyTextField"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, color: primitives.ColorX | None = None, width: primitives.Float | None = None, height: primitives.Float | None = None, thickness: primitives.Float | None = None, slant: primitives.Float | None = None, text_slot: str | Slot | None = None, text_renderer: str | TextRenderer | None = None, text_editor: str | TextEditor | None = None, material: str | PBS_RimMetallic | None = None, mesh: str | BevelStripeMesh | None = None, text_bounds: str | IField[primitives.Float2] | None = None, collider_size: str | IField[primitives.Float3] | None = None, mesh_left: str | BevelStripeMesh | None = None, mesh_right: str | BevelStripeMesh | None = None, text_left_bounds: str | IField[primitives.Float2] | None = None, text_right_bounds: str | IField[primitives.Float2] | None = None, left_text_renderer: str | TextRenderer | None = None, right_text_renderer: str | TextRenderer | None = None, collider_left_size: str | IField[primitives.Float3] | None = None, collider_right_size: str | IField[primitives.Float3] | None = None, left_offset: str | IField[primitives.Float3] | None = None, right_offset: str | IField[primitives.Float3] | None = None, left_text_position: str | IField[primitives.Float3] | None = None, right_text_position: str | IField[primitives.Float3] | None = None, is_enabled: primitives.Bool | None = None, hint_text_renderer: str | TextRenderer | None = None, hint_text_bounds: str | IField[primitives.Float2] | None = None, hint_text_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
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
            text_slot: Initial value for _textSlot.
            text_renderer: Initial value for _textRenderer.
            text_editor: Initial value for _textEditor.
            material: Initial value for _material.
            mesh: Initial value for _mesh.
            text_bounds: Initial value for _textBounds.
            collider_size: Initial value for _colliderSize.
            mesh_left: Initial value for _meshLeft.
            mesh_right: Initial value for _meshRight.
            text_left_bounds: Initial value for _textLeftBounds.
            text_right_bounds: Initial value for _textRightBounds.
            left_text_renderer: Initial value for _leftTextRenderer.
            right_text_renderer: Initial value for _rightTextRenderer.
            collider_left_size: Initial value for _colliderLeftSize.
            collider_right_size: Initial value for _colliderRightSize.
            left_offset: Initial value for _leftOffset.
            right_offset: Initial value for _rightOffset.
            left_text_position: Initial value for _leftTextPosition.
            right_text_position: Initial value for _rightTextPosition.
            is_enabled: Initial value for IsEnabled.
            hint_text_renderer: Initial value for _hintTextRenderer.
            hint_text_bounds: Initial value for _hintTextBounds.
            hint_text_enabled: Initial value for _hintTextEnabled.
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
        if text_slot is not None:
            self.text_slot = text_slot
        if text_renderer is not None:
            self.text_renderer = text_renderer
        if text_editor is not None:
            self.text_editor = text_editor
        if material is not None:
            self.material = material
        if mesh is not None:
            self.mesh = mesh
        if text_bounds is not None:
            self.text_bounds = text_bounds
        if collider_size is not None:
            self.collider_size = collider_size
        if mesh_left is not None:
            self.mesh_left = mesh_left
        if mesh_right is not None:
            self.mesh_right = mesh_right
        if text_left_bounds is not None:
            self.text_left_bounds = text_left_bounds
        if text_right_bounds is not None:
            self.text_right_bounds = text_right_bounds
        if left_text_renderer is not None:
            self.left_text_renderer = left_text_renderer
        if right_text_renderer is not None:
            self.right_text_renderer = right_text_renderer
        if collider_left_size is not None:
            self.collider_left_size = collider_left_size
        if collider_right_size is not None:
            self.collider_right_size = collider_right_size
        if left_offset is not None:
            self.left_offset = left_offset
        if right_offset is not None:
            self.right_offset = right_offset
        if left_text_position is not None:
            self.left_text_position = left_text_position
        if right_text_position is not None:
            self.right_text_position = right_text_position
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if hint_text_renderer is not None:
            self.hint_text_renderer = hint_text_renderer
        if hint_text_bounds is not None:
            self.hint_text_bounds = hint_text_bounds
        if hint_text_enabled is not None:
            self.hint_text_enabled = hint_text_enabled

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
        """The color of the UI elements."""
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
        """The width of the UI."""
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
        """The height of the UI."""
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
        """The thickness of the UI."""
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
        """How beveled the UI elements should be."""
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
    def text_slot(self) -> str | None:
        """The slot of the text visual of this UI element."""
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
        """The text renderer of this UI element."""
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
    def text_editor(self) -> str | None:
        """The text editor that allows direct editing of the value this UI element controls."""
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_editor.setter
    def text_editor(self, target: str | TextEditor | None) -> None:
        """Set the _textEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def material(self) -> str | None:
        """The material of this UI."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _material reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def mesh(self) -> str | None:
        """The mesh of this UI."""
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _mesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def text_bounds(self) -> str | None:
        """The field to drive with the bounds of the text to keep the UI around it."""
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
    def collider_size(self) -> str | None:
        """The field to drive with what the size of this UI's collider should be."""
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
    def mesh_left(self) -> str | None:
        """The mesh of the left button."""
        member = self.get_member("_meshLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_left.setter
    def mesh_left(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _meshLeft reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_meshLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_meshLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def mesh_right(self) -> str | None:
        """The mesh of the right button."""
        member = self.get_member("_meshRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_right.setter
    def mesh_right(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _meshRight reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_meshRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_meshRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def text_left_bounds(self) -> str | None:
        """The field to drive with the bounds of the text on the left button so the UI stays wrapped around it."""
        member = self.get_member("_textLeftBounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_left_bounds.setter
    def text_left_bounds(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _textLeftBounds reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textLeftBounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textLeftBounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def text_right_bounds(self) -> str | None:
        """The field to drive with the bounds of the text on the right button so the UI stays wrapped around it."""
        member = self.get_member("_textRightBounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_right_bounds.setter
    def text_right_bounds(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _textRightBounds reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textRightBounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textRightBounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def left_text_renderer(self) -> str | None:
        """The text renderer of the left button."""
        member = self.get_member("_leftTextRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_text_renderer.setter
    def left_text_renderer(self, target: str | TextRenderer | None) -> None:
        """Set the _leftTextRenderer reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_leftTextRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftTextRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def right_text_renderer(self) -> str | None:
        """The text renderer of the right button."""
        member = self.get_member("_rightTextRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_text_renderer.setter
    def right_text_renderer(self, target: str | TextRenderer | None) -> None:
        """Set the _rightTextRenderer reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_rightTextRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightTextRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def collider_left_size(self) -> str | None:
        """The field to drive with what the size of the left collider should be."""
        member = self.get_member("_colliderLeftSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_left_size.setter
    def collider_left_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderLeftSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderLeftSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderLeftSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_right_size(self) -> str | None:
        """The field to drive with what the size of the right collider should be."""
        member = self.get_member("_colliderRightSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_right_size.setter
    def collider_right_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderRightSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderRightSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderRightSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_offset(self) -> str | None:
        """The field to drive with what the offset of the left collider should be."""
        member = self.get_member("_leftOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_offset.setter
    def left_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_offset(self) -> str | None:
        """The field to drive with what the offset of the right collider should be."""
        member = self.get_member("_rightOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_offset.setter
    def right_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_text_position(self) -> str | None:
        """The field to drive wiyh what the position of the text on the left button should be."""
        member = self.get_member("_leftTextPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_text_position.setter
    def left_text_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftTextPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftTextPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftTextPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_text_position(self) -> str | None:
        """The field to drive wiyh what the position of the text on the right button should be."""
        member = self.get_member("_rightTextPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_text_position.setter
    def right_text_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightTextPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightTextPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightTextPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
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
    def hint_text_renderer(self) -> str | None:
        """the text renderer of the edit text hint"""
        member = self.get_member("_hintTextRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hint_text_renderer.setter
    def hint_text_renderer(self, target: str | TextRenderer | None) -> None:
        """Set the _hintTextRenderer reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_hintTextRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hintTextRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def hint_text_bounds(self) -> str | None:
        """the field to drive with the bounds of the hint text for keeping a UI wrapped around it."""
        member = self.get_member("_hintTextBounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hint_text_bounds.setter
    def hint_text_bounds(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _hintTextBounds reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_hintTextBounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hintTextBounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def hint_text_enabled(self) -> str | None:
        """Whether the hint text should be enabled or not."""
        member = self.get_member("_hintTextEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hint_text_enabled.setter
    def hint_text_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _hintTextEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_hintTextEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hintTextEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

