"""Generated component: VideoStreamingServicesSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class VideoStreamingServicesSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.VideoStreamingServicesSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoStreamingServicesSettings"

    @property
    def use_cookies_from_browser(self) -> members.FieldEnum | None:
        """The UseCookiesFromBrowser member."""
        member = self.get_member("UseCookiesFromBrowser")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @use_cookies_from_browser.setter
    def use_cookies_from_browser(self, value: members.FieldEnum) -> None:
        """Set the UseCookiesFromBrowser member."""
        self.set_member("UseCookiesFromBrowser", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

