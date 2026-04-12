"""Generated component: Sequence."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Sequence(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Sequence node performs each of the provided impulses in order, waiting for the chain of each impulse to finish before executing the next one.

This can be useful for organizational purposes or to avoid code duplication if something needs to be performed after a bunch of branching paths.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Sequence"

    @property
    def calls(self) -> members.SyncList | None:
        """The list of impulses to fire in order. This node will start at the first impulse, and after the context of the impulse finishes, the next impulse is fired. Repeats until the last impulse finishes."""
        member = self.get_member("Calls")
        if isinstance(member, members.SyncList):
            return member
        return None

    @calls.setter
    def calls(self, value: members.SyncList) -> None:
        """Set Calls. The list of impulses to fire in order. This node will start at the first impulse, and after the context of the impulse finishes, the next impulse is fired. Repeats until the last impulse finishes."""
        self.set_member("Calls", value)

