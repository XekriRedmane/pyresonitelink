"""Generated component: EngineDebugDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EngineDebugDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.EngineDebugDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EngineDebugDialog"

    def __init__(self, content_root: str | Slot | None = None, text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            text: Initial value for _text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root
        if text is not None:
            self.text = text

    @property
    def display_mode(self) -> members.FieldEnum | None:
        """The DisplayMode member."""
        member = self.get_member("DisplayMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @display_mode.setter
    def display_mode(self, value: members.FieldEnum) -> None:
        """Set the DisplayMode member."""
        self.set_member("DisplayMode", value)

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def text(self) -> str | None:
        """Target ID of the _text reference (targets Text)."""
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | Text | None) -> None:
        """Set the _text reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

