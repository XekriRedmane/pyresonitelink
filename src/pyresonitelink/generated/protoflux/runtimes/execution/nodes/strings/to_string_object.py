"""Generated component: ToString_object."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.object import object
from pyresonitelink.generated._types.iformat_provider import IFormatProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ToString_object(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_object.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_object"

    def __init__(self, object_: str | INodeObjectOutput[object] | None = None, format_: str | INodeObjectOutput[primitives.String] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            object_: Initial value for Object.
            format_: Initial value for Format.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if object_ is not None:
            self.object_ = object_
        if format_ is not None:
            self.format_ = format_
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def object_(self) -> str | None:
        """Target ID of the Object reference (targets INodeObjectOutput[object])."""
        member = self.get_member("Object")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_.setter
    def object_(self, target: str | INodeObjectOutput[object] | None) -> None:
        """Set the Object reference by target ID or INodeObjectOutput[object] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Object")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Object",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<object>'),
            )

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

