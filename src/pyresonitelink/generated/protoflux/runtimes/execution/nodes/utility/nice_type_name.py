"""Generated component: NiceTypeName."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.type import Type
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NiceTypeName(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Nice Type Name`` node takes in a Type as well as optional open and close symbols, then returns the pretty human readable name of the provided type. For example, using a type that has a float and connecting it to this node, it will return ``float``.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.NiceTypeName"

    def __init__(self, type_: str | INodeObjectOutput[Type] | None = None, open_symbol: str | INodeObjectOutput[primitives.String] | None = None, close_symbol: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            type_: Initial value for Type.
            open_symbol: Initial value for OpenSymbol.
            close_symbol: Initial value for CloseSymbol.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if type_ is not None:
            self.type_ = type_
        if open_symbol is not None:
            self.open_symbol = open_symbol
        if close_symbol is not None:
            self.close_symbol = close_symbol

    @property
    def type_(self) -> str | None:
        """The type we want the nice name of."""
        member = self.get_member("Type")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @type_.setter
    def type_(self, target: str | INodeObjectOutput[Type] | None) -> None:
        """Set the Type reference by target ID or INodeObjectOutput[Type] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Type")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Type",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Type>'),
            )

    @property
    def open_symbol(self) -> str | None:
        """The open symbol from this type (defaults to ``<``)."""
        member = self.get_member("OpenSymbol")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @open_symbol.setter
    def open_symbol(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the OpenSymbol reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("OpenSymbol")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OpenSymbol",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def close_symbol(self) -> str | None:
        """The close symbol from this type (defaults to ``>``)."""
        member = self.get_member("CloseSymbol")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_symbol.setter
    def close_symbol(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the CloseSymbol reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("CloseSymbol")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloseSymbol",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

