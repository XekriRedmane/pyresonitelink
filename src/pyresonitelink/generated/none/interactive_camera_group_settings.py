"""Generated component: InteractiveCameraGroupSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraGroupSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraGroupSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraGroupSettings"

    def __init__(self, group_detection_radius: np.float32 | None = None, group_leave_boundary: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            group_detection_radius: Initial value for GroupDetectionRadius.
            group_leave_boundary: Initial value for GroupLeaveBoundary.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if group_detection_radius is not None:
            self.group_detection_radius = group_detection_radius
        if group_leave_boundary is not None:
            self.group_leave_boundary = group_leave_boundary

    @property
    def group_detection_radius(self) -> np.float32 | None:
        """The GroupDetectionRadius field value."""
        member = self.get_member("GroupDetectionRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_detection_radius.setter
    def group_detection_radius(self, value: np.float32) -> None:
        """Set the GroupDetectionRadius field value."""
        member = self.get_member("GroupDetectionRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupDetectionRadius", fields.FieldFloat(value=value)
            )

    @property
    def group_leave_boundary(self) -> np.float32 | None:
        """The GroupLeaveBoundary field value."""
        member = self.get_member("GroupLeaveBoundary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_leave_boundary.setter
    def group_leave_boundary(self, value: np.float32) -> None:
        """Set the GroupLeaveBoundary field value."""
        member = self.get_member("GroupLeaveBoundary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupLeaveBoundary", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

