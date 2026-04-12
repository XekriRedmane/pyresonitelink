"""Generated component: TextExportable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The TextExportable component allows the user to take a Slot and export it as a text file on their device.

To export using this component, look at the file browser export section.

    Category: Assets/Export

    This can be used to export anything that is text based, or anything you
    can fill the ``TextSource`` with such as log information or anything
    else that you wish to export out.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextExportable"

    def __init__(self, text_source: str | IValue[primitives.String] | None = None, extension: primitives.String | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
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
        """Anything that is a string, such as textfields, contents, etc."""
        member = self.get_member("TextSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_source.setter
    def text_source(self, target: str | IValue[primitives.String] | None) -> None:
        """Set the TextSource reference by target ID or IValue[primitives.String] instance."""
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
    def extension(self) -> primitives.String | None:
        """The file type, defaults to ``.txt``."""
        member = self.get_member("Extension")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @extension.setter
    def extension(self, value: primitives.String) -> None:
        """Set the Extension field value."""
        member = self.get_member("Extension")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Extension", fields.FieldString(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The description of what this text export is. Will be shown during the export process."""
        member = self.get_member("Description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the Description field value."""
        member = self.get_member("Description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Description", fields.FieldString(value=value)
            )

