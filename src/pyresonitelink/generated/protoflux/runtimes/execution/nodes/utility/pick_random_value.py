"""Generated component: PickRandomValue."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PickRandomValue(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Pick Random Value node takes in a list of value of the same Type and then returns one of them at random. Since this is a data node, displaying the output value will cycle through them randomly once per frame.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    Parameterize with a value type::

        PickRandomValue[primitives.Float]
        PickRandomValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<>"

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

