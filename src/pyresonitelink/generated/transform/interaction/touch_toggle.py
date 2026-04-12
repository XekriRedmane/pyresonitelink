"""Generated component: TouchToggle."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.touch_event_type import TouchEventType
from pyresonitelink.generated._enums.event_state import EventState
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.generated._enums.active_user_handling import ActiveUserHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchToggle(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The TouchToggle component acts as a button that works as a check box, and the different Toggle on and off action can be mapped to certain Touch events.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchToggle"

    def __init__(self, state: primitives.Bool | None = None, event_type: TouchEventType | str | None = None, toggle_event: EventState | str | None = None, on_event: EventState | str | None = None, off_event: EventState | str | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, vibrate: VibratePreset | str | None = None, edit_mode_only: primitives.Bool | None = None, active_user_filter: ActiveUserHandling | str | None = None, legacy_active_user_root_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            event_type: Initial value for EventType.
            toggle_event: Initial value for ToggleEvent.
            on_event: Initial value for OnEvent.
            off_event: Initial value for OffEvent.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            vibrate: Initial value for Vibrate.
            edit_mode_only: Initial value for EditModeOnly.
            active_user_filter: Initial value for ActiveUserFilter.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if event_type is not None:
            self.event_type = event_type
        if toggle_event is not None:
            self.toggle_event = toggle_event
        if on_event is not None:
            self.on_event = on_event
        if off_event is not None:
            self.off_event = off_event
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if vibrate is not None:
            self.vibrate = vibrate
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if active_user_filter is not None:
            self.active_user_filter = active_user_filter
        if legacy_active_user_root_only is not None:
            self.legacy_active_user_root_only = legacy_active_user_root_only

    @property
    def state(self) -> primitives.Bool | None:
        """The checkbox state of this touch toggle."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

    @property
    def event_type(self) -> TouchEventType | None:
        """the type of touch event to listen for different event states from."""
        member = self.get_member("EventType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TouchEventType(member.value)
        return None

    @event_type.setter
    def event_type(self, value: TouchEventType | str) -> None:
        """Set EventType. the type of touch event to listen for different event states from."""
        member = self.get_member("EventType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "EventType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def toggle_event(self) -> EventState | None:
        """The event state needed when touching to Toggle the ``State`` value."""
        member = self.get_member("ToggleEvent")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EventState(member.value)
        return None

    @toggle_event.setter
    def toggle_event(self, value: EventState | str) -> None:
        """Set ToggleEvent. The event state needed when touching to Toggle the ``State`` value."""
        member = self.get_member("ToggleEvent")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ToggleEvent",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_event(self) -> EventState | None:
        """The event state needed when touching to switch to true the ``State`` value."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EventState(member.value)
        return None

    @on_event.setter
    def on_event(self, value: EventState | str) -> None:
        """Set OnEvent. The event state needed when touching to switch to true the ``State`` value."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnEvent",
                members.FieldEnum(value=str(value)),
            )

    @property
    def off_event(self) -> EventState | None:
        """The event state needed when touching to switch to false the ``State`` value."""
        member = self.get_member("OffEvent")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EventState(member.value)
        return None

    @off_event.setter
    def off_event(self, value: EventState | str) -> None:
        """Set OffEvent. The event state needed when touching to switch to false the ``State`` value."""
        member = self.get_member("OffEvent")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OffEvent",
                members.FieldEnum(value=str(value)),
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
    def vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's hand when they touch the toggle."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @vibrate.setter
    def vibrate(self, value: VibratePreset | str) -> None:
        """Set Vibrate. How to vibrate the user's hand when they touch the toggle."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Vibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def edit_mode_only(self) -> primitives.Bool | None:
        """Whether this is only available in edit mode."""
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
        """how to filter users in the session who can interact with this component depending on the parent user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ActiveUserHandling(member.value)
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: ActiveUserHandling | str) -> None:
        """Set ActiveUserFilter. how to filter users in the session who can interact with this component depending on the parent user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActiveUserFilter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def legacy_active_user_root_only(self) -> primitives.Bool | None:
        """Whether to use the legacy active user root. Internal."""
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

