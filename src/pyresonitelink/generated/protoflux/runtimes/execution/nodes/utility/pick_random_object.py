"""Generated component: PickRandomObject."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PickRandomObject(GenericComponent[T], INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomObject<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    Parameterize with a value type::

        PickRandomObject[primitives.Float]
        PickRandomObject[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomObject<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomObject<>"

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

