"""Generated component: SampleMinMaxSpatialVariable."""

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


class SampleMinMaxSpatialVariable(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Sample Min Max Spatial Variable node takes in a point in 3D space, and a name that matches that space, then returns the values found in the space that defined a min and max range.

This node works with spatial variable components, and will need a BoxConstantValueSpatialVariable or similar to function as expected.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Spatial

    Parameterize with a value type::

        SampleMinMaxSpatialVariable[primitives.Float]
        SampleMinMaxSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<>"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, name: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            name: Initial value for Name.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if name is not None:
            self.name = name

    @property
    def point(self) -> str | None:
        """The point to check in global 3D space."""
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
        """The named space/area to look for."""
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
    def min(self) -> members.EmptyElement | None:
        """Returns the min value found in this space/area."""
        member = self.get_member("Min")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @min.setter
    def min(self, value: members.EmptyElement) -> None:
        """Set Min. Returns the min value found in this space/area."""
        self.set_member("Min", value)

    @property
    def max(self) -> members.EmptyElement | None:
        """Returns the max value found in this space/area."""
        member = self.get_member("Max")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @max.setter
    def max(self, value: members.EmptyElement) -> None:
        """Set Max. Returns the max value found in this space/area."""
        self.set_member("Max", value)

    @property
    def found_any(self) -> members.EmptyElement | None:
        """Returns if there is a matching space/area at all."""
        member = self.get_member("FoundAny")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @found_any.setter
    def found_any(self, value: members.EmptyElement) -> None:
        """Set FoundAny. Returns if there is a matching space/area at all."""
        self.set_member("FoundAny", value)

