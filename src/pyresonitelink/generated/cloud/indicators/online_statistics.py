"""Generated component: OnlineStatistics."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnlineStatistics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.OnlineStatistics.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OnlineStatistics"

    def __init__(self, timestamp: str | None = None, registered_online_users: np.int32 | None = None, total_online_users: np.int32 | None = None, present_users: np.int32 | None = None, away_users: np.int32 | None = None, users_in_vr: np.int32 | None = None, users_in_screen: np.int32 | None = None, users_on_desktop: np.int32 | None = None, users_on_mobile: np.int32 | None = None, users_in_visible_public_sessions: np.int32 | None = None, users_in_visible_semi_accessible_sessions: np.int32 | None = None, users_in_hidden_sessions: np.int32 | None = None, users_in_private_sessions: np.int32 | None = None, users_in_private: np.int32 | None = None, users_in_lan: np.int32 | None = None, users_in_contacts: np.int32 | None = None, users_in_contacts_plus: np.int32 | None = None, users_in_registered: np.int32 | None = None, users_in_public: np.int32 | None = None, graphical_client_users: np.int32 | None = None, chat_client_users: np.int32 | None = None, headless_users: np.int32 | None = None, bot_users: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            timestamp: Initial value for Timestamp.
            registered_online_users: Initial value for RegisteredOnlineUsers.
            total_online_users: Initial value for TotalOnlineUsers.
            present_users: Initial value for PresentUsers.
            away_users: Initial value for AwayUsers.
            users_in_vr: Initial value for UsersInVR.
            users_in_screen: Initial value for UsersInScreen.
            users_on_desktop: Initial value for UsersOnDesktop.
            users_on_mobile: Initial value for UsersOnMobile.
            users_in_visible_public_sessions: Initial value for UsersInVisiblePublicSessions.
            users_in_visible_semi_accessible_sessions: Initial value for UsersInVisibleSemiAccessibleSessions.
            users_in_hidden_sessions: Initial value for UsersInHiddenSessions.
            users_in_private_sessions: Initial value for UsersInPrivateSessions.
            users_in_private: Initial value for UsersInPrivate.
            users_in_lan: Initial value for UsersInLAN.
            users_in_contacts: Initial value for UsersInContacts.
            users_in_contacts_plus: Initial value for UsersInContactsPlus.
            users_in_registered: Initial value for UsersInRegistered.
            users_in_public: Initial value for UsersInPublic.
            graphical_client_users: Initial value for GraphicalClientUsers.
            chat_client_users: Initial value for ChatClientUsers.
            headless_users: Initial value for HeadlessUsers.
            bot_users: Initial value for BotUsers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if timestamp is not None:
            self.timestamp = timestamp
        if registered_online_users is not None:
            self.registered_online_users = registered_online_users
        if total_online_users is not None:
            self.total_online_users = total_online_users
        if present_users is not None:
            self.present_users = present_users
        if away_users is not None:
            self.away_users = away_users
        if users_in_vr is not None:
            self.users_in_vr = users_in_vr
        if users_in_screen is not None:
            self.users_in_screen = users_in_screen
        if users_on_desktop is not None:
            self.users_on_desktop = users_on_desktop
        if users_on_mobile is not None:
            self.users_on_mobile = users_on_mobile
        if users_in_visible_public_sessions is not None:
            self.users_in_visible_public_sessions = users_in_visible_public_sessions
        if users_in_visible_semi_accessible_sessions is not None:
            self.users_in_visible_semi_accessible_sessions = users_in_visible_semi_accessible_sessions
        if users_in_hidden_sessions is not None:
            self.users_in_hidden_sessions = users_in_hidden_sessions
        if users_in_private_sessions is not None:
            self.users_in_private_sessions = users_in_private_sessions
        if users_in_private is not None:
            self.users_in_private = users_in_private
        if users_in_lan is not None:
            self.users_in_lan = users_in_lan
        if users_in_contacts is not None:
            self.users_in_contacts = users_in_contacts
        if users_in_contacts_plus is not None:
            self.users_in_contacts_plus = users_in_contacts_plus
        if users_in_registered is not None:
            self.users_in_registered = users_in_registered
        if users_in_public is not None:
            self.users_in_public = users_in_public
        if graphical_client_users is not None:
            self.graphical_client_users = graphical_client_users
        if chat_client_users is not None:
            self.chat_client_users = chat_client_users
        if headless_users is not None:
            self.headless_users = headless_users
        if bot_users is not None:
            self.bot_users = bot_users

    @property
    def timestamp(self) -> str | None:
        """The Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timestamp.setter
    def timestamp(self, value: str) -> None:
        """Set the Timestamp field value."""
        member = self.get_member("Timestamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Timestamp", fields.FieldDateTime(value=value)
            )

    @property
    def visible_sessions(self) -> members.SyncObject | None:
        """The VisibleSessions member."""
        member = self.get_member("VisibleSessions")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @visible_sessions.setter
    def visible_sessions(self, value: members.SyncObject) -> None:
        """Set the VisibleSessions member."""
        self.set_member("VisibleSessions", value)

    @property
    def hidden_sessions(self) -> members.SyncObject | None:
        """The HiddenSessions member."""
        member = self.get_member("HiddenSessions")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hidden_sessions.setter
    def hidden_sessions(self, value: members.SyncObject) -> None:
        """Set the HiddenSessions member."""
        self.set_member("HiddenSessions", value)

    @property
    def active_visible_sessions(self) -> members.SyncObject | None:
        """The ActiveVisibleSessions member."""
        member = self.get_member("ActiveVisibleSessions")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @active_visible_sessions.setter
    def active_visible_sessions(self, value: members.SyncObject) -> None:
        """Set the ActiveVisibleSessions member."""
        self.set_member("ActiveVisibleSessions", value)

    @property
    def active_hidden_sessions(self) -> members.SyncObject | None:
        """The ActiveHiddenSessions member."""
        member = self.get_member("ActiveHiddenSessions")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @active_hidden_sessions.setter
    def active_hidden_sessions(self, value: members.SyncObject) -> None:
        """Set the ActiveHiddenSessions member."""
        self.set_member("ActiveHiddenSessions", value)

    @property
    def registered_online_users(self) -> np.int32 | None:
        """The RegisteredOnlineUsers field value."""
        member = self.get_member("RegisteredOnlineUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @registered_online_users.setter
    def registered_online_users(self, value: np.int32) -> None:
        """Set the RegisteredOnlineUsers field value."""
        member = self.get_member("RegisteredOnlineUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RegisteredOnlineUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def total_online_users(self) -> np.int32 | None:
        """The TotalOnlineUsers field value."""
        member = self.get_member("TotalOnlineUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_online_users.setter
    def total_online_users(self, value: np.int32) -> None:
        """Set the TotalOnlineUsers field value."""
        member = self.get_member("TotalOnlineUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalOnlineUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def present_users(self) -> np.int32 | None:
        """The PresentUsers field value."""
        member = self.get_member("PresentUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @present_users.setter
    def present_users(self, value: np.int32) -> None:
        """Set the PresentUsers field value."""
        member = self.get_member("PresentUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PresentUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def away_users(self) -> np.int32 | None:
        """The AwayUsers field value."""
        member = self.get_member("AwayUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @away_users.setter
    def away_users(self, value: np.int32) -> None:
        """Set the AwayUsers field value."""
        member = self.get_member("AwayUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AwayUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_vr(self) -> np.int32 | None:
        """The UsersInVR field value."""
        member = self.get_member("UsersInVR")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_vr.setter
    def users_in_vr(self, value: np.int32) -> None:
        """Set the UsersInVR field value."""
        member = self.get_member("UsersInVR")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInVR", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_screen(self) -> np.int32 | None:
        """The UsersInScreen field value."""
        member = self.get_member("UsersInScreen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_screen.setter
    def users_in_screen(self, value: np.int32) -> None:
        """Set the UsersInScreen field value."""
        member = self.get_member("UsersInScreen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInScreen", fields.FieldNullableInt(value=value)
            )

    @property
    def users_on_desktop(self) -> np.int32 | None:
        """The UsersOnDesktop field value."""
        member = self.get_member("UsersOnDesktop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_on_desktop.setter
    def users_on_desktop(self, value: np.int32) -> None:
        """Set the UsersOnDesktop field value."""
        member = self.get_member("UsersOnDesktop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersOnDesktop", fields.FieldNullableInt(value=value)
            )

    @property
    def users_on_mobile(self) -> np.int32 | None:
        """The UsersOnMobile field value."""
        member = self.get_member("UsersOnMobile")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_on_mobile.setter
    def users_on_mobile(self, value: np.int32) -> None:
        """Set the UsersOnMobile field value."""
        member = self.get_member("UsersOnMobile")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersOnMobile", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_visible_public_sessions(self) -> np.int32 | None:
        """The UsersInVisiblePublicSessions field value."""
        member = self.get_member("UsersInVisiblePublicSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_visible_public_sessions.setter
    def users_in_visible_public_sessions(self, value: np.int32) -> None:
        """Set the UsersInVisiblePublicSessions field value."""
        member = self.get_member("UsersInVisiblePublicSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInVisiblePublicSessions", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_visible_semi_accessible_sessions(self) -> np.int32 | None:
        """The UsersInVisibleSemiAccessibleSessions field value."""
        member = self.get_member("UsersInVisibleSemiAccessibleSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_visible_semi_accessible_sessions.setter
    def users_in_visible_semi_accessible_sessions(self, value: np.int32) -> None:
        """Set the UsersInVisibleSemiAccessibleSessions field value."""
        member = self.get_member("UsersInVisibleSemiAccessibleSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInVisibleSemiAccessibleSessions", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_hidden_sessions(self) -> np.int32 | None:
        """The UsersInHiddenSessions field value."""
        member = self.get_member("UsersInHiddenSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_hidden_sessions.setter
    def users_in_hidden_sessions(self, value: np.int32) -> None:
        """Set the UsersInHiddenSessions field value."""
        member = self.get_member("UsersInHiddenSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInHiddenSessions", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_private_sessions(self) -> np.int32 | None:
        """The UsersInPrivateSessions field value."""
        member = self.get_member("UsersInPrivateSessions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_private_sessions.setter
    def users_in_private_sessions(self, value: np.int32) -> None:
        """Set the UsersInPrivateSessions field value."""
        member = self.get_member("UsersInPrivateSessions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInPrivateSessions", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_private(self) -> np.int32 | None:
        """The UsersInPrivate field value."""
        member = self.get_member("UsersInPrivate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_private.setter
    def users_in_private(self, value: np.int32) -> None:
        """Set the UsersInPrivate field value."""
        member = self.get_member("UsersInPrivate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInPrivate", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_lan(self) -> np.int32 | None:
        """The UsersInLAN field value."""
        member = self.get_member("UsersInLAN")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_lan.setter
    def users_in_lan(self, value: np.int32) -> None:
        """Set the UsersInLAN field value."""
        member = self.get_member("UsersInLAN")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInLAN", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_contacts(self) -> np.int32 | None:
        """The UsersInContacts field value."""
        member = self.get_member("UsersInContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_contacts.setter
    def users_in_contacts(self, value: np.int32) -> None:
        """Set the UsersInContacts field value."""
        member = self.get_member("UsersInContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInContacts", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_contacts_plus(self) -> np.int32 | None:
        """The UsersInContactsPlus field value."""
        member = self.get_member("UsersInContactsPlus")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_contacts_plus.setter
    def users_in_contacts_plus(self, value: np.int32) -> None:
        """Set the UsersInContactsPlus field value."""
        member = self.get_member("UsersInContactsPlus")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInContactsPlus", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_registered(self) -> np.int32 | None:
        """The UsersInRegistered field value."""
        member = self.get_member("UsersInRegistered")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_registered.setter
    def users_in_registered(self, value: np.int32) -> None:
        """Set the UsersInRegistered field value."""
        member = self.get_member("UsersInRegistered")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInRegistered", fields.FieldNullableInt(value=value)
            )

    @property
    def users_in_public(self) -> np.int32 | None:
        """The UsersInPublic field value."""
        member = self.get_member("UsersInPublic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_in_public.setter
    def users_in_public(self, value: np.int32) -> None:
        """Set the UsersInPublic field value."""
        member = self.get_member("UsersInPublic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersInPublic", fields.FieldNullableInt(value=value)
            )

    @property
    def graphical_client_users(self) -> np.int32 | None:
        """The GraphicalClientUsers field value."""
        member = self.get_member("GraphicalClientUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @graphical_client_users.setter
    def graphical_client_users(self, value: np.int32) -> None:
        """Set the GraphicalClientUsers field value."""
        member = self.get_member("GraphicalClientUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GraphicalClientUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def chat_client_users(self) -> np.int32 | None:
        """The ChatClientUsers field value."""
        member = self.get_member("ChatClientUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @chat_client_users.setter
    def chat_client_users(self, value: np.int32) -> None:
        """Set the ChatClientUsers field value."""
        member = self.get_member("ChatClientUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChatClientUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def headless_users(self) -> np.int32 | None:
        """The HeadlessUsers field value."""
        member = self.get_member("HeadlessUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @headless_users.setter
    def headless_users(self, value: np.int32) -> None:
        """Set the HeadlessUsers field value."""
        member = self.get_member("HeadlessUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadlessUsers", fields.FieldNullableInt(value=value)
            )

    @property
    def bot_users(self) -> np.int32 | None:
        """The BotUsers field value."""
        member = self.get_member("BotUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bot_users.setter
    def bot_users(self, value: np.int32) -> None:
        """Set the BotUsers field value."""
        member = self.get_member("BotUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BotUsers", fields.FieldNullableInt(value=value)
            )

