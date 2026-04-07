"""Generated component: ApproximatelyNot_Double3x3."""

import numpy as np

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


class ApproximatelyNot_Double3x3(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ApproximatelyNot_Double3x3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ApproximatelyNot_Double3x3"

    def __init__(self, a: str | INodeValueOutput[primitives.Double3x3] | None = None, b: str | INodeValueOutput[primitives.Double3x3] | None = None, epsilon: str | INodeValueOutput[np.float64] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            b: Initial value for B.
            epsilon: Initial value for Epsilon.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if epsilon is not None:
            self.epsilon = epsilon

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[primitives.Double3x3])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[primitives.Double3x3] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[primitives.Double3x3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets INodeValueOutput[primitives.Double3x3])."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | INodeValueOutput[primitives.Double3x3] | None) -> None:
        """Set the B reference by target ID or INodeValueOutput[primitives.Double3x3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>'),
            )

    @property
    def epsilon(self) -> str | None:
        """Target ID of the Epsilon reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("Epsilon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @epsilon.setter
    def epsilon(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the Epsilon reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Epsilon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Epsilon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

