"""Generated component: DisplayIndex."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DisplayIndex(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DisplayIndex component when duplicated by a DesktopDisplayLayout by being part of the slot hiearchy specified by that component's ``DisplayTemplate``, this component's ``Index`` field will be filled by the screen number that DesktopDisplayLayout was trying to spawn a template for.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DisplayIndex"

    def __init__(self, index_: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index_: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index_ is not None:
            self.index_ = index_

    @property
    def index_(self) -> primitives.Int | None:
        """See above."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index_.setter
    def index_(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

