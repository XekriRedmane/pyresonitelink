"""Generated component: DisplayIndex."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DisplayIndex(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DisplayIndex.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DisplayIndex"

    def __init__(self, index: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index is not None:
            self.index = index

    @property
    def index(self) -> primitives.Int | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

