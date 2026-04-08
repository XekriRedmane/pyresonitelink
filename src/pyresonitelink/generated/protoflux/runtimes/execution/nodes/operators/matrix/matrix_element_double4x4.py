"""Generated component: MatrixElement_Double4x4."""

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


class MatrixElement_Double4x4(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.MatrixElement_Double4x4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Matrix
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.MatrixElement_Double4x4"

    def __init__(self, matrix: str | INodeValueOutput[primitives.Double4x4] | None = None, row: str | INodeValueOutput[primitives.Int] | None = None, column: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            matrix: Initial value for Matrix.
            row: Initial value for Row.
            column: Initial value for Column.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if matrix is not None:
            self.matrix = matrix
        if row is not None:
            self.row = row
        if column is not None:
            self.column = column

    @property
    def matrix(self) -> str | None:
        """Target ID of the Matrix reference (targets INodeValueOutput[primitives.Double4x4])."""
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @matrix.setter
    def matrix(self, target: str | INodeValueOutput[primitives.Double4x4] | None) -> None:
        """Set the Matrix reference by target ID or INodeValueOutput[primitives.Double4x4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Matrix",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>'),
            )

    @property
    def row(self) -> str | None:
        """Target ID of the Row reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Row")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @row.setter
    def row(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Row reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Row")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Row",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def column(self) -> str | None:
        """Target ID of the Column reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Column")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @column.setter
    def column(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Column reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Column")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Column",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

