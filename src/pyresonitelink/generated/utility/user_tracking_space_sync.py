"""Generated component: UserTrackingSpaceSync."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserTrackingSpaceSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """User Tracking Space Sync is a component that provides the local user's height, and whether they are currently using seated mode.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserTrackingSpaceSync"

    def __init__(self, seated_mode: primitives.Bool | None = None, user_height: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            seated_mode: Initial value for SeatedMode.
            user_height: Initial value for UserHeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if seated_mode is not None:
            self.seated_mode = seated_mode
        if user_height is not None:
            self.user_height = user_height

    @property
    def seated_mode(self) -> primitives.Bool | None:
        """whether the local user is using seated mode."""
        member = self.get_member("SeatedMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seated_mode.setter
    def seated_mode(self, value: primitives.Bool) -> None:
        """Set the SeatedMode field value."""
        member = self.get_member("SeatedMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SeatedMode", fields.FieldBool(value=value)
            )

    @property
    def user_height(self) -> primitives.Float | None:
        """the local user's height in meters."""
        member = self.get_member("UserHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_height.setter
    def user_height(self, value: primitives.Float) -> None:
        """Set the UserHeight field value."""
        member = self.get_member("UserHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHeight", fields.FieldFloat(value=value)
            )

