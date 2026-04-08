"""Generated component: WorldItemInterface."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.idata_feed_view import IDataFeedView
from pyresonitelink.generated._types.feed_item_interface import FeedItemInterface
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldItemInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldItemInterface.

    Category: Radiant UI/Data Feeds/Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldItemInterface"

    def __init__(self, has_data: bool | None = None, item_name: str | IField[str] | None = None, item_key: str | IField[str] | None = None, item_description: str | IField[str] | None = None, has_description: str | IField[bool] | None = None, description_cleanup: str | Slot | None = None, item_icon: str | IField[str] | None = None, has_icon: str | IField[bool] | None = None, icon_cleanup: str | Slot | None = None, view: str | SyncRef[IDataFeedView] | None = None, parent_container: str | FeedItemInterface | None = None, child_container: str | Slot | None = None, enabled_state: str | IField[bool] | None = None, world_name: str | IField[str] | None = None, description: str | IField[str] | None = None, thumbnail_url: str | IField[str] | None = None, joined_users: str | IField[np.int32] | None = None, active_users: str | IField[np.int32] | None = None, is_host: str | IField[bool] | None = None, away_kick_enabled: str | IField[bool] | None = None, away_kick_interval: str | IField[str] | None = None, *, component: workers.Component | None = None) -> None:
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
            world_name: Initial value for WorldName.
            description: Initial value for Description.
            thumbnail_url: Initial value for ThumbnailUrl.
            joined_users: Initial value for JoinedUsers.
            active_users: Initial value for ActiveUsers.
            is_host: Initial value for IsHost.
            away_kick_enabled: Initial value for AwayKickEnabled.
            away_kick_interval: Initial value for AwayKickInterval.
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
        if world_name is not None:
            self.world_name = world_name
        if description is not None:
            self.description = description
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if joined_users is not None:
            self.joined_users = joined_users
        if active_users is not None:
            self.active_users = active_users
        if is_host is not None:
            self.is_host = is_host
        if away_kick_enabled is not None:
            self.away_kick_enabled = away_kick_enabled
        if away_kick_interval is not None:
            self.away_kick_interval = away_kick_interval

    @property
    def has_data(self) -> bool | None:
        """The HasData field value."""
        member = self.get_member("HasData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_data.setter
    def has_data(self, value: bool) -> None:
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
        """Target ID of the ItemName reference (targets IField[str])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[str] | None) -> None:
        """Set the ItemName reference by target ID or IField[str] instance."""
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
        """Target ID of the ItemKey reference (targets IField[str])."""
        member = self.get_member("ItemKey")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_key.setter
    def item_key(self, target: str | IField[str] | None) -> None:
        """Set the ItemKey reference by target ID or IField[str] instance."""
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
        """Target ID of the ItemDescription reference (targets IField[str])."""
        member = self.get_member("ItemDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_description.setter
    def item_description(self, target: str | IField[str] | None) -> None:
        """Set the ItemDescription reference by target ID or IField[str] instance."""
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
        """Target ID of the HasDescription reference (targets IField[bool])."""
        member = self.get_member("HasDescription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_description.setter
    def has_description(self, target: str | IField[bool] | None) -> None:
        """Set the HasDescription reference by target ID or IField[bool] instance."""
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
        """Target ID of the HasIcon reference (targets IField[bool])."""
        member = self.get_member("HasIcon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_icon.setter
    def has_icon(self, target: str | IField[bool] | None) -> None:
        """Set the HasIcon reference by target ID or IField[bool] instance."""
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
        """Target ID of the EnabledState reference (targets IField[bool])."""
        member = self.get_member("EnabledState")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled_state.setter
    def enabled_state(self, target: str | IField[bool] | None) -> None:
        """Set the EnabledState reference by target ID or IField[bool] instance."""
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
    def world_name(self) -> str | None:
        """Target ID of the WorldName reference (targets IField[str])."""
        member = self.get_member("WorldName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name.setter
    def world_name(self, target: str | IField[str] | None) -> None:
        """Set the WorldName reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("WorldName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def description(self) -> str | None:
        """Target ID of the Description reference (targets IField[str])."""
        member = self.get_member("Description")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description.setter
    def description(self, target: str | IField[str] | None) -> None:
        """Set the Description reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Description")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Description",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def thumbnail_url(self) -> str | None:
        """Target ID of the ThumbnailUrl reference (targets IField[str])."""
        member = self.get_member("ThumbnailUrl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumbnail_url.setter
    def thumbnail_url(self, target: str | IField[str] | None) -> None:
        """Set the ThumbnailUrl reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ThumbnailUrl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ThumbnailUrl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def joined_users(self) -> str | None:
        """Target ID of the JoinedUsers reference (targets IField[np.int32])."""
        member = self.get_member("JoinedUsers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @joined_users.setter
    def joined_users(self, target: str | IField[np.int32] | None) -> None:
        """Set the JoinedUsers reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("JoinedUsers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "JoinedUsers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def active_users(self) -> str | None:
        """Target ID of the ActiveUsers reference (targets IField[np.int32])."""
        member = self.get_member("ActiveUsers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_users.setter
    def active_users(self, target: str | IField[np.int32] | None) -> None:
        """Set the ActiveUsers reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ActiveUsers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveUsers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def is_host(self) -> str | None:
        """Target ID of the IsHost reference (targets IField[bool])."""
        member = self.get_member("IsHost")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_host.setter
    def is_host(self, target: str | IField[bool] | None) -> None:
        """Set the IsHost reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsHost")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsHost",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def away_kick_enabled(self) -> str | None:
        """Target ID of the AwayKickEnabled reference (targets IField[bool])."""
        member = self.get_member("AwayKickEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_enabled.setter
    def away_kick_enabled(self, target: str | IField[bool] | None) -> None:
        """Set the AwayKickEnabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AwayKickEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AwayKickEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def away_kick_interval(self) -> str | None:
        """Target ID of the AwayKickInterval reference (targets IField[str])."""
        member = self.get_member("AwayKickInterval")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_interval.setter
    def away_kick_interval(self, target: str | IField[str] | None) -> None:
        """Set the AwayKickInterval reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AwayKickInterval")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AwayKickInterval",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<TimeSpan>'),
            )

