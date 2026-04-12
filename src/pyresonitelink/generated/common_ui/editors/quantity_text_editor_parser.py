"""Generated component: QuantityTextEditorParser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.compound_zero_handling import CompoundZeroHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T


class QuantityTextEditorParser(GenericComponent[T]):
    """The QuantityTextEditorParser component takes in a ``ParsedValue`` and if there is a TextEditor on the same slot, it will send the value through the text editor and into either a Text or a TextRenderer component.

}}

    Category: Common UI/Editors

    Place on the same Slot as a TextEditor and anything entered into the
    text editor will be attempted to be parsed as a quantity and output via
    the ``ParsedValue`` field.

    Parameterize with a value type::

        QuantityTextEditorParser[primitives.Float]
        QuantityTextEditorParser[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.QuantityTextEditorParser<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.QuantityTextEditorParser<>"

    def __init__(self, parse_continuously: primitives.Bool | None = None, update_string_from_value: primitives.Bool | None = None, parsed_value: primitives.Double | None = None, min_value: primitives.Double | None = None, max_value: primitives.Double | None = None, ignore_out_of_range: primitives.Bool | None = None, default_unit: primitives.String | None = None, format_unit: primitives.String | None = None, format_number: primitives.String | None = None, compound_use_long_names: primitives.Bool | None = None, compound_override_names: primitives.Bool | None = None, compound_discard_last_fraction: primitives.Bool | None = None, compound_separator: primitives.String | None = None, compound_zero_handling: CompoundZeroHandling | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parse_continuously: Initial value for ParseContinuously.
            update_string_from_value: Initial value for UpdateStringFromValue.
            parsed_value: Initial value for ParsedValue.
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            ignore_out_of_range: Initial value for IgnoreOutOfRange.
            default_unit: Initial value for DefaultUnit.
            format_unit: Initial value for FormatUnit.
            format_number: Initial value for FormatNumber.
            compound_use_long_names: Initial value for CompoundUseLongNames.
            compound_override_names: Initial value for CompoundOverrideNames.
            compound_discard_last_fraction: Initial value for CompoundDiscardLastFraction.
            compound_separator: Initial value for CompoundSeparator.
            compound_zero_handling: Initial value for CompoundZeroHandling.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parse_continuously is not None:
            self.parse_continuously = parse_continuously
        if update_string_from_value is not None:
            self.update_string_from_value = update_string_from_value
        if parsed_value is not None:
            self.parsed_value = parsed_value
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if ignore_out_of_range is not None:
            self.ignore_out_of_range = ignore_out_of_range
        if default_unit is not None:
            self.default_unit = default_unit
        if format_unit is not None:
            self.format_unit = format_unit
        if format_number is not None:
            self.format_number = format_number
        if compound_use_long_names is not None:
            self.compound_use_long_names = compound_use_long_names
        if compound_override_names is not None:
            self.compound_override_names = compound_override_names
        if compound_discard_last_fraction is not None:
            self.compound_discard_last_fraction = compound_discard_last_fraction
        if compound_separator is not None:
            self.compound_separator = compound_separator
        if compound_zero_handling is not None:
            self.compound_zero_handling = compound_zero_handling

    @property
    def parse_continuously(self) -> primitives.Bool | None:
        """If true, makes the value always update and parse. If false, it only updates when submitted."""
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
        """If true, will update the string value from this parsed value."""
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
    def parsed_value(self) -> primitives.Double | None:
        """The value that was read from the text field."""
        member = self.get_member("ParsedValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parsed_value.setter
    def parsed_value(self, value: primitives.Double) -> None:
        """Set the ParsedValue field value."""
        member = self.get_member("ParsedValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParsedValue", fields.FieldDouble(value=value)
            )

    @property
    def min_value(self) -> primitives.Double | None:
        """The minimum value that can be read."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: primitives.Double) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldDouble(value=value)
            )

    @property
    def max_value(self) -> primitives.Double | None:
        """The maximum value that can be read."""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: primitives.Double) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldDouble(value=value)
            )

    @property
    def ignore_out_of_range(self) -> primitives.Bool | None:
        """Ignores any value that is out of range from the min and max."""
        member = self.get_member("IgnoreOutOfRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_out_of_range.setter
    def ignore_out_of_range(self, value: primitives.Bool) -> None:
        """Set the IgnoreOutOfRange field value."""
        member = self.get_member("IgnoreOutOfRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreOutOfRange", fields.FieldBool(value=value)
            )

    @property
    def default_unit(self) -> primitives.String | None:
        """Changes the default unit to show in the text (especially if the ``FormatUnit`` is incorrect)."""
        member = self.get_member("DefaultUnit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_unit.setter
    def default_unit(self, value: primitives.String) -> None:
        """Set the DefaultUnit field value."""
        member = self.get_member("DefaultUnit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultUnit", fields.FieldString(value=value)
            )

    @property
    def format_unit(self) -> primitives.String | None:
        """The unit to show in the text."""
        member = self.get_member("FormatUnit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_unit.setter
    def format_unit(self, value: primitives.String) -> None:
        """Set the FormatUnit field value."""
        member = self.get_member("FormatUnit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormatUnit", fields.FieldString(value=value)
            )

    @property
    def format_number(self) -> primitives.String | None:
        """Formats the string."""
        member = self.get_member("FormatNumber")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_number.setter
    def format_number(self, value: primitives.String) -> None:
        """Set the FormatNumber field value."""
        member = self.get_member("FormatNumber")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormatNumber", fields.FieldString(value=value)
            )

    @property
    def compound_format_units(self) -> members.SyncList | None:
        """Compounds units together (example: feet and inches for height)."""
        member = self.get_member("CompoundFormatUnits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @compound_format_units.setter
    def compound_format_units(self, value: members.SyncList) -> None:
        """Set CompoundFormatUnits. Compounds units together (example: feet and inches for height)."""
        self.set_member("CompoundFormatUnits", value)

    @property
    def compound_use_long_names(self) -> primitives.Bool | None:
        """Use the long version of names."""
        member = self.get_member("CompoundUseLongNames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compound_use_long_names.setter
    def compound_use_long_names(self, value: primitives.Bool) -> None:
        """Set the CompoundUseLongNames field value."""
        member = self.get_member("CompoundUseLongNames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompoundUseLongNames", fields.FieldBool(value=value)
            )

    @property
    def compound_override_names(self) -> primitives.Bool | None:
        """Overrides the names."""
        member = self.get_member("CompoundOverrideNames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compound_override_names.setter
    def compound_override_names(self, value: primitives.Bool) -> None:
        """Set the CompoundOverrideNames field value."""
        member = self.get_member("CompoundOverrideNames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompoundOverrideNames", fields.FieldBool(value=value)
            )

    @property
    def compound_discard_last_fraction(self) -> primitives.Bool | None:
        """Discards the last fraction."""
        member = self.get_member("CompoundDiscardLastFraction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compound_discard_last_fraction.setter
    def compound_discard_last_fraction(self, value: primitives.Bool) -> None:
        """Set the CompoundDiscardLastFraction field value."""
        member = self.get_member("CompoundDiscardLastFraction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompoundDiscardLastFraction", fields.FieldBool(value=value)
            )

    @property
    def compound_separator(self) -> primitives.String | None:
        """Separates the compound units."""
        member = self.get_member("CompoundSeparator")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compound_separator.setter
    def compound_separator(self, value: primitives.String) -> None:
        """Set the CompoundSeparator field value."""
        member = self.get_member("CompoundSeparator")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompoundSeparator", fields.FieldString(value=value)
            )

    @property
    def compound_zero_handling(self) -> CompoundZeroHandling | None:
        """Handles zeros for units."""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CompoundZeroHandling(member.value)
        return None

    @compound_zero_handling.setter
    def compound_zero_handling(self, value: CompoundZeroHandling | str) -> None:
        """Set CompoundZeroHandling. Handles zeros for units."""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CompoundZeroHandling",
                members.FieldEnum(value=str(value)),
            )

