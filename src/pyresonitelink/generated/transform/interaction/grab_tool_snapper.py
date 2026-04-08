"""Generated component: GrabToolSnapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabToolSnapper(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabToolSnapper.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabToolSnapper"

    def __init__(self, offset: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

