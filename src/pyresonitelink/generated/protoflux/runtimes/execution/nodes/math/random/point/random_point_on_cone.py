"""Generated component: RandomPointOnCone."""

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


class RandomPointOnCone(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomPointOnCone.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Random/Point
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomPointOnCone"

    def __init__(self, height: str | INodeValueOutput[np.float32] | None = None, base_radius: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            height: Initial value for Height.
            base_radius: Initial value for BaseRadius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if height is not None:
            self.height = height
        if base_radius is not None:
            self.base_radius = base_radius

    @property
    def height(self) -> str | None:
        """Target ID of the Height reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height.setter
    def height(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Height reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Height",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def base_radius(self) -> str | None:
        """Target ID of the BaseRadius reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("BaseRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_radius.setter
    def base_radius(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the BaseRadius reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BaseRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

