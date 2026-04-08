"""Generated component: CharacterTeleporter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterTeleporter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CharacterTeleporter.

    Category: Locomotion/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterTeleporter"

    def __init__(self, triggers_only: primitives.Bool | None = None, minimum_velocity: primitives.Float | None = None, direction_reference: primitives.Float3 | None = None, max_direction_angle: primitives.Float | None = None, ignore_parent_user: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            minimum_velocity: Initial value for MinimumVelocity.
            direction_reference: Initial value for DirectionReference.
            max_direction_angle: Initial value for MaxDirectionAngle.
            ignore_parent_user: Initial value for IgnoreParentUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if minimum_velocity is not None:
            self.minimum_velocity = minimum_velocity
        if direction_reference is not None:
            self.direction_reference = direction_reference
        if max_direction_angle is not None:
            self.max_direction_angle = max_direction_angle
        if ignore_parent_user is not None:
            self.ignore_parent_user = ignore_parent_user

    @property
    def triggers_only(self) -> primitives.Bool | None:
        """The TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: primitives.Bool) -> None:
        """Set the TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriggersOnly", fields.FieldBool(value=value)
            )

    @property
    def exits(self) -> members.SyncList | None:
        """The Exits member."""
        member = self.get_member("Exits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exits.setter
    def exits(self, value: members.SyncList) -> None:
        """Set the Exits member."""
        self.set_member("Exits", value)

    @property
    def minimum_velocity(self) -> primitives.Float | None:
        """The MinimumVelocity field value."""
        member = self.get_member("MinimumVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_velocity.setter
    def minimum_velocity(self, value: primitives.Float) -> None:
        """Set the MinimumVelocity field value."""
        member = self.get_member("MinimumVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumVelocity", fields.FieldFloat(value=value)
            )

    @property
    def direction_reference(self) -> primitives.Float3 | None:
        """The DirectionReference field value."""
        member = self.get_member("DirectionReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction_reference.setter
    def direction_reference(self, value: primitives.Float3) -> None:
        """Set the DirectionReference field value."""
        member = self.get_member("DirectionReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectionReference", fields.FieldFloat3(value=value)
            )

    @property
    def max_direction_angle(self) -> primitives.Float | None:
        """The MaxDirectionAngle field value."""
        member = self.get_member("MaxDirectionAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_direction_angle.setter
    def max_direction_angle(self, value: primitives.Float) -> None:
        """Set the MaxDirectionAngle field value."""
        member = self.get_member("MaxDirectionAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDirectionAngle", fields.FieldFloat(value=value)
            )

    @property
    def ignore_parent_user(self) -> primitives.Bool | None:
        """The IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_parent_user.setter
    def ignore_parent_user(self, value: primitives.Bool) -> None:
        """Set the IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreParentUser", fields.FieldBool(value=value)
            )

