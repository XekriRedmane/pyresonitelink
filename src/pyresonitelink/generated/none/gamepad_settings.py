"""Generated component: GamepadSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GamepadSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GamepadSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GamepadSettings"

    def __init__(self, thumbstick_look_speed: primitives.Float | None = None, thumbstick_look_exponent: primitives.Float | None = None, use_gamepad_when_unfocused: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            thumbstick_look_speed: Initial value for ThumbstickLookSpeed.
            thumbstick_look_exponent: Initial value for ThumbstickLookExponent.
            use_gamepad_when_unfocused: Initial value for UseGamepadWhenUnfocused.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if thumbstick_look_speed is not None:
            self.thumbstick_look_speed = thumbstick_look_speed
        if thumbstick_look_exponent is not None:
            self.thumbstick_look_exponent = thumbstick_look_exponent
        if use_gamepad_when_unfocused is not None:
            self.use_gamepad_when_unfocused = use_gamepad_when_unfocused

    @property
    def thumbstick_look_speed(self) -> primitives.Float | None:
        """The ThumbstickLookSpeed field value."""
        member = self.get_member("ThumbstickLookSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thumbstick_look_speed.setter
    def thumbstick_look_speed(self, value: primitives.Float) -> None:
        """Set the ThumbstickLookSpeed field value."""
        member = self.get_member("ThumbstickLookSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThumbstickLookSpeed", fields.FieldFloat(value=value)
            )

    @property
    def thumbstick_look_exponent(self) -> primitives.Float | None:
        """The ThumbstickLookExponent field value."""
        member = self.get_member("ThumbstickLookExponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thumbstick_look_exponent.setter
    def thumbstick_look_exponent(self, value: primitives.Float) -> None:
        """Set the ThumbstickLookExponent field value."""
        member = self.get_member("ThumbstickLookExponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThumbstickLookExponent", fields.FieldFloat(value=value)
            )

    @property
    def use_gamepad_when_unfocused(self) -> primitives.Bool | None:
        """The UseGamepadWhenUnfocused field value."""
        member = self.get_member("UseGamepadWhenUnfocused")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_gamepad_when_unfocused.setter
    def use_gamepad_when_unfocused(self, value: primitives.Bool) -> None:
        """Set the UseGamepadWhenUnfocused field value."""
        member = self.get_member("UseGamepadWhenUnfocused")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseGamepadWhenUnfocused", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

