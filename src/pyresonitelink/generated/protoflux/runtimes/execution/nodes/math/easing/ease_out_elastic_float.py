"""Generated component: EaseOutElasticFloat."""

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


class EaseOutElasticFloat(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseOutElasticFloat.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Easing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseOutElasticFloat"

    def __init__(self, time: str | INodeValueOutput[primitives.Float] | None = None, amplitude: str | INodeValueOutput[primitives.Float] | None = None, period: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time: Initial value for Time.
            amplitude: Initial value for Amplitude.
            period: Initial value for Period.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time is not None:
            self.time = time
        if amplitude is not None:
            self.amplitude = amplitude
        if period is not None:
            self.period = period

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

    @property
    def amplitude(self) -> str | None:
        """Target ID of the Amplitude reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Amplitude")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @amplitude.setter
    def amplitude(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Amplitude reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Amplitude")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Amplitude",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def period(self) -> str | None:
        """Target ID of the Period reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Period")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @period.setter
    def period(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Period reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Period")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Period",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

