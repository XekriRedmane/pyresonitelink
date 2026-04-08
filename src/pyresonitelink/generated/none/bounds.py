"""Generated component: Bounds."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Bounds(GeneratedComponent, IBounded, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Bounds.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Bounds"

    def __init__(self, available: bool | None = None, local_bounds: primitives.BoundingBox | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            available: Initial value for Available.
            local_bounds: Initial value for LocalBounds.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if available is not None:
            self.available = available
        if local_bounds is not None:
            self.local_bounds = local_bounds

    @property
    def available(self) -> bool | None:
        """The Available field value."""
        member = self.get_member("Available")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @available.setter
    def available(self, value: bool) -> None:
        """Set the Available field value."""
        member = self.get_member("Available")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Available", fields.FieldBool(value=value)
            )

    @property
    def local_bounds(self) -> primitives.BoundingBox | None:
        """The LocalBounds field value."""
        member = self.get_member("LocalBounds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_bounds.setter
    def local_bounds(self, value: primitives.BoundingBox) -> None:
        """Set the LocalBounds field value."""
        member = self.get_member("LocalBounds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalBounds", fields.FieldBoundingBox(value=value)
            )

