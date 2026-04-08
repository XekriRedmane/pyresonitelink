"""Generated component: PackProtoFluxInPlace."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackProtoFluxInPlace(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Pack ProtoFlux In Place node takes in a start point for your ProtoFlux code, and when called, will pack everything in place, no matter where. If you have all your code sitting in Root or inside a Slot, it will pack it at that exact location.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Nodes
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Nodes.PackProtoFluxInPlace"

    def __init__(self, next: str | INodeOperation | None = None, start_node: str | INodeObjectOutput[ProtoFluxNode] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            start_node: Initial value for StartNode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if start_node is not None:
            self.start_node = start_node

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def start_node(self) -> str | None:
        """Target ID of the StartNode reference (targets INodeObjectOutput[ProtoFluxNode])."""
        member = self.get_member("StartNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_node.setter
    def start_node(self, target: str | INodeObjectOutput[ProtoFluxNode] | None) -> None:
        """Set the StartNode reference by target ID or INodeObjectOutput[ProtoFluxNode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("StartNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StartNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNode>'),
            )

