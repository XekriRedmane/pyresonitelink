"""Generated component: AsyncSequence."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AsyncSequence(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncSequence.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncSequence"

    @property
    def calls(self) -> members.SyncList | None:
        """The Calls member."""
        member = self.get_member("Calls")
        if isinstance(member, members.SyncList):
            return member
        return None

    @calls.setter
    def calls(self, value: members.SyncList) -> None:
        """Set the Calls member."""
        self.set_member("Calls", value)

