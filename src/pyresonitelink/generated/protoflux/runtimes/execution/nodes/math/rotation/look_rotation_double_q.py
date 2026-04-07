"""Generated component: LookRotation_doubleQ."""

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


class LookRotation_doubleQ(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.LookRotation_doubleQ.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rotation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.LookRotation_doubleQ"

    def __init__(self, forward: str | INodeValueOutput[primitives.Double3] | None = None, up: str | INodeValueOutput[primitives.Double3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            forward: Initial value for Forward.
            up: Initial value for Up.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if forward is not None:
            self.forward = forward
        if up is not None:
            self.up = up

    @property
    def forward(self) -> str | None:
        """Target ID of the Forward reference (targets INodeValueOutput[primitives.Double3])."""
        member = self.get_member("Forward")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @forward.setter
    def forward(self, target: str | INodeValueOutput[primitives.Double3] | None) -> None:
        """Set the Forward reference by target ID or INodeValueOutput[primitives.Double3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Forward")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Forward",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3>'),
            )

    @property
    def up(self) -> str | None:
        """Target ID of the Up reference (targets INodeValueOutput[primitives.Double3])."""
        member = self.get_member("Up")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @up.setter
    def up(self, target: str | INodeValueOutput[primitives.Double3] | None) -> None:
        """Set the Up reference by target ID or INodeValueOutput[primitives.Double3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Up")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Up",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3>'),
            )

