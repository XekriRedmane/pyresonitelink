"""Generated component: UserTrackingSpaceSync."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserTrackingSpaceSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserTrackingSpaceSync.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserTrackingSpaceSync"

    def __init__(self, seated_mode: bool | None = None, user_height: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
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
    def seated_mode(self) -> bool | None:
        """The SeatedMode field value."""
        member = self.get_member("SeatedMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seated_mode.setter
    def seated_mode(self, value: bool) -> None:
        """Set the SeatedMode field value."""
        member = self.get_member("SeatedMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SeatedMode", fields.FieldBool(value=value)
            )

    @property
    def user_height(self) -> np.float32 | None:
        """The UserHeight field value."""
        member = self.get_member("UserHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_height.setter
    def user_height(self, value: np.float32) -> None:
        """Set the UserHeight field value."""
        member = self.get_member("UserHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHeight", fields.FieldFloat(value=value)
            )

