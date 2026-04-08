"""Generated component: EditSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class EditSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.EditSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EditSettings"

    def __init__(self, confirm_component_destroy: bool | None = None, confirm_slot_destroy: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            confirm_component_destroy: Initial value for ConfirmComponentDestroy.
            confirm_slot_destroy: Initial value for ConfirmSlotDestroy.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if confirm_component_destroy is not None:
            self.confirm_component_destroy = confirm_component_destroy
        if confirm_slot_destroy is not None:
            self.confirm_slot_destroy = confirm_slot_destroy

    @property
    def confirm_component_destroy(self) -> bool | None:
        """The ConfirmComponentDestroy field value."""
        member = self.get_member("ConfirmComponentDestroy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @confirm_component_destroy.setter
    def confirm_component_destroy(self, value: bool) -> None:
        """Set the ConfirmComponentDestroy field value."""
        member = self.get_member("ConfirmComponentDestroy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConfirmComponentDestroy", fields.FieldBool(value=value)
            )

    @property
    def confirm_slot_destroy(self) -> bool | None:
        """The ConfirmSlotDestroy field value."""
        member = self.get_member("ConfirmSlotDestroy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @confirm_slot_destroy.setter
    def confirm_slot_destroy(self, value: bool) -> None:
        """Set the ConfirmSlotDestroy field value."""
        member = self.get_member("ConfirmSlotDestroy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConfirmSlotDestroy", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

