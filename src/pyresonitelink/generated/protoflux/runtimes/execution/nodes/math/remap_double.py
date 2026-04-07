"""Generated component: Remap_Double."""

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


class Remap_Double(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Remap_Double.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Remap_Double"

    def __init__(self, in_min: str | INodeValueOutput[np.float64] | None = None, in_max: str | INodeValueOutput[np.float64] | None = None, out_min: str | INodeValueOutput[np.float64] | None = None, out_max: str | INodeValueOutput[np.float64] | None = None, value: str | INodeValueOutput[np.float64] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            in_min: Initial value for InMin.
            in_max: Initial value for InMax.
            out_min: Initial value for OutMin.
            out_max: Initial value for OutMax.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if in_min is not None:
            self.in_min = in_min
        if in_max is not None:
            self.in_max = in_max
        if out_min is not None:
            self.out_min = out_min
        if out_max is not None:
            self.out_max = out_max
        if value is not None:
            self.value = value

    @property
    def in_min(self) -> str | None:
        """Target ID of the InMin reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("InMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @in_min.setter
    def in_min(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the InMin reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def in_max(self) -> str | None:
        """Target ID of the InMax reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("InMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @in_max.setter
    def in_max(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the InMax reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def out_min(self) -> str | None:
        """Target ID of the OutMin reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("OutMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @out_min.setter
    def out_min(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the OutMin reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OutMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OutMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def out_max(self) -> str | None:
        """Target ID of the OutMax reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("OutMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @out_max.setter
    def out_max(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the OutMax reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OutMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OutMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

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

