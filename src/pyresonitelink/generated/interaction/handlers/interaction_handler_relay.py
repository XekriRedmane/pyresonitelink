"""Generated component: InteractionHandlerRelay."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent

if TYPE_CHECKING:
    from pyresonitelink.generated.interaction.handlers.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionHandlerRelay(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The InteractionHandlerRelay component is used internally by the game engine to find the source handler of a tool or slot.

    Category: Interaction/Handlers

    not used by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractionHandlerRelay"

    def __init__(self, common_tool: str | InteractionHandler | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            common_tool: Initial value for CommonTool.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if common_tool is not None:
            self.common_tool = common_tool

    @property
    def common_tool(self) -> str | None:
        """The handler this is a relay for."""
        member = self.get_member("CommonTool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @common_tool.setter
    def common_tool(self, target: str | InteractionHandler | None) -> None:
        """Set the CommonTool reference by target ID or InteractionHandler instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("CommonTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CommonTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

