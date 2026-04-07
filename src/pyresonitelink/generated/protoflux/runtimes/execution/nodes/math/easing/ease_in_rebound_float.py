"""Generated component: EaseInReboundFloat."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EaseInReboundFloat(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInReboundFloat.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Easing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInReboundFloat"

    def __init__(self, time: str | INodeValueOutput[np.float32] | None = None, rebound_amplitude: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time: Initial value for Time.
            rebound_amplitude: Initial value for ReboundAmplitude.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time is not None:
            self.time = time
        if rebound_amplitude is not None:
            self.rebound_amplitude = rebound_amplitude

    @property
    def time(self) -> str | None:
        """Target ID of the Time reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time.setter
    def time(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Time reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Time",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def rebound_amplitude(self) -> str | None:
        """Target ID of the ReboundAmplitude reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("ReboundAmplitude")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rebound_amplitude.setter
    def rebound_amplitude(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the ReboundAmplitude reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ReboundAmplitude")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReboundAmplitude",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

