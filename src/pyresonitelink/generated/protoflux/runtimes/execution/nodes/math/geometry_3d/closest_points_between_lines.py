"""Generated component: ClosestPointsBetweenLines."""

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


class ClosestPointsBetweenLines(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointsBetweenLines.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointsBetweenLines"

    def __init__(self, line_point0: str | INodeValueOutput[primitives.Float3] | None = None, line_dir0: str | INodeValueOutput[primitives.Float3] | None = None, line_point1: str | INodeValueOutput[primitives.Float3] | None = None, line_dir1: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            line_point0: Initial value for LinePoint0.
            line_dir0: Initial value for LineDir0.
            line_point1: Initial value for LinePoint1.
            line_dir1: Initial value for LineDir1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_dir0 is not None:
            self.line_dir0 = line_dir0
        if line_point1 is not None:
            self.line_point1 = line_point1
        if line_dir1 is not None:
            self.line_dir1 = line_dir1

    @property
    def line_point0(self) -> str | None:
        """Target ID of the LinePoint0 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point0.setter
    def line_point0(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LinePoint0 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def line_dir0(self) -> str | None:
        """Target ID of the LineDir0 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LineDir0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_dir0.setter
    def line_dir0(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LineDir0 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LineDir0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LineDir0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def line_point1(self) -> str | None:
        """Target ID of the LinePoint1 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point1.setter
    def line_point1(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LinePoint1 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def line_dir1(self) -> str | None:
        """Target ID of the LineDir1 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LineDir1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_dir1.setter
    def line_dir1(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LineDir1 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LineDir1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LineDir1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def point0(self) -> members.EmptyElement | None:
        """The Point0 member."""
        member = self.get_member("Point0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @point0.setter
    def point0(self, value: members.EmptyElement) -> None:
        """Set the Point0 member."""
        self.set_member("Point0", value)

    @property
    def point1(self) -> members.EmptyElement | None:
        """The Point1 member."""
        member = self.get_member("Point1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @point1.setter
    def point1(self, value: members.EmptyElement) -> None:
        """Set the Point1 member."""
        self.set_member("Point1", value)

