"""Generated component: BooleanCounter."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanCounter(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.BooleanCounter.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.BooleanCounter"

    @property
    def booleans(self) -> members.SyncList | None:
        """The Booleans member."""
        member = self.get_member("Booleans")
        if isinstance(member, members.SyncList):
            return member
        return None

    @booleans.setter
    def booleans(self, value: members.SyncList) -> None:
        """Set the Booleans member."""
        self.set_member("Booleans", value)

    @property
    def true_count(self) -> members.EmptyElement | None:
        """The TrueCount member."""
        member = self.get_member("TrueCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @true_count.setter
    def true_count(self, value: members.EmptyElement) -> None:
        """Set the TrueCount member."""
        self.set_member("TrueCount", value)

    @property
    def false_count(self) -> members.EmptyElement | None:
        """The FalseCount member."""
        member = self.get_member("FalseCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @false_count.setter
    def false_count(self, value: members.EmptyElement) -> None:
        """Set the FalseCount member."""
        self.set_member("FalseCount", value)

    @property
    def total_count(self) -> members.EmptyElement | None:
        """The TotalCount member."""
        member = self.get_member("TotalCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @total_count.setter
    def total_count(self, value: members.EmptyElement) -> None:
        """Set the TotalCount member."""
        self.set_member("TotalCount", value)

