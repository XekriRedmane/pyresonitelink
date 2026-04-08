"""Generated component: LocalDateTimeConvertor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalDateTimeConvertor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalDateTimeConvertor.

    Category: Data/Conversions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalDateTimeConvertor"

    def __init__(self, source: str | IField[str] | None = None, local_date_time: str | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Source reference (targets IField[str])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[str] | None) -> None:
        """Set the Source reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<DateTime>'),
            )

    @property
    def local_date_time(self) -> str | None:
        """The LocalDateTime field value."""
        member = self.get_member("LocalDateTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_date_time.setter
    def local_date_time(self, value: str) -> None:
        """Set the LocalDateTime field value."""
        member = self.get_member("LocalDateTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalDateTime", fields.FieldDateTime(value=value)
            )

