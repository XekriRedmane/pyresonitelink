"""Generated component: DistanceMeter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.compound_zero_handling import CompoundZeroHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DistanceMeter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DistanceMeter component is used by the Meter Tool to display the distance between slots placed by it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DistanceMeter"

    def __init__(self, legacy_anchor0: str | Slot | None = None, legacy_anchor1: str | Slot | None = None, format_unit: primitives.String | None = None, format_number: primitives.String | None = None, compound_use_long_names: primitives.Bool | None = None, compound_override_names: primitives.Bool | None = None, compound_discard_last_fraction: primitives.Bool | None = None, compound_separator: primitives.String | None = None, compound_zero_handling: CompoundZeroHandling | str | None = None, distance_text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            legacy_anchor0: Initial value for _legacyAnchor0.
            legacy_anchor1: Initial value for _legacyAnchor1.
            format_unit: Initial value for FormatUnit.
            format_number: Initial value for FormatNumber.
            compound_use_long_names: Initial value for CompoundUseLongNames.
            compound_override_names: Initial value for CompoundOverrideNames.
            compound_discard_last_fraction: Initial value for CompoundDiscardLastFraction.
            compound_separator: Initial value for CompoundSeparator.
            compound_zero_handling: Initial value for CompoundZeroHandling.
            distance_text: Initial value for DistanceText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if legacy_anchor0 is not None:
            self.legacy_anchor0 = legacy_anchor0
        if legacy_anchor1 is not None:
            self.legacy_anchor1 = legacy_anchor1
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
        if distance_text is not None:
            self.distance_text = distance_text

    @property
    def anchors(self) -> members.SyncList | None:
        """List of points being used to measure right now."""
        member = self.get_member("Anchors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @anchors.setter
    def anchors(self, value: members.SyncList) -> None:
        """Set Anchors. List of points being used to measure right now."""
        self.set_member("Anchors", value)

    @property
    def legacy_anchor0(self) -> str | None:
        """Legacy, unused. For when the tool only measured two points."""
        member = self.get_member("_legacyAnchor0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_anchor0.setter
    def legacy_anchor0(self, target: str | Slot | None) -> None:
        """Set the _legacyAnchor0 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_legacyAnchor0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_legacyAnchor0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def legacy_anchor1(self) -> str | None:
        """Legacy, unused. For when the tool only measured two points."""
        member = self.get_member("_legacyAnchor1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_anchor1.setter
    def legacy_anchor1(self, target: str | Slot | None) -> None:
        """Set the _legacyAnchor1 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_legacyAnchor1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_legacyAnchor1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def format_unit(self) -> primitives.String | None:
        """The formatting string to use when formatting the distance number"""
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
        """How to format the distance number"""
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
        """The format string to format compound measurement units with."""
        member = self.get_member("CompoundFormatUnits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @compound_format_units.setter
    def compound_format_units(self, value: members.SyncList) -> None:
        """Set CompoundFormatUnits. The format string to format compound measurement units with."""
        self.set_member("CompoundFormatUnits", value)

    @property
    def compound_use_long_names(self) -> primitives.Bool | None:
        """Whether to use long name of distance (Ex: cm vs Centimeter)"""
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
        """Whether to use compound measurements or not."""
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
        """Whether to discard small distances like Millimeters."""
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
        """What to separate compound measurements with (like spaces or commas)"""
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
        """How to handle compound measurements (1 meter 1cm 10mm)"""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CompoundZeroHandling(member.value)
        return None

    @compound_zero_handling.setter
    def compound_zero_handling(self, value: CompoundZeroHandling | str) -> None:
        """Set CompoundZeroHandling. How to handle compound measurements (1 meter 1cm 10mm)"""
        member = self.get_member("CompoundZeroHandling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CompoundZeroHandling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def measurement_space(self) -> members.SyncObject | None:
        """The transform space to measure in."""
        member = self.get_member("MeasurementSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @measurement_space.setter
    def measurement_space(self, value: members.SyncObject) -> None:
        """Set MeasurementSpace. The transform space to measure in."""
        self.set_member("MeasurementSpace", value)

    @property
    def distance_text(self) -> str | None:
        """The field to drive when displaying the total amount of distance."""
        member = self.get_member("DistanceText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance_text.setter
    def distance_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the DistanceText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DistanceText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DistanceText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

