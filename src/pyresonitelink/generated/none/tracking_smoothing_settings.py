"""Generated component: TrackingSmoothingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TrackingSmoothingSettings(GeneratedComponent, ICustomInspector):
    """The TrackingSmoothingSettings component is better explained on the Settings page.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackingSmoothingSettings"

    def __init__(self, hand_position_smoothing: primitives.Float | None = None, hand_rotation_smoothing: primitives.Float | None = None, feet_position_smoothing: primitives.Float | None = None, feet_rotation_smoothing: primitives.Float | None = None, hips_position_smoothing: primitives.Float | None = None, hips_rotation_smoothing: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hand_position_smoothing: Initial value for HandPositionSmoothing.
            hand_rotation_smoothing: Initial value for HandRotationSmoothing.
            feet_position_smoothing: Initial value for FeetPositionSmoothing.
            feet_rotation_smoothing: Initial value for FeetRotationSmoothing.
            hips_position_smoothing: Initial value for HipsPositionSmoothing.
            hips_rotation_smoothing: Initial value for HipsRotationSmoothing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hand_position_smoothing is not None:
            self.hand_position_smoothing = hand_position_smoothing
        if hand_rotation_smoothing is not None:
            self.hand_rotation_smoothing = hand_rotation_smoothing
        if feet_position_smoothing is not None:
            self.feet_position_smoothing = feet_position_smoothing
        if feet_rotation_smoothing is not None:
            self.feet_rotation_smoothing = feet_rotation_smoothing
        if hips_position_smoothing is not None:
            self.hips_position_smoothing = hips_position_smoothing
        if hips_rotation_smoothing is not None:
            self.hips_rotation_smoothing = hips_rotation_smoothing

    @property
    def hand_position_smoothing(self) -> primitives.Float | None:
        """How much to smooth hand positioning, if not null."""
        member = self.get_member("HandPositionSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_position_smoothing.setter
    def hand_position_smoothing(self, value: primitives.Float) -> None:
        """Set the HandPositionSmoothing field value."""
        member = self.get_member("HandPositionSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandPositionSmoothing", fields.FieldNullableFloat(value=value)
            )

    @property
    def hand_rotation_smoothing(self) -> primitives.Float | None:
        """How much to smooth hand rotation, if not null."""
        member = self.get_member("HandRotationSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_rotation_smoothing.setter
    def hand_rotation_smoothing(self, value: primitives.Float) -> None:
        """Set the HandRotationSmoothing field value."""
        member = self.get_member("HandRotationSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandRotationSmoothing", fields.FieldNullableFloat(value=value)
            )

    @property
    def feet_position_smoothing(self) -> primitives.Float | None:
        """How much to smooth feet positioning, if not null."""
        member = self.get_member("FeetPositionSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_position_smoothing.setter
    def feet_position_smoothing(self, value: primitives.Float) -> None:
        """Set the FeetPositionSmoothing field value."""
        member = self.get_member("FeetPositionSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetPositionSmoothing", fields.FieldNullableFloat(value=value)
            )

    @property
    def feet_rotation_smoothing(self) -> primitives.Float | None:
        """How much to smooth feet rotation, if not null."""
        member = self.get_member("FeetRotationSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_rotation_smoothing.setter
    def feet_rotation_smoothing(self, value: primitives.Float) -> None:
        """Set the FeetRotationSmoothing field value."""
        member = self.get_member("FeetRotationSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetRotationSmoothing", fields.FieldNullableFloat(value=value)
            )

    @property
    def hips_position_smoothing(self) -> primitives.Float | None:
        """How much to smooth hips positioning, if not null."""
        member = self.get_member("HipsPositionSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hips_position_smoothing.setter
    def hips_position_smoothing(self, value: primitives.Float) -> None:
        """Set the HipsPositionSmoothing field value."""
        member = self.get_member("HipsPositionSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HipsPositionSmoothing", fields.FieldNullableFloat(value=value)
            )

    @property
    def hips_rotation_smoothing(self) -> primitives.Float | None:
        """How much to smooth hips rotation, if not null."""
        member = self.get_member("HipsRotationSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hips_rotation_smoothing.setter
    def hips_rotation_smoothing(self, value: primitives.Float) -> None:
        """Set the HipsRotationSmoothing field value."""
        member = self.get_member("HipsRotationSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HipsRotationSmoothing", fields.FieldNullableFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

