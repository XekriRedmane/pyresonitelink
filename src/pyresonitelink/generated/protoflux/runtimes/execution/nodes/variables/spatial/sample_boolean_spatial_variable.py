"""Generated component: SampleBooleanSpatialVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.boolean_spatial_variable_mode import BooleanSpatialVariableMode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleBooleanSpatialVariable(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleBooleanSpatialVariable.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Spatial
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleBooleanSpatialVariable"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, name: str | INodeObjectOutput[primitives.String] | None = None, mode: str | INodeValueOutput[BooleanSpatialVariableMode] | None = None, base_value: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            name: Initial value for Name.
            mode: Initial value for Mode.
            base_value: Initial value for BaseValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if base_value is not None:
            self.base_value = base_value

    @property
    def point(self) -> str | None:
        """Target ID of the Point reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point.setter
    def point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def name(self) -> str | None:
        """Target ID of the Name reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Name reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def mode(self) -> str | None:
        """Target ID of the Mode reference (targets INodeValueOutput[BooleanSpatialVariableMode])."""
        member = self.get_member("Mode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mode.setter
    def mode(self, target: str | INodeValueOutput[BooleanSpatialVariableMode] | None) -> None:
        """Set the Mode reference by target ID or INodeValueOutput[BooleanSpatialVariableMode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Mode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.BooleanSpatialVariableMode>'),
            )

    @property
    def base_value(self) -> str | None:
        """Target ID of the BaseValue reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_value.setter
    def base_value(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the BaseValue reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

