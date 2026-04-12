"""Generated component: SampleValueAnimationTrack."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.animation import Animation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleValueAnimationTrack(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node when provided an Animation Asset sample the given track index for a primitive value at the specified time.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets

    Parameterize with a value type::

        SampleValueAnimationTrack[primitives.Float]
        SampleValueAnimationTrack[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<>"

    def __init__(self, animation: str | INodeObjectOutput[Animation] | None = None, track_index: str | INodeValueOutput[primitives.Int] | None = None, time: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            animation: Initial value for Animation.
            track_index: Initial value for TrackIndex.
            time: Initial value for Time.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if animation is not None:
            self.animation = animation
        if track_index is not None:
            self.track_index = track_index
        if time is not None:
            self.time = time

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
    def track_index(self) -> str | None:
        """The track index of the given Animation (Animation Asset) to sample from"""
        member = self.get_member("TrackIndex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @track_index.setter
    def track_index(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the TrackIndex reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("TrackIndex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrackIndex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def time(self) -> str | None:
        """The time in seconds at which to sample the animation. If between keyframes it will sample based on the AnimJ's interpolation for those frames on the track."""
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time.setter
    def time(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Time reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Time",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

