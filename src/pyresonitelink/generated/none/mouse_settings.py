"""Generated component: MouseSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MouseSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MouseSettings"

    def __init__(self, mouse_sensitivity: primitives.Float | None = None, scroll_wheel_grab_move_speed: primitives.Float | None = None, mouse_look_speed: primitives.Float | None = None, mouse_pan_speed: primitives.Float | None = None, mouse_rotate_speed: primitives.Float | None = None, mouse_freeform_rotate_speed: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mouse_sensitivity: Initial value for MouseSensitivity.
            scroll_wheel_grab_move_speed: Initial value for ScrollWheelGrabMoveSpeed.
            mouse_look_speed: Initial value for MouseLookSpeed.
            mouse_pan_speed: Initial value for MousePanSpeed.
            mouse_rotate_speed: Initial value for MouseRotateSpeed.
            mouse_freeform_rotate_speed: Initial value for MouseFreeformRotateSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mouse_sensitivity is not None:
            self.mouse_sensitivity = mouse_sensitivity
        if scroll_wheel_grab_move_speed is not None:
            self.scroll_wheel_grab_move_speed = scroll_wheel_grab_move_speed
        if mouse_look_speed is not None:
            self.mouse_look_speed = mouse_look_speed
        if mouse_pan_speed is not None:
            self.mouse_pan_speed = mouse_pan_speed
        if mouse_rotate_speed is not None:
            self.mouse_rotate_speed = mouse_rotate_speed
        if mouse_freeform_rotate_speed is not None:
            self.mouse_freeform_rotate_speed = mouse_freeform_rotate_speed

    @property
    def mouse_sensitivity(self) -> primitives.Float | None:
        """How sensitive the game head movement is to mouse movement."""
        member = self.get_member("MouseSensitivity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_sensitivity.setter
    def mouse_sensitivity(self, value: primitives.Float) -> None:
        """Set the MouseSensitivity field value."""
        member = self.get_member("MouseSensitivity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouseSensitivity", fields.FieldFloat(value=value)
            )

    @property
    def scroll_wheel_grab_move_speed(self) -> primitives.Float | None:
        """How far items move to and from the player while being grabbed and the scroll wheel is moved 1 unit."""
        member = self.get_member("ScrollWheelGrabMoveSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scroll_wheel_grab_move_speed.setter
    def scroll_wheel_grab_move_speed(self, value: primitives.Float) -> None:
        """Set the ScrollWheelGrabMoveSpeed field value."""
        member = self.get_member("ScrollWheelGrabMoveSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScrollWheelGrabMoveSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mouse_look_speed(self) -> primitives.Float | None:
        """How fast the mouse moves the camera."""
        member = self.get_member("MouseLookSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_look_speed.setter
    def mouse_look_speed(self, value: primitives.Float) -> None:
        """Set the MouseLookSpeed field value."""
        member = self.get_member("MouseLookSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouseLookSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mouse_pan_speed(self) -> primitives.Float | None:
        """How fast the mouse moves the camera sideways and up/down when focused on an inspector."""
        member = self.get_member("MousePanSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_pan_speed.setter
    def mouse_pan_speed(self, value: primitives.Float) -> None:
        """Set the MousePanSpeed field value."""
        member = self.get_member("MousePanSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MousePanSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mouse_rotate_speed(self) -> primitives.Float | None:
        """How fast the mouse can be used to rotate objects."""
        member = self.get_member("MouseRotateSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_rotate_speed.setter
    def mouse_rotate_speed(self, value: primitives.Float) -> None:
        """Set the MouseRotateSpeed field value."""
        member = self.get_member("MouseRotateSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouseRotateSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mouse_freeform_rotate_speed(self) -> primitives.Float | None:
        """How fast the mouse can be used to free form look in 3rd person desktop mode."""
        member = self.get_member("MouseFreeformRotateSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_freeform_rotate_speed.setter
    def mouse_freeform_rotate_speed(self, value: primitives.Float) -> None:
        """Set the MouseFreeformRotateSpeed field value."""
        member = self.get_member("MouseFreeformRotateSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouseFreeformRotateSpeed", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

