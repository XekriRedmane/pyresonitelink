"""Generated component: FirstPersonTargettingController."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent


class FirstPersonTargettingController(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.FirstPersonTargettingController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FirstPersonTargettingController"

    def __init__(self, min_vertical_angle: np.float32 | None = None, max_vertical_angle: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_vertical_angle: Initial value for MinVerticalAngle.
            max_vertical_angle: Initial value for MaxVerticalAngle.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_vertical_angle is not None:
            self.min_vertical_angle = min_vertical_angle
        if max_vertical_angle is not None:
            self.max_vertical_angle = max_vertical_angle

    @property
    def min_vertical_angle(self) -> np.float32 | None:
        """The MinVerticalAngle field value."""
        member = self.get_member("MinVerticalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_vertical_angle.setter
    def min_vertical_angle(self, value: np.float32) -> None:
        """Set the MinVerticalAngle field value."""
        member = self.get_member("MinVerticalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinVerticalAngle", fields.FieldFloat(value=value)
            )

    @property
    def max_vertical_angle(self) -> np.float32 | None:
        """The MaxVerticalAngle field value."""
        member = self.get_member("MaxVerticalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_vertical_angle.setter
    def max_vertical_angle(self, value: np.float32) -> None:
        """Set the MaxVerticalAngle field value."""
        member = self.get_member("MaxVerticalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxVerticalAngle", fields.FieldFloat(value=value)
            )

