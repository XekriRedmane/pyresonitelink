"""Generated component: CylinderEmitter+LegacyDirectionAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.cylinder_emitter_direction import CylinderEmitterDirection
from pyresonitelink.generated._types.cylinder_emitter_caps_direction import CylinderEmitterCapsDirection
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CylinderEmitter+LegacyDirectionAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.CylinderEmitter+LegacyDirectionAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.CylinderEmitter+LegacyDirectionAdapter"

    def __init__(self, force_direction: bool | None = None, emit_from_shell: str | IValue[bool] | None = None, direction: str | IField[CylinderEmitterDirection] | None = None, caps_direction: str | IField[CylinderEmitterCapsDirection] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            force_direction: Initial value for ForceDirection.
            emit_from_shell: Initial value for EmitFromShell.
            direction: Initial value for Direction.
            caps_direction: Initial value for CapsDirection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if force_direction is not None:
            self.force_direction = force_direction
        if emit_from_shell is not None:
            self.emit_from_shell = emit_from_shell
        if direction is not None:
            self.direction = direction
        if caps_direction is not None:
            self.caps_direction = caps_direction

    @property
    def force_direction(self) -> bool | None:
        """The ForceDirection field value."""
        member = self.get_member("ForceDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_direction.setter
    def force_direction(self, value: bool) -> None:
        """Set the ForceDirection field value."""
        member = self.get_member("ForceDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceDirection", fields.FieldBool(value=value)
            )

    @property
    def emit_from_shell(self) -> str | None:
        """Target ID of the EmitFromShell reference (targets IValue[bool])."""
        member = self.get_member("EmitFromShell")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emit_from_shell.setter
    def emit_from_shell(self, target: str | IValue[bool] | None) -> None:
        """Set the EmitFromShell reference by target ID or IValue[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("EmitFromShell")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmitFromShell",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<bool>'),
            )

    @property
    def direction(self) -> str | None:
        """Target ID of the Direction reference (targets IField[CylinderEmitterDirection])."""
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction.setter
    def direction(self, target: str | IField[CylinderEmitterDirection] | None) -> None:
        """Set the Direction reference by target ID or IField[CylinderEmitterDirection] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.CylinderEmitterDirection>'),
            )

    @property
    def caps_direction(self) -> str | None:
        """Target ID of the CapsDirection reference (targets IField[CylinderEmitterCapsDirection])."""
        member = self.get_member("CapsDirection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @caps_direction.setter
    def caps_direction(self, target: str | IField[CylinderEmitterCapsDirection] | None) -> None:
        """Set the CapsDirection reference by target ID or IField[CylinderEmitterCapsDirection] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CapsDirection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CapsDirection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.CylinderEmitterCapsDirection>'),
            )

