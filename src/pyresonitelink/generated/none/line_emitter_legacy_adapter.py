"""Generated component: LineEmitter+LegacyAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.line_emitter_direction import LineEmitterDirection
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LineEmitter+LegacyAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LineEmitter+LegacyAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LineEmitter+LegacyAdapter"

    def __init__(self, force_direction: primitives.Bool | None = None, forced_direction: primitives.Float3 | None = None, direction_mode: str | IField[LineEmitterDirection] | None = None, direction0: str | IField[primitives.Float3] | None = None, direction1: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force_direction: Initial value for ForceDirection.
            forced_direction: Initial value for ForcedDirection.
            direction_mode: Initial value for DirectionMode.
            direction0: Initial value for Direction0.
            direction1: Initial value for Direction1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if force_direction is not None:
            self.force_direction = force_direction
        if forced_direction is not None:
            self.forced_direction = forced_direction
        if direction_mode is not None:
            self.direction_mode = direction_mode
        if direction0 is not None:
            self.direction0 = direction0
        if direction1 is not None:
            self.direction1 = direction1

    @property
    def force_direction(self) -> primitives.Bool | None:
        """The ForceDirection field value."""
        member = self.get_member("ForceDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_direction.setter
    def force_direction(self, value: primitives.Bool) -> None:
        """Set the ForceDirection field value."""
        member = self.get_member("ForceDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceDirection", fields.FieldBool(value=value)
            )

    @property
    def forced_direction(self) -> primitives.Float3 | None:
        """The ForcedDirection field value."""
        member = self.get_member("ForcedDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forced_direction.setter
    def forced_direction(self, value: primitives.Float3) -> None:
        """Set the ForcedDirection field value."""
        member = self.get_member("ForcedDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForcedDirection", fields.FieldFloat3(value=value)
            )

    @property
    def direction_mode(self) -> str | None:
        """Target ID of the DirectionMode reference (targets IField[LineEmitterDirection])."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction_mode.setter
    def direction_mode(self, target: str | IField[LineEmitterDirection] | None) -> None:
        """Set the DirectionMode reference by target ID or IField[LineEmitterDirection] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DirectionMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DirectionMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.LineEmitterDirection>'),
            )

    @property
    def direction0(self) -> str | None:
        """Target ID of the Direction0 reference (targets IField[primitives.Float3])."""
        member = self.get_member("Direction0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction0.setter
    def direction0(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Direction0 reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Direction0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def direction1(self) -> str | None:
        """Target ID of the Direction1 reference (targets IField[primitives.Float3])."""
        member = self.get_member("Direction1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction1.setter
    def direction1(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Direction1 reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Direction1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

