"""Generated component: Pack_Color32."""

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


class Pack_Color32(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Color32.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Packing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Color32"

    def __init__(self, r: str | INodeValueOutput[primitives.Byte] | None = None, g: str | INodeValueOutput[primitives.Byte] | None = None, b: str | INodeValueOutput[primitives.Byte] | None = None, a: str | INodeValueOutput[primitives.Byte] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            r: Initial value for R.
            g: Initial value for G.
            b: Initial value for B.
            a: Initial value for A.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if r is not None:
            self.r = r
        if g is not None:
            self.g = g
        if b is not None:
            self.b = b
        if a is not None:
            self.a = a

    @property
    def r(self) -> str | None:
        """Target ID of the R reference (targets INodeValueOutput[primitives.Byte])."""
        member = self.get_member("R")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @r.setter
    def r(self, target: str | INodeValueOutput[primitives.Byte] | None) -> None:
        """Set the R reference by target ID or INodeValueOutput[primitives.Byte] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("R")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "R",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<byte>'),
            )

    @property
    def g(self) -> str | None:
        """Target ID of the G reference (targets INodeValueOutput[primitives.Byte])."""
        member = self.get_member("G")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @g.setter
    def g(self, target: str | INodeValueOutput[primitives.Byte] | None) -> None:
        """Set the G reference by target ID or INodeValueOutput[primitives.Byte] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("G")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "G",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<byte>'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets INodeValueOutput[primitives.Byte])."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | INodeValueOutput[primitives.Byte] | None) -> None:
        """Set the B reference by target ID or INodeValueOutput[primitives.Byte] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<byte>'),
            )

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[primitives.Byte])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[primitives.Byte] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[primitives.Byte] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<byte>'),
            )

