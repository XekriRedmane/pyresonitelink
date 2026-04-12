"""Generated component: DevModeController."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DevModeController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DevModeController component only works in userspace and is used to control the user's current edit mode state.

    Used in settings. Not usually used by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DevModeController"

    def __init__(self, dev_mode_enabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dev_mode_enabled: Initial value for DevModeEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dev_mode_enabled is not None:
            self.dev_mode_enabled = dev_mode_enabled

    @property
    def dev_mode_enabled(self) -> primitives.Bool | None:
        """Whether Edit Mode is enabled."""
        member = self.get_member("DevModeEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dev_mode_enabled.setter
    def dev_mode_enabled(self, value: primitives.Bool) -> None:
        """Set the DevModeEnabled field value."""
        member = self.get_member("DevModeEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DevModeEnabled", fields.FieldBool(value=value)
            )

