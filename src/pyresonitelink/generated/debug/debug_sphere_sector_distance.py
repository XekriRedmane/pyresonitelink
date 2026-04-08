"""Generated component: DebugSphereSectorDistance."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugSphereSectorDistance(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugSphereSectorDistance.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSphereSectorDistance"

    def __init__(self, angle: np.float32 | None = None, radius: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            angle: Initial value for Angle.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if angle is not None:
            self.angle = angle
        if radius is not None:
            self.radius = radius

    @property
    def angle(self) -> np.float32 | None:
        """The Angle field value."""
        member = self.get_member("Angle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle.setter
    def angle(self, value: np.float32) -> None:
        """Set the Angle field value."""
        member = self.get_member("Angle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Angle", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def points(self) -> members.SyncList | None:
        """The Points member."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set the Points member."""
        self.set_member("Points", value)

