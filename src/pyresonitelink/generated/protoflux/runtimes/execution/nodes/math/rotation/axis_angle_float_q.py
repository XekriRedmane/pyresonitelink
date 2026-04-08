"""Generated component: AxisAngle_floatQ."""

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


class AxisAngle_floatQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.AxisAngle_floatQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.AxisAngle_floatQ"

    def __init__(self, axis: str | INodeValueOutput[primitives.Float3] | None = None, angle: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            axis: Initial value for Axis.
            angle: Initial value for Angle.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if axis is not None:
            self.axis = axis
        if angle is not None:
            self.angle = angle

    @property
    def axis(self) -> str | None:
        """Target ID of the Axis reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Axis")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @axis.setter
    def axis(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Axis reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Axis")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Axis",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def angle(self) -> str | None:
        """Target ID of the Angle reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Angle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angle.setter
    def angle(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Angle reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Angle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Angle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

