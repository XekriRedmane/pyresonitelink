"""Generated component: SetDateTimeKind."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.date_time_kind import DateTimeKind
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetDateTimeKind(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Set DateTime Kind`` node takes in a DateTime and an enum Kind of DateTime, then returns the new DateTime value.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time/DateTime
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.SetDateTimeKind"

    def __init__(self, date_time: str | INodeValueOutput[str] | None = None, kind: str | INodeValueOutput[DateTimeKind] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            date_time: Initial value for DateTime.
            kind: Initial value for Kind.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if date_time is not None:
            self.date_time = date_time
        if kind is not None:
            self.kind = kind

    @property
    def date_time(self) -> str | None:
        """The DateTime to change."""
        member = self.get_member("DateTime")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @date_time.setter
    def date_time(self, target: str | INodeValueOutput[str] | None) -> None:
        """Set the DateTime reference by target ID or INodeValueOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DateTime")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DateTime",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<DateTime>'),
            )

    @property
    def kind(self) -> str | None:
        """The kind to set for this DateTime."""
        member = self.get_member("Kind")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @kind.setter
    def kind(self, target: str | INodeValueOutput[DateTimeKind] | None) -> None:
        """Set the Kind reference by target ID or INodeValueOutput[DateTimeKind] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Kind")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Kind",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<DateTimeKind>'),
            )

