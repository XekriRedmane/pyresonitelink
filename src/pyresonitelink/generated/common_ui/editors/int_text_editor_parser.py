"""Generated component: IntTextEditorParser."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itext_editor_event_receiver import ITextEditorEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IntTextEditorParser(GeneratedComponent, ITextEditorEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.IntTextEditorParser.

    Category: Common UI/Editors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.IntTextEditorParser"

    def __init__(self, parse_continuously: primitives.Bool | None = None, update_string_from_value: primitives.Bool | None = None, parsed_value: primitives.Int | None = None, min: primitives.Int | None = None, max: primitives.Int | None = None, increments: primitives.Int | None = None, string_format: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parse_continuously: Initial value for ParseContinuously.
            update_string_from_value: Initial value for UpdateStringFromValue.
            parsed_value: Initial value for ParsedValue.
            min: Initial value for Min.
            max: Initial value for Max.
            increments: Initial value for Increments.
            string_format: Initial value for StringFormat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parse_continuously is not None:
            self.parse_continuously = parse_continuously
        if update_string_from_value is not None:
            self.update_string_from_value = update_string_from_value
        if parsed_value is not None:
            self.parsed_value = parsed_value
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if increments is not None:
            self.increments = increments
        if string_format is not None:
            self.string_format = string_format

    @property
    def parse_continuously(self) -> primitives.Bool | None:
        """The ParseContinuously field value."""
        member = self.get_member("ParseContinuously")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parse_continuously.setter
    def parse_continuously(self, value: primitives.Bool) -> None:
        """Set the ParseContinuously field value."""
        member = self.get_member("ParseContinuously")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParseContinuously", fields.FieldBool(value=value)
            )

    @property
    def update_string_from_value(self) -> primitives.Bool | None:
        """The UpdateStringFromValue field value."""
        member = self.get_member("UpdateStringFromValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_string_from_value.setter
    def update_string_from_value(self, value: primitives.Bool) -> None:
        """Set the UpdateStringFromValue field value."""
        member = self.get_member("UpdateStringFromValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateStringFromValue", fields.FieldBool(value=value)
            )

    @property
    def parsed_value(self) -> primitives.Int | None:
        """The ParsedValue field value."""
        member = self.get_member("ParsedValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parsed_value.setter
    def parsed_value(self, value: primitives.Int) -> None:
        """Set the ParsedValue field value."""
        member = self.get_member("ParsedValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParsedValue", fields.FieldInt(value=value)
            )

    @property
    def min(self) -> primitives.Int | None:
        """The Min field value."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: primitives.Int) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Min", fields.FieldInt(value=value)
            )

    @property
    def max(self) -> primitives.Int | None:
        """The Max field value."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: primitives.Int) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Max", fields.FieldInt(value=value)
            )

    @property
    def increments(self) -> primitives.Int | None:
        """The Increments field value."""
        member = self.get_member("Increments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @increments.setter
    def increments(self, value: primitives.Int) -> None:
        """Set the Increments field value."""
        member = self.get_member("Increments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Increments", fields.FieldInt(value=value)
            )

    @property
    def string_format(self) -> primitives.String | None:
        """The StringFormat field value."""
        member = self.get_member("StringFormat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @string_format.setter
    def string_format(self, value: primitives.String) -> None:
        """Set the StringFormat field value."""
        member = self.get_member("StringFormat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StringFormat", fields.FieldString(value=value)
            )

