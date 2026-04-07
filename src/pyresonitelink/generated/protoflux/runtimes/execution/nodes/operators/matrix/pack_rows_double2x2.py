"""Generated component: PackRows_Double2x2."""

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


class PackRows_Double2x2(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackRows_Double2x2.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Matrix
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackRows_Double2x2"

    def __init__(self, row0: str | INodeValueOutput[primitives.Double2] | None = None, row1: str | INodeValueOutput[primitives.Double2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            row0: Initial value for Row0.
            row1: Initial value for Row1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if row0 is not None:
            self.row0 = row0
        if row1 is not None:
            self.row1 = row1

    @property
    def row0(self) -> str | None:
        """Target ID of the Row0 reference (targets INodeValueOutput[primitives.Double2])."""
        member = self.get_member("Row0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @row0.setter
    def row0(self, target: str | INodeValueOutput[primitives.Double2] | None) -> None:
        """Set the Row0 reference by target ID or INodeValueOutput[primitives.Double2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Row0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Row0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double2>'),
            )

    @property
    def row1(self) -> str | None:
        """Target ID of the Row1 reference (targets INodeValueOutput[primitives.Double2])."""
        member = self.get_member("Row1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @row1.setter
    def row1(self, target: str | INodeValueOutput[primitives.Double2] | None) -> None:
        """Set the Row1 reference by target ID or INodeValueOutput[primitives.Double2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Row1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Row1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double2>'),
            )

