"""Generated component: TrackerSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TrackerSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.TrackerSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackerSettings"

    def __init__(self, use_trackers: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_trackers: Initial value for UseTrackers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_trackers is not None:
            self.use_trackers = use_trackers

    @property
    def use_trackers(self) -> bool | None:
        """The UseTrackers field value."""
        member = self.get_member("UseTrackers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_trackers.setter
    def use_trackers(self, value: bool) -> None:
        """Set the UseTrackers field value."""
        member = self.get_member("UseTrackers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseTrackers", fields.FieldBool(value=value)
            )

    @property
    def trackers(self) -> members.SyncList | None:
        """The Trackers member."""
        member = self.get_member("Trackers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @trackers.setter
    def trackers(self, value: members.SyncList) -> None:
        """Set the Trackers member."""
        self.set_member("Trackers", value)

    async def get_tracker_for_subsetting(self, resolink: protocols.ResoniteLinkClient, key: str, debug: bool = False) -> dict:
        """Call the GetTrackerForSubsetting sync method.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetTrackerForSubsetting", {"key": key}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

