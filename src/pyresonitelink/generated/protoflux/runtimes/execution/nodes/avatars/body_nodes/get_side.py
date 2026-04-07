"""Generated component: GetSide."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.body_node import BodyNode
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetSide(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodes.GetSide.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Body Nodes
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodes.GetSide"

    def __init__(self, node: str | INodeValueOutput[BodyNode] | None = None, side: str | INodeValueOutput[Chirality] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            side: Initial value for Side.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if side is not None:
            self.side = side

    @property
    def node(self) -> str | None:
        """Target ID of the Node reference (targets INodeValueOutput[BodyNode])."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | INodeValueOutput[BodyNode] | None) -> None:
        """Set the Node reference by target ID or INodeValueOutput[BodyNode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>'),
            )

    @property
    def side(self) -> str | None:
        """Target ID of the Side reference (targets INodeValueOutput[Chirality])."""
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side.setter
    def side(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Side reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Side",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
            )

