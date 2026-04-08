"""Generated component: CurrentDateTimeTextDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurrentDateTimeTextDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CurrentDateTimeTextDriver.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurrentDateTimeTextDriver"

    def __init__(self, target: str | IField[primitives.String] | None = None, use_utc: primitives.Bool | None = None, override_format: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            use_utc: Initial value for UseUTC.
            override_format: Initial value for OverrideFormat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if use_utc is not None:
            self.use_utc = use_utc
        if override_format is not None:
            self.override_format = override_format

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.String])."""
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
    def pattern(self) -> members.FieldEnum | None:
        """The Pattern member."""
        member = self.get_member("Pattern")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @pattern.setter
    def pattern(self, value: members.FieldEnum) -> None:
        """Set the Pattern member."""
        self.set_member("Pattern", value)

    @property
    def use_utc(self) -> primitives.Bool | None:
        """The UseUTC field value."""
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
        """The OverrideFormat field value."""
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

