"""Generated component: ConstructDateTime."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.date_time_kind import DateTimeKind
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConstructDateTime(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.ConstructDateTime.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time/DateTime
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.ConstructDateTime"

    def __init__(self, year: str | INodeValueOutput[primitives.Int] | None = None, month: str | INodeValueOutput[primitives.Int] | None = None, day: str | INodeValueOutput[primitives.Int] | None = None, hour: str | INodeValueOutput[primitives.Int] | None = None, minute: str | INodeValueOutput[primitives.Int] | None = None, second: str | INodeValueOutput[primitives.Int] | None = None, millisecond: str | INodeValueOutput[primitives.Int] | None = None, kind: str | INodeValueOutput[DateTimeKind] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            year: Initial value for Year.
            month: Initial value for Month.
            day: Initial value for Day.
            hour: Initial value for Hour.
            minute: Initial value for Minute.
            second: Initial value for Second.
            millisecond: Initial value for Millisecond.
            kind: Initial value for Kind.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if day is not None:
            self.day = day
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if second is not None:
            self.second = second
        if millisecond is not None:
            self.millisecond = millisecond
        if kind is not None:
            self.kind = kind

    @property
    def year(self) -> str | None:
        """Target ID of the Year reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Year")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @year.setter
    def year(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Year reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Year")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Year",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def month(self) -> str | None:
        """Target ID of the Month reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Month")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @month.setter
    def month(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Month reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Month")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Month",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def day(self) -> str | None:
        """Target ID of the Day reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Day")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @day.setter
    def day(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Day reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Day")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Day",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def hour(self) -> str | None:
        """Target ID of the Hour reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Hour")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hour.setter
    def hour(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Hour reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Hour")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Hour",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def minute(self) -> str | None:
        """Target ID of the Minute reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Minute")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @minute.setter
    def minute(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Minute reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Minute")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Minute",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def second(self) -> str | None:
        """Target ID of the Second reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Second")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @second.setter
    def second(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Second reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Second")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Second",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def millisecond(self) -> str | None:
        """Target ID of the Millisecond reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Millisecond")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @millisecond.setter
    def millisecond(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Millisecond reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Millisecond")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Millisecond",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def kind(self) -> str | None:
        """Target ID of the Kind reference (targets INodeValueOutput[DateTimeKind])."""
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

