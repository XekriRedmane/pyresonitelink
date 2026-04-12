"""Generated component: HyperlinkOpenDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HyperlinkOpenDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The HyperlinkOpenDialog component shows in user space as a UIX when the user clicks on a HyperLink component.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HyperlinkOpenDialog"

    def __init__(self, url: str | None = None, hyperlink_text: str | Text | None = None, reason_text: str | Text | None = None, open_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            hyperlink_text: Initial value for _hyperlinkText.
            reason_text: Initial value for _reasonText.
            open_button: Initial value for _openButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if hyperlink_text is not None:
            self.hyperlink_text = hyperlink_text
        if reason_text is not None:
            self.reason_text = reason_text
        if open_button is not None:
            self.open_button = open_button

    @property
    def url(self) -> str | None:
        """The url being accessed."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def hyperlink_text(self) -> str | None:
        """The text to fill with what is being accessed."""
        member = self.get_member("_hyperlinkText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hyperlink_text.setter
    def hyperlink_text(self, target: str | Text | None) -> None:
        """Set the _hyperlinkText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_hyperlinkText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hyperlinkText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def reason_text(self) -> str | None:
        """The text to show the reason for the link dialog showing."""
        member = self.get_member("_reasonText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reason_text.setter
    def reason_text(self, target: str | Text | None) -> None:
        """Set the _reasonText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_reasonText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_reasonText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def open_button(self) -> str | None:
        """The button to open the link in ``URL`` using the user's OS default browser."""
        member = self.get_member("_openButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @open_button.setter
    def open_button(self, target: str | Button | None) -> None:
        """Set the _openButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_openButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_openButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

