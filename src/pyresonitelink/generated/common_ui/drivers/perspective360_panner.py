"""Generated component: Perspective360Panner."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Perspective360Panner(GeneratedComponent, IButtonHoverReceiver, IWorldEventReceiver):
    """The Perspective360Panner component allows for moving or panning across 360 degrees around a view, given the parameters of how this panning should work. This is mostly seen in the WorldListFacetPreset component, where each listed item has this component to allow looking around in the world preview thumbnails.

    Category: Common UI/Drivers

    Useful as a way of looking around any 360 type of image.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Perspective360Panner"

    def __init__(self, idle_fov: primitives.Float | None = None, hover_fov: primitives.Float | None = None, fov_speed: primitives.Float | None = None, horizontal_panning_acceleration: primitives.Float | None = None, horizontal_panning_speed: primitives.Float | None = None, vertical_panning_speed: primitives.Float | None = None, vertical_range: primitives.Float | None = None, angle_offset: primitives.Float2 | None = None, fov: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            idle_fov: Initial value for IdleFOV.
            hover_fov: Initial value for HoverFOV.
            fov_speed: Initial value for FOVSpeed.
            horizontal_panning_acceleration: Initial value for HorizontalPanningAcceleration.
            horizontal_panning_speed: Initial value for HorizontalPanningSpeed.
            vertical_panning_speed: Initial value for VerticalPanningSpeed.
            vertical_range: Initial value for VerticalRange.
            angle_offset: Initial value for AngleOffset.
            fov: Initial value for FOV.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if idle_fov is not None:
            self.idle_fov = idle_fov
        if hover_fov is not None:
            self.hover_fov = hover_fov
        if fov_speed is not None:
            self.fov_speed = fov_speed
        if horizontal_panning_acceleration is not None:
            self.horizontal_panning_acceleration = horizontal_panning_acceleration
        if horizontal_panning_speed is not None:
            self.horizontal_panning_speed = horizontal_panning_speed
        if vertical_panning_speed is not None:
            self.vertical_panning_speed = vertical_panning_speed
        if vertical_range is not None:
            self.vertical_range = vertical_range
        if angle_offset is not None:
            self.angle_offset = angle_offset
        if fov is not None:
            self.fov = fov

    @property
    def idle_fov(self) -> primitives.Float | None:
        """The field of view used when not looking around."""
        member = self.get_member("IdleFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @idle_fov.setter
    def idle_fov(self, value: primitives.Float) -> None:
        """Set the IdleFOV field value."""
        member = self.get_member("IdleFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IdleFOV", fields.FieldFloat(value=value)
            )

    @property
    def hover_fov(self) -> primitives.Float | None:
        """The field of view used when looking around."""
        member = self.get_member("HoverFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hover_fov.setter
    def hover_fov(self, value: primitives.Float) -> None:
        """Set the HoverFOV field value."""
        member = self.get_member("HoverFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoverFOV", fields.FieldFloat(value=value)
            )

    @property
    def fov_speed(self) -> primitives.Float | None:
        """The field of view speed."""
        member = self.get_member("FOVSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fov_speed.setter
    def fov_speed(self, value: primitives.Float) -> None:
        """Set the FOVSpeed field value."""
        member = self.get_member("FOVSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FOVSpeed", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_panning_acceleration(self) -> primitives.Float | None:
        """How fast to pick up speed."""
        member = self.get_member("HorizontalPanningAcceleration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_panning_acceleration.setter
    def horizontal_panning_acceleration(self, value: primitives.Float) -> None:
        """Set the HorizontalPanningAcceleration field value."""
        member = self.get_member("HorizontalPanningAcceleration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalPanningAcceleration", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_panning_speed(self) -> primitives.Float | None:
        """The horizontal panning speed."""
        member = self.get_member("HorizontalPanningSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_panning_speed.setter
    def horizontal_panning_speed(self, value: primitives.Float) -> None:
        """Set the HorizontalPanningSpeed field value."""
        member = self.get_member("HorizontalPanningSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalPanningSpeed", fields.FieldFloat(value=value)
            )

    @property
    def vertical_panning_speed(self) -> primitives.Float | None:
        """The vertical panning speed."""
        member = self.get_member("VerticalPanningSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_panning_speed.setter
    def vertical_panning_speed(self, value: primitives.Float) -> None:
        """Set the VerticalPanningSpeed field value."""
        member = self.get_member("VerticalPanningSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalPanningSpeed", fields.FieldFloat(value=value)
            )

    @property
    def vertical_range(self) -> primitives.Float | None:
        """The vertical range of this field of view."""
        member = self.get_member("VerticalRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_range.setter
    def vertical_range(self, value: primitives.Float) -> None:
        """Set the VerticalRange field value."""
        member = self.get_member("VerticalRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalRange", fields.FieldFloat(value=value)
            )

    @property
    def angle_offset(self) -> primitives.Float2 | None:
        """The field of view angle offset."""
        member = self.get_member("AngleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_offset.setter
    def angle_offset(self, value: primitives.Float2) -> None:
        """Set the AngleOffset field value."""
        member = self.get_member("AngleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleOffset", fields.FieldFloat2(value=value)
            )

    @property
    def fov(self) -> primitives.Float2 | None:
        """The 2D field of view."""
        member = self.get_member("FOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fov.setter
    def fov(self, value: primitives.Float2) -> None:
        """Set the FOV field value."""
        member = self.get_member("FOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FOV", fields.FieldFloat2(value=value)
            )

