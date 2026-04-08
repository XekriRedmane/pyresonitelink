"""Generated component: SampleValueSpatialVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleValueSpatialVariable(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Spatial

    Parameterize with a value type::

        SampleValueSpatialVariable[primitives.Float]
        SampleValueSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<>"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, name: str | INodeObjectOutput[primitives.String] | None = None, default_value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            name: Initial value for Name.
            default_value: Initial value for DefaultValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if name is not None:
            self.name = name
        if default_value is not None:
            self.default_value = default_value

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
    def default_value(self) -> str | None:
        """Target ID of the DefaultValue reference (targets INodeValueOutput[T])."""
        member = self.get_member("DefaultValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_value.setter
    def default_value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the DefaultValue reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DefaultValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

