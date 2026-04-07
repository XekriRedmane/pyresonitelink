"""Generated component: FieldAsVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FieldAsVariable(GenericComponent[T], IVariable, INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.FieldAsVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        FieldAsVariable[np.float32]
        FieldAsVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.FieldAsVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.FieldAsVariable<>"

    def __init__(self, field: str | INodeObjectOutput[IValue[T]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            field: Initial value for Field.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if field is not None:
            self.field = field

    @property
    def field(self) -> str | None:
        """Target ID of the Field reference (targets INodeObjectOutput[IValue[T]])."""
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @field.setter
    def field(self, target: str | INodeObjectOutput[IValue[T]] | None) -> None:
        """Set the Field reference by target ID or INodeObjectOutput[IValue[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Field",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IValue<T>>'),
            )

