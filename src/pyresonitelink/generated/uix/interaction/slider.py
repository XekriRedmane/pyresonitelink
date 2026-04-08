"""Generated component: Slider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Slider(GeneratedComponent, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Slider.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Slider"

    def __init__(self, base_color: primitives.ColorX | None = None, legacy_normal_color: primitives.ColorX | None = None, legacy_highlight_color: primitives.ColorX | None = None, legacy_press_color: primitives.ColorX | None = None, legacy_disabled_color: primitives.ColorX | None = None, legacy_color_drive: str | IField[primitives.ColorX] | None = None, is_pressed: primitives.Bool | None = None, is_hovering: primitives.Bool | None = None, value: primitives.Float | None = None, min: primitives.Float | None = None, max: primitives.Float | None = None, integers: primitives.Bool | None = None, max_is_exclusive: primitives.Bool | None = None, power: primitives.Float | None = None, clamp: primitives.Bool | None = None, vibration_threshold: primitives.Float | None = None, anchor_offset: primitives.Float2 | None = None, handle_anchor_min_drive: str | IField[primitives.Float2] | None = None, handle_anchor_max_drive: str | IField[primitives.Float2] | None = None, fill_line_drive: str | IField[primitives.Float2] | None = None, require_lock_in_to_interact: primitives.Bool | None = None, require_initial_press: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_color: Initial value for BaseColor.
            legacy_normal_color: Initial value for __legacy_NormalColor.
            legacy_highlight_color: Initial value for __legacy_HighlightColor.
            legacy_press_color: Initial value for __legacy_PressColor.
            legacy_disabled_color: Initial value for __legacy_DisabledColor.
            legacy_color_drive: Initial value for __legacy_ColorDrive.
            is_pressed: Initial value for IsPressed.
            is_hovering: Initial value for IsHovering.
            value: Initial value for Value.
            min: Initial value for Min.
            max: Initial value for Max.
            integers: Initial value for Integers.
            max_is_exclusive: Initial value for MaxIsExclusive.
            power: Initial value for Power.
            clamp: Initial value for Clamp.
            vibration_threshold: Initial value for VibrationThreshold.
            anchor_offset: Initial value for AnchorOffset.
            handle_anchor_min_drive: Initial value for HandleAnchorMinDrive.
            handle_anchor_max_drive: Initial value for HandleAnchorMaxDrive.
            fill_line_drive: Initial value for FillLineDrive.
            require_lock_in_to_interact: Initial value for RequireLockInToInteract.
            require_initial_press: Initial value for RequireInitialPress.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_color is not None:
            self.base_color = base_color
        if legacy_normal_color is not None:
            self.legacy_normal_color = legacy_normal_color
        if legacy_highlight_color is not None:
            self.legacy_highlight_color = legacy_highlight_color
        if legacy_press_color is not None:
            self.legacy_press_color = legacy_press_color
        if legacy_disabled_color is not None:
            self.legacy_disabled_color = legacy_disabled_color
        if legacy_color_drive is not None:
            self.legacy_color_drive = legacy_color_drive
        if is_pressed is not None:
            self.is_pressed = is_pressed
        if is_hovering is not None:
            self.is_hovering = is_hovering
        if value is not None:
            self.value = value
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if integers is not None:
            self.integers = integers
        if max_is_exclusive is not None:
            self.max_is_exclusive = max_is_exclusive
        if power is not None:
            self.power = power
        if clamp is not None:
            self.clamp = clamp
        if vibration_threshold is not None:
            self.vibration_threshold = vibration_threshold
        if anchor_offset is not None:
            self.anchor_offset = anchor_offset
        if handle_anchor_min_drive is not None:
            self.handle_anchor_min_drive = handle_anchor_min_drive
        if handle_anchor_max_drive is not None:
            self.handle_anchor_max_drive = handle_anchor_max_drive
        if fill_line_drive is not None:
            self.fill_line_drive = fill_line_drive
        if require_lock_in_to_interact is not None:
            self.require_lock_in_to_interact = require_lock_in_to_interact
        if require_initial_press is not None:
            self.require_initial_press = require_initial_press

    @property
    def base_color(self) -> primitives.ColorX | None:
        """The BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def color_drivers(self) -> members.SyncList | None:
        """The ColorDrivers member."""
        member = self.get_member("ColorDrivers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @color_drivers.setter
    def color_drivers(self, value: members.SyncList) -> None:
        """Set the ColorDrivers member."""
        self.set_member("ColorDrivers", value)

    @property
    def legacy_normal_color(self) -> primitives.ColorX | None:
        """The __legacy_NormalColor field value."""
        member = self.get_member("__legacy_NormalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_normal_color.setter
    def legacy_normal_color(self, value: primitives.ColorX) -> None:
        """Set the __legacy_NormalColor field value."""
        member = self.get_member("__legacy_NormalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacy_NormalColor", fields.FieldColorX(value=value)
            )

    @property
    def legacy_highlight_color(self) -> primitives.ColorX | None:
        """The __legacy_HighlightColor field value."""
        member = self.get_member("__legacy_HighlightColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_highlight_color.setter
    def legacy_highlight_color(self, value: primitives.ColorX) -> None:
        """Set the __legacy_HighlightColor field value."""
        member = self.get_member("__legacy_HighlightColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacy_HighlightColor", fields.FieldColorX(value=value)
            )

    @property
    def legacy_press_color(self) -> primitives.ColorX | None:
        """The __legacy_PressColor field value."""
        member = self.get_member("__legacy_PressColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_press_color.setter
    def legacy_press_color(self, value: primitives.ColorX) -> None:
        """Set the __legacy_PressColor field value."""
        member = self.get_member("__legacy_PressColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacy_PressColor", fields.FieldColorX(value=value)
            )

    @property
    def legacy_disabled_color(self) -> primitives.ColorX | None:
        """The __legacy_DisabledColor field value."""
        member = self.get_member("__legacy_DisabledColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_disabled_color.setter
    def legacy_disabled_color(self, value: primitives.ColorX) -> None:
        """Set the __legacy_DisabledColor field value."""
        member = self.get_member("__legacy_DisabledColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacy_DisabledColor", fields.FieldColorX(value=value)
            )

    @property
    def legacy_tint_color_mode(self) -> members.FieldEnum | None:
        """The __legacy_TintColorMode member."""
        member = self.get_member("__legacy_TintColorMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @legacy_tint_color_mode.setter
    def legacy_tint_color_mode(self, value: members.FieldEnum) -> None:
        """Set the __legacy_TintColorMode member."""
        self.set_member("__legacy_TintColorMode", value)

    @property
    def legacy_color_drive(self) -> str | None:
        """Target ID of the __legacy_ColorDrive reference (targets IField[primitives.ColorX])."""
        member = self.get_member("__legacy_ColorDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_color_drive.setter
    def legacy_color_drive(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the __legacy_ColorDrive reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("__legacy_ColorDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "__legacy_ColorDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def is_pressed(self) -> primitives.Bool | None:
        """The IsPressed field value."""
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
    def is_hovering(self) -> primitives.Bool | None:
        """The IsHovering field value."""
        member = self.get_member("IsHovering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_hovering.setter
    def is_hovering(self, value: primitives.Bool) -> None:
        """Set the IsHovering field value."""
        member = self.get_member("IsHovering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsHovering", fields.FieldBool(value=value)
            )

    @property
    def value(self) -> primitives.Float | None:
        """The Value field value."""
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
        """The Min field value."""
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
        """The Max field value."""
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
    def integers(self) -> primitives.Bool | None:
        """The Integers field value."""
        member = self.get_member("Integers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @integers.setter
    def integers(self, value: primitives.Bool) -> None:
        """Set the Integers field value."""
        member = self.get_member("Integers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Integers", fields.FieldBool(value=value)
            )

    @property
    def max_is_exclusive(self) -> primitives.Bool | None:
        """The MaxIsExclusive field value."""
        member = self.get_member("MaxIsExclusive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_is_exclusive.setter
    def max_is_exclusive(self, value: primitives.Bool) -> None:
        """Set the MaxIsExclusive field value."""
        member = self.get_member("MaxIsExclusive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIsExclusive", fields.FieldBool(value=value)
            )

    @property
    def power(self) -> primitives.Float | None:
        """The Power field value."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: primitives.Float) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

    @property
    def clamp(self) -> primitives.Bool | None:
        """The Clamp field value."""
        member = self.get_member("Clamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp.setter
    def clamp(self, value: primitives.Bool) -> None:
        """Set the Clamp field value."""
        member = self.get_member("Clamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Clamp", fields.FieldBool(value=value)
            )

    @property
    def vibration_threshold(self) -> primitives.Float | None:
        """The VibrationThreshold field value."""
        member = self.get_member("VibrationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration_threshold.setter
    def vibration_threshold(self, value: primitives.Float) -> None:
        """Set the VibrationThreshold field value."""
        member = self.get_member("VibrationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VibrationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def slide_direction(self) -> members.FieldEnum | None:
        """The SlideDirection member."""
        member = self.get_member("SlideDirection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @slide_direction.setter
    def slide_direction(self, value: members.FieldEnum) -> None:
        """Set the SlideDirection member."""
        self.set_member("SlideDirection", value)

    @property
    def anchor_offset(self) -> primitives.Float2 | None:
        """The AnchorOffset field value."""
        member = self.get_member("AnchorOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_offset.setter
    def anchor_offset(self, value: primitives.Float2) -> None:
        """Set the AnchorOffset field value."""
        member = self.get_member("AnchorOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorOffset", fields.FieldFloat2(value=value)
            )

    @property
    def handle_anchor_min_drive(self) -> str | None:
        """Target ID of the HandleAnchorMinDrive reference (targets IField[primitives.Float2])."""
        member = self.get_member("HandleAnchorMinDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_anchor_min_drive.setter
    def handle_anchor_min_drive(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the HandleAnchorMinDrive reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HandleAnchorMinDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HandleAnchorMinDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def handle_anchor_max_drive(self) -> str | None:
        """Target ID of the HandleAnchorMaxDrive reference (targets IField[primitives.Float2])."""
        member = self.get_member("HandleAnchorMaxDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_anchor_max_drive.setter
    def handle_anchor_max_drive(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the HandleAnchorMaxDrive reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HandleAnchorMaxDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HandleAnchorMaxDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def fill_line_drive(self) -> str | None:
        """Target ID of the FillLineDrive reference (targets IField[primitives.Float2])."""
        member = self.get_member("FillLineDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fill_line_drive.setter
    def fill_line_drive(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the FillLineDrive reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FillLineDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FillLineDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def require_lock_in_to_interact(self) -> primitives.Bool | None:
        """The RequireLockInToInteract field value."""
        member = self.get_member("RequireLockInToInteract")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_lock_in_to_interact.setter
    def require_lock_in_to_interact(self, value: primitives.Bool) -> None:
        """Set the RequireLockInToInteract field value."""
        member = self.get_member("RequireLockInToInteract")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RequireLockInToInteract", fields.FieldBool(value=value)
            )

    @property
    def require_initial_press(self) -> primitives.Bool | None:
        """The RequireInitialPress field value."""
        member = self.get_member("RequireInitialPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_initial_press.setter
    def require_initial_press(self, value: primitives.Bool) -> None:
        """Set the RequireInitialPress field value."""
        member = self.get_member("RequireInitialPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RequireInitialPress", fields.FieldBool(value=value)
            )

