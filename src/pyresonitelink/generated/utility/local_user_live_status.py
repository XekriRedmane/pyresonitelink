"""Generated component: LocalUserLiveStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalUserLiveStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalUserLiveStatus.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalUserLiveStatus"

    def __init__(self, is_live: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_live: Initial value for IsLive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_live is not None:
            self.is_live = is_live

    @property
    def is_live(self) -> primitives.Bool | None:
        """The IsLive field value."""
        member = self.get_member("IsLive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_live.setter
    def is_live(self, value: primitives.Bool) -> None:
        """Set the IsLive field value."""
        member = self.get_member("IsLive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLive", fields.FieldBool(value=value)
            )

