"""Generated component: FromBaseValue."""

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


class FromBaseValue(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Quantity

    Parameterize with a value type::

        FromBaseValue[primitives.Float]
        FromBaseValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<>"

    def __init__(self, base_value: str | INodeValueOutput[primitives.Double] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_value: Initial value for BaseValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_value is not None:
            self.base_value = base_value

    @property
    def base_value(self) -> str | None:
        """Target ID of the BaseValue reference (targets INodeValueOutput[primitives.Double])."""
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_value.setter
    def base_value(self, target: str | INodeValueOutput[primitives.Double] | None) -> None:
        """Set the BaseValue reference by target ID or INodeValueOutput[primitives.Double] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

