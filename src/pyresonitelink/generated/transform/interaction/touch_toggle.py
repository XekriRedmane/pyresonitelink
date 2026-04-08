"""Generated component: TouchToggle."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchToggle(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchToggle.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchToggle"

    def __init__(self, state: bool | None = None, accept_out_of_sight_touch: bool | None = None, accept_physical_touch: bool | None = None, accept_remote_touch: bool | None = None, edit_mode_only: bool | None = None, legacy_active_user_root_only: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            edit_mode_only: Initial value for EditModeOnly.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if legacy_active_user_root_only is not None:
            self.legacy_active_user_root_only = legacy_active_user_root_only

    @property
    def state(self) -> bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

    @property
    def event_type(self) -> members.FieldEnum | None:
        """The EventType member."""
        member = self.get_member("EventType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @event_type.setter
    def event_type(self, value: members.FieldEnum) -> None:
        """Set the EventType member."""
        self.set_member("EventType", value)

    @property
    def toggle_event(self) -> members.FieldEnum | None:
        """The ToggleEvent member."""
        member = self.get_member("ToggleEvent")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @toggle_event.setter
    def toggle_event(self, value: members.FieldEnum) -> None:
        """Set the ToggleEvent member."""
        self.set_member("ToggleEvent", value)

    @property
    def on_event(self) -> members.FieldEnum | None:
        """The OnEvent member."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_event.setter
    def on_event(self, value: members.FieldEnum) -> None:
        """Set the OnEvent member."""
        self.set_member("OnEvent", value)

    @property
    def off_event(self) -> members.FieldEnum | None:
        """The OffEvent member."""
        member = self.get_member("OffEvent")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @off_event.setter
    def off_event(self, value: members.FieldEnum) -> None:
        """Set the OffEvent member."""
        self.set_member("OffEvent", value)

    @property
    def accept_out_of_sight_touch(self) -> bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_physical_touch(self) -> bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

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
    def edit_mode_only(self) -> bool | None:
        """The EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: bool) -> None:
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
    def legacy_active_user_root_only(self) -> bool | None:
        """The __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_active_user_root_only.setter
    def legacy_active_user_root_only(self, value: bool) -> None:
        """Set the __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyActiveUserRootOnly", fields.FieldBool(value=value)
            )

