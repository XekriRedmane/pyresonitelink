"""Generated component: Pow_floatQ."""

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


class Pow_floatQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.Pow_floatQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.Pow_floatQ"

    def __init__(self, q: str | INodeValueOutput[primitives.FloatQ] | None = None, pow: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            q: Initial value for Q.
            pow: Initial value for Pow.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if q is not None:
            self.q = q
        if pow is not None:
            self.pow = pow

    @property
    def q(self) -> str | None:
        """Target ID of the Q reference (targets INodeValueOutput[primitives.FloatQ])."""
        member = self.get_member("Q")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @q.setter
    def q(self, target: str | INodeValueOutput[primitives.FloatQ] | None) -> None:
        """Set the Q reference by target ID or INodeValueOutput[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Q")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Q",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>'),
            )

    @property
    def pow(self) -> str | None:
        """Target ID of the Pow reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Pow")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pow.setter
    def pow(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Pow reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Pow")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pow",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

