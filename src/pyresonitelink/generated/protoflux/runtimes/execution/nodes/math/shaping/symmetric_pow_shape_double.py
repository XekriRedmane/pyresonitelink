"""Generated component: SymmetricPowShape_Double."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SymmetricPowShape_Double(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.SymmetricPowShape_Double.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Shaping
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.SymmetricPowShape_Double"

    def __init__(self, value: str | INodeValueOutput[np.float64] | None = None, power: str | INodeValueOutput[np.float64] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if power is not None:
            self.power = power

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def power(self) -> str | None:
        """Target ID of the Power reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("Power")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @power.setter
    def power(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the Power reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Power")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Power",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

