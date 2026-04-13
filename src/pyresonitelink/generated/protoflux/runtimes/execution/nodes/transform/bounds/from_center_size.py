"""Generated component: FromCenterSize."""

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


class FromCenterSize(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The From Center Size node outputs a bounding box with the input Center and Size.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.FromCenterSize"

    def __init__(self, center_: str | INodeValueOutput[primitives.Float3] | None = None, size: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            center_: Initial value for Center.
            size: Initial value for Size.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if center_ is not None:
            self.center_ = center_
        if size is not None:
            self.size = size

    @property
    def center_(self) -> str | None:
        """The center point of the bounding box. Default is [0;0;0]."""
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center_.setter
    def center_(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Center reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Center",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def size(self) -> str | None:
        """The size of the bounding box. Default is [0;0;0]"""
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size.setter
    def size(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Size reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Size",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

