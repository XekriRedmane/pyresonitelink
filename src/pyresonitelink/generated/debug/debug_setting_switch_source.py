"""Generated component: DebugSettingSwitchSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugSettingSwitchSource(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugSettingSwitchSource.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSettingSwitchSource"

    def __init__(self, current_profile: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            current_profile: Initial value for CurrentProfile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if current_profile is not None:
            self.current_profile = current_profile

    @property
    def current_profile(self) -> str | None:
        """The CurrentProfile field value."""
        member = self.get_member("CurrentProfile")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_profile.setter
    def current_profile(self, value: str) -> None:
        """Set the CurrentProfile field value."""
        member = self.get_member("CurrentProfile")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentProfile", fields.FieldString(value=value)
            )

