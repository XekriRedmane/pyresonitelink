"""Generated component: DataPreset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataPreset(GeneratedComponent, ICustomInspector, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DataPreset.

    Category: Data/Presets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataPreset"

    def __init__(self, is_active: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_active: Initial value for IsActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_active is not None:
            self.is_active = is_active

    @property
    def is_active(self) -> bool | None:
        """The IsActive field value."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    @property
    def entries(self) -> members.SyncList | None:
        """The Entries member."""
        member = self.get_member("Entries")
        if isinstance(member, members.SyncList):
            return member
        return None

    @entries.setter
    def entries(self, value: members.SyncList) -> None:
        """Set the Entries member."""
        self.set_member("Entries", value)

    async def set_active(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetActive sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetActive", {}, debug,
        )

    async def set_values(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetValues sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetValues", {}, debug,
        )

