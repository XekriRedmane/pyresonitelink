"""Generated component: GlobalToObjectOutput."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalToObjectOutput(GenericComponent[T], IVariable, INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToObjectOutput<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        GlobalToObjectOutput[np.float32]
        GlobalToObjectOutput[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToObjectOutput<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToObjectOutput<>"

    def __init__(self, global_: str | IGlobalValueProxy[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            global_: Initial value for Global.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if global_ is not None:
            self.global_ = global_

    @property
    def global_(self) -> str | None:
        """Target ID of the Global reference (targets IGlobalValueProxy[T])."""
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @global_.setter
    def global_(self, target: str | IGlobalValueProxy[T] | None) -> None:
        """Set the Global reference by target ID or IGlobalValueProxy[T] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Global",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<T>'),
            )

