"""Generated component: PackColumns_Double3x3."""

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


class PackColumns_Double3x3(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackColumns_Double3x3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators/Matrix
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackColumns_Double3x3"

    def __init__(self, column0: str | INodeValueOutput[primitives.Double3] | None = None, column1: str | INodeValueOutput[primitives.Double3] | None = None, column2: str | INodeValueOutput[primitives.Double3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            column0: Initial value for Column0.
            column1: Initial value for Column1.
            column2: Initial value for Column2.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if column0 is not None:
            self.column0 = column0
        if column1 is not None:
            self.column1 = column1
        if column2 is not None:
            self.column2 = column2

    @property
    def column0(self) -> str | None:
        """Target ID of the Column0 reference (targets INodeValueOutput[primitives.Double3])."""
        member = self.get_member("Column0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @column0.setter
    def column0(self, target: str | INodeValueOutput[primitives.Double3] | None) -> None:
        """Set the Column0 reference by target ID or INodeValueOutput[primitives.Double3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Column0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Column0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3>'),
            )

    @property
    def column1(self) -> str | None:
        """Target ID of the Column1 reference (targets INodeValueOutput[primitives.Double3])."""
        member = self.get_member("Column1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @column1.setter
    def column1(self, target: str | INodeValueOutput[primitives.Double3] | None) -> None:
        """Set the Column1 reference by target ID or INodeValueOutput[primitives.Double3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Column1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Column1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3>'),
            )

    @property
    def column2(self) -> str | None:
        """Target ID of the Column2 reference (targets INodeValueOutput[primitives.Double3])."""
        member = self.get_member("Column2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @column2.setter
    def column2(self, target: str | INodeValueOutput[primitives.Double3] | None) -> None:
        """Set the Column2 reference by target ID or INodeValueOutput[primitives.Double3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Column2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Column2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double3>'),
            )

