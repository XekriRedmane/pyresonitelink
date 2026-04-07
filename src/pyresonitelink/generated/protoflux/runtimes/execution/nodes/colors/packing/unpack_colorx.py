"""Generated component: Unpack_ColorX."""

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


class Unpack_ColorX(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Unpack_ColorX.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors/Packing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Unpack_ColorX"

    def __init__(self, v: str | INodeValueOutput[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the V reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @v.setter
    def v(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the V reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("V")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "V",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def r(self) -> members.EmptyElement | None:
        """The R member."""
        member = self.get_member("R")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @r.setter
    def r(self, value: members.EmptyElement) -> None:
        """Set the R member."""
        self.set_member("R", value)

    @property
    def g(self) -> members.EmptyElement | None:
        """The G member."""
        member = self.get_member("G")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @g.setter
    def g(self, value: members.EmptyElement) -> None:
        """Set the G member."""
        self.set_member("G", value)

    @property
    def b(self) -> members.EmptyElement | None:
        """The B member."""
        member = self.get_member("B")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @b.setter
    def b(self, value: members.EmptyElement) -> None:
        """Set the B member."""
        self.set_member("B", value)

    @property
    def a(self) -> members.EmptyElement | None:
        """The A member."""
        member = self.get_member("A")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @a.setter
    def a(self, value: members.EmptyElement) -> None:
        """Set the A member."""
        self.set_member("A", value)

    @property
    def profile(self) -> members.EmptyElement | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @profile.setter
    def profile(self, value: members.EmptyElement) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

