"""Generated component: DateTimeYear."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DateTimeYear(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The DateTime Year node takes in a DateTime and returns the year of that DateTime.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time/DateTime
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.DateTimeYear"

    def __init__(self, date_time: str | INodeValueOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            date_time: Initial value for DateTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if date_time is not None:
            self.date_time = date_time

    @property
    def date_time(self) -> str | None:
        """Target ID of the DateTime reference (targets INodeValueOutput[str])."""
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

