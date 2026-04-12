"""Generated component: LocomotionAnimationBodyCollider."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationBodyCollider(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocomotionAnimationBodyCollider component is required for any colliders to be considered for self-collision for the hands.

    Category: Users/Common Avatar System/Animation

    Attach to a slot on an avatar with a collider. That collider will now be
    a collider the hands will hit and go around while the user is walking in
    desktop.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationBodyCollider"

    def __init__(self, ignore_for_left_hand: primitives.Bool | None = None, ignore_for_right_hand: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ignore_for_left_hand: Initial value for IgnoreForLeftHand.
            ignore_for_right_hand: Initial value for IgnoreForRightHand.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ignore_for_left_hand is not None:
            self.ignore_for_left_hand = ignore_for_left_hand
        if ignore_for_right_hand is not None:
            self.ignore_for_right_hand = ignore_for_right_hand

    @property
    def ignore_for_left_hand(self) -> primitives.Bool | None:
        """Whether this collider is ignored by the player's left hand during locomotion."""
        member = self.get_member("IgnoreForLeftHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_for_left_hand.setter
    def ignore_for_left_hand(self, value: primitives.Bool) -> None:
        """Set the IgnoreForLeftHand field value."""
        member = self.get_member("IgnoreForLeftHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreForLeftHand", fields.FieldBool(value=value)
            )

    @property
    def ignore_for_right_hand(self) -> primitives.Bool | None:
        """Whether this collider is ignored by the player's right hand during locomotion."""
        member = self.get_member("IgnoreForRightHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_for_right_hand.setter
    def ignore_for_right_hand(self, value: primitives.Bool) -> None:
        """Set the IgnoreForRightHand field value."""
        member = self.get_member("IgnoreForRightHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreForRightHand", fields.FieldBool(value=value)
            )

