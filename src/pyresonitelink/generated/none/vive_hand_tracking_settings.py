"""Generated component: ViveHandTrackingSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class ViveHandTrackingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.ViveHandTrackingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ViveHandTrackingSettings"

    def __init__(self, vive_hand_tracking_enabled: bool | None = None, snap_distance: np.float32 | None = None, use_fingers_when_snapped: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            vive_hand_tracking_enabled: Initial value for ViveHandTrackingEnabled.
            snap_distance: Initial value for SnapDistance.
            use_fingers_when_snapped: Initial value for UseFingersWhenSnapped.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if vive_hand_tracking_enabled is not None:
            self.vive_hand_tracking_enabled = vive_hand_tracking_enabled
        if snap_distance is not None:
            self.snap_distance = snap_distance
        if use_fingers_when_snapped is not None:
            self.use_fingers_when_snapped = use_fingers_when_snapped

    @property
    def vive_hand_tracking_enabled(self) -> bool | None:
        """The ViveHandTrackingEnabled field value."""
        member = self.get_member("ViveHandTrackingEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vive_hand_tracking_enabled.setter
    def vive_hand_tracking_enabled(self, value: bool) -> None:
        """Set the ViveHandTrackingEnabled field value."""
        member = self.get_member("ViveHandTrackingEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViveHandTrackingEnabled", fields.FieldBool(value=value)
            )

    @property
    def snap_distance(self) -> np.float32 | None:
        """The SnapDistance field value."""
        member = self.get_member("SnapDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_distance.setter
    def snap_distance(self, value: np.float32) -> None:
        """Set the SnapDistance field value."""
        member = self.get_member("SnapDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapDistance", fields.FieldFloat(value=value)
            )

    @property
    def use_fingers_when_snapped(self) -> bool | None:
        """The UseFingersWhenSnapped field value."""
        member = self.get_member("UseFingersWhenSnapped")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_fingers_when_snapped.setter
    def use_fingers_when_snapped(self, value: bool) -> None:
        """Set the UseFingersWhenSnapped field value."""
        member = self.get_member("UseFingersWhenSnapped")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFingersWhenSnapped", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

