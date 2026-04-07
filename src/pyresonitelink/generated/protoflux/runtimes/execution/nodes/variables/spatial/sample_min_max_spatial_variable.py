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
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Spatial

    Parameterize with a value type::

        SampleMinMaxSpatialVariable[np.float32]
        SampleMinMaxSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<>"

    def __init__(self, point: str | INodeValueOutput[primitives.Float3] | None = None, name: str | INodeObjectOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Name reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Name reference by target ID or INodeObjectOutput[str] instance."""
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
        """The Min member."""
        member = self.get_member("Min")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @min.setter
    def min(self, value: members.EmptyElement) -> None:
        """Set the Min member."""
        self.set_member("Min", value)

    @property
    def max(self) -> members.EmptyElement | None:
        """The Max member."""
        member = self.get_member("Max")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @max.setter
    def max(self, value: members.EmptyElement) -> None:
        """Set the Max member."""
        self.set_member("Max", value)

    @property
    def found_any(self) -> members.EmptyElement | None:
        """The FoundAny member."""
        member = self.get_member("FoundAny")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @found_any.setter
    def found_any(self, value: members.EmptyElement) -> None:
        """Set the FoundAny member."""
        self.set_member("FoundAny", value)

