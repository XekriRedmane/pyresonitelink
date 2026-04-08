"""Generated component: HalfAdder."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HalfAdder(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.HalfAdder.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.HalfAdder"

    def __init__(self, a: str | INodeValueOutput[primitives.Bool] | None = None, b: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            b: Initial value for B.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the B reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def y(self) -> members.EmptyElement | None:
        """The Y member."""
        member = self.get_member("Y")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @y.setter
    def y(self, value: members.EmptyElement) -> None:
        """Set the Y member."""
        self.set_member("Y", value)

    @property
    def carry_out(self) -> members.EmptyElement | None:
        """The CarryOut member."""
        member = self.get_member("CarryOut")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @carry_out.setter
    def carry_out(self, value: members.EmptyElement) -> None:
        """Set the CarryOut member."""
        self.set_member("CarryOut", value)

