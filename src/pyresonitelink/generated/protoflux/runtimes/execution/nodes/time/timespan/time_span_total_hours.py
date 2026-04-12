"""Generated component: TimeSpanTotalHours."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeSpanTotalHours(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``TimeSpan Total Hours`` node takes in a TimeSpan and returns with the amount of hours in that TimeSpan, including the fractional portion of a hour, as well as anything longer than an hour will be added into the total.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time/Timespan
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.TimeSpanTotalHours"

    def __init__(self, time_span: str | INodeValueOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time_span: Initial value for TimeSpan.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time_span is not None:
            self.time_span = time_span

    @property
    def time_span(self) -> str | None:
        """The TimeSpan we are getting info from."""
        member = self.get_member("TimeSpan")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time_span.setter
    def time_span(self, target: str | INodeValueOutput[str] | None) -> None:
        """Set the TimeSpan reference by target ID or INodeValueOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("TimeSpan")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimeSpan",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<TimeSpan>'),
            )

