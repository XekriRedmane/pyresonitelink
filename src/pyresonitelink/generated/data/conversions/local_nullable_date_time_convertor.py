"""Generated component: LocalNullableDateTimeConvertor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalNullableDateTimeConvertor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalNullableDateTimeConvertor.

    Category: Data/Conversions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalNullableDateTimeConvertor"

    def __init__(self, source: str | IField[str | None] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IField[str | None])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[str | None] | None) -> None:
        """Set the Source reference by target ID or IField[str | None] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<DateTime?>'),
            )

    @property
    def local_date_time(self) -> members.EmptyElement | None:
        """The LocalDateTime member."""
        member = self.get_member("LocalDateTime")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @local_date_time.setter
    def local_date_time(self, value: members.EmptyElement) -> None:
        """Set the LocalDateTime member."""
        self.set_member("LocalDateTime", value)

