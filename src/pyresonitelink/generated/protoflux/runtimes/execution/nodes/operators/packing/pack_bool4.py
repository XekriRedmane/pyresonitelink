"""Generated component: Pack_Bool4."""

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


class Pack_Bool4(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Bool4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Packing
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Bool4"

    def __init__(self, x: str | INodeValueOutput[primitives.Bool] | None = None, y: str | INodeValueOutput[primitives.Bool] | None = None, z: str | INodeValueOutput[primitives.Bool] | None = None, w: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x: Initial value for X.
            y: Initial value for Y.
            z: Initial value for Z.
            w: Initial value for W.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if w is not None:
            self.w = w

    @property
    def x(self) -> str | None:
        """Target ID of the X reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the X reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def y(self) -> str | None:
        """Target ID of the Y reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y.setter
    def y(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Y reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Y",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def z(self) -> str | None:
        """Target ID of the Z reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Z")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z.setter
    def z(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Z reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Z")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Z",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def w(self) -> str | None:
        """Target ID of the W reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("W")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @w.setter
    def w(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the W reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("W")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "W",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

