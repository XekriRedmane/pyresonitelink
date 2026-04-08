"""Generated component: ToolEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ToolEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Tool Events node takes in a referenced ITool, and fires events if the tool is equipped or dequipped from the user.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Tools
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.ToolEvents"

    def __init__(self, tool: str | IGlobalValueProxy[ITool] | None = None, equipped: str | ISyncNodeOperation | None = None, dequipped: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tool: Initial value for Tool.
            equipped: Initial value for Equipped.
            dequipped: Initial value for Dequipped.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tool is not None:
            self.tool = tool
        if equipped is not None:
            self.equipped = equipped
        if dequipped is not None:
            self.dequipped = dequipped

    @property
    def tool(self) -> str | None:
        """Target ID of the Tool reference (targets IGlobalValueProxy[ITool])."""
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool.setter
    def tool(self, target: str | IGlobalValueProxy[ITool] | None) -> None:
        """Set the Tool reference by target ID or IGlobalValueProxy[ITool] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.ITool>'),
            )

    @property
    def equipped(self) -> str | None:
        """Target ID of the Equipped reference (targets ISyncNodeOperation)."""
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipped.setter
    def equipped(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Equipped reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Equipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def dequipped(self) -> str | None:
        """Target ID of the Dequipped reference (targets ISyncNodeOperation)."""
        member = self.get_member("Dequipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dequipped.setter
    def dequipped(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Dequipped reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Dequipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dequipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

