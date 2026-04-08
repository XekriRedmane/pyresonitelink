"""Generated component: StringConcatenationDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StringConcatenationDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StringConcatenationDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StringConcatenationDriver"

    def __init__(self, target_string: str | IField[primitives.String] | None = None, separator: primitives.String | None = None, null_output_when_all_are_null: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_string: Initial value for TargetString.
            separator: Initial value for Separator.
            null_output_when_all_are_null: Initial value for NullOutputWhenAllAreNull.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_string is not None:
            self.target_string = target_string
        if separator is not None:
            self.separator = separator
        if null_output_when_all_are_null is not None:
            self.null_output_when_all_are_null = null_output_when_all_are_null

    @property
    def target_string(self) -> str | None:
        """Target ID of the TargetString reference (targets IField[primitives.String])."""
        member = self.get_member("TargetString")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_string.setter
    def target_string(self, target: str | IField[primitives.String] | None) -> None:
        """Set the TargetString reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetString")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetString",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def separator(self) -> primitives.String | None:
        """The Separator field value."""
        member = self.get_member("Separator")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separator.setter
    def separator(self, value: primitives.String) -> None:
        """Set the Separator field value."""
        member = self.get_member("Separator")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separator", fields.FieldString(value=value)
            )

    @property
    def strings(self) -> members.SyncList | None:
        """The Strings member."""
        member = self.get_member("Strings")
        if isinstance(member, members.SyncList):
            return member
        return None

    @strings.setter
    def strings(self, value: members.SyncList) -> None:
        """Set the Strings member."""
        self.set_member("Strings", value)

    @property
    def null_output_when_all_are_null(self) -> primitives.Bool | None:
        """The NullOutputWhenAllAreNull field value."""
        member = self.get_member("NullOutputWhenAllAreNull")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @null_output_when_all_are_null.setter
    def null_output_when_all_are_null(self, value: primitives.Bool) -> None:
        """Set the NullOutputWhenAllAreNull field value."""
        member = self.get_member("NullOutputWhenAllAreNull")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NullOutputWhenAllAreNull", fields.FieldBool(value=value)
            )

