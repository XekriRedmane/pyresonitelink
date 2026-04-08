"""Generated component: ObjectMultiplex."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectMultiplex(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Multiplex node is a node that changes its output to a specific input based on its index.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    **Footnotes**: * It can be made bigger or smaller while editing the flux.

ProtoFlux:Utility

    Parameterize with a value type::

        ObjectMultiplex[primitives.Float]
        ObjectMultiplex[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectMultiplex<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectMultiplex<>"

    def __init__(self, index: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index is not None:
            self.index = index

    @property
    def inputs(self) -> members.SyncList | None:
        """The Inputs member."""
        member = self.get_member("Inputs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @inputs.setter
    def inputs(self, value: members.SyncList) -> None:
        """Set the Inputs member."""
        self.set_member("Inputs", value)

    @property
    def index(self) -> str | None:
        """Target ID of the Index reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @index.setter
    def index(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Index reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Index",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def output(self) -> members.EmptyElement | None:
        """The Output member."""
        member = self.get_member("Output")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @output.setter
    def output(self, value: members.EmptyElement) -> None:
        """Set the Output member."""
        self.set_member("Output", value)

    @property
    def input_count(self) -> members.EmptyElement | None:
        """The InputCount member."""
        member = self.get_member("InputCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @input_count.setter
    def input_count(self, value: members.EmptyElement) -> None:
        """Set the InputCount member."""
        self.set_member("InputCount", value)

