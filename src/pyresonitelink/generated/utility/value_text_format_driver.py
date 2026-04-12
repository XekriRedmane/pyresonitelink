"""Generated component: ValueTextFormatDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueTextFormatDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """ValueTextFormatDriver applies the value of a single source field to a text format string and drives the target string field. The source field is element 0 in the format string. Elements are defined by putting {} brackets around a number. Although the image shown and the field list below have the source field being a float, this component is generic, so any field type (that can be converted to a string) can be used.

    Category: Utility

    Attach to a slot and provide a format string and source value in order
    to drive a string field (possibly text) with the formatted number.

    Parameterize with a value type::

        ValueTextFormatDriver[primitives.Float]
        ValueTextFormatDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueTextFormatDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueTextFormatDriver<>"

    def __init__(self, source: str | IField[T] | None = None, format_: primitives.String | None = None, text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            format_: Initial value for Format.
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if format_ is not None:
            self.format_ = format_
        if text is not None:
            self.text = text

    @property
    def source(self) -> str | None:
        """The source field for the value."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[T] | None) -> None:
        """Set the Source reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def format_(self) -> primitives.String | None:
        """The string format with "{0}" in it somewhere"""
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

