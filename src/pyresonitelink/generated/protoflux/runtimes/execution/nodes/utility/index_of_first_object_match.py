"""Generated component: IndexOfFirstObjectMatch."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IndexOfFirstObjectMatch(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstObjectMatch<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    Parameterize with a value type::

        IndexOfFirstObjectMatch[primitives.Float]
        IndexOfFirstObjectMatch[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstObjectMatch<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstObjectMatch<>"

    def __init__(self, match: str | INodeObjectOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            match: Initial value for Match.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if match is not None:
            self.match = match

    @property
    def match(self) -> str | None:
        """Target ID of the Match reference (targets INodeObjectOutput[T])."""
        member = self.get_member("Match")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @match.setter
    def match(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Match reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Match")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Match",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def values(self) -> members.SyncList | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncList):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncList) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

    @property
    def index_(self) -> members.EmptyElement | None:
        """The Index member."""
        member = self.get_member("Index")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @index_.setter
    def index_(self, value: members.EmptyElement) -> None:
        """Set the Index member."""
        self.set_member("Index", value)

    @property
    def found_match(self) -> members.EmptyElement | None:
        """The FoundMatch member."""
        member = self.get_member("FoundMatch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @found_match.setter
    def found_match(self, value: members.EmptyElement) -> None:
        """Set the FoundMatch member."""
        self.set_member("FoundMatch", value)

