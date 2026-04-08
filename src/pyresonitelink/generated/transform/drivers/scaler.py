"""Generated component: Scaler."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Scaler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Scaler.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Scaler"

    def __init__(self, scale_offset: primitives.Float3 | None = None, scale_multiplier: primitives.Float3 | None = None, scale_source: str | Slot | None = None, scale_target: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale_offset: Initial value for ScaleOffset.
            scale_multiplier: Initial value for ScaleMultiplier.
            scale_source: Initial value for ScaleSource.
            scale_target: Initial value for scaleTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale_offset is not None:
            self.scale_offset = scale_offset
        if scale_multiplier is not None:
            self.scale_multiplier = scale_multiplier
        if scale_source is not None:
            self.scale_source = scale_source
        if scale_target is not None:
            self.scale_target = scale_target

    @property
    def scale_offset(self) -> primitives.Float3 | None:
        """The ScaleOffset field value."""
        member = self.get_member("ScaleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_offset.setter
    def scale_offset(self, value: primitives.Float3) -> None:
        """Set the ScaleOffset field value."""
        member = self.get_member("ScaleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleOffset", fields.FieldFloat3(value=value)
            )

    @property
    def scale_multiplier(self) -> primitives.Float3 | None:
        """The ScaleMultiplier field value."""
        member = self.get_member("ScaleMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_multiplier.setter
    def scale_multiplier(self, value: primitives.Float3) -> None:
        """Set the ScaleMultiplier field value."""
        member = self.get_member("ScaleMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleMultiplier", fields.FieldFloat3(value=value)
            )

    @property
    def scale_source(self) -> str | None:
        """Target ID of the ScaleSource reference (targets Slot)."""
        member = self.get_member("ScaleSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_source.setter
    def scale_source(self, target: str | Slot | None) -> None:
        """Set the ScaleSource reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ScaleSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScaleSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def scale_mode(self) -> members.FieldEnum | None:
        """The ScaleMode member."""
        member = self.get_member("ScaleMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @scale_mode.setter
    def scale_mode(self, value: members.FieldEnum) -> None:
        """Set the ScaleMode member."""
        self.set_member("ScaleMode", value)

    @property
    def scale_space(self) -> members.SyncObject | None:
        """The ScaleSpace member."""
        member = self.get_member("ScaleSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @scale_space.setter
    def scale_space(self, value: members.SyncObject) -> None:
        """Set the ScaleSpace member."""
        self.set_member("ScaleSpace", value)

    @property
    def scale_target(self) -> str | None:
        """Target ID of the scaleTarget reference (targets IField[primitives.Float3])."""
        member = self.get_member("scaleTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_target.setter
    def scale_target(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the scaleTarget reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("scaleTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "scaleTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

