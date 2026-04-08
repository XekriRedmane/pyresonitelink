"""Generated component: RotateLeft_Ulong."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RotateLeft_Ulong(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Ulong.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Boolean
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Ulong"

    def __init__(self, a: str | INodeValueOutput[primitives.ULong] | None = None, rotate: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            rotate: Initial value for Rotate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if rotate is not None:
            self.rotate = rotate

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[primitives.ULong])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[primitives.ULong] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[primitives.ULong] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<ulong>'),
            )

    @property
    def rotate(self) -> str | None:
        """Target ID of the Rotate reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Rotate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotate.setter
    def rotate(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Rotate reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Rotate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rotate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

