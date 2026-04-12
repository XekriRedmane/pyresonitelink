"""Generated component: UserMetricsSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class UserMetricsSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserMetricsSettings"

    def __init__(self, user_height: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_height: Initial value for UserHeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_height is not None:
            self.user_height = user_height

    @property
    def user_height(self) -> primitives.Float | None:
        """The height of the user in meters."""
        member = self.get_member("UserHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_height.setter
    def user_height(self, value: primitives.Float) -> None:
        """Set the UserHeight field value."""
        member = self.get_member("UserHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHeight", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

