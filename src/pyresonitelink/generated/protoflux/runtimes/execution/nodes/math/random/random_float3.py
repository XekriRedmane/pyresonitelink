"""Generated component: RandomFloat3."""

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


class RandomFloat3(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomFloat3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Random
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomFloat3"

    def __init__(self, min: str | INodeValueOutput[primitives.Float3] | None = None, max: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min: Initial value for Min.
            max: Initial value for Max.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def min(self) -> str | None:
        """Target ID of the Min reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min.setter
    def min(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Min reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Min",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def max(self) -> str | None:
        """Target ID of the Max reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max.setter
    def max(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Max reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Max",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

