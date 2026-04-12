"""Generated component: ValueSource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.isource import ISource
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueSource(GenericComponent[T], IVariable, ISource, INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """HTML Visual unavailable due to wiki limitations

thumb|right|alt=Six source nodes of type string, string, bool, float3, floatQ, and int all outputting to display nodes.|Source nodes for the base fields of an empty slot being outputted to display nodes.

The Source node allows one to access the value of the primitive or object that an IValue contains. This node almost never should be created directly through the node menu, lest one knows exactly what they are doing. Source nodes are created by dragging out a field from an inspector, opening the Context menu, then pressing ``Source``.

To access the underlying value that any arbitrary IValue contains, one can spawn out a bare version of this node from the ProtoFlux menu, attach a GlobalReference> to the slot of the node, drag the component header into the ``Source`` field of the Source node, and finally input the IValue into the Reference field of the GlobalReference. This can allow for a more efficient way to conditionally change values if said values are in different fields.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        ValueSource[primitives.Float]
        ValueSource[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.ValueSource<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.ValueSource<>"

    def __init__(self, source: str | IGlobalValueProxy[IValue[T]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IGlobalValueProxy[IValue[T]])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IGlobalValueProxy[IValue[T]] | None) -> None:
        """Set the Source reference by target ID or IGlobalValueProxy[IValue[T]] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.IValue<T>>'),
            )

