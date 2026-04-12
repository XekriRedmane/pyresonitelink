"""Generated component: NamePlateSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.nameplate_visibility import NameplateVisibility
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class NamePlateSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NamePlateSettings"

    def __init__(self, nameplate_visibility: NameplateVisibility | str | None = None, use_custom_nameplates: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            nameplate_visibility: Initial value for NameplateVisibility.
            use_custom_nameplates: Initial value for UseCustomNameplates.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if nameplate_visibility is not None:
            self.nameplate_visibility = nameplate_visibility
        if use_custom_nameplates is not None:
            self.use_custom_nameplates = use_custom_nameplates

    @property
    def nameplate_visibility(self) -> NameplateVisibility | None:
        """can be used to control what nameplates the user sees."""
        member = self.get_member("NameplateVisibility")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NameplateVisibility(member.value)
        return None

    @nameplate_visibility.setter
    def nameplate_visibility(self, value: NameplateVisibility | str) -> None:
        """Set NameplateVisibility. can be used to control what nameplates the user sees."""
        member = self.get_member("NameplateVisibility")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "NameplateVisibility",
                members.FieldEnum(value=str(value)),
            )

    @property
    def use_custom_nameplates(self) -> primitives.Bool | None:
        """Whether to render the default nameplates or user made ones."""
        member = self.get_member("UseCustomNameplates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_custom_nameplates.setter
    def use_custom_nameplates(self, value: primitives.Bool) -> None:
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

