"""Generated component: FindAnimationTrackIndex."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.animation import Animation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FindAnimationTrackIndex(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node when provided an Animation Asset will search the animation's AnimJ data for a field on an object

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.FindAnimationTrackIndex"

    def __init__(self, animation: str | INodeObjectOutput[Animation] | None = None, node: str | INodeObjectOutput[primitives.String] | None = None, property: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            animation: Initial value for Animation.
            node: Initial value for Node.
            property: Initial value for Property.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if animation is not None:
            self.animation = animation
        if node is not None:
            self.node = node
        if property is not None:
            self.property = property

    @property
    def animation(self) -> str | None:
        """The Animation Asset provided by an IAssetProvider."""
        member = self.get_member("Animation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @animation.setter
    def animation(self, target: str | INodeObjectOutput[Animation] | None) -> None:
        """Set the Animation reference by target ID or INodeObjectOutput[Animation] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Animation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Animation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Animation>'),
            )

    @property
    def node(self) -> str | None:
        """A String that is usually the name of the slot which has it's property animated. This can vary though, and AnimJ explains this."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Node reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def property(self) -> str | None:
        """A String that is usually the human name of a field. So a floatQ would be Rotation for a Property. This can vary though, and AnimJ explains this."""
        member = self.get_member("Property")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @property.setter
    def property(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Property reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Property")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Property",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

