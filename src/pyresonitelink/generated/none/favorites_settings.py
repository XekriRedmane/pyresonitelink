"""Generated component: FavoritesSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class FavoritesSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.FavoritesSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FavoritesSettings"

    def __init__(self, auto_load_cloud_home: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_load_cloud_home: Initial value for AutoLoadCloudHome.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_load_cloud_home is not None:
            self.auto_load_cloud_home = auto_load_cloud_home

    @property
    def auto_load_cloud_home(self) -> bool | None:
        """The AutoLoadCloudHome field value."""
        member = self.get_member("AutoLoadCloudHome")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_load_cloud_home.setter
    def auto_load_cloud_home(self, value: bool) -> None:
        """Set the AutoLoadCloudHome field value."""
        member = self.get_member("AutoLoadCloudHome")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoLoadCloudHome", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

