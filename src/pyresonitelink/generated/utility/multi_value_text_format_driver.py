"""Generated component: MultiValueTextFormatDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiValueTextFormatDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ValueTextFormatDriver applies the value of a multiple values to a text format string and drives the target string field. Elements are defined by putting {} brackets around a number to specify an element in ``Sources``.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiValueTextFormatDriver"

    def __init__(self, format_: primitives.String | None = None, text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            format_: Initial value for Format.
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if format_ is not None:
            self.format_ = format_
        if text is not None:
            self.text = text

    @property
    def sources(self) -> members.SyncList | None:
        """A list of source fields."""
        member = self.get_member("Sources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sources.setter
    def sources(self, value: members.SyncList) -> None:
        """Set Sources. A list of source fields."""
        self.set_member("Sources", value)

    @property
    def format_(self) -> primitives.String | None:
        """The format string, which has a list of "{X}" where "X" is a number that refers to an item number in ``Sources``. The entire "{X}" gets replaced by a source with that number."""
        member = self.get_member("Format")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_.setter
    def format_(self, value: primitives.String) -> None:
        """Set the Format field value."""
        member = self.get_member("Format")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Format", fields.FieldString(value=value)
            )

    @property
    def text(self) -> str | None:
        """The target field."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Text reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

