"""Generated component: FingerPoseMultiplexer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPoseMultiplexer(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FingerPoseMultiplexer.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPoseMultiplexer"

    def __init__(self, index: np.int32 | None = None, interpolation_speed: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index: Initial value for Index.
            interpolation_speed: Initial value for InterpolationSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index is not None:
            self.index = index
        if interpolation_speed is not None:
            self.interpolation_speed = interpolation_speed

    @property
    def index(self) -> np.int32 | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: np.int32) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def interpolation_speed(self) -> np.float32 | None:
        """The InterpolationSpeed field value."""
        member = self.get_member("InterpolationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolation_speed.setter
    def interpolation_speed(self, value: np.float32) -> None:
        """Set the InterpolationSpeed field value."""
        member = self.get_member("InterpolationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterpolationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def sources(self) -> members.SyncList | None:
        """The Sources member."""
        member = self.get_member("Sources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sources.setter
    def sources(self, value: members.SyncList) -> None:
        """Set the Sources member."""
        self.set_member("Sources", value)

