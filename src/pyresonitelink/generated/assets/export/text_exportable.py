"""Generated component: TextExportable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextExportable.

    Category: Assets/Export
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextExportable"

    def __init__(self, text_source: str | IValue[str] | None = None, extension: str | None = None, description: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text_source: Initial value for TextSource.
            extension: Initial value for Extension.
            description: Initial value for Description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text_source is not None:
            self.text_source = text_source
        if extension is not None:
            self.extension = extension
        if description is not None:
            self.description = description

    @property
    def text_source(self) -> str | None:
        """Target ID of the TextSource reference (targets IValue[str])."""
        member = self.get_member("TextSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_source.setter
    def text_source(self, target: str | IValue[str] | None) -> None:
        """Set the TextSource reference by target ID or IValue[str] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("TextSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<string>'),
            )

    @property
    def extension(self) -> str | None:
        """The Extension field value."""
        member = self.get_member("Extension")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @extension.setter
    def extension(self, value: str) -> None:
        """Set the Extension field value."""
        member = self.get_member("Extension")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Extension", fields.FieldString(value=value)
            )

    @property
    def description(self) -> str | None:
        """The Description field value."""
        member = self.get_member("Description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: str) -> None:
        """Set the Description field value."""
        member = self.get_member("Description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Description", fields.FieldString(value=value)
            )

