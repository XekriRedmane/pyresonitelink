"""Generated component: IsBetween_Double."""

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


class IsBetween_Double(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.IsBetween_Double.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.IsBetween_Double"

    def __init__(self, value: str | INodeValueOutput[np.float64] | None = None, min: str | INodeValueOutput[np.float64] | None = None, max: str | INodeValueOutput[np.float64] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            min: Initial value for Min.
            max: Initial value for Max.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

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
    def min(self) -> str | None:
        """Target ID of the Min reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min.setter
    def min(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the Min reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Min",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def max(self) -> str | None:
        """Target ID of the Max reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max.setter
    def max(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the Max reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Max",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

