"""Generated component: FormatDateTimeAsDate."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iformat_provider import IFormatProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FormatDateTimeAsDate(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatDateTimeAsDate.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Formatting
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatDateTimeAsDate"

    def __init__(self, date: str | INodeValueOutput[str] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            date: Initial value for Date.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if date is not None:
            self.date = date
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def date(self) -> str | None:
        """Target ID of the Date reference (targets INodeValueOutput[str])."""
        member = self.get_member("Date")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @date.setter
    def date(self, target: str | INodeValueOutput[str] | None) -> None:
        """Set the Date reference by target ID or INodeValueOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Date")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Date",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<DateTime>'),
            )

    @property
    def format_provider(self) -> str | None:
        """Target ID of the FormatProvider reference (targets INodeObjectOutput[IFormatProvider])."""
        member = self.get_member("FormatProvider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_provider.setter
    def format_provider(self, target: str | INodeObjectOutput[IFormatProvider] | None) -> None:
        """Set the FormatProvider reference by target ID or INodeObjectOutput[IFormatProvider] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FormatProvider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatProvider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<IFormatProvider>'),
            )

