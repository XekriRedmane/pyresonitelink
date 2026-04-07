"""Generated component: Parse_Long."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.number_styles import NumberStyles
from pyresonitelink.generated._types.iformat_provider import IFormatProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Parse_Long(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.Parse_Long.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Parsing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.Parse_Long"

    def __init__(self, str_: str | INodeObjectOutput[str] | None = None, number_style: str | INodeValueOutput[NumberStyles] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            number_style: Initial value for NumberStyle.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if number_style is not None:
            self.number_style = number_style
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def str_(self) -> str | None:
        """Target ID of the Str reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Str",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def number_style(self) -> str | None:
        """Target ID of the NumberStyle reference (targets INodeValueOutput[NumberStyles])."""
        member = self.get_member("NumberStyle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @number_style.setter
    def number_style(self, target: str | INodeValueOutput[NumberStyles] | None) -> None:
        """Set the NumberStyle reference by target ID or INodeValueOutput[NumberStyles] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NumberStyle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NumberStyle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<NumberStyles>'),
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

    @property
    def value(self) -> members.EmptyElement | None:
        """The Value member."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set the Value member."""
        self.set_member("Value", value)

    @property
    def is_parsed(self) -> members.EmptyElement | None:
        """The IsParsed member."""
        member = self.get_member("IsParsed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_parsed.setter
    def is_parsed(self, value: members.EmptyElement) -> None:
        """Set the IsParsed member."""
        self.set_member("IsParsed", value)

