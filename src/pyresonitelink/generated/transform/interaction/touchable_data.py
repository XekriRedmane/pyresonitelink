"""Generated component: TouchableData."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchableData(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchableData.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchableData"

    def __init__(self, hovering: bool | None = None, touching: bool | None = None, accept_out_of_sight_touch: bool | None = None, accept_physical_touch: bool | None = None, accept_remote_touch: bool | None = None, edit_mode_only: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hovering: Initial value for Hovering.
            touching: Initial value for Touching.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            edit_mode_only: Initial value for EditModeOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hovering is not None:
            self.hovering = hovering
        if touching is not None:
            self.touching = touching
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only

    @property
    def hovering(self) -> bool | None:
        """The Hovering field value."""
        member = self.get_member("Hovering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hovering.setter
    def hovering(self, value: bool) -> None:
        """Set the Hovering field value."""
        member = self.get_member("Hovering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hovering", fields.FieldBool(value=value)
            )

    @property
    def touching(self) -> bool | None:
        """The Touching field value."""
        member = self.get_member("Touching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touching.setter
    def touching(self, value: bool) -> None:
        """Set the Touching field value."""
        member = self.get_member("Touching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Touching", fields.FieldBool(value=value)
            )

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
    def on_hover_start_vibrate(self) -> members.FieldEnum | None:
        """The OnHoverStartVibrate member."""
        member = self.get_member("OnHoverStartVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_hover_start_vibrate.setter
    def on_hover_start_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnHoverStartVibrate member."""
        self.set_member("OnHoverStartVibrate", value)

    @property
    def on_hover_stay_vibrate(self) -> members.FieldEnum | None:
        """The OnHoverStayVibrate member."""
        member = self.get_member("OnHoverStayVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_hover_stay_vibrate.setter
    def on_hover_stay_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnHoverStayVibrate member."""
        self.set_member("OnHoverStayVibrate", value)

    @property
    def on_hover_end_vibrate(self) -> members.FieldEnum | None:
        """The OnHoverEndVibrate member."""
        member = self.get_member("OnHoverEndVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_hover_end_vibrate.setter
    def on_hover_end_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnHoverEndVibrate member."""
        self.set_member("OnHoverEndVibrate", value)

    @property
    def on_touch_start_vibrate(self) -> members.FieldEnum | None:
        """The OnTouchStartVibrate member."""
        member = self.get_member("OnTouchStartVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_touch_start_vibrate.setter
    def on_touch_start_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnTouchStartVibrate member."""
        self.set_member("OnTouchStartVibrate", value)

    @property
    def on_touch_stay_vibrate(self) -> members.FieldEnum | None:
        """The OnTouchStayVibrate member."""
        member = self.get_member("OnTouchStayVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_touch_stay_vibrate.setter
    def on_touch_stay_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnTouchStayVibrate member."""
        self.set_member("OnTouchStayVibrate", value)

    @property
    def on_touch_end_vibrate(self) -> members.FieldEnum | None:
        """The OnTouchEndVibrate member."""
        member = self.get_member("OnTouchEndVibrate")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_touch_end_vibrate.setter
    def on_touch_end_vibrate(self, value: members.FieldEnum) -> None:
        """Set the OnTouchEndVibrate member."""
        self.set_member("OnTouchEndVibrate", value)

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

