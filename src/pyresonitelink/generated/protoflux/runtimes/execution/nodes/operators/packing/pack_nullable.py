"""Generated component: PackNullable."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackNullable(GenericComponent[T], INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Packing

    Parameterize with a value type::

        PackNullable[primitives.Float]
        PackNullable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<>"

    def __init__(self, value: str | INodeValueOutput[T] | None = None, has_value: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            has_value: Initial value for HasValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if has_value is not None:
            self.has_value = has_value

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def has_value(self) -> str | None:
        """Target ID of the HasValue reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("HasValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_value.setter
    def has_value(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the HasValue reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HasValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

