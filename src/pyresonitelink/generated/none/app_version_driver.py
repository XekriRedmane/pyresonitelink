"""Generated component: AppVersionDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AppVersionDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AppVersionDriver.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AppVersionDriver"

    def __init__(self, text: str | IField[str] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Text reference (targets IField[str])."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IField[str] | None) -> None:
        """Set the Text reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

