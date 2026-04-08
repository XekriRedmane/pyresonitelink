"""Generated component: ColliderUserTracker."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColliderUserTracker(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColliderUserTracker.

    Category: Physics/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColliderUserTracker"

    def __init__(self, triggers_only: primitives.Bool | None = None, is_local_user_inside: primitives.Bool | None = None, is_any_user_inside: primitives.Bool | None = None, number_of_users_inside: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            is_local_user_inside: Initial value for IsLocalUserInside.
            is_any_user_inside: Initial value for IsAnyUserInside.
            number_of_users_inside: Initial value for NumberOfUsersInside.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if is_local_user_inside is not None:
            self.is_local_user_inside = is_local_user_inside
        if is_any_user_inside is not None:
            self.is_any_user_inside = is_any_user_inside
        if number_of_users_inside is not None:
            self.number_of_users_inside = number_of_users_inside

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
    def is_local_user_inside(self) -> primitives.Bool | None:
        """The IsLocalUserInside field value."""
        member = self.get_member("IsLocalUserInside")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_local_user_inside.setter
    def is_local_user_inside(self, value: primitives.Bool) -> None:
        """Set the IsLocalUserInside field value."""
        member = self.get_member("IsLocalUserInside")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLocalUserInside", fields.FieldBool(value=value)
            )

    @property
    def is_any_user_inside(self) -> primitives.Bool | None:
        """The IsAnyUserInside field value."""
        member = self.get_member("IsAnyUserInside")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_any_user_inside.setter
    def is_any_user_inside(self, value: primitives.Bool) -> None:
        """Set the IsAnyUserInside field value."""
        member = self.get_member("IsAnyUserInside")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsAnyUserInside", fields.FieldBool(value=value)
            )

    @property
    def number_of_users_inside(self) -> primitives.Int | None:
        """The NumberOfUsersInside field value."""
        member = self.get_member("NumberOfUsersInside")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @number_of_users_inside.setter
    def number_of_users_inside(self, value: primitives.Int) -> None:
        """Set the NumberOfUsersInside field value."""
        member = self.get_member("NumberOfUsersInside")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NumberOfUsersInside", fields.FieldInt(value=value)
            )

