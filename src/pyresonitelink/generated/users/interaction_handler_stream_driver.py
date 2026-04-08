"""Generated component: InteractionHandlerStreamDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionHandlerStreamDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Used for lasers and interactions.

    Category: Users

    Used for lasers and interactions.

    **Related Components**: Interaction Handler Stream Driver
Interaction Handler Stream Driver
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractionHandlerStreamDriver"

    def __init__(self, side: Chirality | str | None = None, primary_blocked_stream: str | ValueStream[primitives.Bool] | None = None, secondary_blocked_stream: str | ValueStream[primitives.Bool] | None = None, laser_active_stream: str | ValueStream[primitives.Bool] | None = None, show_laser_to_others_stream: str | ValueStream[primitives.Bool] | None = None, laser_target_stream: str | ValueStream[primitives.Float3] | None = None, grab_distance_stream: str | ValueStream[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            side: Initial value for Side.
            primary_blocked_stream: Initial value for PrimaryBlockedStream.
            secondary_blocked_stream: Initial value for SecondaryBlockedStream.
            laser_active_stream: Initial value for LaserActiveStream.
            show_laser_to_others_stream: Initial value for ShowLaserToOthersStream.
            laser_target_stream: Initial value for LaserTargetStream.
            grab_distance_stream: Initial value for GrabDistanceStream.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if side is not None:
            self.side = side
        if primary_blocked_stream is not None:
            self.primary_blocked_stream = primary_blocked_stream
        if secondary_blocked_stream is not None:
            self.secondary_blocked_stream = secondary_blocked_stream
        if laser_active_stream is not None:
            self.laser_active_stream = laser_active_stream
        if show_laser_to_others_stream is not None:
            self.show_laser_to_others_stream = show_laser_to_others_stream
        if laser_target_stream is not None:
            self.laser_target_stream = laser_target_stream
        if grab_distance_stream is not None:
            self.grab_distance_stream = grab_distance_stream

    @property
    def side(self) -> Chirality | None:
        """The side to get the data."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @side.setter
    def side(self, value: Chirality | str) -> None:
        """Set Side. The side to get the data."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Side",
                members.FieldEnum(value=str(value)),
            )

    @property
    def primary_blocked_stream(self) -> str | None:
        """The value interaction data currently being blocked. (Primary)"""
        member = self.get_member("PrimaryBlockedStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_blocked_stream.setter
    def primary_blocked_stream(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the PrimaryBlockedStream reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("PrimaryBlockedStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PrimaryBlockedStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def secondary_blocked_stream(self) -> str | None:
        """The value interaction data currently being blocked. (Secondary)"""
        member = self.get_member("SecondaryBlockedStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_blocked_stream.setter
    def secondary_blocked_stream(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the SecondaryBlockedStream reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryBlockedStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryBlockedStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def laser_active_stream(self) -> str | None:
        """The streamed data for this interaction."""
        member = self.get_member("LaserActiveStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_active_stream.setter
    def laser_active_stream(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the LaserActiveStream reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LaserActiveStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LaserActiveStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def show_laser_to_others_stream(self) -> str | None:
        """Shows the laser data for the other stream."""
        member = self.get_member("ShowLaserToOthersStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_laser_to_others_stream.setter
    def show_laser_to_others_stream(self, target: str | ValueStream[primitives.Bool] | None) -> None:
        """Set the ShowLaserToOthersStream reference by target ID or ValueStream[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("ShowLaserToOthersStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShowLaserToOthersStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def laser_target_stream(self) -> str | None:
        """Shows the value for the target of this interaction."""
        member = self.get_member("LaserTargetStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_target_stream.setter
    def laser_target_stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the LaserTargetStream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LaserTargetStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LaserTargetStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def grab_distance_stream(self) -> str | None:
        """Shows the data of the distance of this interaction."""
        member = self.get_member("GrabDistanceStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grab_distance_stream.setter
    def grab_distance_stream(self, target: str | ValueStream[primitives.Float] | None) -> None:
        """Set the GrabDistanceStream reference by target ID or ValueStream[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("GrabDistanceStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GrabDistanceStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

