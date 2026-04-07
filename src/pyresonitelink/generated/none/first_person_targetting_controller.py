"""Generated component: FirstPersonTargettingController."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.generated._base import GeneratedComponent


class FirstPersonTargettingController(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.FirstPersonTargettingController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FirstPersonTargettingController"

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

