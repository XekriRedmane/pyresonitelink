"""Generated component: ValueMultiLerp."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueMultiLerp(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Multi Lerp node takes in any number of lerp point inputs along with a lerp value of which it lerps linearly towards, then returns the value over time.

This is clamped, meaning that you are stuck with being in between all lerp input values.

This node is the multi version of the Value Lerp node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Interpolation

    Parameterize with a value type::

        ValueMultiLerp[primitives.Float]
        ValueMultiLerp[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<>"

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
        """The lerp value points."""
        member = self.get_member("Operands")
        if isinstance(member, members.SyncList):
            return member
        return None

    @operands.setter
    def operands(self, value: members.SyncList) -> None:
        """Set Operands. The lerp value points."""
        self.set_member("Operands", value)

    @property
    def lerp(self) -> str | None:
        """The lerp value between all points."""
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

