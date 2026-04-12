"""Generated component: CurrentDateTimeTextDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.date_time_pattern import DateTimePattern
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurrentDateTimeTextDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The CurrentDateTimeTextDriver component takes the current time and formats it using C# DateTime to string using format as an argument.

    Category: Utility

    See the .NET Standard date and time format strings for DateTimePattern
    values:
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurrentDateTimeTextDriver"

    def __init__(self, target: str | IField[primitives.String] | None = None, pattern: DateTimePattern | str | None = None, use_utc: primitives.Bool | None = None, override_format: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            pattern: Initial value for Pattern.
            use_utc: Initial value for UseUTC.
            override_format: Initial value for OverrideFormat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if pattern is not None:
            self.pattern = pattern
        if use_utc is not None:
            self.use_utc = use_utc
        if override_format is not None:
            self.override_format = override_format

    @property
    def target(self) -> str | None:
        """What to drive the contents to be the current time formatted."""
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
    def pattern(self) -> DateTimePattern | None:
        """The pattern to use when rendering the date time, EX: 24 vs 12 hr."""
        member = self.get_member("Pattern")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DateTimePattern(member.value)
        return None

    @pattern.setter
    def pattern(self, value: DateTimePattern | str) -> None:
        """Set Pattern. The pattern to use when rendering the date time, EX: 24 vs 12 hr."""
        member = self.get_member("Pattern")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Pattern",
                members.FieldEnum(value=str(value)),
            )

    @property
    def use_utc(self) -> primitives.Bool | None:
        """Whether the current time outputted should be UTC time zone."""
        member = self.get_member("UseUTC")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_utc.setter
    def use_utc(self, value: primitives.Bool) -> None:
        """Set the UseUTC field value."""
        member = self.get_member("UseUTC")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseUTC", fields.FieldBool(value=value)
            )

    @property
    def override_format(self) -> primitives.String | None:
        """How to format the outputted current time."""
        member = self.get_member("OverrideFormat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_format.setter
    def override_format(self, value: primitives.String) -> None:
        """Set the OverrideFormat field value."""
        member = self.get_member("OverrideFormat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideFormat", fields.FieldString(value=value)
            )

