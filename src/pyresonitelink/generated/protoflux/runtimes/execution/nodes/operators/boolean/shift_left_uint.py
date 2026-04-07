"""Generated component: ShiftLeft_Uint."""

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


class ShiftLeft_Uint(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ShiftLeft_Uint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Boolean
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ShiftLeft_Uint"

    def __init__(self, a: str | INodeValueOutput[np.uint32] | None = None, shift: str | INodeValueOutput[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            shift: Initial value for Shift.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if shift is not None:
            self.shift = shift

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[np.uint32])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[np.uint32] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[np.uint32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<uint>'),
            )

    @property
    def shift(self) -> str | None:
        """Target ID of the Shift reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("Shift")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shift.setter
    def shift(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the Shift reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Shift")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Shift",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

