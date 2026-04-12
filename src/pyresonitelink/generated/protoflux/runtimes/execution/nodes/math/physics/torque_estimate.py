"""Generated component: TorqueEstimate."""

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


class TorqueEstimate(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Torque Estimate node takes in the initial torque, drag resistance, and the amount of time it is simulating, then returns the torque simulation value (as a floatQ) that object will rotate in.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Physics.TorqueEstimate"

    def __init__(self, initial_torque: str | INodeValueOutput[primitives.Float3] | None = None, drag: str | INodeValueOutput[primitives.Float] | None = None, time: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            initial_torque: Initial value for InitialTorque.
            drag: Initial value for Drag.
            time: Initial value for Time.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if initial_torque is not None:
            self.initial_torque = initial_torque
        if drag is not None:
            self.drag = drag
        if time is not None:
            self.time = time

    @property
    def initial_torque(self) -> str | None:
        """The amount of push for this torque."""
        member = self.get_member("InitialTorque")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @initial_torque.setter
    def initial_torque(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the InitialTorque reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InitialTorque")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InitialTorque",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def drag(self) -> str | None:
        """The amount of resistance for this torque."""
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
        """The time in between the initial torque and now."""
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

