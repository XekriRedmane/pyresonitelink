"""Generated component: Atan2_Float_Color."""

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


class Atan2_Float_Color(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Atan2_Float_Color.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Trigonometry
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Atan2_Float_Color"

    def __init__(self, y: str | INodeValueOutput[np.float32] | None = None, x: str | INodeValueOutput[primitives.Color] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            y: Initial value for Y.
            x: Initial value for X.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if y is not None:
            self.y = y
        if x is not None:
            self.x = x

    @property
    def y(self) -> str | None:
        """Target ID of the Y reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y.setter
    def y(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Y reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Y",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def x(self) -> str | None:
        """Target ID of the X reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the X reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

