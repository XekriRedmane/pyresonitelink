"""Generated component: UserRestrictionsSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class UserRestrictionsSettings(GeneratedComponent, ICustomInspector):
    """The UserRestrictionsSettings component is found in the user space and contains all blocked user entries. this is a good way to handle blocked users until they fix the regression of no longer having a blocked users list introduced in the settings update.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserRestrictionsSettings"

    @property
    def entries(self) -> members.SyncList | None:
        """A list of blocked users."""
        member = self.get_member("Entries")
        if isinstance(member, members.SyncList):
            return member
        return None

    @entries.setter
    def entries(self, value: members.SyncList) -> None:
        """Set Entries. A list of blocked users."""
        self.set_member("Entries", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

