"""Generated component: SimplexNoise_4D."""

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


class SimplexNoise_4D(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.SimplexNoise_4D.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Random
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.SimplexNoise_4D"

    def __init__(self, position: str | INodeValueOutput[primitives.Float4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position: Initial value for Position.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position is not None:
            self.position = position

    @property
    def position(self) -> str | None:
        """Target ID of the Position reference (targets INodeValueOutput[primitives.Float4])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | INodeValueOutput[primitives.Float4] | None) -> None:
        """Set the Position reference by target ID or INodeValueOutput[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float4>'),
            )

