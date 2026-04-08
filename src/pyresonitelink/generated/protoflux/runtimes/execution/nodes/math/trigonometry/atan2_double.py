"""Generated component: Atan2_Double."""

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


class Atan2_Double(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Atan2_Double.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Trigonometry
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Atan2_Double"

    def __init__(self, y: str | INodeValueOutput[primitives.Double] | None = None, x: str | INodeValueOutput[primitives.Double] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            y: Initial value for Y.
            x: Initial value for X.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if y is not None:
            self.y = y
        if x is not None:
            self.x = x

    @property
    def y(self) -> str | None:
        """Target ID of the Y reference (targets INodeValueOutput[primitives.Double])."""
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y.setter
    def y(self, target: str | INodeValueOutput[primitives.Double] | None) -> None:
        """Set the Y reference by target ID or INodeValueOutput[primitives.Double] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Y",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

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

