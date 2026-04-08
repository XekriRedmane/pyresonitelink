"""Generated component: MultiSlerpWithMagnitude_Float2."""

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


class MultiSlerpWithMagnitude_Float2(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.MultiSlerpWithMagnitude_Float2.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Interpolation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.MultiSlerpWithMagnitude_Float2"

    def __init__(self, lerp: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if lerp is not None:
            self.lerp = lerp

    @property
    def operands(self) -> members.SyncList | None:
        """The Operands member."""
        member = self.get_member("Operands")
        if isinstance(member, members.SyncList):
            return member
        return None

    @operands.setter
    def operands(self, value: members.SyncList) -> None:
        """Set the Operands member."""
        self.set_member("Operands", value)

    @property
    def lerp(self) -> str | None:
        """Target ID of the Lerp reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp.setter
    def lerp(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Lerp reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Lerp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

