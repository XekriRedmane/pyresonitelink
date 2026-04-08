"""Generated component: FloatTextEditorParser."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itext_editor_event_receiver import ITextEditorEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FloatTextEditorParser(GeneratedComponent, ITextEditorEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FloatTextEditorParser.

    Category: Common UI/Editors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FloatTextEditorParser"

    def __init__(self, parse_continuously: bool | None = None, update_string_from_value: bool | None = None, parsed_value: np.float32 | None = None, min: np.float32 | None = None, max: np.float32 | None = None, decimal_places: np.int32 | None = None, string_format: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parse_continuously: Initial value for ParseContinuously.
            update_string_from_value: Initial value for UpdateStringFromValue.
            parsed_value: Initial value for ParsedValue.
            min: Initial value for Min.
            max: Initial value for Max.
            decimal_places: Initial value for DecimalPlaces.
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
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if string_format is not None:
            self.string_format = string_format

    @property
    def parse_continuously(self) -> bool | None:
        """The ParseContinuously field value."""
        member = self.get_member("ParseContinuously")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parse_continuously.setter
    def parse_continuously(self, value: bool) -> None:
        """Set the ParseContinuously field value."""
        member = self.get_member("ParseContinuously")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParseContinuously", fields.FieldBool(value=value)
            )

    @property
    def update_string_from_value(self) -> bool | None:
        """The UpdateStringFromValue field value."""
        member = self.get_member("UpdateStringFromValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_string_from_value.setter
    def update_string_from_value(self, value: bool) -> None:
        """Set the UpdateStringFromValue field value."""
        member = self.get_member("UpdateStringFromValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateStringFromValue", fields.FieldBool(value=value)
            )

    @property
    def parsed_value(self) -> np.float32 | None:
        """The ParsedValue field value."""
        member = self.get_member("ParsedValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parsed_value.setter
    def parsed_value(self, value: np.float32) -> None:
        """Set the ParsedValue field value."""
        member = self.get_member("ParsedValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParsedValue", fields.FieldFloat(value=value)
            )

    @property
    def min(self) -> np.float32 | None:
        """The Min field value."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: np.float32) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Min", fields.FieldFloat(value=value)
            )

    @property
    def max(self) -> np.float32 | None:
        """The Max field value."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: np.float32) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Max", fields.FieldFloat(value=value)
            )

    @property
    def decimal_places(self) -> np.int32 | None:
        """The DecimalPlaces field value."""
        member = self.get_member("DecimalPlaces")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @decimal_places.setter
    def decimal_places(self, value: np.int32) -> None:
        """Set the DecimalPlaces field value."""
        member = self.get_member("DecimalPlaces")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DecimalPlaces", fields.FieldInt(value=value)
            )

    @property
    def string_format(self) -> str | None:
        """The StringFormat field value."""
        member = self.get_member("StringFormat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @string_format.setter
    def string_format(self, value: str) -> None:
        """Set the StringFormat field value."""
        member = self.get_member("StringFormat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StringFormat", fields.FieldString(value=value)
            )

