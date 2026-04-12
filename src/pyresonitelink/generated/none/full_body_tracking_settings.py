"""Generated component: FullBodyTrackingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class FullBodyTrackingSettings(GeneratedComponent, ICustomInspector):
    """The FullBodyTrackingSettings component is used to control full body behavior in the game. It's part of the Settings menu.

    Not used directly by the user, and instead is part of the Settings menu.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FullBodyTrackingSettings"

    def __init__(self, body_horizontal_angle: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            body_horizontal_angle: Initial value for BodyHorizontalAngle.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if body_horizontal_angle is not None:
            self.body_horizontal_angle = body_horizontal_angle

    @property
    def body_horizontal_angle(self) -> primitives.Float | None:
        """The max horizontal angle before the feet no longer attempt to do walking animations."""
        member = self.get_member("BodyHorizontalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @body_horizontal_angle.setter
    def body_horizontal_angle(self, value: primitives.Float) -> None:
        """Set the BodyHorizontalAngle field value."""
        member = self.get_member("BodyHorizontalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BodyHorizontalAngle", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

