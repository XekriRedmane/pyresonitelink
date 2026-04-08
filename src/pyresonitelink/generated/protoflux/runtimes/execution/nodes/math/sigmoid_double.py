"""Generated component: SigmoidDouble."""

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


class SigmoidDouble(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SigmoidDouble.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SigmoidDouble"

    def __init__(self, x: str | INodeValueOutput[primitives.Double] | None = None, e: str | INodeValueOutput[primitives.Double] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x: Initial value for X.
            e: Initial value for E.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x is not None:
            self.x = x
        if e is not None:
            self.e = e

    @property
    def x(self) -> str | None:
        """Target ID of the X reference (targets INodeValueOutput[primitives.Double])."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | INodeValueOutput[primitives.Double] | None) -> None:
        """Set the X reference by target ID or INodeValueOutput[primitives.Double] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def e(self) -> str | None:
        """Target ID of the E reference (targets INodeValueOutput[primitives.Double])."""
        member = self.get_member("E")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @e.setter
    def e(self, target: str | INodeValueOutput[primitives.Double] | None) -> None:
        """Set the E reference by target ID or INodeValueOutput[primitives.Double] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("E")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "E",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

