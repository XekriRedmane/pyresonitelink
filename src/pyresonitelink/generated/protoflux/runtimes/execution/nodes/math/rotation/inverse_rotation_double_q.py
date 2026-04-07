"""Generated component: InverseRotation_doubleQ."""

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


class InverseRotation_doubleQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.InverseRotation_doubleQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.InverseRotation_doubleQ"

    def __init__(self, q: str | INodeValueOutput[primitives.DoubleQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            q: Initial value for Q.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if q is not None:
            self.q = q

    @property
    def q(self) -> str | None:
        """Target ID of the Q reference (targets INodeValueOutput[primitives.DoubleQ])."""
        member = self.get_member("Q")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @q.setter
    def q(self, target: str | INodeValueOutput[primitives.DoubleQ] | None) -> None:
        """Set the Q reference by target ID or INodeValueOutput[primitives.DoubleQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Q")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Q",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>'),
            )

