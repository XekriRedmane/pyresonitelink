"""Generated component: LocalScreenPointToWorld."""

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


class LocalScreenPointToWorld(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Local Screen Point To World node takes in a normalized screen space (``0`` to ``1`` along the user's screen in the X and Y position), and converts it to a position in world space. This node just takes where you are looking plus the distance from the local user and makes a value someplace outward from your camera/screen.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Conversion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalScreen.LocalScreenPointToWorld"

    def __init__(self, normalized_screen_point: str | INodeValueOutput[primitives.Float2] | None = None, distance: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            normalized_screen_point: Initial value for NormalizedScreenPoint.
            distance: Initial value for Distance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if normalized_screen_point is not None:
            self.normalized_screen_point = normalized_screen_point
        if distance is not None:
            self.distance = distance

    @property
    def normalized_screen_point(self) -> str | None:
        """The screen point from the user's perspective."""
        member = self.get_member("NormalizedScreenPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normalized_screen_point.setter
    def normalized_screen_point(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the NormalizedScreenPoint reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NormalizedScreenPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalizedScreenPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def distance(self) -> str | None:
        """The distance from this local user's view point."""
        member = self.get_member("Distance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance.setter
    def distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Distance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Distance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Distance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

