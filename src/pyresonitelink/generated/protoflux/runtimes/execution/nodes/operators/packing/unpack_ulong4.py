"""Generated component: Unpack_Ulong4."""

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


class Unpack_Ulong4(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Unpack_Ulong4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Packing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Unpack_Ulong4"

    def __init__(self, v: str | INodeValueOutput[primitives.ULong4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            v: Initial value for V.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if v is not None:
            self.v = v

    @property
    def v(self) -> str | None:
        """Target ID of the V reference (targets INodeValueOutput[primitives.ULong4])."""
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @v.setter
    def v(self, target: str | INodeValueOutput[primitives.ULong4] | None) -> None:
        """Set the V reference by target ID or INodeValueOutput[primitives.ULong4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "V",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>'),
            )

    @property
    def x(self) -> members.EmptyElement | None:
        """The X member."""
        member = self.get_member("X")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @x.setter
    def x(self, value: members.EmptyElement) -> None:
        """Set the X member."""
        self.set_member("X", value)

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
    def z(self) -> members.EmptyElement | None:
        """The Z member."""
        member = self.get_member("Z")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @z.setter
    def z(self, value: members.EmptyElement) -> None:
        """Set the Z member."""
        self.set_member("Z", value)

    @property
    def w(self) -> members.EmptyElement | None:
        """The W member."""
        member = self.get_member("W")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @w.setter
    def w(self, value: members.EmptyElement) -> None:
        """Set the W member."""
        self.set_member("W", value)

