"""Generated component: DataPreset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataPreset(GeneratedComponent, ICustomInspector, IButtonPressReceiver, IWorldEventReceiver):
    """The DataPreset is a component that is useful for switching a list of values to a predetermined set.

    Category: Data/Presets

    Each entry in the list of Entries is a DataPresetReference or a
    DataPresetValue. These may be added manually, or, if the
    DataPresetReferences and DataPresetValues are components in this slot or
    child slots, the Add All Children button will add them for you
    (replacing any existing list). Each entry consists of the value or
    reference, plus a target field. The Set Active button applies all values
    and references to their respective target fields. The only way to
    programmatically apply the preset is to use a ProtoFlux Tool, grab the
    ``SetActive()`` Delegate, and press the "Proxy" button in your Context
    Menu, then feed a Call into the node.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataPreset"

    def __init__(self, is_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_active: Initial value for IsActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_active is not None:
            self.is_active = is_active

    @property
    def is_active(self) -> primitives.Bool | None:
        """Indicates that all the presets in Entries have been applied. Cannot be driven."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: primitives.Bool) -> None:
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
        """A list of data preset references and values."""
        member = self.get_member("Entries")
        if isinstance(member, members.SyncList):
            return member
        return None

    @entries.setter
    def entries(self, value: members.SyncList) -> None:
        """Set Entries. A list of data preset references and values."""
        self.set_member("Entries", value)

    async def set_active(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Set all target values targeted by ``Entries`` to their preset values.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetActive", {}, debug,
        )

    async def set_values(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Set all preset values in ``Entries`` to their target values.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetValues", {}, debug,
        )

