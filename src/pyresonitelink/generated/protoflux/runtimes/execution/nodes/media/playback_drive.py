"""Generated component: PlaybackDrive."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackDrive(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Playback Drive is a node that will take a SyncPlayback and allow you to start or stop driving it to a set of provided playback settings and values. The driving of the SyncPlayback is non networked.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Media
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.PlaybackDrive"

    def __init__(self, target: str | INodeObjectOutput[SyncPlayback] | None = None, normalized_position: str | INodeValueOutput[primitives.Float] | None = None, maximum_position_error: str | INodeValueOutput[primitives.Float] | None = None, speed: str | INodeValueOutput[primitives.Float] | None = None, play: str | INodeValueOutput[primitives.Bool] | None = None, loop: str | INodeValueOutput[primitives.Bool] | None = None, on_start_drive: str | INodeOperation | None = None, on_stop_drive: str | INodeOperation | None = None, on_resync: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            normalized_position: Initial value for NormalizedPosition.
            maximum_position_error: Initial value for MaximumPositionError.
            speed: Initial value for Speed.
            play: Initial value for Play.
            loop: Initial value for Loop.
            on_start_drive: Initial value for OnStartDrive.
            on_stop_drive: Initial value for OnStopDrive.
            on_resync: Initial value for OnResync.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if normalized_position is not None:
            self.normalized_position = normalized_position
        if maximum_position_error is not None:
            self.maximum_position_error = maximum_position_error
        if speed is not None:
            self.speed = speed
        if play is not None:
            self.play = play
        if loop is not None:
            self.loop = loop
        if on_start_drive is not None:
            self.on_start_drive = on_start_drive
        if on_stop_drive is not None:
            self.on_stop_drive = on_stop_drive
        if on_resync is not None:
            self.on_resync = on_resync

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[SyncPlayback])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[SyncPlayback] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[SyncPlayback] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.SyncPlayback>'),
            )

    @property
    def normalized_position(self) -> str | None:
        """Target ID of the NormalizedPosition reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("NormalizedPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normalized_position.setter
    def normalized_position(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the NormalizedPosition reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("NormalizedPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalizedPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def maximum_position_error(self) -> str | None:
        """Target ID of the MaximumPositionError reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MaximumPositionError")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @maximum_position_error.setter
    def maximum_position_error(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MaximumPositionError reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MaximumPositionError")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaximumPositionError",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def speed(self) -> str | None:
        """Target ID of the Speed reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @speed.setter
    def speed(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Speed reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Speed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def play(self) -> str | None:
        """Target ID of the Play reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Play")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @play.setter
    def play(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Play reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Play")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Play",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def loop(self) -> str | None:
        """Target ID of the Loop reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Loop")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop.setter
    def loop(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Loop reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Loop")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Loop",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def is_driving(self) -> members.EmptyElement | None:
        """The IsDriving member."""
        member = self.get_member("IsDriving")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_driving.setter
    def is_driving(self, value: members.EmptyElement) -> None:
        """Set the IsDriving member."""
        self.set_member("IsDriving", value)

    @property
    def start_drive(self) -> members.EmptyElement | None:
        """The StartDrive member."""
        member = self.get_member("StartDrive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @start_drive.setter
    def start_drive(self, value: members.EmptyElement) -> None:
        """Set the StartDrive member."""
        self.set_member("StartDrive", value)

    @property
    def stop_drive(self) -> members.EmptyElement | None:
        """The StopDrive member."""
        member = self.get_member("StopDrive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @stop_drive.setter
    def stop_drive(self, value: members.EmptyElement) -> None:
        """Set the StopDrive member."""
        self.set_member("StopDrive", value)

    @property
    def force_resync(self) -> members.EmptyElement | None:
        """The ForceResync member."""
        member = self.get_member("ForceResync")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @force_resync.setter
    def force_resync(self, value: members.EmptyElement) -> None:
        """Set the ForceResync member."""
        self.set_member("ForceResync", value)

    @property
    def on_start_drive(self) -> str | None:
        """Target ID of the OnStartDrive reference (targets INodeOperation)."""
        member = self.get_member("OnStartDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_start_drive.setter
    def on_start_drive(self, target: str | INodeOperation | None) -> None:
        """Set the OnStartDrive reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStartDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStartDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_stop_drive(self) -> str | None:
        """Target ID of the OnStopDrive reference (targets INodeOperation)."""
        member = self.get_member("OnStopDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_stop_drive.setter
    def on_stop_drive(self, target: str | INodeOperation | None) -> None:
        """Set the OnStopDrive reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStopDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStopDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_resync(self) -> str | None:
        """Target ID of the OnResync reference (targets INodeOperation)."""
        member = self.get_member("OnResync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_resync.setter
    def on_resync(self, target: str | INodeOperation | None) -> None:
        """Set the OnResync reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnResync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnResync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

