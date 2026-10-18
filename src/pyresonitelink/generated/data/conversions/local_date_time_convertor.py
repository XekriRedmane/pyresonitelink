"""Generated component: LocalDateTimeConvertor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalDateTimeConvertor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocalDateTimeConvertor converts an inputted time to the user's local timezone.

    Category: Data/Conversions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalDateTimeConvertor"

    def __init__(self, source: str | IField[primitives.DateTime] | None = None, local_date_time: primitives.DateTime | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            local_date_time: Initial value for LocalDateTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if local_date_time is not None:
            self.local_date_time = local_date_time

    @property
    def source(self) -> str | None:
        """The source field holding the date time to convert."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[primitives.DateTime] | None) -> None:
        """Set the Source reference by target ID or IField[primitives.DateTime] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<DateTime>'),
            )

    @property
    def local_date_time(self) -> primitives.DateTime | None:
        """The value of the field targeted by ``Source`` converted to the local user's datetime."""
        member = self.get_member("LocalDateTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_date_time.setter
    def local_date_time(self, value: primitives.DateTime) -> None:
        """Set the LocalDateTime field value."""
        member = self.get_member("LocalDateTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalDateTime", fields.FieldDateTime(value=value)
            )

