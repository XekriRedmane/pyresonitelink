"""Generated component: DebugValueStreamRange."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugValueStreamRange(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugValueStreamRange component is used to debug the range of a Float3 stream for debugging. Like a graph of sorts.

    Not generally useful to the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugValueStreamRange"

    def __init__(self, stream: str | ValueStream[primitives.Float3] | None = None, position_drive: str | IField[primitives.Float3] | None = None, size_drive: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stream: Initial value for Stream.
            position_drive: Initial value for positionDrive.
            size_drive: Initial value for sizeDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stream is not None:
            self.stream = stream
        if position_drive is not None:
            self.position_drive = position_drive
        if size_drive is not None:
            self.size_drive = size_drive

    @property
    def stream(self) -> str | None:
        """The stream to debug."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the Stream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def position_drive(self) -> str | None:
        """The position field to drive with the stream position."""
        member = self.get_member("positionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the positionDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("positionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "positionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def size_drive(self) -> str | None:
        """The field to drive with the overall stream range."""
        member = self.get_member("sizeDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_drive.setter
    def size_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the sizeDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("sizeDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "sizeDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

