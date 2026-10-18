"""Generated component: JoinString."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ienumerable import IEnumerable
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class JoinString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Join String node takes in an IEnumerable and a string separator, then returns the entire string array as a Collection.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.JoinString"

    def __init__(self, values: str | INodeObjectOutput[IEnumerable[primitives.String]] | None = None, separator: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            values: Initial value for Values.
            separator: Initial value for Separator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if values is not None:
            self.values = values
        if separator is not None:
            self.separator = separator

    @property
    def values(self) -> str | None:
        """All the values as a collection."""
        member = self.get_member("Values")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @values.setter
    def values(self, target: str | INodeObjectOutput[IEnumerable[primitives.String]] | None) -> None:
        """Set the Values reference by target ID or INodeObjectOutput[IEnumerable[primitives.String]] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Values")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Values",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<IEnumerable<string>>'),
            )

    @property
    def separator(self) -> str | None:
        """The string separator used to separate the string collection."""
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @separator.setter
    def separator(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Separator reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Separator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Separator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

