"""Generated component: GeneralVRSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GeneralVRSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GeneralVRSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GeneralVRSettings"

    def __init__(self, use_vr_hotswitching: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_vr_hotswitching: Initial value for UseVRHotswitching.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_vr_hotswitching is not None:
            self.use_vr_hotswitching = use_vr_hotswitching

    @property
    def use_vr_hotswitching(self) -> primitives.Bool | None:
        """The UseVRHotswitching field value."""
        member = self.get_member("UseVRHotswitching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vr_hotswitching.setter
    def use_vr_hotswitching(self, value: primitives.Bool) -> None:
        """Set the UseVRHotswitching field value."""
        member = self.get_member("UseVRHotswitching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVRHotswitching", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

