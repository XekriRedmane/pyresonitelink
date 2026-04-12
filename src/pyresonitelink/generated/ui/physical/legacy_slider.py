"""Generated component: LegacySlider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.multi_bevel_stripe_mesh import MultiBevelStripeMesh
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.islider import ISlider
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySlider(GeneratedComponent, ISlider, ITouchable, IWorldEventReceiver):
    """The LegacySlider component was used in old legacy content to act as a UI for adjusting a float via a slider. This component should not be used in new content and should be replaced whenever possible.

    Category: UI/Physical
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySlider"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, is_enabled_field: primitives.Bool | None = None, drive_field: str | IField[primitives.Float] | None = None, allow_write_back: primitives.Bool | None = None, create_undo_step: primitives.Bool | None = None, value: primitives.Float | None = None, min: primitives.Float | None = None, max: primitives.Float | None = None, increment: primitives.Float | None = None, integer_only: primitives.Bool | None = None, color_field: primitives.ColorX | None = None, symmetrical_field: primitives.Bool | None = None, width_field: primitives.Float | None = None, height_field: primitives.Float | None = None, cursor_ratio_field: primitives.Float | None = None, thickness_field: primitives.Float | None = None, slant_field: primitives.Float | None = None, spacing_ratio_field: primitives.Float | None = None, track_ratio_field: primitives.Float | None = None, button_ratio_field: primitives.Float | None = None, track_mesh: str | MultiBevelStripeMesh | None = None, left_mesh: str | BevelStripeMesh | None = None, right_mesh: str | BevelStripeMesh | None = None, cursor_mesh: str | BevelStripeMesh | None = None, track_material: str | PBS_RimMetallic | None = None, left_material: str | PBS_RimMetallic | None = None, right_material: str | PBS_RimMetallic | None = None, cursor_material: str | PBS_RimMetallic | None = None, left_position: str | IField[primitives.Float3] | None = None, right_position: str | IField[primitives.Float3] | None = None, cursor_position: str | IField[primitives.Float3] | None = None, left_collider_size: str | IField[primitives.Float3] | None = None, right_collider_size: str | IField[primitives.Float3] | None = None, track_collider_size: str | IField[primitives.Float3] | None = None, cursor_collider_size: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            is_enabled_field: Initial value for IsEnabledField.
            drive_field: Initial value for DriveField.
            allow_write_back: Initial value for AllowWriteBack.
            create_undo_step: Initial value for CreateUndoStep.
            value: Initial value for Value.
            min: Initial value for Min.
            max: Initial value for Max.
            increment: Initial value for Increment.
            integer_only: Initial value for IntegerOnly.
            color_field: Initial value for ColorField.
            symmetrical_field: Initial value for SymmetricalField.
            width_field: Initial value for WidthField.
            height_field: Initial value for HeightField.
            cursor_ratio_field: Initial value for CursorRatioField.
            thickness_field: Initial value for ThicknessField.
            slant_field: Initial value for SlantField.
            spacing_ratio_field: Initial value for SpacingRatioField.
            track_ratio_field: Initial value for TrackRatioField.
            button_ratio_field: Initial value for ButtonRatioField.
            track_mesh: Initial value for _trackMesh.
            left_mesh: Initial value for _leftMesh.
            right_mesh: Initial value for _rightMesh.
            cursor_mesh: Initial value for _cursorMesh.
            track_material: Initial value for _trackMaterial.
            left_material: Initial value for _leftMaterial.
            right_material: Initial value for _rightMaterial.
            cursor_material: Initial value for _cursorMaterial.
            left_position: Initial value for _leftPosition.
            right_position: Initial value for _rightPosition.
            cursor_position: Initial value for _cursorPosition.
            left_collider_size: Initial value for _leftColliderSize.
            right_collider_size: Initial value for _rightColliderSize.
            track_collider_size: Initial value for _trackColliderSize.
            cursor_collider_size: Initial value for _cursorColliderSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if is_enabled_field is not None:
            self.is_enabled_field = is_enabled_field
        if drive_field is not None:
            self.drive_field = drive_field
        if allow_write_back is not None:
            self.allow_write_back = allow_write_back
        if create_undo_step is not None:
            self.create_undo_step = create_undo_step
        if value is not None:
            self.value = value
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if increment is not None:
            self.increment = increment
        if integer_only is not None:
            self.integer_only = integer_only
        if color_field is not None:
            self.color_field = color_field
        if symmetrical_field is not None:
            self.symmetrical_field = symmetrical_field
        if width_field is not None:
            self.width_field = width_field
        if height_field is not None:
            self.height_field = height_field
        if cursor_ratio_field is not None:
            self.cursor_ratio_field = cursor_ratio_field
        if thickness_field is not None:
            self.thickness_field = thickness_field
        if slant_field is not None:
            self.slant_field = slant_field
        if spacing_ratio_field is not None:
            self.spacing_ratio_field = spacing_ratio_field
        if track_ratio_field is not None:
            self.track_ratio_field = track_ratio_field
        if button_ratio_field is not None:
            self.button_ratio_field = button_ratio_field
        if track_mesh is not None:
            self.track_mesh = track_mesh
        if left_mesh is not None:
            self.left_mesh = left_mesh
        if right_mesh is not None:
            self.right_mesh = right_mesh
        if cursor_mesh is not None:
            self.cursor_mesh = cursor_mesh
        if track_material is not None:
            self.track_material = track_material
        if left_material is not None:
            self.left_material = left_material
        if right_material is not None:
            self.right_material = right_material
        if cursor_material is not None:
            self.cursor_material = cursor_material
        if left_position is not None:
            self.left_position = left_position
        if right_position is not None:
            self.right_position = right_position
        if cursor_position is not None:
            self.cursor_position = cursor_position
        if left_collider_size is not None:
            self.left_collider_size = left_collider_size
        if right_collider_size is not None:
            self.right_collider_size = right_collider_size
        if track_collider_size is not None:
            self.track_collider_size = track_collider_size
        if cursor_collider_size is not None:
            self.cursor_collider_size = cursor_collider_size

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
    def is_enabled_field(self) -> primitives.Bool | None:
        """The IsEnabledField field value."""
        member = self.get_member("IsEnabledField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled_field.setter
    def is_enabled_field(self, value: primitives.Bool) -> None:
        """Set the IsEnabledField field value."""
        member = self.get_member("IsEnabledField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabledField", fields.FieldBool(value=value)
            )

    @property
    def drive_field(self) -> str | None:
        """The float field to drive with ``Value``"""
        member = self.get_member("DriveField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_field.setter
    def drive_field(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the DriveField reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def allow_write_back(self) -> primitives.Bool | None:
        """Whether changes to the value of the field targeted by ``DriveField`` should be written back to ``Value``."""
        member = self.get_member("AllowWriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_back.setter
    def allow_write_back(self, value: primitives.Bool) -> None:
        """Set the AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteBack", fields.FieldBool(value=value)
            )

    @property
    def create_undo_step(self) -> primitives.Bool | None:
        """Whether using this UI creates an Undo step."""
        member = self.get_member("CreateUndoStep")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @create_undo_step.setter
    def create_undo_step(self, value: primitives.Bool) -> None:
        """Set the CreateUndoStep field value."""
        member = self.get_member("CreateUndoStep")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreateUndoStep", fields.FieldBool(value=value)
            )

    @property
    def value(self) -> primitives.Float | None:
        """The value this component is influencing."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: primitives.Float) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Value", fields.FieldFloat(value=value)
            )

    @property
    def min(self) -> primitives.Float | None:
        """The minimum value for ``Value``."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: primitives.Float) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Min", fields.FieldFloat(value=value)
            )

    @property
    def max(self) -> primitives.Float | None:
        """The maximum value for ``Value``."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: primitives.Float) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Max", fields.FieldFloat(value=value)
            )

    @property
    def increment(self) -> primitives.Float | None:
        """How much to shift ``Value`` by when using the slider side buttons."""
        member = self.get_member("Increment")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @increment.setter
    def increment(self, value: primitives.Float) -> None:
        """Set the Increment field value."""
        member = self.get_member("Increment")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Increment", fields.FieldFloat(value=value)
            )

    @property
    def integer_only(self) -> primitives.Bool | None:
        """Whether ``Value`` can only be a whole number."""
        member = self.get_member("IntegerOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @integer_only.setter
    def integer_only(self, value: primitives.Bool) -> None:
        """Set the IntegerOnly field value."""
        member = self.get_member("IntegerOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IntegerOnly", fields.FieldBool(value=value)
            )

    @property
    def color_field(self) -> primitives.ColorX | None:
        """The color of this UI."""
        member = self.get_member("ColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_field.setter
    def color_field(self, value: primitives.ColorX) -> None:
        """Set the ColorField field value."""
        member = self.get_member("ColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorField", fields.FieldColorX(value=value)
            )

    @property
    def symmetrical_field(self) -> primitives.Bool | None:
        """whether this UI should be symmetrical."""
        member = self.get_member("SymmetricalField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @symmetrical_field.setter
    def symmetrical_field(self, value: primitives.Bool) -> None:
        """Set the SymmetricalField field value."""
        member = self.get_member("SymmetricalField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SymmetricalField", fields.FieldBool(value=value)
            )

    @property
    def width_field(self) -> primitives.Float | None:
        """The width of this UI."""
        member = self.get_member("WidthField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width_field.setter
    def width_field(self, value: primitives.Float) -> None:
        """Set the WidthField field value."""
        member = self.get_member("WidthField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WidthField", fields.FieldFloat(value=value)
            )

    @property
    def height_field(self) -> primitives.Float | None:
        """The height of this UI."""
        member = self.get_member("HeightField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_field.setter
    def height_field(self, value: primitives.Float) -> None:
        """Set the HeightField field value."""
        member = self.get_member("HeightField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightField", fields.FieldFloat(value=value)
            )

    @property
    def cursor_ratio_field(self) -> primitives.Float | None:
        """the size of the slider cursor compared to the slider container."""
        member = self.get_member("CursorRatioField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cursor_ratio_field.setter
    def cursor_ratio_field(self, value: primitives.Float) -> None:
        """Set the CursorRatioField field value."""
        member = self.get_member("CursorRatioField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CursorRatioField", fields.FieldFloat(value=value)
            )

    @property
    def thickness_field(self) -> primitives.Float | None:
        """the thickness of the UI."""
        member = self.get_member("ThicknessField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness_field.setter
    def thickness_field(self, value: primitives.Float) -> None:
        """Set the ThicknessField field value."""
        member = self.get_member("ThicknessField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThicknessField", fields.FieldFloat(value=value)
            )

    @property
    def slant_field(self) -> primitives.Float | None:
        """How beveled the UI is."""
        member = self.get_member("SlantField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant_field.setter
    def slant_field(self, value: primitives.Float) -> None:
        """Set the SlantField field value."""
        member = self.get_member("SlantField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlantField", fields.FieldFloat(value=value)
            )

    @property
    def spacing_ratio_field(self) -> primitives.Float | None:
        """How to space out the center UI and its buttons."""
        member = self.get_member("SpacingRatioField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spacing_ratio_field.setter
    def spacing_ratio_field(self, value: primitives.Float) -> None:
        """Set the SpacingRatioField field value."""
        member = self.get_member("SpacingRatioField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpacingRatioField", fields.FieldFloat(value=value)
            )

    @property
    def track_ratio_field(self) -> primitives.Float | None:
        """How big the slider track should be compared to the UI."""
        member = self.get_member("TrackRatioField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @track_ratio_field.setter
    def track_ratio_field(self, value: primitives.Float) -> None:
        """Set the TrackRatioField field value."""
        member = self.get_member("TrackRatioField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrackRatioField", fields.FieldFloat(value=value)
            )

    @property
    def button_ratio_field(self) -> primitives.Float | None:
        """How big the buttons should be compared to the slider."""
        member = self.get_member("ButtonRatioField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @button_ratio_field.setter
    def button_ratio_field(self, value: primitives.Float) -> None:
        """Set the ButtonRatioField field value."""
        member = self.get_member("ButtonRatioField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ButtonRatioField", fields.FieldFloat(value=value)
            )

    @property
    def track_mesh(self) -> str | None:
        """The mesh for the slider track."""
        member = self.get_member("_trackMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @track_mesh.setter
    def track_mesh(self, target: str | MultiBevelStripeMesh | None) -> None:
        """Set the _trackMesh reference by target ID or MultiBevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, MultiBevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_trackMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_trackMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MultiBevelStripeMesh'),
            )

    @property
    def left_mesh(self) -> str | None:
        """The mesh for the left button."""
        member = self.get_member("_leftMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_mesh.setter
    def left_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _leftMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_leftMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def right_mesh(self) -> str | None:
        """The mesh for the right button."""
        member = self.get_member("_rightMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_mesh.setter
    def right_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _rightMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_rightMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def cursor_mesh(self) -> str | None:
        """The mesh for the slider cursor."""
        member = self.get_member("_cursorMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_mesh.setter
    def cursor_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _cursorMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_cursorMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def track_material(self) -> str | None:
        """The material of the slider track."""
        member = self.get_member("_trackMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @track_material.setter
    def track_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _trackMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_trackMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_trackMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def left_material(self) -> str | None:
        """The material of the left button."""
        member = self.get_member("_leftMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_material.setter
    def left_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _leftMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_leftMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def right_material(self) -> str | None:
        """The material of the right button."""
        member = self.get_member("_rightMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_material.setter
    def right_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _rightMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_rightMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def cursor_material(self) -> str | None:
        """The material of the slider cursor."""
        member = self.get_member("_cursorMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_material.setter
    def cursor_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _cursorMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_cursorMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def left_position(self) -> str | None:
        """The position field of the left button."""
        member = self.get_member("_leftPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_position.setter
    def left_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_position(self) -> str | None:
        """The position field of the right button."""
        member = self.get_member("_rightPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_position.setter
    def right_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def cursor_position(self) -> str | None:
        """The position field of the cursor."""
        member = self.get_member("_cursorPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_position.setter
    def cursor_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cursorPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_collider_size(self) -> str | None:
        """The size field of the left button's collider."""
        member = self.get_member("_leftColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_collider_size.setter
    def left_collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_collider_size(self) -> str | None:
        """The size field of the right button's collider."""
        member = self.get_member("_rightColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_collider_size.setter
    def right_collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def track_collider_size(self) -> str | None:
        """The size field of the track's collider."""
        member = self.get_member("_trackColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @track_collider_size.setter
    def track_collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _trackColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_trackColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_trackColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def cursor_collider_size(self) -> str | None:
        """The size field of the cursor's collider."""
        member = self.get_member("_cursorColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cursor_collider_size.setter
    def cursor_collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cursorColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cursorColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cursorColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

