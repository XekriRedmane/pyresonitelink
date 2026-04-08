"""Generated component: DebugLocomotionSimulator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugLocomotionSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugLocomotionSimulator.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugLocomotionSimulator"

    def __init__(self, track_position: bool | None = None, movement_speed: primitives.Float3 | None = None, angular_speed: np.float32 | None = None, rotate_direction: bool | None = None, offset_root: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            track_position: Initial value for TrackPosition.
            movement_speed: Initial value for MovementSpeed.
            angular_speed: Initial value for AngularSpeed.
            rotate_direction: Initial value for RotateDirection.
            offset_root: Initial value for OffsetRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if track_position is not None:
            self.track_position = track_position
        if movement_speed is not None:
            self.movement_speed = movement_speed
        if angular_speed is not None:
            self.angular_speed = angular_speed
        if rotate_direction is not None:
            self.rotate_direction = rotate_direction
        if offset_root is not None:
            self.offset_root = offset_root

    @property
    def track_position(self) -> bool | None:
        """The TrackPosition field value."""
        member = self.get_member("TrackPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @track_position.setter
    def track_position(self, value: bool) -> None:
        """Set the TrackPosition field value."""
        member = self.get_member("TrackPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrackPosition", fields.FieldBool(value=value)
            )

    @property
    def state(self) -> members.FieldEnum | None:
        """The State member."""
        member = self.get_member("State")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state.setter
    def state(self, value: members.FieldEnum) -> None:
        """Set the State member."""
        self.set_member("State", value)

    @property
    def movement_speed(self) -> primitives.Float3 | None:
        """The MovementSpeed field value."""
        member = self.get_member("MovementSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @movement_speed.setter
    def movement_speed(self, value: primitives.Float3) -> None:
        """Set the MovementSpeed field value."""
        member = self.get_member("MovementSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MovementSpeed", fields.FieldFloat3(value=value)
            )

    @property
    def angular_speed(self) -> np.float32 | None:
        """The AngularSpeed field value."""
        member = self.get_member("AngularSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angular_speed.setter
    def angular_speed(self, value: np.float32) -> None:
        """Set the AngularSpeed field value."""
        member = self.get_member("AngularSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngularSpeed", fields.FieldFloat(value=value)
            )

    @property
    def rotate_direction(self) -> bool | None:
        """The RotateDirection field value."""
        member = self.get_member("RotateDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotate_direction.setter
    def rotate_direction(self, value: bool) -> None:
        """Set the RotateDirection field value."""
        member = self.get_member("RotateDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotateDirection", fields.FieldBool(value=value)
            )

    @property
    def offset_root(self) -> bool | None:
        """The OffsetRoot field value."""
        member = self.get_member("OffsetRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_root.setter
    def offset_root(self, value: bool) -> None:
        """Set the OffsetRoot field value."""
        member = self.get_member("OffsetRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetRoot", fields.FieldBool(value=value)
            )

