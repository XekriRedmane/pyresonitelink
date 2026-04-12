"""Generated component: TextureSheetAnimator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.texture_sheet_animation_type import TextureSheetAnimationType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureSheetAnimator(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The TextureSheetAnimator component makes particles animate their texture over lifetime or duration.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TextureSheetAnimator"

    def __init__(self, tile_grid_size: primitives.Int2 | None = None, animation_cycle_count: primitives.Float | None = None, animation_type: TextureSheetAnimationType | str | None = None, row_index: primitives.Int | None = None, use_random_row: primitives.Bool | None = None, start_with_random_offset: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tile_grid_size: Initial value for TileGridSize.
            animation_cycle_count: Initial value for AnimationCycleCount.
            animation_type: Initial value for AnimationType.
            row_index: Initial value for RowIndex.
            use_random_row: Initial value for UseRandomRow.
            start_with_random_offset: Initial value for StartWithRandomOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tile_grid_size is not None:
            self.tile_grid_size = tile_grid_size
        if animation_cycle_count is not None:
            self.animation_cycle_count = animation_cycle_count
        if animation_type is not None:
            self.animation_type = animation_type
        if row_index is not None:
            self.row_index = row_index
        if use_random_row is not None:
            self.use_random_row = use_random_row
        if start_with_random_offset is not None:
            self.start_with_random_offset = start_with_random_offset

    @property
    def tile_grid_size(self) -> primitives.Int2 | None:
        """The amount of cells and rows that the texture atlas sheet has."""
        member = self.get_member("TileGridSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tile_grid_size.setter
    def tile_grid_size(self, value: primitives.Int2) -> None:
        """Set the TileGridSize field value."""
        member = self.get_member("TileGridSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TileGridSize", fields.FieldInt2(value=value)
            )

    @property
    def animation_cycle_count(self) -> primitives.Float | None:
        """How many times to cycle the animation during the specified time frame."""
        member = self.get_member("AnimationCycleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_cycle_count.setter
    def animation_cycle_count(self, value: primitives.Float) -> None:
        """Set the AnimationCycleCount field value."""
        member = self.get_member("AnimationCycleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationCycleCount", fields.FieldFloat(value=value)
            )

    @property
    def animation_type(self) -> TextureSheetAnimationType | None:
        """The animation type to use for the texture sheet animation."""
        member = self.get_member("AnimationType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureSheetAnimationType(member.value)
        return None

    @animation_type.setter
    def animation_type(self, value: TextureSheetAnimationType | str) -> None:
        """Set AnimationType. The animation type to use for the texture sheet animation."""
        member = self.get_member("AnimationType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AnimationType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def row_index(self) -> primitives.Int | None:
        """The row index to start on."""
        member = self.get_member("RowIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @row_index.setter
    def row_index(self, value: primitives.Int) -> None:
        """Set the RowIndex field value."""
        member = self.get_member("RowIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RowIndex", fields.FieldInt(value=value)
            )

    @property
    def use_random_row(self) -> primitives.Bool | None:
        """Whether to start the texture sheet animation in a random row."""
        member = self.get_member("UseRandomRow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_random_row.setter
    def use_random_row(self, value: primitives.Bool) -> None:
        """Set the UseRandomRow field value."""
        member = self.get_member("UseRandomRow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseRandomRow", fields.FieldBool(value=value)
            )

    @property
    def start_with_random_offset(self) -> primitives.Bool | None:
        """Start the texture sheet animation in a random column."""
        member = self.get_member("StartWithRandomOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_with_random_offset.setter
    def start_with_random_offset(self, value: primitives.Bool) -> None:
        """Set the StartWithRandomOffset field value."""
        member = self.get_member("StartWithRandomOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartWithRandomOffset", fields.FieldBool(value=value)
            )

