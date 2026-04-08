"""Generated component: DebugFeed."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugFeed(GeneratedComponent, IDataFeedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugFeed.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugFeed"

    def __init__(self, category_count: primitives.Int | None = None, label_item_count: primitives.Int | None = None, string_item_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            category_count: Initial value for CategoryCount.
            label_item_count: Initial value for LabelItemCount.
            string_item_count: Initial value for StringItemCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if category_count is not None:
            self.category_count = category_count
        if label_item_count is not None:
            self.label_item_count = label_item_count
        if string_item_count is not None:
            self.string_item_count = string_item_count

    @property
    def category_count(self) -> primitives.Int | None:
        """The CategoryCount field value."""
        member = self.get_member("CategoryCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @category_count.setter
    def category_count(self, value: primitives.Int) -> None:
        """Set the CategoryCount field value."""
        member = self.get_member("CategoryCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CategoryCount", fields.FieldInt(value=value)
            )

    @property
    def label_item_count(self) -> primitives.Int | None:
        """The LabelItemCount field value."""
        member = self.get_member("LabelItemCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_item_count.setter
    def label_item_count(self, value: primitives.Int) -> None:
        """Set the LabelItemCount field value."""
        member = self.get_member("LabelItemCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelItemCount", fields.FieldInt(value=value)
            )

    @property
    def string_item_count(self) -> primitives.Int | None:
        """The StringItemCount field value."""
        member = self.get_member("StringItemCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @string_item_count.setter
    def string_item_count(self, value: primitives.Int) -> None:
        """Set the StringItemCount field value."""
        member = self.get_member("StringItemCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StringItemCount", fields.FieldInt(value=value)
            )

    @property
    def string_values(self) -> members.SyncList | None:
        """The StringValues member."""
        member = self.get_member("StringValues")
        if isinstance(member, members.SyncList):
            return member
        return None

    @string_values.setter
    def string_values(self, value: members.SyncList) -> None:
        """Set the StringValues member."""
        self.set_member("StringValues", value)

