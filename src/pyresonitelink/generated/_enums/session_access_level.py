"""Generated enum: SessionAccessLevel."""

from enum import StrEnum


class SessionAccessLevel(StrEnum):
    """Enum: [SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel."""

    private = "Private"
    lan = "LAN"
    contacts = "Contacts"
    friends = "Friends"
    contacts_plus = "ContactsPlus"
    friends_of_friends = "FriendsOfFriends"
    registered_users = "RegisteredUsers"
    anyone = "Anyone"

