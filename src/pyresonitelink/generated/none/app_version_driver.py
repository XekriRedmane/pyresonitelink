"""Generated component: AppVersionDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AppVersionDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """App version driver is a component that drives the content of the string field provided to ``Text`` to Resonite's version.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AppVersionDriver"

    def __init__(self, text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text

    @property
    def text(self) -> str | None:
        """Drives the provided text field's content to Resonite's version. The text is formatted starting with "Beta", "Alpha", or "Release", followed by the game's compile date. The date is formatted ``year.day.month.minuteOfDay``. Minute of day is the minutes since midnight. The time is in UTC."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Text reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

