"""Generated component: FormatString."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iformat_provider import IFormatProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FormatString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node simply calls the C# String.Format function using the provided parameters. It allows you to take a string like "I am a {0} who likes to do {1} while {2}" And populate {0}, {1}, and {2} with values. If you plug any value into the list of inputs for the Parameters, it will auto add a cast node into an object.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Formatting
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatString"

    def __init__(self, format_: str | INodeObjectOutput[primitives.String] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            format_: Initial value for Format.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if format_ is not None:
            self.format_ = format_
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def format_(self) -> str | None:
        """Target ID of the Format reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Format")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_.setter
    def format_(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Format reference by target ID or INodeObjectOutput[primitives.String] instance."""
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
    def parameters(self) -> members.SyncList | None:
        """The Parameters member."""
        member = self.get_member("Parameters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @parameters.setter
    def parameters(self, value: members.SyncList) -> None:
        """Set the Parameters member."""
        self.set_member("Parameters", value)

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

