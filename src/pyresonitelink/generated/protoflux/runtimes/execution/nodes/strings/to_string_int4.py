"""Generated component: ToString_Int4."""

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


class ToString_Int4(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_Int4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_Int4"

    def __init__(self, v: str | INodeValueOutput[primitives.Int4] | None = None, format_: str | INodeObjectOutput[str] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            v: Initial value for V.
            format_: Initial value for Format.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if v is not None:
            self.v = v
        if format_ is not None:
            self.format_ = format_
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def v(self) -> str | None:
        """Target ID of the V reference (targets INodeValueOutput[primitives.Int4])."""
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @v.setter
    def v(self, target: str | INodeValueOutput[primitives.Int4] | None) -> None:
        """Set the V reference by target ID or INodeValueOutput[primitives.Int4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "V",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int4>'),
            )

    @property
    def format_(self) -> str | None:
        """Target ID of the Format reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Format")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_.setter
    def format_(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Format reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Format")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Format",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
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

