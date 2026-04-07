"""Generated component: HSL_ToColor."""

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


class HSL_ToColor(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSL_ToColor.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSL_ToColor"

    def __init__(self, h: str | INodeValueOutput[np.float32] | None = None, s: str | INodeValueOutput[np.float32] | None = None, l: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            h: Initial value for H.
            s: Initial value for S.
            l: Initial value for L.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if h is not None:
            self.h = h
        if s is not None:
            self.s = s
        if l is not None:
            self.l = l

    @property
    def h(self) -> str | None:
        """Target ID of the H reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("H")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @h.setter
    def h(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the H reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("H")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "H",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def s(self) -> str | None:
        """Target ID of the S reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("S")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @s.setter
    def s(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the S reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("S")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "S",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def l(self) -> str | None:
        """Target ID of the L reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("L")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @l.setter
    def l(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the L reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("L")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "L",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

