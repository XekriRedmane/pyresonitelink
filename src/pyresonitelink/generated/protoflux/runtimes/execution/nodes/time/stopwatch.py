"""Generated component: Stopwatch."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Stopwatch(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Stopwatch node keeps track of time when running. Akin to a real stopwatch, it allows one to start time, stop time, and reset time.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.Stopwatch"

    def __init__(self, on_start: str | INodeOperation | None = None, on_stop: str | INodeOperation | None = None, on_reset: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_start: Initial value for OnStart.
            on_stop: Initial value for OnStop.
            on_reset: Initial value for OnReset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_start is not None:
            self.on_start = on_start
        if on_stop is not None:
            self.on_stop = on_stop
        if on_reset is not None:
            self.on_reset = on_reset

    @property
    def time(self) -> members.EmptyElement | None:
        """The time in seconds stored by the stopwatch. This value increments when in the running state and freezes when in the stopped state. If ``Reset`` is pulsed, this output is set to ``0``, but continues the same behavior of the state the watch is in.

Sometimes, it may be desirable to obtain a TimeSpan type from this value. To do so, use a TimeSpan From Seconds node."""
        member = self.get_member("Time")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @time.setter
    def time(self, value: members.EmptyElement) -> None:
        """Set Time. The time in seconds stored by the stopwatch. This value increments when in the running state and freezes when in the stopped state. If ``Reset`` is pulsed, this output is set to ``0``, but continues the same behavior of the state the watch is in.

Sometimes, it may be desirable to obtain a TimeSpan type from this value. To do so, use a TimeSpan From Seconds node."""
        self.set_member("Time", value)

    @property
    def is_running(self) -> members.EmptyElement | None:
        """``True`` if the stopwatch is in a running state, ``False`` otherwise."""
        member = self.get_member("IsRunning")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_running.setter
    def is_running(self, value: members.EmptyElement) -> None:
        """Set IsRunning. ``True`` if the stopwatch is in a running state, ``False`` otherwise."""
        self.set_member("IsRunning", value)

    @property
    def start(self) -> members.EmptyElement | None:
        """Starts the stopwatch, putting it in the running state."""
        member = self.get_member("Start")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @start.setter
    def start(self, value: members.EmptyElement) -> None:
        """Set Start. Starts the stopwatch, putting it in the running state."""
        self.set_member("Start", value)

    @property
    def stop(self) -> members.EmptyElement | None:
        """Stops the stopwatch, putting it in the stopped state."""
        member = self.get_member("Stop")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @stop.setter
    def stop(self, value: members.EmptyElement) -> None:
        """Set Stop. Stops the stopwatch, putting it in the stopped state."""
        self.set_member("Stop", value)

    @property
    def reset(self) -> members.EmptyElement | None:
        """Resets the stopwatch time. Does not affect the state of the stopwatch."""
        member = self.get_member("Reset")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reset.setter
    def reset(self, value: members.EmptyElement) -> None:
        """Set Reset. Resets the stopwatch time. Does not affect the state of the stopwatch."""
        self.set_member("Reset", value)

    @property
    def on_start(self) -> str | None:
        """Target ID of the OnStart reference (targets INodeOperation)."""
        member = self.get_member("OnStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_start.setter
    def on_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_stop(self) -> str | None:
        """Target ID of the OnStop reference (targets INodeOperation)."""
        member = self.get_member("OnStop")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_stop.setter
    def on_stop(self, target: str | INodeOperation | None) -> None:
        """Set the OnStop reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStop")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStop",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_reset(self) -> str | None:
        """Sends an impulse when ``Reset`` is impulsed. Is not affected by the state of the stopwatch."""
        member = self.get_member("OnReset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_reset.setter
    def on_reset(self, target: str | INodeOperation | None) -> None:
        """Set the OnReset reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

