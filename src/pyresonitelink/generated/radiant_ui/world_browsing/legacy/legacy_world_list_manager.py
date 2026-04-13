"""Generated component: LegacyWorldListManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.generated._enums.owner_type import OwnerType
from pyresonitelink.generated._enums.empty_session_filter import EmptySessionFilter
from pyresonitelink.generated._enums.session_access_level import SessionAccessLevel
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_world_item import LegacyWorldItem
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyWorldListManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyWorldListManager component is used in the old dash to manage the world list before the WorldsDataFeed component was implemented.

    Category: Radiant UI/World Browsing/Legacy

    This is a Legacy component. Don't use.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyWorldListManager"

    def __init__(self, world_item_template: str | LegacyWorldItem | None = None, world_item_type: Type | str | None = None, show_opened_worlds: primitives.Bool | None = None, show_sessions: primitives.Bool | None = None, show_published_worlds: primitives.Bool | None = None, show_locally_saved_worlds: primitives.Bool | None = None, merge_sessions_by_world_id: primitives.Bool | None = None, idle_sort_delay: primitives.Float | None = None, interacting_sort_delay: primitives.Float | None = None, search_term: primitives.String | None = None, submitted_to: primitives.String | None = None, only_featured: primitives.Bool | None = None, own_worlds: primitives.Bool | None = None, by_owner: primitives.String | None = None, owner_type: OwnerType | str | None = None, min_date: str | None = None, max_date: str | None = None, max_items: primitives.Int | None = None, skip_items: primitives.Int | None = None, empty_sessions: EmptySessionFilter | str | None = None, incompatible_sessions: primitives.Bool | None = None, only_headless_hosts: primitives.Bool | None = None, minimum_total_users: primitives.Int | None = None, minimum_total_contacts: primitives.Int | None = None, min_session_access_level: SessionAccessLevel | str | None = None, max_session_access_level: SessionAccessLevel | str | None = None, min_uptime: primitives.Double | None = None, max_uptime: primitives.Double | None = None, parent_session_id: primitives.String | None = None, visited: primitives.Bool | None = None, is_searching: primitives.Bool | None = None, has_more_results: primitives.Bool | None = None, total_results: primitives.Int | None = None, filtered_results: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_item_template: Initial value for WorldItemTemplate.
            world_item_type: Initial value for WorldItemType.
            show_opened_worlds: Initial value for ShowOpenedWorlds.
            show_sessions: Initial value for ShowSessions.
            show_published_worlds: Initial value for ShowPublishedWorlds.
            show_locally_saved_worlds: Initial value for ShowLocallySavedWorlds.
            merge_sessions_by_world_id: Initial value for MergeSessionsByWorldId.
            idle_sort_delay: Initial value for IdleSortDelay.
            interacting_sort_delay: Initial value for InteractingSortDelay.
            search_term: Initial value for SearchTerm.
            submitted_to: Initial value for SubmittedTo.
            only_featured: Initial value for OnlyFeatured.
            own_worlds: Initial value for OwnWorlds.
            by_owner: Initial value for ByOwner.
            owner_type: Initial value for OwnerType.
            min_date: Initial value for MinDate.
            max_date: Initial value for MaxDate.
            max_items: Initial value for MaxItems.
            skip_items: Initial value for SkipItems.
            empty_sessions: Initial value for EmptySessions.
            incompatible_sessions: Initial value for IncompatibleSessions.
            only_headless_hosts: Initial value for OnlyHeadlessHosts.
            minimum_total_users: Initial value for MinimumTotalUsers.
            minimum_total_contacts: Initial value for MinimumTotalContacts.
            min_session_access_level: Initial value for MinSessionAccessLevel.
            max_session_access_level: Initial value for MaxSessionAccessLevel.
            min_uptime: Initial value for MinUptime.
            max_uptime: Initial value for MaxUptime.
            parent_session_id: Initial value for ParentSessionId.
            visited: Initial value for Visited.
            is_searching: Initial value for IsSearching.
            has_more_results: Initial value for HasMoreResults.
            total_results: Initial value for TotalResults.
            filtered_results: Initial value for FilteredResults.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_item_template is not None:
            self.world_item_template = world_item_template
        if world_item_type is not None:
            self.world_item_type = world_item_type
        if show_opened_worlds is not None:
            self.show_opened_worlds = show_opened_worlds
        if show_sessions is not None:
            self.show_sessions = show_sessions
        if show_published_worlds is not None:
            self.show_published_worlds = show_published_worlds
        if show_locally_saved_worlds is not None:
            self.show_locally_saved_worlds = show_locally_saved_worlds
        if merge_sessions_by_world_id is not None:
            self.merge_sessions_by_world_id = merge_sessions_by_world_id
        if idle_sort_delay is not None:
            self.idle_sort_delay = idle_sort_delay
        if interacting_sort_delay is not None:
            self.interacting_sort_delay = interacting_sort_delay
        if search_term is not None:
            self.search_term = search_term
        if submitted_to is not None:
            self.submitted_to = submitted_to
        if only_featured is not None:
            self.only_featured = only_featured
        if own_worlds is not None:
            self.own_worlds = own_worlds
        if by_owner is not None:
            self.by_owner = by_owner
        if owner_type is not None:
            self.owner_type = owner_type
        if min_date is not None:
            self.min_date = min_date
        if max_date is not None:
            self.max_date = max_date
        if max_items is not None:
            self.max_items = max_items
        if skip_items is not None:
            self.skip_items = skip_items
        if empty_sessions is not None:
            self.empty_sessions = empty_sessions
        if incompatible_sessions is not None:
            self.incompatible_sessions = incompatible_sessions
        if only_headless_hosts is not None:
            self.only_headless_hosts = only_headless_hosts
        if minimum_total_users is not None:
            self.minimum_total_users = minimum_total_users
        if minimum_total_contacts is not None:
            self.minimum_total_contacts = minimum_total_contacts
        if min_session_access_level is not None:
            self.min_session_access_level = min_session_access_level
        if max_session_access_level is not None:
            self.max_session_access_level = max_session_access_level
        if min_uptime is not None:
            self.min_uptime = min_uptime
        if max_uptime is not None:
            self.max_uptime = max_uptime
        if parent_session_id is not None:
            self.parent_session_id = parent_session_id
        if visited is not None:
            self.visited = visited
        if is_searching is not None:
            self.is_searching = is_searching
        if has_more_results is not None:
            self.has_more_results = has_more_results
        if total_results is not None:
            self.total_results = total_results
        if filtered_results is not None:
            self.filtered_results = filtered_results

    @property
    def updating_user(self) -> members.SyncObject | None:
        """The user handling this component's update logic."""
        member = self.get_member("UpdatingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @updating_user.setter
    def updating_user(self, value: members.SyncObject) -> None:
        """Set UpdatingUser. The user handling this component's update logic."""
        self.set_member("UpdatingUser", value)

    @property
    def world_item_template(self) -> str | None:
        """The item Component to use as a template when making the world list."""
        member = self.get_member("WorldItemTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_item_template.setter
    def world_item_template(self, target: str | LegacyWorldItem | None) -> None:
        """Set the WorldItemTemplate reference by target ID or LegacyWorldItem instance."""
        target_id: str | None = target.id if isinstance(target, LegacyWorldItem) else target  # type: ignore[assignment]
        member = self.get_member("WorldItemTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldItemTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyWorldItem'),
            )

    @property
    def world_item_type(self) -> Type | None:
        """The C# Type of the world items. Auto filled."""
        member = self.get_member("WorldItemType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @world_item_type.setter
    def world_item_type(self, value: Type | str) -> None:
        """Set WorldItemType. The C# Type of the world items. Auto filled."""
        member = self.get_member("WorldItemType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WorldItemType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def show_opened_worlds(self) -> primitives.Bool | None:
        """Show world's that are currently open."""
        member = self.get_member("ShowOpenedWorlds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_opened_worlds.setter
    def show_opened_worlds(self, value: primitives.Bool) -> None:
        """Set the ShowOpenedWorlds field value."""
        member = self.get_member("ShowOpenedWorlds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowOpenedWorlds", fields.FieldBool(value=value)
            )

    @property
    def show_sessions(self) -> primitives.Bool | None:
        """Show sessions currently open."""
        member = self.get_member("ShowSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_sessions.setter
    def show_sessions(self, value: primitives.Bool) -> None:
        """Set the ShowSessions field value."""
        member = self.get_member("ShowSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowSessions", fields.FieldBool(value=value)
            )

    @property
    def show_published_worlds(self) -> primitives.Bool | None:
        """Show worlds that are currently published."""
        member = self.get_member("ShowPublishedWorlds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_published_worlds.setter
    def show_published_worlds(self, value: primitives.Bool) -> None:
        """Set the ShowPublishedWorlds field value."""
        member = self.get_member("ShowPublishedWorlds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowPublishedWorlds", fields.FieldBool(value=value)
            )

    @property
    def show_locally_saved_worlds(self) -> primitives.Bool | None:
        """Show locally saved worlds."""
        member = self.get_member("ShowLocallySavedWorlds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_locally_saved_worlds.setter
    def show_locally_saved_worlds(self, value: primitives.Bool) -> None:
        """Set the ShowLocallySavedWorlds field value."""
        member = self.get_member("ShowLocallySavedWorlds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowLocallySavedWorlds", fields.FieldBool(value=value)
            )

    @property
    def merge_sessions_by_world_id(self) -> primitives.Bool | None:
        """group sessions by world they were opened from."""
        member = self.get_member("MergeSessionsByWorldId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @merge_sessions_by_world_id.setter
    def merge_sessions_by_world_id(self, value: primitives.Bool) -> None:
        """Set the MergeSessionsByWorldId field value."""
        member = self.get_member("MergeSessionsByWorldId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MergeSessionsByWorldId", fields.FieldBool(value=value)
            )

    @property
    def idle_sort_delay(self) -> primitives.Float | None:
        """How long to wait before sorting session list while idle."""
        member = self.get_member("IdleSortDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @idle_sort_delay.setter
    def idle_sort_delay(self, value: primitives.Float) -> None:
        """Set the IdleSortDelay field value."""
        member = self.get_member("IdleSortDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IdleSortDelay", fields.FieldFloat(value=value)
            )

    @property
    def interacting_sort_delay(self) -> primitives.Float | None:
        """How long to wait before sorting session list while still interacting."""
        member = self.get_member("InteractingSortDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interacting_sort_delay.setter
    def interacting_sort_delay(self, value: primitives.Float) -> None:
        """Set the InteractingSortDelay field value."""
        member = self.get_member("InteractingSortDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InteractingSortDelay", fields.FieldFloat(value=value)
            )

    @property
    def search_term(self) -> primitives.String | None:
        """The current search term for worlds."""
        member = self.get_member("SearchTerm")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_term.setter
    def search_term(self, value: primitives.String) -> None:
        """Set the SearchTerm field value."""
        member = self.get_member("SearchTerm")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchTerm", fields.FieldString(value=value)
            )

    @property
    def submitted_to(self) -> primitives.String | None:
        """The universe owner ID to search for worlds under (Usually G-Resonite)"""
        member = self.get_member("SubmittedTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @submitted_to.setter
    def submitted_to(self, value: primitives.String) -> None:
        """Set the SubmittedTo field value."""
        member = self.get_member("SubmittedTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubmittedTo", fields.FieldString(value=value)
            )

    @property
    def only_featured(self) -> primitives.Bool | None:
        """Show only featured worlds."""
        member = self.get_member("OnlyFeatured")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @only_featured.setter
    def only_featured(self, value: primitives.Bool) -> None:
        """Set the OnlyFeatured field value."""
        member = self.get_member("OnlyFeatured")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnlyFeatured", fields.FieldBool(value=value)
            )

    @property
    def own_worlds(self) -> primitives.Bool | None:
        """Show worlds made by ``UpdatingUser``."""
        member = self.get_member("OwnWorlds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @own_worlds.setter
    def own_worlds(self, value: primitives.Bool) -> None:
        """Set the OwnWorlds field value."""
        member = self.get_member("OwnWorlds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OwnWorlds", fields.FieldBool(value=value)
            )

    @property
    def by_owner(self) -> primitives.String | None:
        """Show the worlds made by this user ID."""
        member = self.get_member("ByOwner")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @by_owner.setter
    def by_owner(self, value: primitives.String) -> None:
        """Set the ByOwner field value."""
        member = self.get_member("ByOwner")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ByOwner", fields.FieldString(value=value)
            )

    @property
    def owner_type(self) -> OwnerType | None:
        """The kind of entity that can own the world."""
        member = self.get_member("OwnerType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OwnerType(member.value)
        return None

    @owner_type.setter
    def owner_type(self, value: OwnerType | str) -> None:
        """Set OwnerType. The kind of entity that can own the world."""
        member = self.get_member("OwnerType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OwnerType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_date(self) -> str | None:
        """The minimum date for a world to show up in the results."""
        member = self.get_member("MinDate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_date.setter
    def min_date(self, value: str) -> None:
        """Set the MinDate field value."""
        member = self.get_member("MinDate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDate", fields.FieldNullableDateTime(value=value)
            )

    @property
    def max_date(self) -> str | None:
        """The maximum date allowed for a world to show up in the results."""
        member = self.get_member("MaxDate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_date.setter
    def max_date(self, value: str) -> None:
        """Set the MaxDate field value."""
        member = self.get_member("MaxDate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDate", fields.FieldNullableDateTime(value=value)
            )

    @property
    def max_items(self) -> primitives.Int | None:
        """The maximum amount of items to show."""
        member = self.get_member("MaxItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_items.setter
    def max_items(self, value: primitives.Int) -> None:
        """Set the MaxItems field value."""
        member = self.get_member("MaxItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxItems", fields.FieldInt(value=value)
            )

    @property
    def skip_items(self) -> primitives.Int | None:
        """how many starter items to skip."""
        member = self.get_member("SkipItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @skip_items.setter
    def skip_items(self, value: primitives.Int) -> None:
        """Set the SkipItems field value."""
        member = self.get_member("SkipItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SkipItems", fields.FieldInt(value=value)
            )

    @property
    def empty_sessions(self) -> EmptySessionFilter | None:
        """How to apply filters to empty sessions."""
        member = self.get_member("EmptySessions")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EmptySessionFilter(member.value)
        return None

    @empty_sessions.setter
    def empty_sessions(self, value: EmptySessionFilter | str) -> None:
        """Set EmptySessions. How to apply filters to empty sessions."""
        member = self.get_member("EmptySessions")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "EmptySessions",
                members.FieldEnum(value=str(value)),
            )

    @property
    def incompatible_sessions(self) -> primitives.Bool | None:
        """Whether to show incompatible sessions due to game version number/plugins."""
        member = self.get_member("IncompatibleSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @incompatible_sessions.setter
    def incompatible_sessions(self, value: primitives.Bool) -> None:
        """Set the IncompatibleSessions field value."""
        member = self.get_member("IncompatibleSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IncompatibleSessions", fields.FieldBool(value=value)
            )

    @property
    def only_headless_hosts(self) -> primitives.Bool | None:
        """Whether to only Show headless worlds."""
        member = self.get_member("OnlyHeadlessHosts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @only_headless_hosts.setter
    def only_headless_hosts(self, value: primitives.Bool) -> None:
        """Set the OnlyHeadlessHosts field value."""
        member = self.get_member("OnlyHeadlessHosts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnlyHeadlessHosts", fields.FieldBool(value=value)
            )

    @property
    def minimum_total_users(self) -> primitives.Int | None:
        """The minimum amount of users in order for it to show up in the list."""
        member = self.get_member("MinimumTotalUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_total_users.setter
    def minimum_total_users(self, value: primitives.Int) -> None:
        """Set the MinimumTotalUsers field value."""
        member = self.get_member("MinimumTotalUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTotalUsers", fields.FieldInt(value=value)
            )

    @property
    def minimum_total_contacts(self) -> primitives.Int | None:
        """The maximum amount of users allowed for it to show up in the list."""
        member = self.get_member("MinimumTotalContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_total_contacts.setter
    def minimum_total_contacts(self, value: primitives.Int) -> None:
        """Set the MinimumTotalContacts field value."""
        member = self.get_member("MinimumTotalContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTotalContacts", fields.FieldInt(value=value)
            )

    @property
    def min_session_access_level(self) -> SessionAccessLevel | None:
        """The minimum session access level allowed for an item to show up in the list."""
        member = self.get_member("MinSessionAccessLevel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SessionAccessLevel(member.value)
        return None

    @min_session_access_level.setter
    def min_session_access_level(self, value: SessionAccessLevel | str) -> None:
        """Set MinSessionAccessLevel. The minimum session access level allowed for an item to show up in the list."""
        member = self.get_member("MinSessionAccessLevel")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MinSessionAccessLevel",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_session_access_level(self) -> SessionAccessLevel | None:
        """The maximum session access level allowed for an item to show up in the list."""
        member = self.get_member("MaxSessionAccessLevel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SessionAccessLevel(member.value)
        return None

    @max_session_access_level.setter
    def max_session_access_level(self, value: SessionAccessLevel | str) -> None:
        """Set MaxSessionAccessLevel. The maximum session access level allowed for an item to show up in the list."""
        member = self.get_member("MaxSessionAccessLevel")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MaxSessionAccessLevel",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_uptime(self) -> primitives.Double | None:
        """The minimum session access time allowed for an item to show up in the list."""
        member = self.get_member("MinUptime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_uptime.setter
    def min_uptime(self, value: primitives.Double) -> None:
        """Set the MinUptime field value."""
        member = self.get_member("MinUptime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinUptime", fields.FieldDouble(value=value)
            )

    @property
    def max_uptime(self) -> primitives.Double | None:
        """The maximum session access time allowed for an item in the list."""
        member = self.get_member("MaxUptime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_uptime.setter
    def max_uptime(self, value: primitives.Double) -> None:
        """Set the MaxUptime field value."""
        member = self.get_member("MaxUptime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxUptime", fields.FieldDouble(value=value)
            )

    @property
    def parent_session_id(self) -> primitives.String | None:
        """The ID of the session for the user login."""
        member = self.get_member("ParentSessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_session_id.setter
    def parent_session_id(self, value: primitives.String) -> None:
        """Set the ParentSessionId field value."""
        member = self.get_member("ParentSessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentSessionId", fields.FieldString(value=value)
            )

    @property
    def visited(self) -> primitives.Bool | None:
        """Whether worlds should be shown if they are either visited or not visited."""
        member = self.get_member("Visited")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visited.setter
    def visited(self, value: primitives.Bool) -> None:
        """Set the Visited field value."""
        member = self.get_member("Visited")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Visited", fields.FieldNullableBool(value=value)
            )

    @property
    def sort_properties(self) -> members.SyncList | None:
        """A list of sorting rules for the list of displayed items."""
        member = self.get_member("SortProperties")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sort_properties.setter
    def sort_properties(self, value: members.SyncList) -> None:
        """Set SortProperties. A list of sorting rules for the list of displayed items."""
        self.set_member("SortProperties", value)

    @property
    def is_searching(self) -> primitives.Bool | None:
        """Whether the component is currently doing a search."""
        member = self.get_member("IsSearching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_searching.setter
    def is_searching(self, value: primitives.Bool) -> None:
        """Set the IsSearching field value."""
        member = self.get_member("IsSearching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSearching", fields.FieldBool(value=value)
            )

    @property
    def has_more_results(self) -> primitives.Bool | None:
        """Whether there is more results on other pages."""
        member = self.get_member("HasMoreResults")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_more_results.setter
    def has_more_results(self, value: primitives.Bool) -> None:
        """Set the HasMoreResults field value."""
        member = self.get_member("HasMoreResults")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasMoreResults", fields.FieldBool(value=value)
            )

    @property
    def total_results(self) -> primitives.Int | None:
        """The total results before filtering."""
        member = self.get_member("TotalResults")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_results.setter
    def total_results(self, value: primitives.Int) -> None:
        """Set the TotalResults field value."""
        member = self.get_member("TotalResults")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalResults", fields.FieldInt(value=value)
            )

    @property
    def filtered_results(self) -> primitives.Int | None:
        """How many results appeared after filtering."""
        member = self.get_member("FilteredResults")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filtered_results.setter
    def filtered_results(self, value: primitives.Int) -> None:
        """Set the FilteredResults field value."""
        member = self.get_member("FilteredResults")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FilteredResults", fields.FieldInt(value=value)
            )

