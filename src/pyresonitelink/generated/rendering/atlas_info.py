"""Generated component: AtlasInfo."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AtlasInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AtlasInfo.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AtlasInfo"

    def __init__(self, grid_size: primitives.Int2 | None = None, grid_frames: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
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
        """The GridSize field value."""
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
    def grid_frames(self) -> np.int32 | None:
        """The GridFrames field value."""
        member = self.get_member("GridFrames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_frames.setter
    def grid_frames(self, value: np.int32) -> None:
        """Set the GridFrames field value."""
        member = self.get_member("GridFrames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridFrames", fields.FieldInt(value=value)
            )

