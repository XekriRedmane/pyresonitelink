"""Generated component: Parse_Ushort3."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Parse_Ushort3(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.Parse_Ushort3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Parsing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.Parse_Ushort3"

    def __init__(self, str_: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_

    @property
    def str_(self) -> str | None:
        """Target ID of the Str reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[primitives.String] instance."""
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

