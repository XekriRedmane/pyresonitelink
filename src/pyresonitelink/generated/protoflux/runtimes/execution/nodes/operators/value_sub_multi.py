"""Generated component: ValueSubMulti."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueSubMulti(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators

    Parameterize with a value type::

        ValueSubMulti[np.float32]
        ValueSubMulti[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<>"

    @property
    def inputs(self) -> members.SyncList | None:
        """The Inputs member."""
        member = self.get_member("Inputs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @inputs.setter
    def inputs(self, value: members.SyncList) -> None:
        """Set the Inputs member."""
        self.set_member("Inputs", value)

