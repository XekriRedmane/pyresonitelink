"""Generated component: QuantityTextFormatDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.compound_zero_handling import CompoundZeroHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class QuantityTextFormatDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The QuantityTextFormatDriver allows driving a string with an auto formatted quantity.

    Category: Utility

    **Behavior**: The most suitable unit type is automatically chosen based on the BaseValue, you can override this behavior by inputting a unit type into FormatUnit or using compound units.

    Parameterize with a value type::

        QuantityTextFormatDriver[primitives.Float]
        QuantityTextFormatDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.QuantityTextFormatDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.QuantityTextFormatDriver<>"

    def __init__(self, target: str | IField[primitives.String] | None = None, base_value: primitives.Double | None = None, format_unit: primitives.String | None = None, format_number: primitives.String | None = None, compound_use_long_names: primitives.Bool | None = None, compound_override_names: primitives.Bool | None = None, compound_discard_last_fraction: primitives.Bool | None = None, compound_separator: primitives.String | None = None, compound_zero_handling: CompoundZeroHandling | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            base_value: Initial value for BaseValue.
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
        if target is not None:
            self.target = target
        if base_value is not None:
            self.base_value = base_value
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
    def target(self) -> str | None:
        """The field to drive with the formatted Quantity string."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def base_value(self) -> primitives.Double | None:
        """Value to get converted into string"""
        member = self.get_member("BaseValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_value.setter
    def base_value(self, value: primitives.Double) -> None:
        """Set the BaseValue field value."""
        member = self.get_member("BaseValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseValue", fields.FieldDouble(value=value)
            )

    @property
    def format_unit(self) -> primitives.String | None:
        """Unit to format BaseValue in."""
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
        """How to format the number when making it part of the string (So if it should remove decimals."""
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
        """A list of format Units this can use to format the base value (common ones are "ft" as an entry followed by another entry with "in" or "m" as an entry followed by another entry with "cm" )."""
        member = self.get_member("CompoundFormatUnits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @compound_format_units.setter
    def compound_format_units(self, value: members.SyncList) -> None:
        """Set CompoundFormatUnits. A list of format Units this can use to format the base value (common ones are "ft" as an entry followed by another entry with "in" or "m" as an entry followed by another entry with "cm" )."""
        self.set_member("CompoundFormatUnits", value)

    @property
    def compound_use_long_names(self) -> primitives.Bool | None:
        """Show the long names of compound units."""
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
        """Whether the compound format unit names should be used rather than their usual name."""
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
        """Whether to discard the decimal of the smallest unit being displayed in the output or not. (so "3m 2.5cm" will become 3m 2cm")"""
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
        """String to put between compound units."""
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
        """Remove or trim compound units with a value of zero."""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CompoundZeroHandling(member.value)
        return None

    @compound_zero_handling.setter
    def compound_zero_handling(self, value: CompoundZeroHandling | str) -> None:
        """Set CompoundZeroHandling. Remove or trim compound units with a value of zero."""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CompoundZeroHandling",
                members.FieldEnum(value=str(value)),
            )

