"""Generated component: AngularVelocityDelta_floatQ."""

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


class AngularVelocityDelta_floatQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.AngularVelocityDelta_floatQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.AngularVelocityDelta_floatQ"

    def __init__(self, angular_velocity: str | INodeValueOutput[primitives.Float3] | None = None, delta_time: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            angular_velocity: Initial value for AngularVelocity.
            delta_time: Initial value for DeltaTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if angular_velocity is not None:
            self.angular_velocity = angular_velocity
        if delta_time is not None:
            self.delta_time = delta_time

    @property
    def angular_velocity(self) -> str | None:
        """Target ID of the AngularVelocity reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("AngularVelocity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angular_velocity.setter
    def angular_velocity(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the AngularVelocity reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("AngularVelocity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AngularVelocity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def delta_time(self) -> str | None:
        """Target ID of the DeltaTime reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("DeltaTime")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delta_time.setter
    def delta_time(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the DeltaTime reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DeltaTime")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DeltaTime",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

