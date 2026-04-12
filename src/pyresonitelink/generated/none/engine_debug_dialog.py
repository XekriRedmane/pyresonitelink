"""Generated component: EngineDebugDialog."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EngineDebugDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The EngineDebugDialog component is used in the debug screen of the dash to show debug information about the game at the current moment.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EngineDebugDialog"

    def __init__(self, display_mode: Mode | str | None = None, content_root: str | Slot | None = None, text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_mode: Initial value for DisplayMode.
            content_root: Initial value for _contentRoot.
            text: Initial value for _text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_mode is not None:
            self.display_mode = display_mode
        if content_root is not None:
            self.content_root = content_root
        if text is not None:
            self.text = text

    @property
    def display_mode(self) -> Mode | None:
        """How to display the content."""
        member = self.get_member("DisplayMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @display_mode.setter
    def display_mode(self, value: Mode | str) -> None:
        """Set DisplayMode. How to display the content."""
        member = self.get_member("DisplayMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DisplayMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def content_root(self) -> str | None:
        """Content of the debug dialouge."""
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
        """The text displaying the engine debug info."""
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

