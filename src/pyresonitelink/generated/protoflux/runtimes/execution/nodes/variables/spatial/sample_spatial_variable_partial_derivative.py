"""Generated component: SampleSpatialVariablePartialDerivative."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.value_spatial_variable_mode import ValueSpatialVariableMode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleSpatialVariablePartialDerivative(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The SampleSpatialVariablePartialDerivative node samples a numerical spatial variable and returns the partial derivatives of the variable in the x, y, and z directions according to an orientation. In essence, it computes the numerical gradient of the sampled spatial variable.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Spatial

    Parameterize with a value type::

        SampleSpatialVariablePartialDerivative[primitives.Float]
        SampleSpatialVariablePartialDerivative[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<>"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, orientation: str | INodeValueOutput[primitives.FloatQ] | None = None, name: str | INodeObjectOutput[primitives.String] | None = None, mode: str | INodeValueOutput[ValueSpatialVariableMode] | None = None, base_value: str | INodeValueOutput[T] | None = None, sampling_distance: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            orientation: Initial value for Orientation.
            name: Initial value for Name.
            mode: Initial value for Mode.
            base_value: Initial value for BaseValue.
            sampling_distance: Initial value for SamplingDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if orientation is not None:
            self.orientation = orientation
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if base_value is not None:
            self.base_value = base_value
        if sampling_distance is not None:
            self.sampling_distance = sampling_distance

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
    def orientation(self) -> str | None:
        """Target ID of the Orientation reference (targets INodeValueOutput[primitives.FloatQ])."""
        member = self.get_member("Orientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orientation.setter
    def orientation(self, target: str | INodeValueOutput[primitives.FloatQ] | None) -> None:
        """Set the Orientation reference by target ID or INodeValueOutput[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Orientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Orientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>'),
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
        """Target ID of the Mode reference (targets INodeValueOutput[ValueSpatialVariableMode])."""
        member = self.get_member("Mode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mode.setter
    def mode(self, target: str | INodeValueOutput[ValueSpatialVariableMode] | None) -> None:
        """Set the Mode reference by target ID or INodeValueOutput[ValueSpatialVariableMode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Mode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.ValueSpatialVariableMode>'),
            )

    @property
    def base_value(self) -> str | None:
        """Target ID of the BaseValue reference (targets INodeValueOutput[T])."""
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_value.setter
    def base_value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the BaseValue reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BaseValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sampling_distance(self) -> str | None:
        """Target ID of the SamplingDistance reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("SamplingDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sampling_distance.setter
    def sampling_distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the SamplingDistance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SamplingDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SamplingDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def x(self) -> members.EmptyElement | None:
        """The X member."""
        member = self.get_member("X")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @x.setter
    def x(self, value: members.EmptyElement) -> None:
        """Set the X member."""
        self.set_member("X", value)

    @property
    def y(self) -> members.EmptyElement | None:
        """The Y member."""
        member = self.get_member("Y")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @y.setter
    def y(self, value: members.EmptyElement) -> None:
        """Set the Y member."""
        self.set_member("Y", value)

    @property
    def z(self) -> members.EmptyElement | None:
        """The Z member."""
        member = self.get_member("Z")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @z.setter
    def z(self, value: members.EmptyElement) -> None:
        """Set the Z member."""
        self.set_member("Z", value)

