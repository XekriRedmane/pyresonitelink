"""Generated component: LegacyAudioOutputDopplerAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAudioOutputDopplerAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyAudioOutputDopplerAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyAudioOutputDopplerAdapter"

    def __init__(self, target: str | IField[primitives.Float] | None = None, value: primitives.Float | None = None, spatial_blend: str | IField[primitives.Float] | None = None, spatialize: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value: Initial value for Value.
            spatial_blend: Initial value for SpatialBlend.
            spatialize: Initial value for Spatialize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value is not None:
            self.value = value
        if spatial_blend is not None:
            self.spatial_blend = spatial_blend
        if spatialize is not None:
            self.spatialize = spatialize

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Float])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def value(self) -> primitives.Float | None:
        """The Value field value."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: primitives.Float) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Value", fields.FieldFloat(value=value)
            )

    @property
    def spatial_blend(self) -> str | None:
        """Target ID of the SpatialBlend reference (targets IField[primitives.Float])."""
        member = self.get_member("SpatialBlend")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatial_blend.setter
    def spatial_blend(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the SpatialBlend reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpatialBlend")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpatialBlend",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def spatialize(self) -> str | None:
        """Target ID of the Spatialize reference (targets IField[primitives.Bool])."""
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatialize.setter
    def spatialize(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Spatialize reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Spatialize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

