"""Generated component: Pow_Double2."""

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


class Pow_Double2(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Pow_Double2.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Pow_Double2"

    def __init__(self, n: str | INodeValueOutput[primitives.Double2] | None = None, power: str | INodeValueOutput[primitives.Double2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            n: Initial value for N.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if n is not None:
            self.n = n
        if power is not None:
            self.power = power

    @property
    def n(self) -> str | None:
        """Target ID of the N reference (targets INodeValueOutput[primitives.Double2])."""
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @n.setter
    def n(self, target: str | INodeValueOutput[primitives.Double2] | None) -> None:
        """Set the N reference by target ID or INodeValueOutput[primitives.Double2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "N",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double2>'),
            )

    @property
    def power(self) -> str | None:
        """Target ID of the Power reference (targets INodeValueOutput[primitives.Double2])."""
        member = self.get_member("Power")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @power.setter
    def power(self, target: str | INodeValueOutput[primitives.Double2] | None) -> None:
        """Set the Power reference by target ID or INodeValueOutput[primitives.Double2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Power")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Power",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double2>'),
            )

