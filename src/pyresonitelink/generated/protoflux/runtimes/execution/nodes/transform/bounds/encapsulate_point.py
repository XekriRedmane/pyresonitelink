"""Generated component: EncapsulatePoint."""

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


class EncapsulatePoint(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulatePoint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulatePoint"

    def __init__(self, bounds: str | INodeValueOutput[primitives.BoundingBox] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bounds: Initial value for Bounds.
            point: Initial value for Point.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bounds is not None:
            self.bounds = bounds
        if point is not None:
            self.point = point

    @property
    def bounds(self) -> str | None:
        """Target ID of the Bounds reference (targets INodeValueOutput[primitives.BoundingBox])."""
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds.setter
    def bounds(self, target: str | INodeValueOutput[primitives.BoundingBox] | None) -> None:
        """Set the Bounds reference by target ID or INodeValueOutput[primitives.BoundingBox] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>'),
            )

    @property
    def point(self) -> str | None:
        """Target ID of the Point reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point.setter
    def point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

