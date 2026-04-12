"""Generated component: WorldsDataFeed."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.session_access_level import SessionAccessLevel
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldsDataFeed(GeneratedComponent, IDataFeedComponent, IComponent, IWorldEventReceiver):
    """The WorldsDataFeed is a data feed that provides a list of worlds or sessions, depending on the settings.

    Category: Radiant UI/Data Feeds/Feeds

    Used in the system of Data Feeds. This feed provides
    MergedWorldDataItemInterface as well as DataFeedEntity and
    DataFeedEntity as part of its feed.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldsDataFeed"

    def __init__(self, list_opened_worlds: primitives.Bool | None = None, list_sessions: primitives.Bool | None = None, merge_by_world_id: primitives.Bool | None = None, merge_by_session_id: primitives.Bool | None = None, incompatible_sessions: primitives.Bool | None = None, headless_hosts: primitives.Bool | None = None, user_hosts: primitives.Bool | None = None, minimum_total_users: primitives.Int | None = None, minimum_total_contacts: primitives.Int | None = None, min_session_access_level: SessionAccessLevel | str | None = None, max_session_access_level: SessionAccessLevel | str | None = None, min_uptime: primitives.Double | None = None, max_uptime: primitives.Double | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            list_opened_worlds: Initial value for ListOpenedWorlds.
            list_sessions: Initial value for ListSessions.
            merge_by_world_id: Initial value for MergeByWorldId.
            merge_by_session_id: Initial value for MergeBySessionId.
            incompatible_sessions: Initial value for IncompatibleSessions.
            headless_hosts: Initial value for HeadlessHosts.
            user_hosts: Initial value for UserHosts.
            minimum_total_users: Initial value for MinimumTotalUsers.
            minimum_total_contacts: Initial value for MinimumTotalContacts.
            min_session_access_level: Initial value for MinSessionAccessLevel.
            max_session_access_level: Initial value for MaxSessionAccessLevel.
            min_uptime: Initial value for MinUptime.
            max_uptime: Initial value for MaxUptime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if list_opened_worlds is not None:
            self.list_opened_worlds = list_opened_worlds
        if list_sessions is not None:
            self.list_sessions = list_sessions
        if merge_by_world_id is not None:
            self.merge_by_world_id = merge_by_world_id
        if merge_by_session_id is not None:
            self.merge_by_session_id = merge_by_session_id
        if incompatible_sessions is not None:
            self.incompatible_sessions = incompatible_sessions
        if headless_hosts is not None:
            self.headless_hosts = headless_hosts
        if user_hosts is not None:
            self.user_hosts = user_hosts
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

    @property
    def list_opened_worlds(self) -> primitives.Bool | None:
        """Whether to list open worlds."""
        member = self.get_member("ListOpenedWorlds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @list_opened_worlds.setter
    def list_opened_worlds(self, value: primitives.Bool) -> None:
        """Set the ListOpenedWorlds field value."""
        member = self.get_member("ListOpenedWorlds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ListOpenedWorlds", fields.FieldBool(value=value)
            )

    @property
    def list_sessions(self) -> primitives.Bool | None:
        """Whether to list sessions of worlds."""
        member = self.get_member("ListSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @list_sessions.setter
    def list_sessions(self, value: primitives.Bool) -> None:
        """Set the ListSessions field value."""
        member = self.get_member("ListSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ListSessions", fields.FieldBool(value=value)
            )

    @property
    def merge_by_world_id(self) -> primitives.Bool | None:
        """Whether to merge by world IDs. Used to make Component:MergedWorldDataItemInterface."""
        member = self.get_member("MergeByWorldId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @merge_by_world_id.setter
    def merge_by_world_id(self, value: primitives.Bool) -> None:
        """Set the MergeByWorldId field value."""
        member = self.get_member("MergeByWorldId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MergeByWorldId", fields.FieldBool(value=value)
            )

    @property
    def merge_by_session_id(self) -> primitives.Bool | None:
        """Whether to merge by session IDs. Used to make Component:MergedWorldDataItemInterface"""
        member = self.get_member("MergeBySessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @merge_by_session_id.setter
    def merge_by_session_id(self, value: primitives.Bool) -> None:
        """Set the MergeBySessionId field value."""
        member = self.get_member("MergeBySessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MergeBySessionId", fields.FieldBool(value=value)
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
    def headless_hosts(self) -> primitives.Bool | None:
        """Whether to list headless hosts."""
        member = self.get_member("HeadlessHosts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @headless_hosts.setter
    def headless_hosts(self, value: primitives.Bool) -> None:
        """Set the HeadlessHosts field value."""
        member = self.get_member("HeadlessHosts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadlessHosts", fields.FieldBool(value=value)
            )

    @property
    def user_hosts(self) -> primitives.Bool | None:
        """Whether to list normal user hosts."""
        member = self.get_member("UserHosts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_hosts.setter
    def user_hosts(self, value: primitives.Bool) -> None:
        """Set the UserHosts field value."""
        member = self.get_member("UserHosts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHosts", fields.FieldBool(value=value)
            )

    @property
    def minimum_total_users(self) -> primitives.Int | None:
        """List sessions that have more than this many users."""
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
        """List sessions that have more than this many users that are contacts to the user."""
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
        """List sessions that have a session access greater or equal to this."""
        member = self.get_member("MinSessionAccessLevel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SessionAccessLevel(member.value)
        return None

    @min_session_access_level.setter
    def min_session_access_level(self, value: SessionAccessLevel | str) -> None:
        """Set MinSessionAccessLevel. List sessions that have a session access greater or equal to this."""
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
        """List sessions that have a session access less than or equal to this."""
        member = self.get_member("MaxSessionAccessLevel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SessionAccessLevel(member.value)
        return None

    @max_session_access_level.setter
    def max_session_access_level(self, value: SessionAccessLevel | str) -> None:
        """Set MaxSessionAccessLevel. List sessions that have a session access less than or equal to this."""
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
        """A session has to be open for at least this long to be listed."""
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
        """A session has to be open for less than this long to be listed."""
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

