"""Generated component: FormatTimespan."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class FormatTimespan(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Format Timespan node takes in a TimeSpan and extra parameters to convert it into a string.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Formatting
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatTimespan"

    def __init__(self, time_span: str | INodeValueOutput[str] | None = None, show_seconds: str | INodeValueOutput[primitives.Bool] | None = None, show_milliseconds: str | INodeValueOutput[primitives.Bool] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time_span: Initial value for TimeSpan.
            show_seconds: Initial value for ShowSeconds.
            show_milliseconds: Initial value for ShowMilliseconds.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time_span is not None:
            self.time_span = time_span
        if show_seconds is not None:
            self.show_seconds = show_seconds
        if show_milliseconds is not None:
            self.show_milliseconds = show_milliseconds
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def time_span(self) -> str | None:
        """Target ID of the TimeSpan reference (targets INodeValueOutput[str])."""
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

    @property
    def show_seconds(self) -> str | None:
        """Target ID of the ShowSeconds reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ShowSeconds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_seconds.setter
    def show_seconds(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ShowSeconds reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ShowSeconds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShowSeconds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def show_milliseconds(self) -> str | None:
        """Target ID of the ShowMilliseconds reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ShowMilliseconds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_milliseconds.setter
    def show_milliseconds(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ShowMilliseconds reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ShowMilliseconds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShowMilliseconds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
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

