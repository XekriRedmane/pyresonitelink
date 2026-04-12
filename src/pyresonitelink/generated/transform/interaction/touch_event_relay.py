"""Generated component: TouchEventRelay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchEventRelay(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The TouchEventRelay component is used to relay touch events recieved by a slot to other ITouchables.

    Category: Transform/Interaction

    *To trigger a hyperlink component without a touchable/interactable
    component you can use a TouchEventRelay. You a touch event relay on the
    collider of your object, then put a hyperlink or other touchables as
    children (with no colliders on them) then add them to the
    TouchableTargets list of the TouchEventRelay.

    **Related Components**: * Touchable Events can be used with TouchEventRelay.
TouchEventRelay can relay events from a Touchable element to fire another ITouchable component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchEventRelay"

    def __init__(self, accept_out_of_sight_touch: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch

    @property
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """Whether this component allows touch events from a user not looking directly at the slot with this component."""
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
    def touchable_targets(self) -> members.SyncList | None:
        """Target touchable components to send the touch event to."""
        member = self.get_member("TouchableTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @touchable_targets.setter
    def touchable_targets(self, value: members.SyncList) -> None:
        """Set TouchableTargets. Target touchable components to send the touch event to."""
        self.set_member("TouchableTargets", value)

