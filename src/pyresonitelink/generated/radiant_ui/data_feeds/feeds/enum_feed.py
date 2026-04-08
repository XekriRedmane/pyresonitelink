"""Generated component: EnumFeed."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EnumFeed(GenericComponent[T], IDataFeedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.EnumFeed<>.

    Category: Radiant UI/Data Feeds/Feeds

    Parameterize with a value type::

        EnumFeed[np.float32]
        EnumFeed[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EnumFeed<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.EnumFeed<>"

    def __init__(self, display_order: bool | None = None, distinct: bool | None = None, include_obsolete: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_order: Initial value for DisplayOrder.
            distinct: Initial value for Distinct.
            include_obsolete: Initial value for IncludeObsolete.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_order is not None:
            self.display_order = display_order
        if distinct is not None:
            self.distinct = distinct
        if include_obsolete is not None:
            self.include_obsolete = include_obsolete

    @property
    def display_order(self) -> bool | None:
        """The DisplayOrder field value."""
        member = self.get_member("DisplayOrder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_order.setter
    def display_order(self, value: bool) -> None:
        """Set the DisplayOrder field value."""
        member = self.get_member("DisplayOrder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayOrder", fields.FieldBool(value=value)
            )

    @property
    def distinct(self) -> bool | None:
        """The Distinct field value."""
        member = self.get_member("Distinct")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distinct.setter
    def distinct(self, value: bool) -> None:
        """Set the Distinct field value."""
        member = self.get_member("Distinct")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distinct", fields.FieldBool(value=value)
            )

    @property
    def include_obsolete(self) -> bool | None:
        """The IncludeObsolete field value."""
        member = self.get_member("IncludeObsolete")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @include_obsolete.setter
    def include_obsolete(self, value: bool) -> None:
        """Set the IncludeObsolete field value."""
        member = self.get_member("IncludeObsolete")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IncludeObsolete", fields.FieldBool(value=value)
            )

