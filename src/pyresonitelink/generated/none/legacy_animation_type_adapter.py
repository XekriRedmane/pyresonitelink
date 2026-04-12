"""Generated component: LegacyAnimationTypeAdapter."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.legacy_particle_animation_type import LegacyParticleAnimationType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.texture_sheet_animation_type import TextureSheetAnimationType
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAnimationTypeAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyAnimationTypeAdapter component is used in converted legacy particle systems that were converted to PhotonDust as part of The Performance Updates.

    Not used directly by the user. Don't use this in new content!
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyAnimationTypeAdapter"

    def __init__(self, source: LegacyParticleAnimationType | str | None = None, target: str | IField[TextureSheetAnimationType] | None = None, animation_tiles: str | IValue[primitives.Int2] | None = None, animation_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            animation_tiles: Initial value for AnimationTiles.
            animation_enabled: Initial value for AnimationEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if animation_tiles is not None:
            self.animation_tiles = animation_tiles
        if animation_enabled is not None:
            self.animation_enabled = animation_enabled

    @property
    def source(self) -> LegacyParticleAnimationType | None:
        """The original animation type from legacy content."""
        member = self.get_member("Source")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LegacyParticleAnimationType(member.value)
        return None

    @source.setter
    def source(self, value: LegacyParticleAnimationType | str) -> None:
        """Set Source. The original animation type from legacy content."""
        member = self.get_member("Source")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Source",
                members.FieldEnum(value=str(value)),
            )

    @property
    def target(self) -> str | None:
        """The target field to drive with the legacy animation values."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[TextureSheetAnimationType] | None) -> None:
        """Set the Target reference by target ID or IField[TextureSheetAnimationType] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.TextureSheetAnimationType>'),
            )

    @property
    def animation_tiles(self) -> str | None:
        """The field to set to the amount of animation tiles."""
        member = self.get_member("AnimationTiles")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @animation_tiles.setter
    def animation_tiles(self, target: str | IValue[primitives.Int2] | None) -> None:
        """Set the AnimationTiles reference by target ID or IValue[primitives.Int2] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("AnimationTiles")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnimationTiles",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<int2>'),
            )

    @property
    def animation_enabled(self) -> str | None:
        """The field to drive with whether animation should be enabled."""
        member = self.get_member("AnimationEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @animation_enabled.setter
    def animation_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the AnimationEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AnimationEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnimationEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

