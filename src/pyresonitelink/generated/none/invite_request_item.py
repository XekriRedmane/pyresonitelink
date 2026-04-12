"""Generated component: InviteRequestItem."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.contacts_dialog import ContactsDialog
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InviteRequestItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Invite Request Item component is used to handle the visual and behavior of invite requests received in chats from other users.

    Not used directly by the user, but is used in the contacts screen.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InviteRequestItem"

    def __init__(self, contact_dialog: str | ContactsDialog | None = None, header_text: str | Text | None = None, invite_button: str | Button | None = None, add_contact_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            contact_dialog: Initial value for ContactDialog.
            header_text: Initial value for HeaderText.
            invite_button: Initial value for InviteButton.
            add_contact_button: Initial value for AddContactButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if contact_dialog is not None:
            self.contact_dialog = contact_dialog
        if header_text is not None:
            self.header_text = header_text
        if invite_button is not None:
            self.invite_button = invite_button
        if add_contact_button is not None:
            self.add_contact_button = add_contact_button

    @property
    def contact_dialog(self) -> str | None:
        """The dialog component that this is under."""
        member = self.get_member("ContactDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @contact_dialog.setter
    def contact_dialog(self, target: str | ContactsDialog | None) -> None:
        """Set the ContactDialog reference by target ID or ContactsDialog instance."""
        target_id: str | None = target.id if isinstance(target, ContactsDialog) else target  # type: ignore[assignment]
        member = self.get_member("ContactDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContactDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContactsDialog'),
            )

    @property
    def header_text(self) -> str | None:
        """The text field that makes up the header for this request in the chat."""
        member = self.get_member("HeaderText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_text.setter
    def header_text(self, target: str | Text | None) -> None:
        """Set the HeaderText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("HeaderText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HeaderText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def invite_button(self) -> str | None:
        """The button to invite the user or forward the invite to the next in command."""
        member = self.get_member("InviteButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @invite_button.setter
    def invite_button(self, target: str | Button | None) -> None:
        """Set the InviteButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("InviteButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InviteButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def add_contact_button(self) -> str | None:
        """The button to add the user who is asking for an invite as a contact."""
        member = self.get_member("AddContactButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_contact_button.setter
    def add_contact_button(self, target: str | Button | None) -> None:
        """Set the AddContactButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("AddContactButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AddContactButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

