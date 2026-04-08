"""Generated component: LegacyWorldItem."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyWorldItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyWorldItem.

    Category: Radiant UI/World Browsing/Legacy
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyWorldItem"

    def __init__(self, world_or_session_id: str | None = None, visited: bool | None = None, total_active_users: np.int32 | None = None, total_contacts: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_or_session_id: Initial value for WorldOrSessionId.
            visited: Initial value for _visited.
            total_active_users: Initial value for _totalActiveUsers.
            total_contacts: Initial value for _totalContacts.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_or_session_id is not None:
            self.world_or_session_id = world_or_session_id
        if visited is not None:
            self.visited = visited
        if total_active_users is not None:
            self.total_active_users = total_active_users
        if total_contacts is not None:
            self.total_contacts = total_contacts

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
    def world_or_session_id(self) -> str | None:
        """The WorldOrSessionId field value."""
        member = self.get_member("WorldOrSessionId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @world_or_session_id.setter
    def world_or_session_id(self, value: str) -> None:
        """Set the WorldOrSessionId field value."""
        member = self.get_member("WorldOrSessionId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldOrSessionId", fields.FieldString(value=value)
            )

    @property
    def visited(self) -> bool | None:
        """The _visited field value."""
        member = self.get_member("_visited")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visited.setter
    def visited(self, value: bool) -> None:
        """Set the _visited field value."""
        member = self.get_member("_visited")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_visited", fields.FieldBool(value=value)
            )

    @property
    def total_active_users(self) -> np.int32 | None:
        """The _totalActiveUsers field value."""
        member = self.get_member("_totalActiveUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_active_users.setter
    def total_active_users(self, value: np.int32) -> None:
        """Set the _totalActiveUsers field value."""
        member = self.get_member("_totalActiveUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_totalActiveUsers", fields.FieldInt(value=value)
            )

    @property
    def total_contacts(self) -> np.int32 | None:
        """The _totalContacts field value."""
        member = self.get_member("_totalContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_contacts.setter
    def total_contacts(self, value: np.int32) -> None:
        """Set the _totalContacts field value."""
        member = self.get_member("_totalContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_totalContacts", fields.FieldInt(value=value)
            )

