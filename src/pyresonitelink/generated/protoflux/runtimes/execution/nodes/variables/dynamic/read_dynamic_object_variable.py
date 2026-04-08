"""Generated component: ReadDynamicObjectVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReadDynamicObjectVariable(GenericComponent[T], IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicObjectVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        ReadDynamicObjectVariable[primitives.Float]
        ReadDynamicObjectVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicObjectVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicObjectVariable<>"

    def __init__(self, source: str | INodeObjectOutput[Slot] | None = None, path: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            path: Initial value for Path.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if path is not None:
            self.path = path

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Source reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def path(self) -> str | None:
        """Target ID of the Path reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path.setter
    def path(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Path reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Path",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def found_value(self) -> members.EmptyElement | None:
        """The FoundValue member."""
        member = self.get_member("FoundValue")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @found_value.setter
    def found_value(self, value: members.EmptyElement) -> None:
        """Set the FoundValue member."""
        self.set_member("FoundValue", value)

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

