"""Generated component: SessionInfoSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_link import IWorldLink
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionInfoSource(GeneratedComponent, IWorldLink, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SessionInfoSource.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionInfoSource"

    def __init__(self, session_id: primitives.String | None = None, is_open: primitives.Bool | None = None, last_updated: str | None = None, name: primitives.String | None = None, description: primitives.String | None = None, corresponding_record_id: primitives.String | None = None, corresponding_owner_id: primitives.String | None = None, host_user_id: primitives.String | None = None, host_username: primitives.String | None = None, sanitized_host_username: primitives.String | None = None, app_version: primitives.String | None = None, headless_host: primitives.Bool | None = None, thumbnail: primitives.String | None = None, joined_users: primitives.Int | None = None, active_users: primitives.Int | None = None, total_joined_users: primitives.Int | None = None, total_active_users: primitives.Int | None = None, maximum_users: primitives.Int | None = None, mobile_friendly: primitives.Bool | None = None, is_on_lan: primitives.Bool | None = None, away_kick_enabled: primitives.Bool | None = None, away_kick_interval: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            session_id: Initial value for SessionId.
            is_open: Initial value for IsOpen.
            last_updated: Initial value for LastUpdated.
            name: Initial value for Name.
            description: Initial value for Description.
            corresponding_record_id: Initial value for CorrespondingRecordId.
            corresponding_owner_id: Initial value for CorrespondingOwnerId.
            host_user_id: Initial value for HostUserId.
            host_username: Initial value for HostUsername.
            sanitized_host_username: Initial value for SanitizedHostUsername.
            app_version: Initial value for AppVersion.
            headless_host: Initial value for HeadlessHost.
            thumbnail: Initial value for Thumbnail.
            joined_users: Initial value for JoinedUsers.
            active_users: Initial value for ActiveUsers.
            total_joined_users: Initial value for TotalJoinedUsers.
            total_active_users: Initial value for TotalActiveUsers.
            maximum_users: Initial value for MaximumUsers.
            mobile_friendly: Initial value for MobileFriendly.
            is_on_lan: Initial value for IsOnLAN.
            away_kick_enabled: Initial value for AwayKickEnabled.
            away_kick_interval: Initial value for AwayKickInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if session_id is not None:
            self.session_id = session_id
        if is_open is not None:
            self.is_open = is_open
        if last_updated is not None:
            self.last_updated = last_updated
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if corresponding_record_id is not None:
            self.corresponding_record_id = corresponding_record_id
        if corresponding_owner_id is not None:
            self.corresponding_owner_id = corresponding_owner_id
        if host_user_id is not None:
            self.host_user_id = host_user_id
        if host_username is not None:
            self.host_username = host_username
        if sanitized_host_username is not None:
            self.sanitized_host_username = sanitized_host_username
        if app_version is not None:
            self.app_version = app_version
        if headless_host is not None:
            self.headless_host = headless_host
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if joined_users is not None:
            self.joined_users = joined_users
        if active_users is not None:
            self.active_users = active_users
        if total_joined_users is not None:
            self.total_joined_users = total_joined_users
        if total_active_users is not None:
            self.total_active_users = total_active_users
        if maximum_users is not None:
            self.maximum_users = maximum_users
        if mobile_friendly is not None:
            self.mobile_friendly = mobile_friendly
        if is_on_lan is not None:
            self.is_on_lan = is_on_lan
        if away_kick_enabled is not None:
            self.away_kick_enabled = away_kick_enabled
        if away_kick_interval is not None:
            self.away_kick_interval = away_kick_interval

    @property
    def session_id(self) -> primitives.String | None:
        """The SessionId field value."""
        member = self.get_member("SessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @session_id.setter
    def session_id(self, value: primitives.String) -> None:
        """Set the SessionId field value."""
        member = self.get_member("SessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SessionId", fields.FieldString(value=value)
            )

    @property
    def is_open(self) -> primitives.Bool | None:
        """The IsOpen field value."""
        member = self.get_member("IsOpen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_open.setter
    def is_open(self, value: primitives.Bool) -> None:
        """Set the IsOpen field value."""
        member = self.get_member("IsOpen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsOpen", fields.FieldBool(value=value)
            )

    @property
    def last_updated(self) -> str | None:
        """The LastUpdated field value."""
        member = self.get_member("LastUpdated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_updated.setter
    def last_updated(self, value: str) -> None:
        """Set the LastUpdated field value."""
        member = self.get_member("LastUpdated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastUpdated", fields.FieldDateTime(value=value)
            )

    @property
    def name(self) -> primitives.String | None:
        """The Name field value."""
        member = self.get_member("Name")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name.setter
    def name(self, value: primitives.String) -> None:
        """Set the Name field value."""
        member = self.get_member("Name")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Name", fields.FieldString(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The Description field value."""
        member = self.get_member("Description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the Description field value."""
        member = self.get_member("Description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Description", fields.FieldString(value=value)
            )

    @property
    def tags(self) -> members.SyncList | None:
        """The Tags member."""
        member = self.get_member("Tags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tags.setter
    def tags(self, value: members.SyncList) -> None:
        """Set the Tags member."""
        self.set_member("Tags", value)

    @property
    def corresponding_record_id(self) -> primitives.String | None:
        """The CorrespondingRecordId field value."""
        member = self.get_member("CorrespondingRecordId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @corresponding_record_id.setter
    def corresponding_record_id(self, value: primitives.String) -> None:
        """Set the CorrespondingRecordId field value."""
        member = self.get_member("CorrespondingRecordId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CorrespondingRecordId", fields.FieldString(value=value)
            )

    @property
    def corresponding_owner_id(self) -> primitives.String | None:
        """The CorrespondingOwnerId field value."""
        member = self.get_member("CorrespondingOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @corresponding_owner_id.setter
    def corresponding_owner_id(self, value: primitives.String) -> None:
        """Set the CorrespondingOwnerId field value."""
        member = self.get_member("CorrespondingOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CorrespondingOwnerId", fields.FieldString(value=value)
            )

    @property
    def host_user_id(self) -> primitives.String | None:
        """The HostUserId field value."""
        member = self.get_member("HostUserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @host_user_id.setter
    def host_user_id(self, value: primitives.String) -> None:
        """Set the HostUserId field value."""
        member = self.get_member("HostUserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HostUserId", fields.FieldString(value=value)
            )

    @property
    def host_username(self) -> primitives.String | None:
        """The HostUsername field value."""
        member = self.get_member("HostUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @host_username.setter
    def host_username(self, value: primitives.String) -> None:
        """Set the HostUsername field value."""
        member = self.get_member("HostUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HostUsername", fields.FieldString(value=value)
            )

    @property
    def sanitized_host_username(self) -> primitives.String | None:
        """The SanitizedHostUsername field value."""
        member = self.get_member("SanitizedHostUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sanitized_host_username.setter
    def sanitized_host_username(self, value: primitives.String) -> None:
        """Set the SanitizedHostUsername field value."""
        member = self.get_member("SanitizedHostUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SanitizedHostUsername", fields.FieldString(value=value)
            )

    @property
    def app_version(self) -> primitives.String | None:
        """The AppVersion field value."""
        member = self.get_member("AppVersion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @app_version.setter
    def app_version(self, value: primitives.String) -> None:
        """Set the AppVersion field value."""
        member = self.get_member("AppVersion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppVersion", fields.FieldString(value=value)
            )

    @property
    def headless_host(self) -> primitives.Bool | None:
        """The HeadlessHost field value."""
        member = self.get_member("HeadlessHost")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @headless_host.setter
    def headless_host(self, value: primitives.Bool) -> None:
        """Set the HeadlessHost field value."""
        member = self.get_member("HeadlessHost")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadlessHost", fields.FieldBool(value=value)
            )

    @property
    def session_urls(self) -> members.SyncList | None:
        """The SessionURLs member."""
        member = self.get_member("SessionURLs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @session_urls.setter
    def session_urls(self, value: members.SyncList) -> None:
        """Set the SessionURLs member."""
        self.set_member("SessionURLs", value)

    @property
    def thumbnail(self) -> primitives.String | None:
        """The Thumbnail field value."""
        member = self.get_member("Thumbnail")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thumbnail.setter
    def thumbnail(self, value: primitives.String) -> None:
        """Set the Thumbnail field value."""
        member = self.get_member("Thumbnail")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thumbnail", fields.FieldString(value=value)
            )

    @property
    def joined_users(self) -> primitives.Int | None:
        """The JoinedUsers field value."""
        member = self.get_member("JoinedUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @joined_users.setter
    def joined_users(self, value: primitives.Int) -> None:
        """Set the JoinedUsers field value."""
        member = self.get_member("JoinedUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "JoinedUsers", fields.FieldInt(value=value)
            )

    @property
    def active_users(self) -> primitives.Int | None:
        """The ActiveUsers field value."""
        member = self.get_member("ActiveUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_users.setter
    def active_users(self, value: primitives.Int) -> None:
        """Set the ActiveUsers field value."""
        member = self.get_member("ActiveUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUsers", fields.FieldInt(value=value)
            )

    @property
    def total_joined_users(self) -> primitives.Int | None:
        """The TotalJoinedUsers field value."""
        member = self.get_member("TotalJoinedUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_joined_users.setter
    def total_joined_users(self, value: primitives.Int) -> None:
        """Set the TotalJoinedUsers field value."""
        member = self.get_member("TotalJoinedUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalJoinedUsers", fields.FieldInt(value=value)
            )

    @property
    def total_active_users(self) -> primitives.Int | None:
        """The TotalActiveUsers field value."""
        member = self.get_member("TotalActiveUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_active_users.setter
    def total_active_users(self, value: primitives.Int) -> None:
        """Set the TotalActiveUsers field value."""
        member = self.get_member("TotalActiveUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalActiveUsers", fields.FieldInt(value=value)
            )

    @property
    def maximum_users(self) -> primitives.Int | None:
        """The MaximumUsers field value."""
        member = self.get_member("MaximumUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_users.setter
    def maximum_users(self, value: primitives.Int) -> None:
        """Set the MaximumUsers field value."""
        member = self.get_member("MaximumUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumUsers", fields.FieldInt(value=value)
            )

    @property
    def mobile_friendly(self) -> primitives.Bool | None:
        """The MobileFriendly field value."""
        member = self.get_member("MobileFriendly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mobile_friendly.setter
    def mobile_friendly(self, value: primitives.Bool) -> None:
        """Set the MobileFriendly field value."""
        member = self.get_member("MobileFriendly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MobileFriendly", fields.FieldBool(value=value)
            )

    @property
    def access_level(self) -> members.FieldEnum | None:
        """The AccessLevel member."""
        member = self.get_member("AccessLevel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @access_level.setter
    def access_level(self, value: members.FieldEnum) -> None:
        """Set the AccessLevel member."""
        self.set_member("AccessLevel", value)

    @property
    def is_on_lan(self) -> primitives.Bool | None:
        """The IsOnLAN field value."""
        member = self.get_member("IsOnLAN")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_on_lan.setter
    def is_on_lan(self, value: primitives.Bool) -> None:
        """Set the IsOnLAN field value."""
        member = self.get_member("IsOnLAN")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsOnLAN", fields.FieldBool(value=value)
            )

    @property
    def away_kick_enabled(self) -> primitives.Bool | None:
        """The AwayKickEnabled field value."""
        member = self.get_member("AwayKickEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @away_kick_enabled.setter
    def away_kick_enabled(self, value: primitives.Bool) -> None:
        """Set the AwayKickEnabled field value."""
        member = self.get_member("AwayKickEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AwayKickEnabled", fields.FieldBool(value=value)
            )

    @property
    def away_kick_interval(self) -> str | None:
        """The AwayKickInterval field value."""
        member = self.get_member("AwayKickInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @away_kick_interval.setter
    def away_kick_interval(self, value: str) -> None:
        """Set the AwayKickInterval field value."""
        member = self.get_member("AwayKickInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AwayKickInterval", fields.FieldTimeSpan(value=value)
            )

