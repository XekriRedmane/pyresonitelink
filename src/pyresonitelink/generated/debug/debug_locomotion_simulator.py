"""Generated component: DebugLocomotionSimulator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.locomotion_state import LocomotionState
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugLocomotionSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugLocomotionSimulator component is used to draw Debug visuals for a virtual locomotion simulator that drives the procedural animation system.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugLocomotionSimulator"

    def __init__(self, track_position: primitives.Bool | None = None, state: LocomotionState | str | None = None, movement_speed: primitives.Float3 | None = None, angular_speed: primitives.Float | None = None, rotate_direction: primitives.Bool | None = None, offset_root: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            track_position: Initial value for TrackPosition.
            state: Initial value for State.
            movement_speed: Initial value for MovementSpeed.
            angular_speed: Initial value for AngularSpeed.
            rotate_direction: Initial value for RotateDirection.
            offset_root: Initial value for OffsetRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if track_position is not None:
            self.track_position = track_position
        if state is not None:
            self.state = state
        if movement_speed is not None:
            self.movement_speed = movement_speed
        if angular_speed is not None:
            self.angular_speed = angular_speed
        if rotate_direction is not None:
            self.rotate_direction = rotate_direction
        if offset_root is not None:
            self.offset_root = offset_root

    @property
    def track_position(self) -> primitives.Bool | None:
        """Whether to keep track of this Debug locomotion's progressively moving position."""
        member = self.get_member("TrackPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @track_position.setter
    def track_position(self, value: primitives.Bool) -> None:
        """Set the TrackPosition field value."""
        member = self.get_member("TrackPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrackPosition", fields.FieldBool(value=value)
            )

    @property
    def state(self) -> LocomotionState | None:
        """The kind of locomotion this is debugging"""
        member = self.get_member("State")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LocomotionState(member.value)
        return None

    @state.setter
    def state(self, value: LocomotionState | str) -> None:
        """Set State. The kind of locomotion this is debugging"""
        member = self.get_member("State")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "State",
                members.FieldEnum(value=str(value)),
            )

    @property
    def movement_speed(self) -> primitives.Float3 | None:
        """How fast the locomotion should be moving."""
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
    def angular_speed(self) -> primitives.Float | None:
        """How fast this locomotion should be turning."""
        member = self.get_member("AngularSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angular_speed.setter
    def angular_speed(self, value: primitives.Float) -> None:
        """Set the AngularSpeed field value."""
        member = self.get_member("AngularSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngularSpeed", fields.FieldFloat(value=value)
            )

    @property
    def rotate_direction(self) -> primitives.Bool | None:
        """Whether the locomotion should rotate its movement direction."""
        member = self.get_member("RotateDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotate_direction.setter
    def rotate_direction(self, value: primitives.Bool) -> None:
        """Set the RotateDirection field value."""
        member = self.get_member("RotateDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotateDirection", fields.FieldBool(value=value)
            )

    @property
    def offset_root(self) -> primitives.Bool | None:
        """Whether this locomotion should be offsetting from root as a starting position"""
        member = self.get_member("OffsetRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_root.setter
    def offset_root(self, value: primitives.Bool) -> None:
        """Set the OffsetRoot field value."""
        member = self.get_member("OffsetRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetRoot", fields.FieldBool(value=value)
            )

