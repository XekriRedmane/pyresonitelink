"""Generated component: ValueMaxMulti."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueMaxMulti(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math

    Parameterize with a value type::

        ValueMaxMulti[np.float32]
        ValueMaxMulti[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<>"

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

