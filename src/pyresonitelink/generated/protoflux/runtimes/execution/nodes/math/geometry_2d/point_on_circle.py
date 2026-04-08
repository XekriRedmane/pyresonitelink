"""Generated component: PointOnCircle."""

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


class PointOnCircle(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Point On Circle node returns the point a fractional part of the trace along a circle path of a given radius.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 2D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.PointOnCircle"

    def __init__(self, normalized_position: str | INodeValueOutput[primitives.Float] | None = None, radius: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            normalized_position: Initial value for NormalizedPosition.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if normalized_position is not None:
            self.normalized_position = normalized_position
        if radius is not None:
            self.radius = radius

    @property
    def normalized_position(self) -> str | None:
        """Target ID of the NormalizedPosition reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("NormalizedPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normalized_position.setter
    def normalized_position(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the NormalizedPosition reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NormalizedPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalizedPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def radius(self) -> str | None:
        """Target ID of the Radius reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @radius.setter
    def radius(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Radius reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Radius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

