"""Generated component: NamePlateSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class NamePlateSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.NamePlateSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NamePlateSettings"

    def __init__(self, use_custom_nameplates: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_custom_nameplates: Initial value for UseCustomNameplates.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_custom_nameplates is not None:
            self.use_custom_nameplates = use_custom_nameplates

    @property
    def nameplate_visibility(self) -> members.FieldEnum | None:
        """The NameplateVisibility member."""
        member = self.get_member("NameplateVisibility")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @nameplate_visibility.setter
    def nameplate_visibility(self, value: members.FieldEnum) -> None:
        """Set the NameplateVisibility member."""
        self.set_member("NameplateVisibility", value)

    @property
    def use_custom_nameplates(self) -> bool | None:
        """The UseCustomNameplates field value."""
        member = self.get_member("UseCustomNameplates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_custom_nameplates.setter
    def use_custom_nameplates(self, value: bool) -> None:
        """Set the UseCustomNameplates field value."""
        member = self.get_member("UseCustomNameplates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseCustomNameplates", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

