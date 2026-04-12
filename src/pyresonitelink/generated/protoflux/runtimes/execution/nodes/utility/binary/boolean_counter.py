"""Generated component: BooleanCounter."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanCounter(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Boolean Counter`` node takes in a list of booleans and counts the number of true and false values, as well as a count of all booleans in the list.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.BooleanCounter"

    @property
    def booleans(self) -> members.SyncList | None:
        """The list of booleans to be counted."""
        member = self.get_member("Booleans")
        if isinstance(member, members.SyncList):
            return member
        return None

    @booleans.setter
    def booleans(self, value: members.SyncList) -> None:
        """Set Booleans. The list of booleans to be counted."""
        self.set_member("Booleans", value)

    @property
    def true_count(self) -> members.EmptyElement | None:
        """The true count of all booleans in the list."""
        member = self.get_member("TrueCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @true_count.setter
    def true_count(self, value: members.EmptyElement) -> None:
        """Set TrueCount. The true count of all booleans in the list."""
        self.set_member("TrueCount", value)

    @property
    def false_count(self) -> members.EmptyElement | None:
        """The false count of all booleans in the list."""
        member = self.get_member("FalseCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @false_count.setter
    def false_count(self, value: members.EmptyElement) -> None:
        """Set FalseCount. The false count of all booleans in the list."""
        self.set_member("FalseCount", value)

    @property
    def total_count(self) -> members.EmptyElement | None:
        """The total count of booleans in this list."""
        member = self.get_member("TotalCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @total_count.setter
    def total_count(self, value: members.EmptyElement) -> None:
        """Set TotalCount. The total count of booleans in this list."""
        self.set_member("TotalCount", value)

