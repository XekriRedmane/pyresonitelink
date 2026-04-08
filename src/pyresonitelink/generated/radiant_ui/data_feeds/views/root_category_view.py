"""Generated component: RootCategoryView."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RootCategoryView(GeneratedComponent, ICustomInspector, IDataFeedView, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RootCategoryView.

    Category: Radiant UI/Data Feeds/Views
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RootCategoryView"

    def __init__(self, feed: str | IDataFeedComponent | None = None, search_phrase: primitives.String | None = None, reset_view_on_save: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            feed: Initial value for Feed.
            search_phrase: Initial value for SearchPhrase.
            reset_view_on_save: Initial value for ResetViewOnSave.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if feed is not None:
            self.feed = feed
        if search_phrase is not None:
            self.search_phrase = search_phrase
        if reset_view_on_save is not None:
            self.reset_view_on_save = reset_view_on_save

    @property
    def feed(self) -> str | None:
        """Target ID of the Feed reference (targets IDataFeedComponent)."""
        member = self.get_member("Feed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @feed.setter
    def feed(self, target: str | IDataFeedComponent | None) -> None:
        """Set the Feed reference by target ID or IDataFeedComponent instance."""
        target_id: str | None = target.id if isinstance(target, IDataFeedComponent) else target  # type: ignore[assignment]
        member = self.get_member("Feed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Feed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IDataFeedComponent'),
            )

    @property
    def path(self) -> members.SyncList | None:
        """The Path member."""
        member = self.get_member("Path")
        if isinstance(member, members.SyncList):
            return member
        return None

    @path.setter
    def path(self, value: members.SyncList) -> None:
        """Set the Path member."""
        self.set_member("Path", value)

    @property
    def grouping_keys(self) -> members.SyncList | None:
        """The GroupingKeys member."""
        member = self.get_member("GroupingKeys")
        if isinstance(member, members.SyncList):
            return member
        return None

    @grouping_keys.setter
    def grouping_keys(self, value: members.SyncList) -> None:
        """Set the GroupingKeys member."""
        self.set_member("GroupingKeys", value)

    @property
    def search_phrase(self) -> primitives.String | None:
        """The SearchPhrase field value."""
        member = self.get_member("SearchPhrase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_phrase.setter
    def search_phrase(self, value: primitives.String) -> None:
        """Set the SearchPhrase field value."""
        member = self.get_member("SearchPhrase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchPhrase", fields.FieldString(value=value)
            )

    @property
    def updating_user(self) -> members.SyncObject | None:
        """The UpdatingUser member."""
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @updating_user.setter
    def updating_user(self, value: members.SyncObject) -> None:
        """Set the UpdatingUser member."""
        self.set_member("UpdatingUser", value)

    @property
    def reset_view_on_save(self) -> primitives.Bool | None:
        """The ResetViewOnSave field value."""
        member = self.get_member("ResetViewOnSave")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_view_on_save.setter
    def reset_view_on_save(self, value: primitives.Bool) -> None:
        """Set the ResetViewOnSave field value."""
        member = self.get_member("ResetViewOnSave")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetViewOnSave", fields.FieldBool(value=value)
            )

    @property
    def category_manager(self) -> members.SyncObject | None:
        """The CategoryManager member."""
        member = self.get_member("CategoryManager")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @category_manager.setter
    def category_manager(self, value: members.SyncObject) -> None:
        """Set the CategoryManager member."""
        self.set_member("CategoryManager", value)

    @property
    def items_manager(self) -> members.SyncObject | None:
        """The ItemsManager member."""
        member = self.get_member("ItemsManager")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @items_manager.setter
    def items_manager(self, value: members.SyncObject) -> None:
        """Set the ItemsManager member."""
        self.set_member("ItemsManager", value)

