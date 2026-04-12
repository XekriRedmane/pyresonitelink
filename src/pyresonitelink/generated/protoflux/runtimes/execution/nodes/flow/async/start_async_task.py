"""Generated component: StartAsyncTask."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StartAsyncTask(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Start Async Task node starts a new ExecutionContext using async flow at the current impulse.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.StartAsyncTask"

    def __init__(self, task_start: str | INodeOperation | None = None, on_started: str | INodeOperation | None = None, on_failed: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            task_start: Initial value for TaskStart.
            on_started: Initial value for OnStarted.
            on_failed: Initial value for OnFailed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if task_start is not None:
            self.task_start = task_start
        if on_started is not None:
            self.on_started = on_started
        if on_failed is not None:
            self.on_failed = on_failed

    @property
    def task_start(self) -> str | None:
        """The new ExecutionContext made by the node. This impulse chain is async and will run until it encounters any sort of delay, at which it will continue execution along the ``OnStarted`` chain and follow standard sync/async flow.

The context made by this node is nested, meaning that any context-specific things, such as locals, are duplicated from the context that ``*`` comes from. Any future changes to context-specific things will not be reflected in the ``OnStarted`` chain and vice versa."""
        member = self.get_member("TaskStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @task_start.setter
    def task_start(self, target: str | INodeOperation | None) -> None:
        """Set the TaskStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("TaskStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TaskStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_started(self) -> str | None:
        """Fires once ``TaskStart`` encounters any sort of delay, effectively running at the same time given the now-separate contexts."""
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_started.setter
    def on_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_failed(self) -> str | None:
        """Fires if the task was unable to be started. This only fires if ``TaskStart`` is not connected to any node."""
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_failed.setter
    def on_failed(self, target: str | INodeOperation | None) -> None:
        """Set the OnFailed reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

