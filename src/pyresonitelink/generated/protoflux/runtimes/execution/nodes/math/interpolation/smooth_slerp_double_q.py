"""Generated component: SmoothSlerp_doubleQ."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_update_receiver import IExecutionUpdateReceiver
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SmoothSlerp_doubleQ(GeneratedComponent, INodeValueOutput, IExecutionUpdateReceiver, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SmoothSlerp_doubleQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Interpolation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SmoothSlerp_doubleQ"

    def __init__(self, input_: str | INodeValueOutput[primitives.DoubleQ] | None = None, speed: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_: Initial value for Input.
            speed: Initial value for Speed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_ is not None:
            self.input_ = input_
        if speed is not None:
            self.speed = speed

    @property
    def input_(self) -> str | None:
        """Target ID of the Input reference (targets INodeValueOutput[primitives.DoubleQ])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeValueOutput[primitives.DoubleQ] | None) -> None:
        """Set the Input reference by target ID or INodeValueOutput[primitives.DoubleQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>'),
            )

    @property
    def speed(self) -> str | None:
        """Target ID of the Speed reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @speed.setter
    def speed(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Speed reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Speed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

