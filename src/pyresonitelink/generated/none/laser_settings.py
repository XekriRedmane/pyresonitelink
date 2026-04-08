"""Generated component: LaserSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class LaserSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.LaserSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LaserSettings"

    def __init__(self, smooth_speed: primitives.Float | None = None, modulate_start_angle: primitives.Float | None = None, modulate_end_angle: primitives.Float | None = None, modulate_exponent: primitives.Float | None = None, modulate_speed_multiplier: primitives.Float | None = None, stick_threshold: primitives.Float | None = None, show_in_desktop: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            smooth_speed: Initial value for SmoothSpeed.
            modulate_start_angle: Initial value for ModulateStartAngle.
            modulate_end_angle: Initial value for ModulateEndAngle.
            modulate_exponent: Initial value for ModulateExponent.
            modulate_speed_multiplier: Initial value for ModulateSpeedMultiplier.
            stick_threshold: Initial value for StickThreshold.
            show_in_desktop: Initial value for ShowInDesktop.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if smooth_speed is not None:
            self.smooth_speed = smooth_speed
        if modulate_start_angle is not None:
            self.modulate_start_angle = modulate_start_angle
        if modulate_end_angle is not None:
            self.modulate_end_angle = modulate_end_angle
        if modulate_exponent is not None:
            self.modulate_exponent = modulate_exponent
        if modulate_speed_multiplier is not None:
            self.modulate_speed_multiplier = modulate_speed_multiplier
        if stick_threshold is not None:
            self.stick_threshold = stick_threshold
        if show_in_desktop is not None:
            self.show_in_desktop = show_in_desktop

    @property
    def smooth_speed(self) -> primitives.Float | None:
        """The SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_speed.setter
    def smooth_speed(self, value: primitives.Float) -> None:
        """Set the SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def modulate_start_angle(self) -> primitives.Float | None:
        """The ModulateStartAngle field value."""
        member = self.get_member("ModulateStartAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modulate_start_angle.setter
    def modulate_start_angle(self, value: primitives.Float) -> None:
        """Set the ModulateStartAngle field value."""
        member = self.get_member("ModulateStartAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModulateStartAngle", fields.FieldFloat(value=value)
            )

    @property
    def modulate_end_angle(self) -> primitives.Float | None:
        """The ModulateEndAngle field value."""
        member = self.get_member("ModulateEndAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modulate_end_angle.setter
    def modulate_end_angle(self, value: primitives.Float) -> None:
        """Set the ModulateEndAngle field value."""
        member = self.get_member("ModulateEndAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModulateEndAngle", fields.FieldFloat(value=value)
            )

    @property
    def modulate_exponent(self) -> primitives.Float | None:
        """The ModulateExponent field value."""
        member = self.get_member("ModulateExponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modulate_exponent.setter
    def modulate_exponent(self, value: primitives.Float) -> None:
        """Set the ModulateExponent field value."""
        member = self.get_member("ModulateExponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModulateExponent", fields.FieldFloat(value=value)
            )

    @property
    def modulate_speed_multiplier(self) -> primitives.Float | None:
        """The ModulateSpeedMultiplier field value."""
        member = self.get_member("ModulateSpeedMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modulate_speed_multiplier.setter
    def modulate_speed_multiplier(self, value: primitives.Float) -> None:
        """Set the ModulateSpeedMultiplier field value."""
        member = self.get_member("ModulateSpeedMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModulateSpeedMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def stick_threshold(self) -> primitives.Float | None:
        """The StickThreshold field value."""
        member = self.get_member("StickThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stick_threshold.setter
    def stick_threshold(self, value: primitives.Float) -> None:
        """Set the StickThreshold field value."""
        member = self.get_member("StickThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StickThreshold", fields.FieldFloat(value=value)
            )

    @property
    def show_in_desktop(self) -> primitives.Bool | None:
        """The ShowInDesktop field value."""
        member = self.get_member("ShowInDesktop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_in_desktop.setter
    def show_in_desktop(self, value: primitives.Bool) -> None:
        """Set the ShowInDesktop field value."""
        member = self.get_member("ShowInDesktop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowInDesktop", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

