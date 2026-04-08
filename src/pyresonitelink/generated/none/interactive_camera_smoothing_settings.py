"""Generated component: InteractiveCameraSmoothingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraSmoothingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraSmoothingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraSmoothingSettings"

    def __init__(self, position_smooth_speed: primitives.Float | None = None, angle_smooth_speed: primitives.Float | None = None, framing_smooth_speed: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_smooth_speed: Initial value for PositionSmoothSpeed.
            angle_smooth_speed: Initial value for AngleSmoothSpeed.
            framing_smooth_speed: Initial value for FramingSmoothSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_smooth_speed is not None:
            self.position_smooth_speed = position_smooth_speed
        if angle_smooth_speed is not None:
            self.angle_smooth_speed = angle_smooth_speed
        if framing_smooth_speed is not None:
            self.framing_smooth_speed = framing_smooth_speed

    @property
    def position_smooth_speed(self) -> primitives.Float | None:
        """The PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_smooth_speed.setter
    def position_smooth_speed(self, value: primitives.Float) -> None:
        """Set the PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def angle_smooth_speed(self) -> primitives.Float | None:
        """The AngleSmoothSpeed field value."""
        member = self.get_member("AngleSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_smooth_speed.setter
    def angle_smooth_speed(self, value: primitives.Float) -> None:
        """Set the AngleSmoothSpeed field value."""
        member = self.get_member("AngleSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def framing_smooth_speed(self) -> primitives.Float | None:
        """The FramingSmoothSpeed field value."""
        member = self.get_member("FramingSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_smooth_speed.setter
    def framing_smooth_speed(self, value: primitives.Float) -> None:
        """Set the FramingSmoothSpeed field value."""
        member = self.get_member("FramingSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingSmoothSpeed", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

