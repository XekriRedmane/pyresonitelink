"""Generated component: CharsToString."""

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


class CharsToString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Chars To Strings node takes in a Collection of Chars and converts it into a string.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.CharsToString"

    def __init__(self, values: str | INodeObjectOutput[IEnumerable[primitives.Char]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            values: Initial value for Values.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if values is not None:
            self.values = values

    @property
    def values(self) -> str | None:
        """The list of characters to form into a string."""
        member = self.get_member("Values")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @values.setter
    def values(self, target: str | INodeObjectOutput[IEnumerable[primitives.Char]] | None) -> None:
        """Set the Values reference by target ID or INodeObjectOutput[IEnumerable[primitives.Char]] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Values")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Values",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<IEnumerable<char>>'),
            )

