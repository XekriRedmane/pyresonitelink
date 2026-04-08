"""Generated component: DebugWorld."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugWorld(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugWorld.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugWorld"

    def __init__(self, text: str | Sync[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text

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

