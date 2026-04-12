"""Generated component: TouchButton."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.active_user_handling import ActiveUserHandling
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchButton(GeneratedComponent, ITouchable, IButton, IWorldEventReceiver):
    """The TouchButton component is used to make a physical button with no press depth that is instantly pressable upon click or touch. For a button with press depth, please see PhysicalButton.

    Category: Transform/Interaction

    Used in boopers and buttons where PhysicalButton is a bad choice because
    the button press needs to have no press depth. In the case where the
    user does want press depth, use PhysicalButton.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchButton"

    def __init__(self, is_pressed: primitives.Bool | None = None, is_hovering: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, edit_mode_only: primitives.Bool | None = None, active_user_filter: ActiveUserHandling | str | None = None, begin_press_vibration: VibratePreset | str | None = None, press_vibration: VibratePreset | str | None = None, hover_vibration: VibratePreset | str | None = None, label: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_pressed: Initial value for IsPressed.
            is_hovering: Initial value for IsHovering.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            edit_mode_only: Initial value for EditModeOnly.
            active_user_filter: Initial value for ActiveUserFilter.
            begin_press_vibration: Initial value for BeginPressVibration.
            press_vibration: Initial value for PressVibration.
            hover_vibration: Initial value for HoverVibration.
            label: Initial value for Label.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_pressed is not None:
            self.is_pressed = is_pressed
        if is_hovering is not None:
            self.is_hovering = is_hovering
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if active_user_filter is not None:
            self.active_user_filter = active_user_filter
        if begin_press_vibration is not None:
            self.begin_press_vibration = begin_press_vibration
        if press_vibration is not None:
            self.press_vibration = press_vibration
        if hover_vibration is not None:
            self.hover_vibration = hover_vibration
        if label is not None:
            self.label = label

    @property
    def is_pressed(self) -> primitives.Bool | None:
        """Whether the button is pressed or not"""
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
        """Whether the button is being pointed at with the laser in the case of a touch button"""
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
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """The AcceptOutOfSightTouch field value."""
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
    def edit_mode_only(self) -> primitives.Bool | None:
        """Whether this button will only work if the user is in Edit Mode"""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: primitives.Bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def active_user_filter(self) -> ActiveUserHandling | None:
        """How to handle user interaction depending on active user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ActiveUserHandling(member.value)
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: ActiveUserHandling | str) -> None:
        """Set ActiveUserFilter. How to handle user interaction depending on active user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActiveUserFilter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def begin_press_vibration(self) -> VibratePreset | None:
        """What vibration to send when this button is starting to be pressed."""
        member = self.get_member("BeginPressVibration")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @begin_press_vibration.setter
    def begin_press_vibration(self, value: VibratePreset | str) -> None:
        """Set BeginPressVibration. What vibration to send when this button is starting to be pressed."""
        member = self.get_member("BeginPressVibration")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BeginPressVibration",
                members.FieldEnum(value=str(value)),
            )

    @property
    def press_vibration(self) -> VibratePreset | None:
        """What vibration to send when this button is pressed."""
        member = self.get_member("PressVibration")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @press_vibration.setter
    def press_vibration(self, value: VibratePreset | str) -> None:
        """Set PressVibration. What vibration to send when this button is pressed."""
        member = self.get_member("PressVibration")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PressVibration",
                members.FieldEnum(value=str(value)),
            )

    @property
    def hover_vibration(self) -> VibratePreset | None:
        """What vibration to send when this button is hovered over via laser."""
        member = self.get_member("HoverVibration")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @hover_vibration.setter
    def hover_vibration(self, value: VibratePreset | str) -> None:
        """Set HoverVibration. What vibration to send when this button is hovered over via laser."""
        member = self.get_member("HoverVibration")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HoverVibration",
                members.FieldEnum(value=str(value)),
            )

    @property
    def label(self) -> str | None:
        """The field that represents this button's label."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Label reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

