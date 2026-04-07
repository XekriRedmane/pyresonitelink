"""Generated component: FromEuler_floatQ."""

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


class FromEuler_floatQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.FromEuler_floatQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.FromEuler_floatQ"

    def __init__(self, angles: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            angles: Initial value for Angles.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if angles is not None:
            self.angles = angles

    @property
    def angles(self) -> str | None:
        """Target ID of the Angles reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Angles")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angles.setter
    def angles(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Angles reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Angles")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Angles",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

