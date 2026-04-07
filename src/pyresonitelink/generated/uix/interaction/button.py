"""Generated component: Button."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button_event_handler import ButtonEventHandler
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Button(GeneratedComponent, IButton, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Button.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Button"

    def __init__(self, legacy_color_drive: str | IField[primitives.ColorX] | None = None, pressed: str | ButtonEventHandler | None = None, pressing: str | ButtonEventHandler | None = None, released: str | ButtonEventHandler | None = None, hover_enter: str | ButtonEventHandler | None = None, hover_stay: str | ButtonEventHandler | None = None, hover_leave: str | ButtonEventHandler | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            legacy_color_drive: Initial value for __legacy_ColorDrive.
            pressed: Initial value for Pressed.
            pressing: Initial value for Pressing.
            released: Initial value for Released.
            hover_enter: Initial value for HoverEnter.
            hover_stay: Initial value for HoverStay.
            hover_leave: Initial value for HoverLeave.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if legacy_color_drive is not None:
            self.legacy_color_drive = legacy_color_drive
        if pressed is not None:
            self.pressed = pressed
        if pressing is not None:
            self.pressing = pressing
        if released is not None:
            self.released = released
        if hover_enter is not None:
            self.hover_enter = hover_enter
        if hover_stay is not None:
            self.hover_stay = hover_stay
        if hover_leave is not None:
            self.hover_leave = hover_leave

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
    def is_pressed(self) -> bool | None:
        """The IsPressed field value."""
        member = self.get_member("IsPressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_pressed.setter
    def is_pressed(self, value: bool) -> None:
        """Set the IsPressed field value."""
        member = self.get_member("IsPressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPressed", fields.FieldBool(value=value)
            )

    @property
    def is_hovering(self) -> bool | None:
        """The IsHovering field value."""
        member = self.get_member("IsHovering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_hovering.setter
    def is_hovering(self, value: bool) -> None:
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
    def clear_focus_on_press(self) -> bool | None:
        """The ClearFocusOnPress field value."""
        member = self.get_member("ClearFocusOnPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clear_focus_on_press.setter
    def clear_focus_on_press(self, value: bool) -> None:
        """Set the ClearFocusOnPress field value."""
        member = self.get_member("ClearFocusOnPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClearFocusOnPress", fields.FieldBool(value=value)
            )

    @property
    def pass_through_horizontal_movement(self) -> bool | None:
        """The PassThroughHorizontalMovement field value."""
        member = self.get_member("PassThroughHorizontalMovement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pass_through_horizontal_movement.setter
    def pass_through_horizontal_movement(self, value: bool) -> None:
        """Set the PassThroughHorizontalMovement field value."""
        member = self.get_member("PassThroughHorizontalMovement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PassThroughHorizontalMovement", fields.FieldBool(value=value)
            )

    @property
    def pass_through_vertical_movement(self) -> bool | None:
        """The PassThroughVerticalMovement field value."""
        member = self.get_member("PassThroughVerticalMovement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pass_through_vertical_movement.setter
    def pass_through_vertical_movement(self, value: bool) -> None:
        """Set the PassThroughVerticalMovement field value."""
        member = self.get_member("PassThroughVerticalMovement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PassThroughVerticalMovement", fields.FieldBool(value=value)
            )

    @property
    def require_lock_in_to_press(self) -> bool | None:
        """The RequireLockInToPress field value."""
        member = self.get_member("RequireLockInToPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_lock_in_to_press.setter
    def require_lock_in_to_press(self, value: bool) -> None:
        """Set the RequireLockInToPress field value."""
        member = self.get_member("RequireLockInToPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RequireLockInToPress", fields.FieldBool(value=value)
            )

    @property
    def require_initial_press(self) -> bool | None:
        """The RequireInitialPress field value."""
        member = self.get_member("RequireInitialPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_initial_press.setter
    def require_initial_press(self, value: bool) -> None:
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
    def send_slot_events(self) -> bool | None:
        """The SendSlotEvents field value."""
        member = self.get_member("SendSlotEvents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @send_slot_events.setter
    def send_slot_events(self, value: bool) -> None:
        """Set the SendSlotEvents field value."""
        member = self.get_member("SendSlotEvents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SendSlotEvents", fields.FieldBool(value=value)
            )

    @property
    def pressed(self) -> str | None:
        """Target ID of the Pressed reference (targets ButtonEventHandler)."""
        member = self.get_member("Pressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pressed.setter
    def pressed(self, target: str | ButtonEventHandler | None) -> None:
        """Set the Pressed reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("Pressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pressed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

    @property
    def pressing(self) -> str | None:
        """Target ID of the Pressing reference (targets ButtonEventHandler)."""
        member = self.get_member("Pressing")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pressing.setter
    def pressing(self, target: str | ButtonEventHandler | None) -> None:
        """Set the Pressing reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("Pressing")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pressing",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

    @property
    def released(self) -> str | None:
        """Target ID of the Released reference (targets ButtonEventHandler)."""
        member = self.get_member("Released")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @released.setter
    def released(self, target: str | ButtonEventHandler | None) -> None:
        """Set the Released reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("Released")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Released",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

    @property
    def hover_enter(self) -> str | None:
        """Target ID of the HoverEnter reference (targets ButtonEventHandler)."""
        member = self.get_member("HoverEnter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_enter.setter
    def hover_enter(self, target: str | ButtonEventHandler | None) -> None:
        """Set the HoverEnter reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("HoverEnter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverEnter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

    @property
    def hover_stay(self) -> str | None:
        """Target ID of the HoverStay reference (targets ButtonEventHandler)."""
        member = self.get_member("HoverStay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_stay.setter
    def hover_stay(self, target: str | ButtonEventHandler | None) -> None:
        """Set the HoverStay reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("HoverStay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverStay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

    @property
    def hover_leave(self) -> str | None:
        """Target ID of the HoverLeave reference (targets ButtonEventHandler)."""
        member = self.get_member("HoverLeave")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_leave.setter
    def hover_leave(self, target: str | ButtonEventHandler | None) -> None:
        """Set the HoverLeave reference by target ID or ButtonEventHandler instance."""
        target_id: str | None = target.id if isinstance(target, ButtonEventHandler) else target  # type: ignore[assignment]
        member = self.get_member("HoverLeave")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverLeave",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ButtonEventHandler'),
            )

