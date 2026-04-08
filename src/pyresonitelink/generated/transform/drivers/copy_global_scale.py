"""Generated component: CopyGlobalScale."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CopyGlobalScale(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CopyGlobalScale.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CopyGlobalScale"

    def __init__(self, source: str | Slot | None = None, non_uniform: bool | None = None, scale_drive: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            non_uniform: Initial value for NonUniform.
            scale_drive: Initial value for _scaleDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if non_uniform is not None:
            self.non_uniform = non_uniform
        if scale_drive is not None:
            self.scale_drive = scale_drive

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
    def non_uniform(self) -> bool | None:
        """The NonUniform field value."""
        member = self.get_member("NonUniform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @non_uniform.setter
    def non_uniform(self, value: bool) -> None:
        """Set the NonUniform field value."""
        member = self.get_member("NonUniform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NonUniform", fields.FieldBool(value=value)
            )

    @property
    def scale_drive(self) -> str | None:
        """Target ID of the _scaleDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_drive.setter
    def scale_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scaleDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

