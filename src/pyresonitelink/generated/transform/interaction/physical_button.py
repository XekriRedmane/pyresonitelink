"""Generated component: PhysicalButton."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PhysicalButton(GeneratedComponent, IButton, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhysicalButton.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhysicalButton"

    def __init__(self, press_axis: primitives.Float3 | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, edit_mode_only: primitives.Bool | None = None, legacy_active_user_root_only: primitives.Bool | None = None, press_depth: primitives.Float | None = None, press_threshold: primitives.Float | None = None, release_threshold: primitives.Float | None = None, is_pressed: primitives.Bool | None = None, is_hovering: primitives.Bool | None = None, is_holding: primitives.Bool | None = None, is_pressed_or_holding: primitives.Bool | None = None, hold: primitives.Bool | None = None, hold_depth_ratio: primitives.Float | None = None, label: str | IField[primitives.String] | None = None, current_pressing_depth: primitives.Float | None = None, button_offset: primitives.Float3 | None = None, button_position: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            press_axis: Initial value for PressAxis.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            edit_mode_only: Initial value for EditModeOnly.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            press_depth: Initial value for PressDepth.
            press_threshold: Initial value for PressThreshold.
            release_threshold: Initial value for ReleaseThreshold.
            is_pressed: Initial value for IsPressed.
            is_hovering: Initial value for IsHovering.
            is_holding: Initial value for IsHolding.
            is_pressed_or_holding: Initial value for IsPressedOrHolding.
            hold: Initial value for Hold.
            hold_depth_ratio: Initial value for HoldDepthRatio.
            label: Initial value for Label.
            current_pressing_depth: Initial value for _currentPressingDepth.
            button_offset: Initial value for _buttonOffset.
            button_position: Initial value for _buttonPosition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if press_axis is not None:
            self.press_axis = press_axis
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if legacy_active_user_root_only is not None:
            self.legacy_active_user_root_only = legacy_active_user_root_only
        if press_depth is not None:
            self.press_depth = press_depth
        if press_threshold is not None:
            self.press_threshold = press_threshold
        if release_threshold is not None:
            self.release_threshold = release_threshold
        if is_pressed is not None:
            self.is_pressed = is_pressed
        if is_hovering is not None:
            self.is_hovering = is_hovering
        if is_holding is not None:
            self.is_holding = is_holding
        if is_pressed_or_holding is not None:
            self.is_pressed_or_holding = is_pressed_or_holding
        if hold is not None:
            self.hold = hold
        if hold_depth_ratio is not None:
            self.hold_depth_ratio = hold_depth_ratio
        if label is not None:
            self.label = label
        if current_pressing_depth is not None:
            self.current_pressing_depth = current_pressing_depth
        if button_offset is not None:
            self.button_offset = button_offset
        if button_position is not None:
            self.button_position = button_position

    @property
    def press_axis(self) -> primitives.Float3 | None:
        """The PressAxis field value."""
        member = self.get_member("PressAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @press_axis.setter
    def press_axis(self, value: primitives.Float3) -> None:
        """Set the PressAxis field value."""
        member = self.get_member("PressAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressAxis", fields.FieldFloat3(value=value)
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
        """The EditModeOnly field value."""
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
    def active_user_filter(self) -> members.FieldEnum | None:
        """The ActiveUserFilter member."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: members.FieldEnum) -> None:
        """Set the ActiveUserFilter member."""
        self.set_member("ActiveUserFilter", value)

    @property
    def legacy_active_user_root_only(self) -> primitives.Bool | None:
        """The __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_active_user_root_only.setter
    def legacy_active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyActiveUserRootOnly", fields.FieldBool(value=value)
            )

    @property
    def press_depth(self) -> primitives.Float | None:
        """The PressDepth field value."""
        member = self.get_member("PressDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @press_depth.setter
    def press_depth(self, value: primitives.Float) -> None:
        """Set the PressDepth field value."""
        member = self.get_member("PressDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressDepth", fields.FieldFloat(value=value)
            )

    @property
    def press_threshold(self) -> primitives.Float | None:
        """The PressThreshold field value."""
        member = self.get_member("PressThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @press_threshold.setter
    def press_threshold(self, value: primitives.Float) -> None:
        """Set the PressThreshold field value."""
        member = self.get_member("PressThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressThreshold", fields.FieldFloat(value=value)
            )

    @property
    def release_threshold(self) -> primitives.Float | None:
        """The ReleaseThreshold field value."""
        member = self.get_member("ReleaseThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_threshold.setter
    def release_threshold(self, value: primitives.Float) -> None:
        """Set the ReleaseThreshold field value."""
        member = self.get_member("ReleaseThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseThreshold", fields.FieldFloat(value=value)
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
    def is_holding(self) -> primitives.Bool | None:
        """The IsHolding field value."""
        member = self.get_member("IsHolding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_holding.setter
    def is_holding(self, value: primitives.Bool) -> None:
        """Set the IsHolding field value."""
        member = self.get_member("IsHolding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsHolding", fields.FieldBool(value=value)
            )

    @property
    def is_pressed_or_holding(self) -> primitives.Bool | None:
        """The IsPressedOrHolding field value."""
        member = self.get_member("IsPressedOrHolding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_pressed_or_holding.setter
    def is_pressed_or_holding(self, value: primitives.Bool) -> None:
        """Set the IsPressedOrHolding field value."""
        member = self.get_member("IsPressedOrHolding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPressedOrHolding", fields.FieldBool(value=value)
            )

    @property
    def hold(self) -> primitives.Bool | None:
        """The Hold field value."""
        member = self.get_member("Hold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold.setter
    def hold(self, value: primitives.Bool) -> None:
        """Set the Hold field value."""
        member = self.get_member("Hold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hold", fields.FieldBool(value=value)
            )

    @property
    def hold_depth_ratio(self) -> primitives.Float | None:
        """The HoldDepthRatio field value."""
        member = self.get_member("HoldDepthRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_depth_ratio.setter
    def hold_depth_ratio(self, value: primitives.Float) -> None:
        """Set the HoldDepthRatio field value."""
        member = self.get_member("HoldDepthRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldDepthRatio", fields.FieldFloat(value=value)
            )

    @property
    def begin_press_vibration(self) -> members.FieldEnum | None:
        """The BeginPressVibration member."""
        member = self.get_member("BeginPressVibration")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @begin_press_vibration.setter
    def begin_press_vibration(self, value: members.FieldEnum) -> None:
        """Set the BeginPressVibration member."""
        self.set_member("BeginPressVibration", value)

    @property
    def press_vibration(self) -> members.FieldEnum | None:
        """The PressVibration member."""
        member = self.get_member("PressVibration")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @press_vibration.setter
    def press_vibration(self, value: members.FieldEnum) -> None:
        """Set the PressVibration member."""
        self.set_member("PressVibration", value)

    @property
    def hover_vibration(self) -> members.FieldEnum | None:
        """The HoverVibration member."""
        member = self.get_member("HoverVibration")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hover_vibration.setter
    def hover_vibration(self, value: members.FieldEnum) -> None:
        """Set the HoverVibration member."""
        self.set_member("HoverVibration", value)

    @property
    def label(self) -> str | None:
        """Target ID of the Label reference (targets IField[primitives.String])."""
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

    @property
    def current_pressing_depth(self) -> primitives.Float | None:
        """The _currentPressingDepth field value."""
        member = self.get_member("_currentPressingDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_pressing_depth.setter
    def current_pressing_depth(self, value: primitives.Float) -> None:
        """Set the _currentPressingDepth field value."""
        member = self.get_member("_currentPressingDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_currentPressingDepth", fields.FieldFloat(value=value)
            )

    @property
    def button_offset(self) -> primitives.Float3 | None:
        """The _buttonOffset field value."""
        member = self.get_member("_buttonOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @button_offset.setter
    def button_offset(self, value: primitives.Float3) -> None:
        """Set the _buttonOffset field value."""
        member = self.get_member("_buttonOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_buttonOffset", fields.FieldFloat3(value=value)
            )

    @property
    def button_position(self) -> str | None:
        """Target ID of the _buttonPosition reference (targets IField[primitives.Float3])."""
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

