"""Generated component: VideoStreamingServicesSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.cookies_browser import CookiesBrowser
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class VideoStreamingServicesSettings(GeneratedComponent, ICustomInspector):
    """The VideoStreamingServicesSettings component handles settings for streaming service content downloading like allowing usage of browser cookies to get around the issue of "login to confirm you're not a bot" issue.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoStreamingServicesSettings"

    def __init__(self, use_cookies_from_browser: CookiesBrowser | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_cookies_from_browser: Initial value for UseCookiesFromBrowser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_cookies_from_browser is not None:
            self.use_cookies_from_browser = use_cookies_from_browser

    @property
    def use_cookies_from_browser(self) -> CookiesBrowser | None:
        """allows usage of browser cookies to get around the issue of "login to confirm you're not a bot" issue."""
        member = self.get_member("UseCookiesFromBrowser")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CookiesBrowser(member.value)
        return None

    @use_cookies_from_browser.setter
    def use_cookies_from_browser(self, value: CookiesBrowser | str) -> None:
        """Set UseCookiesFromBrowser. allows usage of browser cookies to get around the issue of "login to confirm you're not a bot" issue."""
        member = self.get_member("UseCookiesFromBrowser")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "UseCookiesFromBrowser",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

