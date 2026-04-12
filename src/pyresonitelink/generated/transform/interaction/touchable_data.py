"""Generated component: TouchableData."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.generated._enums.active_user_handling import ActiveUserHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchableData(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The TouchableData component can be used to create simple touch based interactions.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchableData"

    def __init__(self, hovering: primitives.Bool | None = None, touching: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, on_hover_start_vibrate: VibratePreset | str | None = None, on_hover_stay_vibrate: VibratePreset | str | None = None, on_hover_end_vibrate: VibratePreset | str | None = None, on_touch_start_vibrate: VibratePreset | str | None = None, on_touch_stay_vibrate: VibratePreset | str | None = None, on_touch_end_vibrate: VibratePreset | str | None = None, edit_mode_only: primitives.Bool | None = None, active_user_filter: ActiveUserHandling | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hovering: Initial value for Hovering.
            touching: Initial value for Touching.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            on_hover_start_vibrate: Initial value for OnHoverStartVibrate.
            on_hover_stay_vibrate: Initial value for OnHoverStayVibrate.
            on_hover_end_vibrate: Initial value for OnHoverEndVibrate.
            on_touch_start_vibrate: Initial value for OnTouchStartVibrate.
            on_touch_stay_vibrate: Initial value for OnTouchStayVibrate.
            on_touch_end_vibrate: Initial value for OnTouchEndVibrate.
            edit_mode_only: Initial value for EditModeOnly.
            active_user_filter: Initial value for ActiveUserFilter.
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
        if on_hover_start_vibrate is not None:
            self.on_hover_start_vibrate = on_hover_start_vibrate
        if on_hover_stay_vibrate is not None:
            self.on_hover_stay_vibrate = on_hover_stay_vibrate
        if on_hover_end_vibrate is not None:
            self.on_hover_end_vibrate = on_hover_end_vibrate
        if on_touch_start_vibrate is not None:
            self.on_touch_start_vibrate = on_touch_start_vibrate
        if on_touch_stay_vibrate is not None:
            self.on_touch_stay_vibrate = on_touch_stay_vibrate
        if on_touch_end_vibrate is not None:
            self.on_touch_end_vibrate = on_touch_end_vibrate
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if active_user_filter is not None:
            self.active_user_filter = active_user_filter

    @property
    def hovering(self) -> primitives.Bool | None:
        """Whether a user's laser is hovering over the component's collider"""
        member = self.get_member("Hovering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hovering.setter
    def hovering(self, value: primitives.Bool) -> None:
        """Set the Hovering field value."""
        member = self.get_member("Hovering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Hovering", fields.FieldBool(value=value)
            )

    @property
    def touching(self) -> primitives.Bool | None:
        """Whether a user is clicking on the collider this component is on."""
        member = self.get_member("Touching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @touching.setter
    def touching(self, value: primitives.Bool) -> None:
        """Set the Touching field value."""
        member = self.get_member("Touching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Touching", fields.FieldBool(value=value)
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
    def on_hover_start_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller when they started hovering on the component."""
        member = self.get_member("OnHoverStartVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_hover_start_vibrate.setter
    def on_hover_start_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnHoverStartVibrate. How to vibrate the user's controller when they started hovering on the component."""
        member = self.get_member("OnHoverStartVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnHoverStartVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_hover_stay_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller every game update when they are hovering on the component."""
        member = self.get_member("OnHoverStayVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_hover_stay_vibrate.setter
    def on_hover_stay_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnHoverStayVibrate. How to vibrate the user's controller every game update when they are hovering on the component."""
        member = self.get_member("OnHoverStayVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnHoverStayVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_hover_end_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller when they stopped hovering on the component."""
        member = self.get_member("OnHoverEndVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_hover_end_vibrate.setter
    def on_hover_end_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnHoverEndVibrate. How to vibrate the user's controller when they stopped hovering on the component."""
        member = self.get_member("OnHoverEndVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnHoverEndVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_touch_start_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller when they started primary pressing on the component."""
        member = self.get_member("OnTouchStartVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_touch_start_vibrate.setter
    def on_touch_start_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnTouchStartVibrate. How to vibrate the user's controller when they started primary pressing on the component."""
        member = self.get_member("OnTouchStartVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnTouchStartVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_touch_stay_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller every game update when they hold primary press on the component."""
        member = self.get_member("OnTouchStayVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_touch_stay_vibrate.setter
    def on_touch_stay_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnTouchStayVibrate. How to vibrate the user's controller every game update when they hold primary press on the component."""
        member = self.get_member("OnTouchStayVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnTouchStayVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_touch_end_vibrate(self) -> VibratePreset | None:
        """How to vibrate the user's controller when they ended primary pressing on the component."""
        member = self.get_member("OnTouchEndVibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @on_touch_end_vibrate.setter
    def on_touch_end_vibrate(self, value: VibratePreset | str) -> None:
        """Set OnTouchEndVibrate. How to vibrate the user's controller when they ended primary pressing on the component."""
        member = self.get_member("OnTouchEndVibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnTouchEndVibrate",
                members.FieldEnum(value=str(value)),
            )

    @property
    def edit_mode_only(self) -> primitives.Bool | None:
        """Whether this component can only be interacted with by users in edit mode."""
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
        """How to handle which users can use this component based on the current active user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ActiveUserHandling(member.value)
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: ActiveUserHandling | str) -> None:
        """Set ActiveUserFilter. How to handle which users can use this component based on the current active user."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActiveUserFilter",
                members.FieldEnum(value=str(value)),
            )

