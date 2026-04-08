"""Generated component: FocusedWorldStatus."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FocusedWorldStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FocusedWorldStatus.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FocusedWorldStatus"

    def __init__(self, world_name: str | None = None, raw_world_name: str | None = None, session_id: str | None = None, is_host: bool | None = None, can_save: bool | None = None, should_save: bool | None = None, can_close: bool | None = None, role_name: str | None = None, user_count: np.int32 | None = None, active_user_count: np.int32 | None = None, max_user_count: np.int32 | None = None, hide_from_listing: bool | None = None, away_kick_enabled: bool | None = None, away_kick_minutes: np.float32 | None = None, unsafe_mode: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_name: Initial value for WorldName.
            raw_world_name: Initial value for RawWorldName.
            session_id: Initial value for SessionId.
            is_host: Initial value for IsHost.
            can_save: Initial value for CanSave.
            should_save: Initial value for ShouldSave.
            can_close: Initial value for CanClose.
            role_name: Initial value for RoleName.
            user_count: Initial value for UserCount.
            active_user_count: Initial value for ActiveUserCount.
            max_user_count: Initial value for MaxUserCount.
            hide_from_listing: Initial value for HideFromListing.
            away_kick_enabled: Initial value for AwayKickEnabled.
            away_kick_minutes: Initial value for AwayKickMinutes.
            unsafe_mode: Initial value for UnsafeMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_name is not None:
            self.world_name = world_name
        if raw_world_name is not None:
            self.raw_world_name = raw_world_name
        if session_id is not None:
            self.session_id = session_id
        if is_host is not None:
            self.is_host = is_host
        if can_save is not None:
            self.can_save = can_save
        if should_save is not None:
            self.should_save = should_save
        if can_close is not None:
            self.can_close = can_close
        if role_name is not None:
            self.role_name = role_name
        if user_count is not None:
            self.user_count = user_count
        if active_user_count is not None:
            self.active_user_count = active_user_count
        if max_user_count is not None:
            self.max_user_count = max_user_count
        if hide_from_listing is not None:
            self.hide_from_listing = hide_from_listing
        if away_kick_enabled is not None:
            self.away_kick_enabled = away_kick_enabled
        if away_kick_minutes is not None:
            self.away_kick_minutes = away_kick_minutes
        if unsafe_mode is not None:
            self.unsafe_mode = unsafe_mode

    @property
    def world_name(self) -> str | None:
        """The WorldName field value."""
        member = self.get_member("WorldName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @world_name.setter
    def world_name(self, value: str) -> None:
        """Set the WorldName field value."""
        member = self.get_member("WorldName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldName", fields.FieldString(value=value)
            )

    @property
    def raw_world_name(self) -> str | None:
        """The RawWorldName field value."""
        member = self.get_member("RawWorldName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_world_name.setter
    def raw_world_name(self, value: str) -> None:
        """Set the RawWorldName field value."""
        member = self.get_member("RawWorldName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawWorldName", fields.FieldString(value=value)
            )

    @property
    def session_id(self) -> str | None:
        """The SessionId field value."""
        member = self.get_member("SessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @session_id.setter
    def session_id(self, value: str) -> None:
        """Set the SessionId field value."""
        member = self.get_member("SessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SessionId", fields.FieldString(value=value)
            )

    @property
    def is_host(self) -> bool | None:
        """The IsHost field value."""
        member = self.get_member("IsHost")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_host.setter
    def is_host(self, value: bool) -> None:
        """Set the IsHost field value."""
        member = self.get_member("IsHost")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsHost", fields.FieldBool(value=value)
            )

    @property
    def can_save(self) -> bool | None:
        """The CanSave field value."""
        member = self.get_member("CanSave")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_save.setter
    def can_save(self, value: bool) -> None:
        """Set the CanSave field value."""
        member = self.get_member("CanSave")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanSave", fields.FieldBool(value=value)
            )

    @property
    def should_save(self) -> bool | None:
        """The ShouldSave field value."""
        member = self.get_member("ShouldSave")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @should_save.setter
    def should_save(self, value: bool) -> None:
        """Set the ShouldSave field value."""
        member = self.get_member("ShouldSave")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShouldSave", fields.FieldBool(value=value)
            )

    @property
    def can_close(self) -> bool | None:
        """The CanClose field value."""
        member = self.get_member("CanClose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_close.setter
    def can_close(self, value: bool) -> None:
        """Set the CanClose field value."""
        member = self.get_member("CanClose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanClose", fields.FieldBool(value=value)
            )

    @property
    def role_name(self) -> str | None:
        """The RoleName field value."""
        member = self.get_member("RoleName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @role_name.setter
    def role_name(self, value: str) -> None:
        """Set the RoleName field value."""
        member = self.get_member("RoleName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RoleName", fields.FieldString(value=value)
            )

    @property
    def user_count(self) -> np.int32 | None:
        """The UserCount field value."""
        member = self.get_member("UserCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_count.setter
    def user_count(self, value: np.int32) -> None:
        """Set the UserCount field value."""
        member = self.get_member("UserCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserCount", fields.FieldInt(value=value)
            )

    @property
    def active_user_count(self) -> np.int32 | None:
        """The ActiveUserCount field value."""
        member = self.get_member("ActiveUserCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_user_count.setter
    def active_user_count(self, value: np.int32) -> None:
        """Set the ActiveUserCount field value."""
        member = self.get_member("ActiveUserCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUserCount", fields.FieldInt(value=value)
            )

    @property
    def max_user_count(self) -> np.int32 | None:
        """The MaxUserCount field value."""
        member = self.get_member("MaxUserCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_user_count.setter
    def max_user_count(self, value: np.int32) -> None:
        """Set the MaxUserCount field value."""
        member = self.get_member("MaxUserCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxUserCount", fields.FieldInt(value=value)
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
    def hide_from_listing(self) -> bool | None:
        """The HideFromListing field value."""
        member = self.get_member("HideFromListing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_from_listing.setter
    def hide_from_listing(self, value: bool) -> None:
        """Set the HideFromListing field value."""
        member = self.get_member("HideFromListing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideFromListing", fields.FieldBool(value=value)
            )

    @property
    def away_kick_enabled(self) -> bool | None:
        """The AwayKickEnabled field value."""
        member = self.get_member("AwayKickEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @away_kick_enabled.setter
    def away_kick_enabled(self, value: bool) -> None:
        """Set the AwayKickEnabled field value."""
        member = self.get_member("AwayKickEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AwayKickEnabled", fields.FieldBool(value=value)
            )

    @property
    def away_kick_minutes(self) -> np.float32 | None:
        """The AwayKickMinutes field value."""
        member = self.get_member("AwayKickMinutes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @away_kick_minutes.setter
    def away_kick_minutes(self, value: np.float32) -> None:
        """Set the AwayKickMinutes field value."""
        member = self.get_member("AwayKickMinutes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AwayKickMinutes", fields.FieldFloat(value=value)
            )

    @property
    def unsafe_mode(self) -> bool | None:
        """The UnsafeMode field value."""
        member = self.get_member("UnsafeMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unsafe_mode.setter
    def unsafe_mode(self, value: bool) -> None:
        """Set the UnsafeMode field value."""
        member = self.get_member("UnsafeMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnsafeMode", fields.FieldBool(value=value)
            )

