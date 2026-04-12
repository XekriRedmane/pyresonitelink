"""Generated component: BoundingBoxProperties."""

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


class BoundingBoxProperties(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Bounding Box Properties node provides several pieces of information about the input bounding box.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.BoundingBoxProperties"

    def __init__(self, bounds: str | INodeValueOutput[primitives.BoundingBox] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bounds: Initial value for Bounds.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bounds is not None:
            self.bounds = bounds

    @property
    def bounds(self) -> str | None:
        """Default is a bounding box with center [0;0;0] and size [0;0;0]."""
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds.setter
    def bounds(self, target: str | INodeValueOutput[primitives.BoundingBox] | None) -> None:
        """Set the Bounds reference by target ID or INodeValueOutput[primitives.BoundingBox] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>'),
            )

    @property
    def min(self) -> members.EmptyElement | None:
        """The minimum position values for the Bounds along each axis."""
        member = self.get_member("Min")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @min.setter
    def min(self, value: members.EmptyElement) -> None:
        """Set Min. The minimum position values for the Bounds along each axis."""
        self.set_member("Min", value)

    @property
    def max(self) -> members.EmptyElement | None:
        """The maximum position values for the Bounds along each axis."""
        member = self.get_member("Max")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @max.setter
    def max(self, value: members.EmptyElement) -> None:
        """Set Max. The maximum position values for the Bounds along each axis."""
        self.set_member("Max", value)

    @property
    def center(self) -> members.EmptyElement | None:
        """The center point of the Bounds."""
        member = self.get_member("Center")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @center.setter
    def center(self, value: members.EmptyElement) -> None:
        """Set Center. The center point of the Bounds."""
        self.set_member("Center", value)

    @property
    def size(self) -> members.EmptyElement | None:
        """The size of the Bounds along each axis."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set Size. The size of the Bounds along each axis."""
        self.set_member("Size", value)

    @property
    def valid(self) -> members.EmptyElement | None:
        """Returns whether the Bounds is a valid bounding box."""
        member = self.get_member("Valid")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @valid.setter
    def valid(self, value: members.EmptyElement) -> None:
        """Set Valid. Returns whether the Bounds is a valid bounding box."""
        self.set_member("Valid", value)

    @property
    def empty(self) -> members.EmptyElement | None:
        """Returns whether the Bounds is an empty bounding box."""
        member = self.get_member("Empty")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @empty.setter
    def empty(self, value: members.EmptyElement) -> None:
        """Set Empty. Returns whether the Bounds is an empty bounding box."""
        self.set_member("Empty", value)

