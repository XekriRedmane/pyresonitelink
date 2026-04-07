"""Generated component: TriangleNormal."""

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


class TriangleNormal(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.TriangleNormal.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.TriangleNormal"

    def __init__(self, point0: str | INodeValueOutput[primitives.Float3] | None = None, point1: str | INodeValueOutput[primitives.Float3] | None = None, point2: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            point2: Initial value for Point2.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if point2 is not None:
            self.point2 = point2

    @property
    def point0(self) -> str | None:
        """Target ID of the Point0 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point0.setter
    def point0(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point0 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def point1(self) -> str | None:
        """Target ID of the Point1 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point1.setter
    def point1(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point1 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def point2(self) -> str | None:
        """Target ID of the Point2 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point2.setter
    def point2(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point2 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def normal(self) -> members.EmptyElement | None:
        """The Normal member."""
        member = self.get_member("Normal")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @normal.setter
    def normal(self, value: members.EmptyElement) -> None:
        """Set the Normal member."""
        self.set_member("Normal", value)

    @property
    def is_valid(self) -> members.EmptyElement | None:
        """The IsValid member."""
        member = self.get_member("IsValid")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_valid.setter
    def is_valid(self, value: members.EmptyElement) -> None:
        """Set the IsValid member."""
        self.set_member("IsValid", value)

