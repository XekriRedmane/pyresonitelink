"""Generated component: TextureSheetAnimator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureSheetAnimator(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.TextureSheetAnimator.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TextureSheetAnimator"

    def __init__(self, tile_grid_size: primitives.Int2 | None = None, animation_cycle_count: np.float32 | None = None, row_index: np.int32 | None = None, use_random_row: bool | None = None, start_with_random_offset: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tile_grid_size: Initial value for TileGridSize.
            animation_cycle_count: Initial value for AnimationCycleCount.
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
        if row_index is not None:
            self.row_index = row_index
        if use_random_row is not None:
            self.use_random_row = use_random_row
        if start_with_random_offset is not None:
            self.start_with_random_offset = start_with_random_offset

    @property
    def tile_grid_size(self) -> primitives.Int2 | None:
        """The TileGridSize field value."""
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
    def animation_cycle_count(self) -> np.float32 | None:
        """The AnimationCycleCount field value."""
        member = self.get_member("AnimationCycleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_cycle_count.setter
    def animation_cycle_count(self, value: np.float32) -> None:
        """Set the AnimationCycleCount field value."""
        member = self.get_member("AnimationCycleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationCycleCount", fields.FieldFloat(value=value)
            )

    @property
    def animation_type(self) -> members.FieldEnum | None:
        """The AnimationType member."""
        member = self.get_member("AnimationType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @animation_type.setter
    def animation_type(self, value: members.FieldEnum) -> None:
        """Set the AnimationType member."""
        self.set_member("AnimationType", value)

    @property
    def row_index(self) -> np.int32 | None:
        """The RowIndex field value."""
        member = self.get_member("RowIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @row_index.setter
    def row_index(self, value: np.int32) -> None:
        """Set the RowIndex field value."""
        member = self.get_member("RowIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RowIndex", fields.FieldInt(value=value)
            )

    @property
    def use_random_row(self) -> bool | None:
        """The UseRandomRow field value."""
        member = self.get_member("UseRandomRow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_random_row.setter
    def use_random_row(self, value: bool) -> None:
        """Set the UseRandomRow field value."""
        member = self.get_member("UseRandomRow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseRandomRow", fields.FieldBool(value=value)
            )

    @property
    def start_with_random_offset(self) -> bool | None:
        """The StartWithRandomOffset field value."""
        member = self.get_member("StartWithRandomOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_with_random_offset.setter
    def start_with_random_offset(self, value: bool) -> None:
        """Set the StartWithRandomOffset field value."""
        member = self.get_member("StartWithRandomOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartWithRandomOffset", fields.FieldBool(value=value)
            )

