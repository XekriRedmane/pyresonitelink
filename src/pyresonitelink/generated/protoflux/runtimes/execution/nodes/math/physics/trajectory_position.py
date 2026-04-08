"""Generated component: TrajectoryPosition."""

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


class TrajectoryPosition(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Trajectory Position node takes an initial velocity, force of gravity, drag, and time period, and then outputs the change in position of an object that it would experience. This is very useful for simulating movement.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Physics.TrajectoryPosition"

    def __init__(self, initial_velocity: str | INodeValueOutput[primitives.Float3] | None = None, gravity: str | INodeValueOutput[primitives.Float3] | None = None, drag: str | INodeValueOutput[primitives.Float] | None = None, time: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            initial_velocity: Initial value for InitialVelocity.
            gravity: Initial value for Gravity.
            drag: Initial value for Drag.
            time: Initial value for Time.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if initial_velocity is not None:
            self.initial_velocity = initial_velocity
        if gravity is not None:
            self.gravity = gravity
        if drag is not None:
            self.drag = drag
        if time is not None:
            self.time = time

    @property
    def initial_velocity(self) -> str | None:
        """Target ID of the InitialVelocity reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("InitialVelocity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @initial_velocity.setter
    def initial_velocity(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the InitialVelocity reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InitialVelocity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InitialVelocity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def gravity(self) -> str | None:
        """Target ID of the Gravity reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Gravity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gravity.setter
    def gravity(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Gravity reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Gravity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Gravity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def drag(self) -> str | None:
        """Target ID of the Drag reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Drag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drag.setter
    def drag(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Drag reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Drag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def time(self) -> str | None:
        """Target ID of the Time reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time.setter
    def time(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Time reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Time",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

