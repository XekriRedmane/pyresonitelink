"""Generated component: DebugHandOffsetCompensation."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugHandOffsetCompensation(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugHandOffsetCompensation.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugHandOffsetCompensation"

    def __init__(self, left_hand_position: primitives.Float3 | None = None, left_hand_rotation: primitives.FloatQ | None = None, right_hand_position: primitives.Float3 | None = None, right_hand_rotation: primitives.FloatQ | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            left_hand_position: Initial value for LeftHandPosition.
            left_hand_rotation: Initial value for LeftHandRotation.
            right_hand_position: Initial value for RightHandPosition.
            right_hand_rotation: Initial value for RightHandRotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if left_hand_position is not None:
            self.left_hand_position = left_hand_position
        if left_hand_rotation is not None:
            self.left_hand_rotation = left_hand_rotation
        if right_hand_position is not None:
            self.right_hand_position = right_hand_position
        if right_hand_rotation is not None:
            self.right_hand_rotation = right_hand_rotation

    @property
    def left_hand_position(self) -> primitives.Float3 | None:
        """The LeftHandPosition field value."""
        member = self.get_member("LeftHandPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_hand_position.setter
    def left_hand_position(self, value: primitives.Float3) -> None:
        """Set the LeftHandPosition field value."""
        member = self.get_member("LeftHandPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftHandPosition", fields.FieldFloat3(value=value)
            )

    @property
    def left_hand_rotation(self) -> primitives.FloatQ | None:
        """The LeftHandRotation field value."""
        member = self.get_member("LeftHandRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_hand_rotation.setter
    def left_hand_rotation(self, value: primitives.FloatQ) -> None:
        """Set the LeftHandRotation field value."""
        member = self.get_member("LeftHandRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftHandRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def right_hand_position(self) -> primitives.Float3 | None:
        """The RightHandPosition field value."""
        member = self.get_member("RightHandPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_hand_position.setter
    def right_hand_position(self, value: primitives.Float3) -> None:
        """Set the RightHandPosition field value."""
        member = self.get_member("RightHandPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightHandPosition", fields.FieldFloat3(value=value)
            )

    @property
    def right_hand_rotation(self) -> primitives.FloatQ | None:
        """The RightHandRotation field value."""
        member = self.get_member("RightHandRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_hand_rotation.setter
    def right_hand_rotation(self, value: primitives.FloatQ) -> None:
        """Set the RightHandRotation field value."""
        member = self.get_member("RightHandRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightHandRotation", fields.FieldFloatQ(value=value)
            )

