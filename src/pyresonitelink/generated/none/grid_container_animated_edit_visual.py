"""Generated component: GridContainerAnimatedEditVisual."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.grid_container import GridContainer
from pyresonitelink.generated._types.tiled_raw_image import TiledRawImage
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GridContainerAnimatedEditVisual(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The GridContainerAnimatedEditVisual component is used to handle the animation of turning on and off UI Edit Mode.

    Not used by the user, but used by the game in visuals.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GridContainerAnimatedEditVisual"

    def __init__(self, grid: str | GridContainer | None = None, tiled_image: str | TiledRawImage | None = None, tiling: str | IField[primitives.Float2] | None = None, offset: str | IField[primitives.Float2] | None = None, tint: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grid: Initial value for Grid.
            tiled_image: Initial value for _tiledImage.
            tiling: Initial value for _tiling.
            offset: Initial value for _offset.
            tint: Initial value for _tint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grid is not None:
            self.grid = grid
        if tiled_image is not None:
            self.tiled_image = tiled_image
        if tiling is not None:
            self.tiling = tiling
        if offset is not None:
            self.offset = offset
        if tint is not None:
            self.tint = tint

    @property
    def grid(self) -> str | None:
        """The grid to edit."""
        member = self.get_member("Grid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grid.setter
    def grid(self, target: str | GridContainer | None) -> None:
        """Set the Grid reference by target ID or GridContainer instance."""
        target_id: str | None = target.id if isinstance(target, GridContainer) else target  # type: ignore[assignment]
        member = self.get_member("Grid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Grid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GridContainer'),
            )

    @property
    def tiled_image(self) -> str | None:
        """The image being used to show the grid alignment."""
        member = self.get_member("_tiledImage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tiled_image.setter
    def tiled_image(self, target: str | TiledRawImage | None) -> None:
        """Set the _tiledImage reference by target ID or TiledRawImage instance."""
        target_id: str | None = target.id if isinstance(target, TiledRawImage) else target  # type: ignore[assignment]
        member = self.get_member("_tiledImage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tiledImage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TiledRawImage'),
            )

    @property
    def tiling(self) -> str | None:
        """The tiling of the grid."""
        member = self.get_member("_tiling")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tiling.setter
    def tiling(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _tiling reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_tiling")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tiling",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def offset(self) -> str | None:
        """The position shift of the grid from default."""
        member = self.get_member("_offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset.setter
    def offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _offset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def tint(self) -> str | None:
        """The color tint of the grid."""
        member = self.get_member("_tint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tint.setter
    def tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _tint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_tint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

