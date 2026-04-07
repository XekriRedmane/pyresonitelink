"""Generated component: UnpackColumns_Double3x3."""

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


class UnpackColumns_Double3x3(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.UnpackColumns_Double3x3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Matrix
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.UnpackColumns_Double3x3"

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
    def column0(self) -> members.EmptyElement | None:
        """The Column0 member."""
        member = self.get_member("Column0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @column0.setter
    def column0(self, value: members.EmptyElement) -> None:
        """Set the Column0 member."""
        self.set_member("Column0", value)

    @property
    def column1(self) -> members.EmptyElement | None:
        """The Column1 member."""
        member = self.get_member("Column1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @column1.setter
    def column1(self, value: members.EmptyElement) -> None:
        """Set the Column1 member."""
        self.set_member("Column1", value)

    @property
    def column2(self) -> members.EmptyElement | None:
        """The Column2 member."""
        member = self.get_member("Column2")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @column2.setter
    def column2(self, value: members.EmptyElement) -> None:
        """Set the Column2 member."""
        self.set_member("Column2", value)

