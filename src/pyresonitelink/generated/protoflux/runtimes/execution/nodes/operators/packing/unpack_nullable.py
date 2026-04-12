"""Generated component: UnpackNullable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.nullable import Nullable
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnpackNullable(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Unpack Nullable node takes in a nullable, and returns the value and if this nullable has a value.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Packing

    Parameterize with a value type::

        UnpackNullable[primitives.Float]
        UnpackNullable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<>"

    def __init__(self, nullable: str | INodeObjectOutput[Nullable[T]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            nullable: Initial value for Nullable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if nullable is not None:
            self.nullable = nullable

    @property
    def nullable(self) -> str | None:
        """The nullable value."""
        member = self.get_member("Nullable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nullable.setter
    def nullable(self, target: str | INodeObjectOutput[Nullable[T]] | None) -> None:
        """Set the Nullable reference by target ID or INodeObjectOutput[Nullable[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Nullable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Nullable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Nullable<T>>'),
            )

    @property
    def value(self) -> members.EmptyElement | None:
        """Returns the value itself."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set Value. Returns the value itself."""
        self.set_member("Value", value)

    @property
    def has_value(self) -> members.EmptyElement | None:
        """Returns if this has a value."""
        member = self.get_member("HasValue")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_value.setter
    def has_value(self, value: members.EmptyElement) -> None:
        """Set HasValue. Returns if this has a value."""
        self.set_member("HasValue", value)

