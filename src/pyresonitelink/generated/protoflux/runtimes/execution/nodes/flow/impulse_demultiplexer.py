"""Generated component: ImpulseDemultiplexer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImpulseDemultiplexer(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """An Impulse Demultiplexer is useful for condensing down multiple lines of execution code into one line. For example, let's say that you have 10 buttons, and you want to change a text to 10 different strings, positions, and colors using those 10 buttons. Using an Impulse Demultiplexer you can put each button into Operations (List of Impulses) on the impulse demultiplexer, then use the index in 3 different Multiplexers. Writing the multiplexer's output to the properties of the text object now allows you to reduce what would take up to 70 nodes and 60 connections down to 43 nodes and 43 connections. And also it makes it a lot less complex and easier to read.

This node could commonly be called a switch, switchboard, router, or an impulse array.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseDemultiplexer"

    def __init__(self, on_triggered: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_triggered: Initial value for OnTriggered.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_triggered is not None:
            self.on_triggered = on_triggered

    @property
    def operations(self) -> members.SyncList | None:
        """List of impulses to take impulses from."""
        member = self.get_member("Operations")
        if isinstance(member, members.SyncList):
            return member
        return None

    @operations.setter
    def operations(self, value: members.SyncList) -> None:
        """Set Operations. List of impulses to take impulses from."""
        self.set_member("Operations", value)

    @property
    def on_triggered(self) -> str | None:
        """Sends an impulse when any one of Operations (List of Impulses) is called."""
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_triggered.setter
    def on_triggered(self, target: str | INodeOperation | None) -> None:
        """Set the OnTriggered reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnTriggered",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def index_(self) -> members.EmptyElement | None:
        """The position of the Impulse on the list of Operations (List of Impulses) that was called starting at 0 for the first one.

Only exists during OnTriggered (Continuation)"""
        member = self.get_member("Index")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @index_.setter
    def index_(self, value: members.EmptyElement) -> None:
        """Set Index. The position of the Impulse on the list of Operations (List of Impulses) that was called starting at 0 for the first one.

Only exists during OnTriggered (Continuation)"""
        self.set_member("Index", value)

