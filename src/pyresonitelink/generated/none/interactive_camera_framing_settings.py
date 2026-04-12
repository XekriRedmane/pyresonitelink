"""Generated component: InteractiveCameraFramingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.camera_positioning_mode import CameraPositioningMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraFramingSettings(GeneratedComponent, ICustomInspector):
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraFramingSettings"

    def __init__(self, positioning_mode: CameraPositioningMode | str | None = None, field_of_view: primitives.Float | None = None, angle_position: primitives.Float | None = None, distance: primitives.Float | None = None, height_offset: primitives.Float | None = None, first_person_pitch: primitives.Float | None = None, first_person_roll: primitives.Float | None = None, first_person_offset: primitives.Float | None = None, framing_viewport_position: primitives.Float2 | None = None, aim_in_front_of_head: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            positioning_mode: Initial value for PositioningMode.
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
        if positioning_mode is not None:
            self.positioning_mode = positioning_mode
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
    def positioning_mode(self) -> CameraPositioningMode | None:
        """how the camera should position itself."""
        member = self.get_member("PositioningMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CameraPositioningMode(member.value)
        return None

    @positioning_mode.setter
    def positioning_mode(self, value: CameraPositioningMode | str) -> None:
        """Set PositioningMode. how the camera should position itself."""
        member = self.get_member("PositioningMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositioningMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def field_of_view(self) -> primitives.Float | None:
        """How wide the view angle is."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: primitives.Float) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def angle_position(self) -> primitives.Float | None:
        """tilt of the camera side to side"""
        member = self.get_member("AnglePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_position.setter
    def angle_position(self, value: primitives.Float) -> None:
        """Set the AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnglePosition", fields.FieldFloat(value=value)
            )

    @property
    def distance(self) -> primitives.Float | None:
        """How far away to stay from a subject during auto tracking."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: primitives.Float) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def height_offset(self) -> primitives.Float | None:
        """How much offset to add to targeting a user's head vertically."""
        member = self.get_member("HeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_offset.setter
    def height_offset(self, value: primitives.Float) -> None:
        """Set the HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def first_person_pitch(self) -> primitives.Float | None:
        """The first person rotation transform pitch."""
        member = self.get_member("FirstPersonPitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_pitch.setter
    def first_person_pitch(self, value: primitives.Float) -> None:
        """Set the FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonPitch", fields.FieldFloat(value=value)
            )

    @property
    def first_person_roll(self) -> primitives.Float | None:
        """The first person rotation transform roll."""
        member = self.get_member("FirstPersonRoll")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_roll.setter
    def first_person_roll(self, value: primitives.Float) -> None:
        """Set the FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonRoll", fields.FieldFloat(value=value)
            )

    @property
    def first_person_offset(self) -> primitives.Float | None:
        """The offset forward or backwards in first person."""
        member = self.get_member("FirstPersonOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_offset.setter
    def first_person_offset(self, value: primitives.Float) -> None:
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
        """Where to frame the target object in the viewport of the camera rather than the center of the image."""
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
    def aim_in_front_of_head(self) -> primitives.Bool | None:
        """Aim at a spot a little in front of the user's head."""
        member = self.get_member("AimInFrontOfHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aim_in_front_of_head.setter
    def aim_in_front_of_head(self, value: primitives.Bool) -> None:
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

