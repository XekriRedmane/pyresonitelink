"""Generated component: ImportSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.openable_url_import_preference import OpenableUrlImportPreference
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class ImportSettings(GeneratedComponent, ICustomInspector):
    """The Import Settings component handles how world links being pasted into the game should be imported.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImportSettings"

    def __init__(self, session_urls: OpenableUrlImportPreference | str | None = None, world_urls: OpenableUrlImportPreference | str | None = None, network_urls: OpenableUrlImportPreference | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            session_urls: Initial value for SessionUrls.
            world_urls: Initial value for WorldUrls.
            network_urls: Initial value for NetworkUrls.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if session_urls is not None:
            self.session_urls = session_urls
        if world_urls is not None:
            self.world_urls = world_urls
        if network_urls is not None:
            self.network_urls = network_urls

    @property
    def session_urls(self) -> OpenableUrlImportPreference | None:
        """How to handle pasted session URLs."""
        member = self.get_member("SessionUrls")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OpenableUrlImportPreference(member.value)
        return None

    @session_urls.setter
    def session_urls(self, value: OpenableUrlImportPreference | str) -> None:
        """Set SessionUrls. How to handle pasted session URLs."""
        member = self.get_member("SessionUrls")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SessionUrls",
                members.FieldEnum(value=str(value)),
            )

    @property
    def world_urls(self) -> OpenableUrlImportPreference | None:
        """How to handle pasted world URLs."""
        member = self.get_member("WorldUrls")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OpenableUrlImportPreference(member.value)
        return None

    @world_urls.setter
    def world_urls(self, value: OpenableUrlImportPreference | str) -> None:
        """Set WorldUrls. How to handle pasted world URLs."""
        member = self.get_member("WorldUrls")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WorldUrls",
                members.FieldEnum(value=str(value)),
            )

    @property
    def network_urls(self) -> OpenableUrlImportPreference | None:
        """How to handle pasted network URLs."""
        member = self.get_member("NetworkUrls")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OpenableUrlImportPreference(member.value)
        return None

    @network_urls.setter
    def network_urls(self, value: OpenableUrlImportPreference | str) -> None:
        """Set NetworkUrls. How to handle pasted network URLs."""
        member = self.get_member("NetworkUrls")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "NetworkUrls",
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

