"""Generated component: PlaybackState."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackState(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """PlayBack State is a ProtoFlux node that provides information of a (IPlayable). This can be used to get information of if the a source is playing, the current time position, and the length of the audio source.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Media
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.PlaybackState"

    def __init__(self, source: str | INodeObjectOutput[IPlayable] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets INodeObjectOutput[IPlayable])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | INodeObjectOutput[IPlayable] | None) -> None:
        """Set the Source reference by target ID or INodeObjectOutput[IPlayable] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IPlayable>'),
            )

    @property
    def is_playing(self) -> members.EmptyElement | None:
        """The IsPlaying member."""
        member = self.get_member("IsPlaying")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_playing.setter
    def is_playing(self, value: members.EmptyElement) -> None:
        """Set the IsPlaying member."""
        self.set_member("IsPlaying", value)

    @property
    def loop(self) -> members.EmptyElement | None:
        """The Loop member."""
        member = self.get_member("Loop")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @loop.setter
    def loop(self, value: members.EmptyElement) -> None:
        """Set the Loop member."""
        self.set_member("Loop", value)

    @property
    def position(self) -> members.EmptyElement | None:
        """The Position member."""
        member = self.get_member("Position")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @position.setter
    def position(self, value: members.EmptyElement) -> None:
        """Set the Position member."""
        self.set_member("Position", value)

    @property
    def normalized_position(self) -> members.EmptyElement | None:
        """The NormalizedPosition member."""
        member = self.get_member("NormalizedPosition")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @normalized_position.setter
    def normalized_position(self, value: members.EmptyElement) -> None:
        """Set the NormalizedPosition member."""
        self.set_member("NormalizedPosition", value)

    @property
    def clip_length(self) -> members.EmptyElement | None:
        """The ClipLength member."""
        member = self.get_member("ClipLength")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @clip_length.setter
    def clip_length(self, value: members.EmptyElement) -> None:
        """Set the ClipLength member."""
        self.set_member("ClipLength", value)

    @property
    def speed(self) -> members.EmptyElement | None:
        """The Speed member."""
        member = self.get_member("Speed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @speed.setter
    def speed(self, value: members.EmptyElement) -> None:
        """Set the Speed member."""
        self.set_member("Speed", value)

