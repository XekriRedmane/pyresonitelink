"""Generated component: LeapMotionSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class LeapMotionSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.LeapMotionSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LeapMotionSettings"

    def __init__(self, leap_motion_enabled: primitives.Bool | None = None, offset: primitives.Float3 | None = None, snap_distance: primitives.Float | None = None, use_fingers_when_snapped: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            leap_motion_enabled: Initial value for LeapMotionEnabled.
            offset: Initial value for Offset.
            snap_distance: Initial value for SnapDistance.
            use_fingers_when_snapped: Initial value for UseFingersWhenSnapped.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if leap_motion_enabled is not None:
            self.leap_motion_enabled = leap_motion_enabled
        if offset is not None:
            self.offset = offset
        if snap_distance is not None:
            self.snap_distance = snap_distance
        if use_fingers_when_snapped is not None:
            self.use_fingers_when_snapped = use_fingers_when_snapped

    @property
    def leap_motion_enabled(self) -> primitives.Bool | None:
        """The LeapMotionEnabled field value."""
        member = self.get_member("LeapMotionEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @leap_motion_enabled.setter
    def leap_motion_enabled(self, value: primitives.Bool) -> None:
        """Set the LeapMotionEnabled field value."""
        member = self.get_member("LeapMotionEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeapMotionEnabled", fields.FieldBool(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def snap_distance(self) -> primitives.Float | None:
        """The SnapDistance field value."""
        member = self.get_member("SnapDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_distance.setter
    def snap_distance(self, value: primitives.Float) -> None:
        """Set the SnapDistance field value."""
        member = self.get_member("SnapDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapDistance", fields.FieldFloat(value=value)
            )

    @property
    def use_fingers_when_snapped(self) -> primitives.Bool | None:
        """The UseFingersWhenSnapped field value."""
        member = self.get_member("UseFingersWhenSnapped")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_fingers_when_snapped.setter
    def use_fingers_when_snapped(self, value: primitives.Bool) -> None:
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

