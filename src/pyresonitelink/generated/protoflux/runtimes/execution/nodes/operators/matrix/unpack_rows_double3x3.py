"""Generated component: UnpackRows_Double3x3."""

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


class UnpackRows_Double3x3(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.UnpackRows_Double3x3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Matrix
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.UnpackRows_Double3x3"

    def __init__(self, matrix: str | INodeValueOutput[primitives.Double3x3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            matrix: Initial value for Matrix.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if matrix is not None:
            self.matrix = matrix

    @property
    def matrix(self) -> str | None:
        """Target ID of the Matrix reference (targets INodeValueOutput[primitives.Double3x3])."""
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @matrix.setter
    def matrix(self, target: str | INodeValueOutput[primitives.Double3x3] | None) -> None:
        """Set the Matrix reference by target ID or INodeValueOutput[primitives.Double3x3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Matrix",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>'),
            )

    @property
    def row0(self) -> members.EmptyElement | None:
        """The Row0 member."""
        member = self.get_member("Row0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @row0.setter
    def row0(self, value: members.EmptyElement) -> None:
        """Set the Row0 member."""
        self.set_member("Row0", value)

    @property
    def row1(self) -> members.EmptyElement | None:
        """The Row1 member."""
        member = self.get_member("Row1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @row1.setter
    def row1(self, value: members.EmptyElement) -> None:
        """Set the Row1 member."""
        self.set_member("Row1", value)

    @property
    def row2(self) -> members.EmptyElement | None:
        """The Row2 member."""
        member = self.get_member("Row2")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @row2.setter
    def row2(self, value: members.EmptyElement) -> None:
        """Set the Row2 member."""
        self.set_member("Row2", value)

