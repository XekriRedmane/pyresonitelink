"""Generated component: LocalLeakyImpulseBucket."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalLeakyImpulseBucket(GeneratedComponent, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalLeakyImpulseBucket.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalLeakyImpulseBucket"

    def __init__(self, pulse: str | ISyncNodeOperation | None = None, overflow: str | INodeOperation | None = None, interval: str | INodeValueOutput[primitives.Float] | None = None, maximum_capacity: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pulse: Initial value for Pulse.
            overflow: Initial value for Overflow.
            interval: Initial value for Interval.
            maximum_capacity: Initial value for MaximumCapacity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pulse is not None:
            self.pulse = pulse
        if overflow is not None:
            self.overflow = overflow
        if interval is not None:
            self.interval = interval
        if maximum_capacity is not None:
            self.maximum_capacity = maximum_capacity

    @property
    def pulse(self) -> str | None:
        """Target ID of the Pulse reference (targets ISyncNodeOperation)."""
        member = self.get_member("Pulse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pulse.setter
    def pulse(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Pulse reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Pulse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pulse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def overflow(self) -> str | None:
        """Target ID of the Overflow reference (targets INodeOperation)."""
        member = self.get_member("Overflow")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overflow.setter
    def overflow(self, target: str | INodeOperation | None) -> None:
        """Set the Overflow reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Overflow")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Overflow",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def interval(self) -> str | None:
        """Target ID of the Interval reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Interval")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interval.setter
    def interval(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Interval reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Interval")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Interval",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def maximum_capacity(self) -> str | None:
        """Target ID of the MaximumCapacity reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("MaximumCapacity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @maximum_capacity.setter
    def maximum_capacity(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the MaximumCapacity reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MaximumCapacity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaximumCapacity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def current_capacity(self) -> members.EmptyElement | None:
        """The CurrentCapacity member."""
        member = self.get_member("CurrentCapacity")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @current_capacity.setter
    def current_capacity(self, value: members.EmptyElement) -> None:
        """Set the CurrentCapacity member."""
        self.set_member("CurrentCapacity", value)

    @property
    def trigger(self) -> members.EmptyElement | None:
        """The Trigger member."""
        member = self.get_member("Trigger")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.EmptyElement) -> None:
        """Set the Trigger member."""
        self.set_member("Trigger", value)

    @property
    def reset(self) -> members.EmptyElement | None:
        """The Reset member."""
        member = self.get_member("Reset")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reset.setter
    def reset(self, value: members.EmptyElement) -> None:
        """Set the Reset member."""
        self.set_member("Reset", value)

