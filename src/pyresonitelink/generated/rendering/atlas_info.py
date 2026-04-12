"""Generated component: AtlasInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AtlasInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Atlas info is used in the UVAtlasAnimator to provide the animator with information on format of an image that is an atlas of all the frames in an animation.

    Category: Rendering

    When used in conjunction with a TimeIntDriver, and a UVAtlasAnimator
    this can let you animate for example pixel art images (spritesheets,
    Atlases, etc) AtlasInfo by itself dosen't have much use but when placed
    on a UVAtlasAnimator which is driving the Scale and Offset fields of a
    Material it will transform the UV of the material so that only one frame
    of the Texture is visible at a time To automate the change of frames
    over time, you can use a TimeIntDriver and set the repeat to Frames +1
    Repeat field is [0,x) || [0,x]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AtlasInfo"

    def __init__(self, grid_size: primitives.Int2 | None = None, grid_frames: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grid_size: Initial value for GridSize.
            grid_frames: Initial value for GridFrames.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grid_size is not None:
            self.grid_size = grid_size
        if grid_frames is not None:
            self.grid_frames = grid_frames

    @property
    def grid_size(self) -> primitives.Int2 | None:
        """The size of the grid that the image frames take up on the atlas (Ex: 4 by 8 grid of frames for a max of 32 total frames)"""
        member = self.get_member("GridSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_size.setter
    def grid_size(self, value: primitives.Int2) -> None:
        """Set the GridSize field value."""
        member = self.get_member("GridSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridSize", fields.FieldInt2(value=value)
            )

    @property
    def grid_frames(self) -> primitives.Int | None:
        """The amount of frames on the animation atlas image. If the amount of frames is less than the max (the two ``GridSize`` numbers multiplied together) then it will stop on frame ``GridFrames`` when this component is used by UVAtlasAnimator."""
        member = self.get_member("GridFrames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_frames.setter
    def grid_frames(self, value: primitives.Int) -> None:
        """Set the GridFrames field value."""
        member = self.get_member("GridFrames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridFrames", fields.FieldInt(value=value)
            )

