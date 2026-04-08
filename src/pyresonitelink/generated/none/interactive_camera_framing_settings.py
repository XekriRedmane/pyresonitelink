"""Generated component: InteractiveCameraFramingSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraFramingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraFramingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraFramingSettings"

    def __init__(self, field_of_view: np.float32 | None = None, angle_position: np.float32 | None = None, distance: np.float32 | None = None, height_offset: np.float32 | None = None, first_person_pitch: np.float32 | None = None, first_person_roll: np.float32 | None = None, first_person_offset: np.float32 | None = None, framing_viewport_position: primitives.Float2 | None = None, aim_in_front_of_head: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            field_of_view: Initial value for FieldOfView.
            angle_position: Initial value for AnglePosition.
            distance: Initial value for Distance.
            height_offset: Initial value for HeightOffset.
            first_person_pitch: Initial value for FirstPersonPitch.
            first_person_roll: Initial value for FirstPersonRoll.
            first_person_offset: Initial value for FirstPersonOffset.
            framing_viewport_position: Initial value for FramingViewportPosition.
            aim_in_front_of_head: Initial value for AimInFrontOfHead.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if angle_position is not None:
            self.angle_position = angle_position
        if distance is not None:
            self.distance = distance
        if height_offset is not None:
            self.height_offset = height_offset
        if first_person_pitch is not None:
            self.first_person_pitch = first_person_pitch
        if first_person_roll is not None:
            self.first_person_roll = first_person_roll
        if first_person_offset is not None:
            self.first_person_offset = first_person_offset
        if framing_viewport_position is not None:
            self.framing_viewport_position = framing_viewport_position
        if aim_in_front_of_head is not None:
            self.aim_in_front_of_head = aim_in_front_of_head

    @property
    def positioning_mode(self) -> members.FieldEnum | None:
        """The PositioningMode member."""
        member = self.get_member("PositioningMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @positioning_mode.setter
    def positioning_mode(self, value: members.FieldEnum) -> None:
        """Set the PositioningMode member."""
        self.set_member("PositioningMode", value)

    @property
    def field_of_view(self) -> np.float32 | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: np.float32) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def angle_position(self) -> np.float32 | None:
        """The AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_position.setter
    def angle_position(self, value: np.float32) -> None:
        """Set the AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnglePosition", fields.FieldFloat(value=value)
            )

    @property
    def distance(self) -> np.float32 | None:
        """The Distance field value."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: np.float32) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def height_offset(self) -> np.float32 | None:
        """The HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_offset.setter
    def height_offset(self, value: np.float32) -> None:
        """Set the HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def first_person_pitch(self) -> np.float32 | None:
        """The FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_pitch.setter
    def first_person_pitch(self, value: np.float32) -> None:
        """Set the FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonPitch", fields.FieldFloat(value=value)
            )

    @property
    def first_person_roll(self) -> np.float32 | None:
        """The FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_roll.setter
    def first_person_roll(self, value: np.float32) -> None:
        """Set the FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonRoll", fields.FieldFloat(value=value)
            )

    @property
    def first_person_offset(self) -> np.float32 | None:
        """The FirstPersonOffset field value."""
        member = self.get_member("FirstPersonOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_offset.setter
    def first_person_offset(self, value: np.float32) -> None:
        """Set the FirstPersonOffset field value."""
        member = self.get_member("FirstPersonOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonOffset", fields.FieldFloat(value=value)
            )

    @property
    def framing_viewport_position(self) -> primitives.Float2 | None:
        """The FramingViewportPosition field value."""
        member = self.get_member("FramingViewportPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_viewport_position.setter
    def framing_viewport_position(self, value: primitives.Float2) -> None:
        """Set the FramingViewportPosition field value."""
        member = self.get_member("FramingViewportPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingViewportPosition", fields.FieldFloat2(value=value)
            )

    @property
    def aim_in_front_of_head(self) -> bool | None:
        """The AimInFrontOfHead field value."""
        member = self.get_member("AimInFrontOfHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aim_in_front_of_head.setter
    def aim_in_front_of_head(self, value: bool) -> None:
        """Set the AimInFrontOfHead field value."""
        member = self.get_member("AimInFrontOfHead")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AimInFrontOfHead", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

