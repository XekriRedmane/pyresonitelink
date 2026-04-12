"""Generated component: AppEnder."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.end_mode import EndMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AppEnder(GeneratedComponent, IComponent, IWorldEventReceiver):
    """AppEnder is used by the local world to handle the logging out or exiting the game of the local user.

    **EndMode**: EndMode
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AppEnder"

    def __init__(self, mode: EndMode | str | None = None, changes_saved: primitives.Bool | None = None, text: str | TextRenderer | None = None, text_color: str | IField[primitives.ColorX] | None = None, outline_color: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mode: Initial value for Mode.
            changes_saved: Initial value for ChangesSaved.
            text: Initial value for _text.
            text_color: Initial value for _textColor.
            outline_color: Initial value for _outlineColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mode is not None:
            self.mode = mode
        if changes_saved is not None:
            self.changes_saved = changes_saved
        if text is not None:
            self.text = text
        if text_color is not None:
            self.text_color = text_color
        if outline_color is not None:
            self.outline_color = outline_color

    @property
    def mode(self) -> EndMode | None:
        """Whether to exit the game or logout."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EndMode(member.value)
        return None

    @mode.setter
    def mode(self, value: EndMode | str) -> None:
        """Set Mode. Whether to exit the game or logout."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def changes_saved(self) -> primitives.Bool | None:
        """Whether the items saved and dash changes for the current user have been saved"""
        member = self.get_member("ChangesSaved")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @changes_saved.setter
    def changes_saved(self, value: primitives.Bool) -> None:
        """Set the ChangesSaved field value."""
        member = self.get_member("ChangesSaved")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChangesSaved", fields.FieldBool(value=value)
            )

    @property
    def text(self) -> str | None:
        """the text object that is currently showing the status of the game exiting or logging out"""
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | TextRenderer | None) -> None:
        """Set the _text reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def text_color(self) -> str | None:
        """the color of the text object for this ender."""
        member = self.get_member("_textColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_color.setter
    def text_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _textColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def outline_color(self) -> str | None:
        """The outline color of the text object for this ender."""
        member = self.get_member("_outlineColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outline_color.setter
    def outline_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _outlineColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_outlineColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_outlineColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

