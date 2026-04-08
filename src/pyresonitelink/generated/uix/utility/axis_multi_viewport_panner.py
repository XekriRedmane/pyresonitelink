"""Generated component: AxisMultiViewportPanner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisMultiViewportPanner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.AxisMultiViewportPanner.

    Category: UIX/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.AxisMultiViewportPanner"

    def __init__(self, viewport_index: np.int32 | None = None, animation_time: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            viewport_index: Initial value for ViewportIndex.
            animation_time: Initial value for AnimationTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if viewport_index is not None:
            self.viewport_index = viewport_index
        if animation_time is not None:
            self.animation_time = animation_time

    @property
    def viewport_index(self) -> np.int32 | None:
        """The ViewportIndex field value."""
        member = self.get_member("ViewportIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @viewport_index.setter
    def viewport_index(self, value: np.int32) -> None:
        """Set the ViewportIndex field value."""
        member = self.get_member("ViewportIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViewportIndex", fields.FieldInt(value=value)
            )

    @property
    def animation_time(self) -> np.float32 | None:
        """The AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_time.setter
    def animation_time(self, value: np.float32) -> None:
        """Set the AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationTime", fields.FieldFloat(value=value)
            )

    @property
    def direction(self) -> members.FieldEnum | None:
        """The Direction member."""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @direction.setter
    def direction(self, value: members.FieldEnum) -> None:
        """Set the Direction member."""
        self.set_member("Direction", value)

    @property
    def viewports(self) -> members.SyncList | None:
        """The Viewports member."""
        member = self.get_member("Viewports")
        if isinstance(member, members.SyncList):
            return member
        return None

    @viewports.setter
    def viewports(self, value: members.SyncList) -> None:
        """Set the Viewports member."""
        self.set_member("Viewports", value)

