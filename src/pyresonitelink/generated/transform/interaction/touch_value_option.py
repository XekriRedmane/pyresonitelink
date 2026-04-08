"""Generated component: TouchValueOption."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchValueOption(GenericComponent[T], ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchValueOption<>.

    Category: Transform/Interaction

    Parameterize with a value type::

        TouchValueOption[primitives.Float]
        TouchValueOption[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchValueOption<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.TouchValueOption<>"

    def __init__(self, target: str | IField[T] | None = None, value: T | None = None, active_indicator: str | IField[primitives.Bool] | None = None, hover_indicator: str | IField[primitives.Bool] | None = None, set_on_touch_begin: primitives.Bool | None = None, set_on_touch_stay: primitives.Bool | None = None, set_on_touch_end: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, edit_mode_only: primitives.Bool | None = None, active_user_root_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value: Initial value for Value.
            active_indicator: Initial value for ActiveIndicator.
            hover_indicator: Initial value for HoverIndicator.
            set_on_touch_begin: Initial value for SetOnTouchBegin.
            set_on_touch_stay: Initial value for SetOnTouchStay.
            set_on_touch_end: Initial value for SetOnTouchEnd.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            edit_mode_only: Initial value for EditModeOnly.
            active_user_root_only: Initial value for ActiveUserRootOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value is not None:
            self.value = value
        if active_indicator is not None:
            self.active_indicator = active_indicator
        if hover_indicator is not None:
            self.hover_indicator = hover_indicator
        if set_on_touch_begin is not None:
            self.set_on_touch_begin = set_on_touch_begin
        if set_on_touch_stay is not None:
            self.set_on_touch_stay = set_on_touch_stay
        if set_on_touch_end is not None:
            self.set_on_touch_end = set_on_touch_end
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if active_user_root_only is not None:
            self.active_user_root_only = active_user_root_only

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
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
    def active_indicator(self) -> str | None:
        """Target ID of the ActiveIndicator reference (targets IField[primitives.Bool])."""
        member = self.get_member("ActiveIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_indicator.setter
    def active_indicator(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the ActiveIndicator reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ActiveIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def hover_indicator(self) -> str | None:
        """Target ID of the HoverIndicator reference (targets IField[primitives.Bool])."""
        member = self.get_member("HoverIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_indicator.setter
    def hover_indicator(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HoverIndicator reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HoverIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
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
    def vibrate(self) -> members.FieldEnum | None:
        """The Vibrate member."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vibrate.setter
    def vibrate(self, value: members.FieldEnum) -> None:
        """Set the Vibrate member."""
        self.set_member("Vibrate", value)

    @property
    def set_on_touch_begin(self) -> primitives.Bool | None:
        """The SetOnTouchBegin field value."""
        member = self.get_member("SetOnTouchBegin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_touch_begin.setter
    def set_on_touch_begin(self, value: primitives.Bool) -> None:
        """Set the SetOnTouchBegin field value."""
        member = self.get_member("SetOnTouchBegin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnTouchBegin", fields.FieldBool(value=value)
            )

    @property
    def set_on_touch_stay(self) -> primitives.Bool | None:
        """The SetOnTouchStay field value."""
        member = self.get_member("SetOnTouchStay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_touch_stay.setter
    def set_on_touch_stay(self, value: primitives.Bool) -> None:
        """Set the SetOnTouchStay field value."""
        member = self.get_member("SetOnTouchStay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnTouchStay", fields.FieldBool(value=value)
            )

    @property
    def set_on_touch_end(self) -> primitives.Bool | None:
        """The SetOnTouchEnd field value."""
        member = self.get_member("SetOnTouchEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_touch_end.setter
    def set_on_touch_end(self, value: primitives.Bool) -> None:
        """Set the SetOnTouchEnd field value."""
        member = self.get_member("SetOnTouchEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnTouchEnd", fields.FieldBool(value=value)
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
    def active_user_root_only(self) -> primitives.Bool | None:
        """The ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_user_root_only.setter
    def active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUserRootOnly", fields.FieldBool(value=value)
            )

