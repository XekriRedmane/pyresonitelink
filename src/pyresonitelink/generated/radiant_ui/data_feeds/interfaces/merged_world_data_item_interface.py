"""Generated component: MergedWorldDataItemInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.feed_item_interface import FeedItemInterface
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MergedWorldDataItemInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The MergedWorldDataItemInterface component is used to display world details from a WorldsDataFeed.

    Category: Radiant UI/Data Feeds/Interfaces

    Used in data feed Template generating systems. See Data Feeds.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MergedWorldDataItemInterface"

    def __init__(self, has_data: primitives.Bool | None = None, item_name: str | IField[primitives.String] | None = None, item_key: str | IField[primitives.String] | None = None, item_description: str | IField[primitives.String] | None = None, has_description: str | IField[primitives.Bool] | None = None, description_cleanup: str | Slot | None = None, item_icon: str | IField[str] | None = None, has_icon: str | IField[primitives.Bool] | None = None, icon_cleanup: str | Slot | None = None, view: str | SyncRef[IDataFeedView] | None = None, parent_container: str | FeedItemInterface | None = None, child_container: str | Slot | None = None, enabled_state: str | IField[primitives.Bool] | None = None, is_merged: str | IField[primitives.Bool] | None = None, session_count: str | IField[primitives.Int] | None = None, world_count: str | IField[primitives.Int] | None = None, main_name: str | IField[primitives.String] | None = None, main_thumbnail: str | IField[str] | None = None, world_or_session_id: str | IField[primitives.String] | None = None, total_aggregate_active_users: str | IField[primitives.Int] | None = None, total_aggregate_contacts: str | IField[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            has_data: Initial value for HasData.
            item_name: Initial value for ItemName.
            item_key: Initial value for ItemKey.
            item_description: Initial value for ItemDescription.
            has_description: Initial value for HasDescription.
            description_cleanup: Initial value for DescriptionCleanup.
            item_icon: Initial value for ItemIcon.
            has_icon: Initial value for HasIcon.
            icon_cleanup: Initial value for IconCleanup.
            view: Initial value for View.
            parent_container: Initial value for ParentContainer.
            child_container: Initial value for ChildContainer.
            enabled_state: Initial value for EnabledState.
            is_merged: Initial value for IsMerged.
            session_count: Initial value for SessionCount.
            world_count: Initial value for WorldCount.
            main_name: Initial value for MainName.
            main_thumbnail: Initial value for MainThumbnail.
            world_or_session_id: Initial value for WorldOrSessionId.
            total_aggregate_active_users: Initial value for TotalAggregateActiveUsers.
            total_aggregate_contacts: Initial value for TotalAggregateContacts.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if has_data is not None:
            self.has_data = has_data
        if item_name is not None:
            self.item_name = item_name
        if item_key is not None:
            self.item_key = item_key
        if item_description is not None:
            self.item_description = item_description
        if has_description is not None:
            self.has_description = has_description
        if description_cleanup is not None:
            self.description_cleanup = description_cleanup
        if item_icon is not None:
            self.item_icon = item_icon
        if has_icon is not None:
            self.has_icon = has_icon
        if icon_cleanup is not None:
            self.icon_cleanup = icon_cleanup
        if view is not None:
            self.view = view
        if parent_container is not None:
            self.parent_container = parent_container
        if child_container is not None:
            self.child_container = child_container
        if enabled_state is not None:
            self.enabled_state = enabled_state
        if is_merged is not None:
            self.is_merged = is_merged
        if session_count is not None:
            self.session_count = session_count
        if world_count is not None:
            self.world_count = world_count
        if main_name is not None:
            self.main_name = main_name
        if main_thumbnail is not None:
            self.main_thumbnail = main_thumbnail
        if world_or_session_id is not None:
            self.world_or_session_id = world_or_session_id
        if total_aggregate_active_users is not None:
            self.total_aggregate_active_users = total_aggregate_active_users
        if total_aggregate_contacts is not None:
            self.total_aggregate_contacts = total_aggregate_contacts

    @property
    def has_data(self) -> primitives.Bool | None:
        """The HasData field value."""
        member = self.get_member("HasData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_data.setter
    def has_data(self, value: primitives.Bool) -> None:
        """Set the HasData field value."""
        member = self.get_member("HasData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasData", fields.FieldBool(value=value)
            )

    @property
    def item_name(self) -> str | None:
        """Target ID of the ItemName reference (targets IField[primitives.String])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def item_key(self) -> str | None:
        """Target ID of the ItemKey reference (targets IField[primitives.String])."""
        member = self.get_member("ItemKey")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_key.setter
    def item_key(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemKey reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemKey")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemKey",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def item_description(self) -> str | None:
        """Target ID of the ItemDescription reference (targets IField[primitives.String])."""
        member = self.get_member("ItemDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_description.setter
    def item_description(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemDescription reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemDescription")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemDescription",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def has_description(self) -> str | None:
        """Target ID of the HasDescription reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_description.setter
    def has_description(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasDescription reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasDescription")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasDescription",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def description_cleanup(self) -> str | None:
        """Target ID of the DescriptionCleanup reference (targets Slot)."""
        member = self.get_member("DescriptionCleanup")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description_cleanup.setter
    def description_cleanup(self, target: str | Slot | None) -> None:
        """Set the DescriptionCleanup reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DescriptionCleanup")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DescriptionCleanup",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def item_icon(self) -> str | None:
        """Target ID of the ItemIcon reference (targets IField[str])."""
        member = self.get_member("ItemIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_icon.setter
    def item_icon(self, target: str | IField[str] | None) -> None:
        """Set the ItemIcon reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemIcon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemIcon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def has_icon(self) -> str | None:
        """Target ID of the HasIcon reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_icon.setter
    def has_icon(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasIcon reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasIcon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasIcon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def icon_cleanup(self) -> str | None:
        """Target ID of the IconCleanup reference (targets Slot)."""
        member = self.get_member("IconCleanup")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_cleanup.setter
    def icon_cleanup(self, target: str | Slot | None) -> None:
        """Set the IconCleanup reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("IconCleanup")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IconCleanup",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def view(self) -> str | None:
        """Target ID of the View reference (targets SyncRef[IDataFeedView])."""
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @view.setter
    def view(self, target: str | SyncRef[IDataFeedView] | None) -> None:
        """Set the View reference by target ID or SyncRef[IDataFeedView] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("View")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "View",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IDataFeedView>'),
            )

    @property
    def parent_container(self) -> str | None:
        """Target ID of the ParentContainer reference (targets FeedItemInterface)."""
        member = self.get_member("ParentContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_container.setter
    def parent_container(self, target: str | FeedItemInterface | None) -> None:
        """Set the ParentContainer reference by target ID or FeedItemInterface instance."""
        target_id: str | None = target.id if isinstance(target, FeedItemInterface) else target  # type: ignore[assignment]
        member = self.get_member("ParentContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FeedItemInterface'),
            )

    @property
    def child_container(self) -> str | None:
        """Target ID of the ChildContainer reference (targets Slot)."""
        member = self.get_member("ChildContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @child_container.setter
    def child_container(self, target: str | Slot | None) -> None:
        """Set the ChildContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ChildContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ChildContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def nested_items(self) -> members.SyncList | None:
        """The NestedItems member."""
        member = self.get_member("NestedItems")
        if isinstance(member, members.SyncList):
            return member
        return None

    @nested_items.setter
    def nested_items(self, value: members.SyncList) -> None:
        """Set the NestedItems member."""
        self.set_member("NestedItems", value)

    @property
    def enabled_state(self) -> str | None:
        """Target ID of the EnabledState reference (targets IField[primitives.Bool])."""
        member = self.get_member("EnabledState")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled_state.setter
    def enabled_state(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the EnabledState reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("EnabledState")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EnabledState",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def is_merged(self) -> str | None:
        """The field to drive with whether or not the source data feed item was merged."""
        member = self.get_member("IsMerged")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_merged.setter
    def is_merged(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsMerged reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsMerged")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsMerged",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def session_count(self) -> str | None:
        """The field to drive with the amount of sessions in this set of worlds."""
        member = self.get_member("SessionCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_count.setter
    def session_count(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the SessionCount reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SessionCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SessionCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def world_count(self) -> str | None:
        """The field to drive with the amount of Merged worlds into this item."""
        member = self.get_member("WorldCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_count.setter
    def world_count(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the WorldCount reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("WorldCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def main_name(self) -> str | None:
        """The field to drive with the main world name of this Merged item."""
        member = self.get_member("MainName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_name.setter
    def main_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the MainName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MainName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MainName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def main_thumbnail(self) -> str | None:
        """The field to drive with the main world's thumbnail of this Merged item."""
        member = self.get_member("MainThumbnail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_thumbnail.setter
    def main_thumbnail(self, target: str | IField[str] | None) -> None:
        """Set the MainThumbnail reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MainThumbnail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MainThumbnail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def world_or_session_id(self) -> str | None:
        """The field to drive with the main world or session ID of this Merged item."""
        member = self.get_member("WorldOrSessionId")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_or_session_id.setter
    def world_or_session_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the WorldOrSessionId reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("WorldOrSessionId")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldOrSessionId",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def total_aggregate_active_users(self) -> str | None:
        """The field to drive with the total active users of all the worlds Merged into this item."""
        member = self.get_member("TotalAggregateActiveUsers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_aggregate_active_users.setter
    def total_aggregate_active_users(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalAggregateActiveUsers reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalAggregateActiveUsers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalAggregateActiveUsers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_aggregate_contacts(self) -> str | None:
        """The field to drive with the total users that are contacts in all the worlds Merged into this item."""
        member = self.get_member("TotalAggregateContacts")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_aggregate_contacts.setter
    def total_aggregate_contacts(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalAggregateContacts reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalAggregateContacts")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalAggregateContacts",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def sessions(self) -> members.SyncObject | None:
        """The list of item templates to instantiate with session info from this merged item."""
        member = self.get_member("Sessions")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @sessions.setter
    def sessions(self, value: members.SyncObject) -> None:
        """Set Sessions. The list of item templates to instantiate with session info from this merged item."""
        self.set_member("Sessions", value)

    @property
    def worlds(self) -> members.SyncObject | None:
        """The list of item templates to instantiate with the world data of this merged item."""
        member = self.get_member("Worlds")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @worlds.setter
    def worlds(self, value: members.SyncObject) -> None:
        """Set Worlds. The list of item templates to instantiate with the world data of this merged item."""
        self.set_member("Worlds", value)

