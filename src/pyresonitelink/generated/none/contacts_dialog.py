"""Generated component: ContactsDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.scroll_rect import ScrollRect
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContactsDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ContactsDialog component is used in the contacts screen of the Dash Menu to search, view, and talk to contacts.

    Not used by the user. Exists as the dash's Contacts tab.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContactsDialog"

    def __init__(self, search_bar: str | TextField | None = None, list_root: str | Slot | None = None, sessions_root: str | Slot | None = None, messages_root: str | Slot | None = None, status: str | Image | None = None, avatar: str | Image | None = None, username: str | Text | None = None, user_actions_root: str | Slot | None = None, send_message_button: str | Button | None = None, send_voice_message_button: str | Button | None = None, send_message_text_field: str | TextField | None = None, messages_scroll_rect: str | ScrollRect | None = None, invite_button: str | Button | None = None, request_invite_button: str | Button | None = None, ban_all_button: str | Button | None = None, ban_session_button: str | Button | None = None, unblocked_button: str | Button | None = None, avatar_block_button: str | Button | None = None, mutual_block_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            search_bar: Initial value for _searchBar.
            list_root: Initial value for _listRoot.
            sessions_root: Initial value for _sessionsRoot.
            messages_root: Initial value for _messagesRoot.
            status: Initial value for _status.
            avatar: Initial value for _avatar.
            username: Initial value for _username.
            user_actions_root: Initial value for _userActionsRoot.
            send_message_button: Initial value for _sendMessageButton.
            send_voice_message_button: Initial value for _sendVoiceMessageButton.
            send_message_text_field: Initial value for _sendMessageTextField.
            messages_scroll_rect: Initial value for _messagesScrollRect.
            invite_button: Initial value for _inviteButton.
            request_invite_button: Initial value for _requestInviteButton.
            ban_all_button: Initial value for _banAllButton.
            ban_session_button: Initial value for _banSessionButton.
            unblocked_button: Initial value for _unblockedButton.
            avatar_block_button: Initial value for _avatarBlockButton.
            mutual_block_button: Initial value for _mutualBlockButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if search_bar is not None:
            self.search_bar = search_bar
        if list_root is not None:
            self.list_root = list_root
        if sessions_root is not None:
            self.sessions_root = sessions_root
        if messages_root is not None:
            self.messages_root = messages_root
        if status is not None:
            self.status = status
        if avatar is not None:
            self.avatar = avatar
        if username is not None:
            self.username = username
        if user_actions_root is not None:
            self.user_actions_root = user_actions_root
        if send_message_button is not None:
            self.send_message_button = send_message_button
        if send_voice_message_button is not None:
            self.send_voice_message_button = send_voice_message_button
        if send_message_text_field is not None:
            self.send_message_text_field = send_message_text_field
        if messages_scroll_rect is not None:
            self.messages_scroll_rect = messages_scroll_rect
        if invite_button is not None:
            self.invite_button = invite_button
        if request_invite_button is not None:
            self.request_invite_button = request_invite_button
        if ban_all_button is not None:
            self.ban_all_button = ban_all_button
        if ban_session_button is not None:
            self.ban_session_button = ban_session_button
        if unblocked_button is not None:
            self.unblocked_button = unblocked_button
        if avatar_block_button is not None:
            self.avatar_block_button = avatar_block_button
        if mutual_block_button is not None:
            self.mutual_block_button = mutual_block_button

    @property
    def search_bar(self) -> str | None:
        """The search bar to search for users."""
        member = self.get_member("_searchBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_bar.setter
    def search_bar(self, target: str | TextField | None) -> None:
        """Set the _searchBar reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_searchBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def list_root(self) -> str | None:
        """The list of contacts."""
        member = self.get_member("_listRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @list_root.setter
    def list_root(self, target: str | Slot | None) -> None:
        """Set the _listRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_listRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_listRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def sessions_root(self) -> str | None:
        """The slot where the list of sessions from the selected user will be."""
        member = self.get_member("_sessionsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sessions_root.setter
    def sessions_root(self, target: str | Slot | None) -> None:
        """Set the _sessionsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_sessionsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sessionsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def messages_root(self) -> str | None:
        """The slot where the list of messages from the selected user will be."""
        member = self.get_member("_messagesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @messages_root.setter
    def messages_root(self, target: str | Slot | None) -> None:
        """Set the _messagesRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_messagesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_messagesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def status(self) -> str | None:
        """The image icon being used for the selected user's status."""
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @status.setter
    def status(self, target: str | Image | None) -> None:
        """Set the _status reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_status")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_status",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def avatar(self) -> str | None:
        """The image icon being used for the selected user's avatar image."""
        member = self.get_member("_avatar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar.setter
    def avatar(self, target: str | Image | None) -> None:
        """Set the _avatar reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_avatar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def username(self) -> str | None:
        """The text for the selected user's username."""
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | Text | None) -> None:
        """Set the _username reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def user_actions_root(self) -> str | None:
        """The root slot to store buttons for performing actions on the selected user."""
        member = self.get_member("_userActionsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_actions_root.setter
    def user_actions_root(self, target: str | Slot | None) -> None:
        """Set the _userActionsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_userActionsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userActionsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def send_message_button(self) -> str | None:
        """The button for sending the currently typed message to the selected user."""
        member = self.get_member("_sendMessageButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @send_message_button.setter
    def send_message_button(self, target: str | Button | None) -> None:
        """Set the _sendMessageButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_sendMessageButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sendMessageButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def send_voice_message_button(self) -> str | None:
        """The button for sending a voice message to the currently selected user."""
        member = self.get_member("_sendVoiceMessageButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @send_voice_message_button.setter
    def send_voice_message_button(self, target: str | Button | None) -> None:
        """Set the _sendVoiceMessageButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_sendVoiceMessageButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sendVoiceMessageButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def send_message_text_field(self) -> str | None:
        """The text field to type messages to send to users."""
        member = self.get_member("_sendMessageTextField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @send_message_text_field.setter
    def send_message_text_field(self, target: str | TextField | None) -> None:
        """Set the _sendMessageTextField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_sendMessageTextField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sendMessageTextField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def messages_scroll_rect(self) -> str | None:
        """The scroll rectangle component for the scroll area for messages to and from the selected user."""
        member = self.get_member("_messagesScrollRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @messages_scroll_rect.setter
    def messages_scroll_rect(self, target: str | ScrollRect | None) -> None:
        """Set the _messagesScrollRect reference by target ID or ScrollRect instance."""
        target_id: str | None = target.id if isinstance(target, ScrollRect) else target  # type: ignore[assignment]
        member = self.get_member("_messagesScrollRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_messagesScrollRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ScrollRect'),
            )

    @property
    def invite_button(self) -> str | None:
        """Invite the selected user to the currently focused session if possible."""
        member = self.get_member("_inviteButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @invite_button.setter
    def invite_button(self, target: str | Button | None) -> None:
        """Set the _inviteButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_inviteButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inviteButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def request_invite_button(self) -> str | None:
        """Ask for an invite from the selected user."""
        member = self.get_member("_requestInviteButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @request_invite_button.setter
    def request_invite_button(self, target: str | Button | None) -> None:
        """Set the _requestInviteButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_requestInviteButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_requestInviteButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def ban_all_button(self) -> str | None:
        """Ban the selected user from all sessions that the current local user will host."""
        member = self.get_member("_banAllButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ban_all_button.setter
    def ban_all_button(self, target: str | Button | None) -> None:
        """Set the _banAllButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_banAllButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_banAllButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def ban_session_button(self) -> str | None:
        """Ban the selected user from the current focused session."""
        member = self.get_member("_banSessionButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ban_session_button.setter
    def ban_session_button(self, target: str | Button | None) -> None:
        """Set the _banSessionButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_banSessionButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_banSessionButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def unblocked_button(self) -> str | None:
        """The button to unblock the currently selected user."""
        member = self.get_member("_unblockedButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unblocked_button.setter
    def unblocked_button(self, target: str | Button | None) -> None:
        """Set the _unblockedButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_unblockedButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unblockedButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def avatar_block_button(self) -> str | None:
        """The button to block the currently selected user's avatar."""
        member = self.get_member("_avatarBlockButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_block_button.setter
    def avatar_block_button(self, target: str | Button | None) -> None:
        """Set the _avatarBlockButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_avatarBlockButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avatarBlockButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def mutual_block_button(self) -> str | None:
        """The button to do a mutual block with the currently selected user."""
        member = self.get_member("_mutualBlockButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mutual_block_button.setter
    def mutual_block_button(self, target: str | Button | None) -> None:
        """Set the _mutualBlockButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_mutualBlockButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mutualBlockButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

