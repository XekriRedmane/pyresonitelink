"""Generated component: LogN_Double_Double4."""

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


class LogN_Double_Double4(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.LogN_Double_Double4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.LogN_Double_Double4"

    def __init__(self, n: str | INodeValueOutput[np.float64] | None = None, base: str | INodeValueOutput[primitives.Double4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            n: Initial value for N.
            base: Initial value for Base.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if n is not None:
            self.n = n
        if base is not None:
            self.base = base

    @property
    def n(self) -> str | None:
        """Target ID of the N reference (targets INodeValueOutput[np.float64])."""
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @n.setter
    def n(self, target: str | INodeValueOutput[np.float64] | None) -> None:
        """Set the N reference by target ID or INodeValueOutput[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "N",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

    @property
    def base(self) -> str | None:
        """Target ID of the Base reference (targets INodeValueOutput[primitives.Double4])."""
        member = self.get_member("Base")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base.setter
    def base(self, target: str | INodeValueOutput[primitives.Double4] | None) -> None:
        """Set the Base reference by target ID or INodeValueOutput[primitives.Double4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Base")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Base",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double4>'),
            )

