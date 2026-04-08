"""Generated component: CopyGlobalTransform."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CopyGlobalTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CopyGlobalTransform.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CopyGlobalTransform"

    def __init__(self, source: str | Slot | None = None, pos_drive: str | IField[primitives.Float3] | None = None, rot_drive: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            pos_drive: Initial value for _posDrive.
            rot_drive: Initial value for _rotDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if pos_drive is not None:
            self.pos_drive = pos_drive
        if rot_drive is not None:
            self.rot_drive = rot_drive

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets Slot)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | Slot | None) -> None:
        """Set the Source reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pos_drive(self) -> str | None:
        """Target ID of the _posDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_posDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos_drive.setter
    def pos_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _posDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_posDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_posDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rot_drive(self) -> str | None:
        """Target ID of the _rotDrive reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rotDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rot_drive.setter
    def rot_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

