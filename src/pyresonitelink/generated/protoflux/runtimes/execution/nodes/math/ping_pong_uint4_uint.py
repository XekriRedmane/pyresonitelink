"""Generated component: PingPong_Uint4_Uint."""

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


class PingPong_Uint4_Uint(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint4_Uint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint4_Uint"

    def __init__(self, n: str | INodeValueOutput[primitives.UInt4] | None = None, length: str | INodeValueOutput[np.uint32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            n: Initial value for N.
            length: Initial value for Length.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if n is not None:
            self.n = n
        if length is not None:
            self.length = length

    @property
    def n(self) -> str | None:
        """Target ID of the N reference (targets INodeValueOutput[primitives.UInt4])."""
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @n.setter
    def n(self, target: str | INodeValueOutput[primitives.UInt4] | None) -> None:
        """Set the N reference by target ID or INodeValueOutput[primitives.UInt4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "N",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<uint4>'),
            )

    @property
    def length(self) -> str | None:
        """Target ID of the Length reference (targets INodeValueOutput[np.uint32])."""
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length.setter
    def length(self, target: str | INodeValueOutput[np.uint32] | None) -> None:
        """Set the Length reference by target ID or INodeValueOutput[np.uint32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Length",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<uint>'),
            )

