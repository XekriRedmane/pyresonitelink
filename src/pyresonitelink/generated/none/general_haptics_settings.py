"""Generated component: GeneralHapticsSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GeneralHapticsSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GeneralHapticsSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GeneralHapticsSettings"

    def __init__(self, enable_controller_vibration: primitives.Bool | None = None, enable_haptics: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            enable_controller_vibration: Initial value for EnableControllerVibration.
            enable_haptics: Initial value for EnableHaptics.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if enable_controller_vibration is not None:
            self.enable_controller_vibration = enable_controller_vibration
        if enable_haptics is not None:
            self.enable_haptics = enable_haptics

    @property
    def enable_controller_vibration(self) -> primitives.Bool | None:
        """The EnableControllerVibration field value."""
        member = self.get_member("EnableControllerVibration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enable_controller_vibration.setter
    def enable_controller_vibration(self, value: primitives.Bool) -> None:
        """Set the EnableControllerVibration field value."""
        member = self.get_member("EnableControllerVibration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnableControllerVibration", fields.FieldBool(value=value)
            )

    @property
    def enable_haptics(self) -> primitives.Bool | None:
        """The EnableHaptics field value."""
        member = self.get_member("EnableHaptics")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enable_haptics.setter
    def enable_haptics(self, value: primitives.Bool) -> None:
        """Set the EnableHaptics field value."""
        member = self.get_member("EnableHaptics")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnableHaptics", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

