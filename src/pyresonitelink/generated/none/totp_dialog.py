"""Generated component: TOTP_Dialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TOTP_Dialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TOTP_Dialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TOTP_Dialog"

    def __init__(self, swap_region: str | SlideSwapRegion | None = None, code_field: str | TextField | None = None, message_text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            swap_region: Initial value for _swapRegion.
            code_field: Initial value for _codeField.
            message_text: Initial value for _messageText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if swap_region is not None:
            self.swap_region = swap_region
        if code_field is not None:
            self.code_field = code_field
        if message_text is not None:
            self.message_text = message_text

    @property
    def swap_region(self) -> str | None:
        """Target ID of the _swapRegion reference (targets SlideSwapRegion)."""
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @swap_region.setter
    def swap_region(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _swapRegion reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_swapRegion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

    @property
    def state(self) -> members.FieldEnum | None:
        """The _state member."""
        member = self.get_member("_state")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state.setter
    def state(self, value: members.FieldEnum) -> None:
        """Set the _state member."""
        self.set_member("_state", value)

    @property
    def code_field(self) -> str | None:
        """Target ID of the _codeField reference (targets TextField)."""
        member = self.get_member("_codeField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @code_field.setter
    def code_field(self, target: str | TextField | None) -> None:
        """Set the _codeField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_codeField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_codeField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def message_text(self) -> str | None:
        """Target ID of the _messageText reference (targets Text)."""
        member = self.get_member("_messageText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @message_text.setter
    def message_text(self, target: str | Text | None) -> None:
        """Set the _messageText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_messageText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_messageText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

