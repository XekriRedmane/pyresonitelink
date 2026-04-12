"""Generated component: LegacyEnumEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyEnumEditor(GenericComponent[T], ITouchable, IWorldEventReceiver):
    """The LegacyEnumEditor component is used to cycle between enums. It is Legacy content migrated from other platforms. This should not be used, and replaced whenever possible.

    Category: UI/Physical

    When attaching, the component needs an Enum type for E. But just don't
    use this component for new content at all.

    Parameterize with a value type::

        LegacyEnumEditor[primitives.Float]
        LegacyEnumEditor[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyEnumEditor<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.LegacyEnumEditor<>"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, color: primitives.ColorX | None = None, width: primitives.Float | None = None, height: primitives.Float | None = None, thickness: primitives.Float | None = None, slant: primitives.Float | None = None, text_slot: str | Slot | None = None, text_renderer: str | TextRenderer | None = None, text_editor: str | TextEditor | None = None, material: str | PBS_RimMetallic | None = None, mesh: str | BevelStripeMesh | None = None, text_bounds: str | IField[primitives.Float2] | None = None, collider_size: str | IField[primitives.Float3] | None = None, mesh_left: str | BevelStripeMesh | None = None, mesh_right: str | BevelStripeMesh | None = None, text_left_bounds: str | IField[primitives.Float2] | None = None, text_right_bounds: str | IField[primitives.Float2] | None = None, left_text_renderer: str | TextRenderer | None = None, right_text_renderer: str | TextRenderer | None = None, collider_left_size: str | IField[primitives.Float3] | None = None, collider_right_size: str | IField[primitives.Float3] | None = None, left_offset: str | IField[primitives.Float3] | None = None, right_offset: str | IField[primitives.Float3] | None = None, left_text_position: str | IField[primitives.Float3] | None = None, right_text_position: str | IField[primitives.Float3] | None = None, is_enabled: primitives.Bool | None = None, value: T | None = None, text_drive: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
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
            value: Initial value for Value.
            text_drive: Initial value for _textDrive.
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
        if value is not None:
            self.value = value
        if text_drive is not None:
            self.text_drive = text_drive

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
        """The color of the UI."""
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
        """The width of the UI"""
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
        """How thick the UI is."""
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
        """The beveledness of the UI elements."""
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
        """The slot of the text visual for the enum indicator"""
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
        """The text renderer of the enum indcator."""
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
        """The text editor for editing the enum text."""
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
        """The material of the UI."""
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
        """The mesh of the ui."""
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
        """The field that is used to make the UI wrap around the text"""
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
        """The size of the collider for the UI."""
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
        """The mesh of the left cycle button"""
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
        """The mesh of the right cycle button"""
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
        """The field to make the UI wrap around the left button text."""
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
        """The field to make the UI wrap around the right button text."""
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
        """The renderer for the text of the left button."""
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
        """The renderer for the text of the right button."""
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
        """The collider field to drive to make the collider envelop the left UI."""
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
        """the collider firld to drive to make the collider envelop the right UI."""
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
        """The field to drive for the left button offset."""
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
        """The field to drive for the right button offset."""
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
        """The field to drive for the left text position."""
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
        """The field to drive for the right text position."""
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
    def value(self) -> T | None:
        """The Value field value (type depends on type parameter)."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: T) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value", self._type_info.field_class(value=value)
            )

    @property
    def text_drive(self) -> str | None:
        """The string field to drive with the string version of the selected enum from ``Value``."""
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_drive.setter
    def text_drive(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _textDrive reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

