"""Generated component: CustomizationSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class CustomizationSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.CustomizationSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CustomizationSettings"

    def __init__(self, user_interface_edit_mode: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_interface_edit_mode: Initial value for UserInterfaceEditMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_interface_edit_mode is not None:
            self.user_interface_edit_mode = user_interface_edit_mode

    @property
    def user_interface_edit_mode(self) -> bool | None:
        """The UserInterfaceEditMode field value."""
        member = self.get_member("UserInterfaceEditMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_interface_edit_mode.setter
    def user_interface_edit_mode(self, value: bool) -> None:
        """Set the UserInterfaceEditMode field value."""
        member = self.get_member("UserInterfaceEditMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserInterfaceEditMode", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

