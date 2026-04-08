"""Generated component: LegacyAnimationTypeAdapter."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.texture_sheet_animation_type import TextureSheetAnimationType
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAnimationTypeAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LegacyAnimationTypeAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyAnimationTypeAdapter"

    def __init__(self, target: str | IField[TextureSheetAnimationType] | None = None, animation_tiles: str | IValue[primitives.Int2] | None = None, animation_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            animation_tiles: Initial value for AnimationTiles.
            animation_enabled: Initial value for AnimationEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if animation_tiles is not None:
            self.animation_tiles = animation_tiles
        if animation_enabled is not None:
            self.animation_enabled = animation_enabled

    @property
    def source(self) -> members.FieldEnum | None:
        """The Source member."""
        member = self.get_member("Source")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @source.setter
    def source(self, value: members.FieldEnum) -> None:
        """Set the Source member."""
        self.set_member("Source", value)

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[TextureSheetAnimationType])."""
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
        """Target ID of the AnimationTiles reference (targets IValue[primitives.Int2])."""
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
        """Target ID of the AnimationEnabled reference (targets IField[primitives.Bool])."""
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

