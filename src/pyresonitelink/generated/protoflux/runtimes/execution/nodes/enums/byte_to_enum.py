"""Generated component: ByteToEnum."""

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


class ByteToEnum(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ByteToEnum<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Enums

    Parameterize with a value type::

        ByteToEnum[primitives.Float]
        ByteToEnum[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ByteToEnum<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ByteToEnum<>"

    def __init__(self, value: str | INodeValueOutput[primitives.Byte] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[primitives.Byte])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[primitives.Byte] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[primitives.Byte] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<byte>'),
            )

