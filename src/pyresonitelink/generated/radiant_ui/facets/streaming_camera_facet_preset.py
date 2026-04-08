"""Generated component: StreamingCameraFacetPreset."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StreamingCameraFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StreamingCameraFacetPreset.

    Category: Radiant UI/Facets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StreamingCameraFacetPreset"

    def __init__(self, fully_loaded: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            fully_loaded: Initial value for _fullyLoaded.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if fully_loaded is not None:
            self.fully_loaded = fully_loaded

    @property
    def fully_loaded(self) -> primitives.Bool | None:
        """The _fullyLoaded field value."""
        member = self.get_member("_fullyLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fully_loaded.setter
    def fully_loaded(self, value: primitives.Bool) -> None:
        """Set the _fullyLoaded field value."""
        member = self.get_member("_fullyLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_fullyLoaded", fields.FieldBool(value=value)
            )

