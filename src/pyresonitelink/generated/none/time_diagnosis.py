"""Generated component: TimeDiagnosis."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeDiagnosis(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TimeDiagnosis.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TimeDiagnosis"

    def __init__(self, format_time: bool | None = None, text: str | Sync[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            format_time: Initial value for FormatTime.
            text: Initial value for text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if format_time is not None:
            self.format_time = format_time
        if text is not None:
            self.text = text

    @property
    def format_time(self) -> bool | None:
        """The FormatTime field value."""
        member = self.get_member("FormatTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_time.setter
    def format_time(self, value: bool) -> None:
        """Set the FormatTime field value."""
        member = self.get_member("FormatTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormatTime", fields.FieldBool(value=value)
            )

    @property
    def text(self) -> str | None:
        """Target ID of the text reference (targets Sync[str])."""
        member = self.get_member("text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | Sync[str] | None) -> None:
        """Set the text reference by target ID or Sync[str] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<string>'),
            )

