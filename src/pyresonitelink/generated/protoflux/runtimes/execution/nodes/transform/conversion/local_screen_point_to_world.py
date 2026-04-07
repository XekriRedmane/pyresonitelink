"""Generated component: LocalScreenPointToWorld."""

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


class LocalScreenPointToWorld(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalScreen.LocalScreenPointToWorld.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Conversion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalScreen.LocalScreenPointToWorld"

    def __init__(self, normalized_screen_point: str | INodeValueOutput[primitives.Float2] | None = None, distance: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            normalized_screen_point: Initial value for NormalizedScreenPoint.
            distance: Initial value for Distance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if normalized_screen_point is not None:
            self.normalized_screen_point = normalized_screen_point
        if distance is not None:
            self.distance = distance

    @property
    def normalized_screen_point(self) -> str | None:
        """Target ID of the NormalizedScreenPoint reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("NormalizedScreenPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normalized_screen_point.setter
    def normalized_screen_point(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the NormalizedScreenPoint reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NormalizedScreenPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalizedScreenPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def distance(self) -> str | None:
        """Target ID of the Distance reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Distance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance.setter
    def distance(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Distance reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Distance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Distance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

