"""Generated component: UnitSystemSwitcher."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_field_list import SyncFieldList
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnitSystemSwitcher(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UnitSystemSwitcher.

    Category: Common UI/Editors/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnitSystemSwitcher"

    def __init__(self, default_unit: str | IField[primitives.String] | None = None, format_unit: str | IField[primitives.String] | None = None, format_number: str | IField[primitives.String] | None = None, compound_format_units: str | SyncFieldList[primitives.String] | None = None, compound_override_names: str | IField[primitives.Bool] | None = None, compound_use_long_names: str | IField[primitives.Bool] | None = None, compound_separator: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_unit: Initial value for DefaultUnit.
            format_unit: Initial value for FormatUnit.
            format_number: Initial value for FormatNumber.
            compound_format_units: Initial value for CompoundFormatUnits.
            compound_override_names: Initial value for CompoundOverrideNames.
            compound_use_long_names: Initial value for CompoundUseLongNames.
            compound_separator: Initial value for CompoundSeparator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_unit is not None:
            self.default_unit = default_unit
        if format_unit is not None:
            self.format_unit = format_unit
        if format_number is not None:
            self.format_number = format_number
        if compound_format_units is not None:
            self.compound_format_units = compound_format_units
        if compound_override_names is not None:
            self.compound_override_names = compound_override_names
        if compound_use_long_names is not None:
            self.compound_use_long_names = compound_use_long_names
        if compound_separator is not None:
            self.compound_separator = compound_separator

    @property
    def default_unit(self) -> str | None:
        """Target ID of the DefaultUnit reference (targets IField[primitives.String])."""
        member = self.get_member("DefaultUnit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_unit.setter
    def default_unit(self, target: str | IField[primitives.String] | None) -> None:
        """Set the DefaultUnit reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DefaultUnit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultUnit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def format_unit(self) -> str | None:
        """Target ID of the FormatUnit reference (targets IField[primitives.String])."""
        member = self.get_member("FormatUnit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_unit.setter
    def format_unit(self, target: str | IField[primitives.String] | None) -> None:
        """Set the FormatUnit reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FormatUnit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatUnit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def format_number(self) -> str | None:
        """Target ID of the FormatNumber reference (targets IField[primitives.String])."""
        member = self.get_member("FormatNumber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_number.setter
    def format_number(self, target: str | IField[primitives.String] | None) -> None:
        """Set the FormatNumber reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FormatNumber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatNumber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def compound_format_units(self) -> str | None:
        """Target ID of the CompoundFormatUnits reference (targets SyncFieldList[primitives.String])."""
        member = self.get_member("CompoundFormatUnits")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compound_format_units.setter
    def compound_format_units(self, target: str | SyncFieldList[primitives.String] | None) -> None:
        """Set the CompoundFormatUnits reference by target ID or SyncFieldList[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, SyncFieldList) else target  # type: ignore[assignment]
        member = self.get_member("CompoundFormatUnits")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompoundFormatUnits",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncFieldList<string>'),
            )

    @property
    def compound_override_names(self) -> str | None:
        """Target ID of the CompoundOverrideNames reference (targets IField[primitives.Bool])."""
        member = self.get_member("CompoundOverrideNames")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compound_override_names.setter
    def compound_override_names(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the CompoundOverrideNames reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CompoundOverrideNames")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompoundOverrideNames",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def compound_use_long_names(self) -> str | None:
        """Target ID of the CompoundUseLongNames reference (targets IField[primitives.Bool])."""
        member = self.get_member("CompoundUseLongNames")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compound_use_long_names.setter
    def compound_use_long_names(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the CompoundUseLongNames reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CompoundUseLongNames")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompoundUseLongNames",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def compound_separator(self) -> str | None:
        """Target ID of the CompoundSeparator reference (targets IField[primitives.String])."""
        member = self.get_member("CompoundSeparator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @compound_separator.setter
    def compound_separator(self, target: str | IField[primitives.String] | None) -> None:
        """Set the CompoundSeparator reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CompoundSeparator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompoundSeparator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def default_preset(self) -> members.SyncObject | None:
        """The DefaultPreset member."""
        member = self.get_member("DefaultPreset")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @default_preset.setter
    def default_preset(self, value: members.SyncObject) -> None:
        """Set the DefaultPreset member."""
        self.set_member("DefaultPreset", value)

    @property
    def imperial_preset(self) -> members.SyncObject | None:
        """The ImperialPreset member."""
        member = self.get_member("ImperialPreset")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @imperial_preset.setter
    def imperial_preset(self, value: members.SyncObject) -> None:
        """Set the ImperialPreset member."""
        self.set_member("ImperialPreset", value)

