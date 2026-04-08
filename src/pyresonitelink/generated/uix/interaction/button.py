"""Generated component: Button."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Button(GeneratedComponent, IButton, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Button.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Button"

    def __init__(self, base_color: primitives.ColorX | None = None, legacy_normal_color: primitives.ColorX | None = None, legacy_highlight_color: primitives.ColorX | None = None, legacy_press_color: primitives.ColorX | None = None, legacy_disabled_color: primitives.ColorX | None = None, legacy_color_drive: str | IField[primitives.ColorX] | None = None, is_pressed: primitives.Bool | None = None, is_hovering: primitives.Bool | None = None, clear_focus_on_press: primitives.Bool | None = None, pass_through_horizontal_movement: primitives.Bool | None = None, pass_through_vertical_movement: primitives.Bool | None = None, require_lock_in_to_press: primitives.Bool | None = None, require_initial_press: primitives.Bool | None = None, press_point: primitives.Float2 | None = None, send_slot_events: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
            clear_focus_on_press: Initial value for ClearFocusOnPress.
            pass_through_horizontal_movement: Initial value for PassThroughHorizontalMovement.
            pass_through_vertical_movement: Initial value for PassThroughVerticalMovement.
            require_lock_in_to_press: Initial value for RequireLockInToPress.
            require_initial_press: Initial value for RequireInitialPress.
            press_point: Initial value for PressPoint.
            send_slot_events: Initial value for SendSlotEvents.
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
        if clear_focus_on_press is not None:
            self.clear_focus_on_press = clear_focus_on_press
        if pass_through_horizontal_movement is not None:
            self.pass_through_horizontal_movement = pass_through_horizontal_movement
        if pass_through_vertical_movement is not None:
            self.pass_through_vertical_movement = pass_through_vertical_movement
        if require_lock_in_to_press is not None:
            self.require_lock_in_to_press = require_lock_in_to_press
        if require_initial_press is not None:
            self.require_initial_press = require_initial_press
        if press_point is not None:
            self.press_point = press_point
        if send_slot_events is not None:
            self.send_slot_events = send_slot_events

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
    def hover_vibrate(self) -> members.FieldEnum | None:
        """The HoverVibrate member."""
        member = self.get_member("HoverVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hover_vibrate.setter
    def hover_vibrate(self, value: members.FieldEnum) -> None:
        """Set the HoverVibrate member."""
        self.set_member("HoverVibrate", value)

    @property
    def press_vibrate(self) -> members.FieldEnum | None:
        """The PressVibrate member."""
        member = self.get_member("PressVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @press_vibrate.setter
    def press_vibrate(self, value: members.FieldEnum) -> None:
        """Set the PressVibrate member."""
        self.set_member("PressVibrate", value)

    @property
    def clear_focus_on_press(self) -> primitives.Bool | None:
        """The ClearFocusOnPress field value."""
        member = self.get_member("ClearFocusOnPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clear_focus_on_press.setter
    def clear_focus_on_press(self, value: primitives.Bool) -> None:
        """Set the ClearFocusOnPress field value."""
        member = self.get_member("ClearFocusOnPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClearFocusOnPress", fields.FieldBool(value=value)
            )

    @property
    def pass_through_horizontal_movement(self) -> primitives.Bool | None:
        """The PassThroughHorizontalMovement field value."""
        member = self.get_member("PassThroughHorizontalMovement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pass_through_horizontal_movement.setter
    def pass_through_horizontal_movement(self, value: primitives.Bool) -> None:
        """Set the PassThroughHorizontalMovement field value."""
        member = self.get_member("PassThroughHorizontalMovement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PassThroughHorizontalMovement", fields.FieldBool(value=value)
            )

    @property
    def pass_through_vertical_movement(self) -> primitives.Bool | None:
        """The PassThroughVerticalMovement field value."""
        member = self.get_member("PassThroughVerticalMovement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pass_through_vertical_movement.setter
    def pass_through_vertical_movement(self, value: primitives.Bool) -> None:
        """Set the PassThroughVerticalMovement field value."""
        member = self.get_member("PassThroughVerticalMovement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PassThroughVerticalMovement", fields.FieldBool(value=value)
            )

    @property
    def require_lock_in_to_press(self) -> primitives.Bool | None:
        """The RequireLockInToPress field value."""
        member = self.get_member("RequireLockInToPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_lock_in_to_press.setter
    def require_lock_in_to_press(self, value: primitives.Bool) -> None:
        """Set the RequireLockInToPress field value."""
        member = self.get_member("RequireLockInToPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RequireLockInToPress", fields.FieldBool(value=value)
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

    @property
    def press_point(self) -> primitives.Float2 | None:
        """The PressPoint field value."""
        member = self.get_member("PressPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @press_point.setter
    def press_point(self, value: primitives.Float2) -> None:
        """Set the PressPoint field value."""
        member = self.get_member("PressPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressPoint", fields.FieldFloat2(value=value)
            )

    @property
    def send_slot_events(self) -> primitives.Bool | None:
        """The SendSlotEvents field value."""
        member = self.get_member("SendSlotEvents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @send_slot_events.setter
    def send_slot_events(self, value: primitives.Bool) -> None:
        """Set the SendSlotEvents field value."""
        member = self.get_member("SendSlotEvents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SendSlotEvents", fields.FieldBool(value=value)
            )

