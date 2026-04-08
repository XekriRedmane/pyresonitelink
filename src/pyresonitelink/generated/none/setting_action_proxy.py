"""Generated component: SettingActionProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingActionProxy(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SettingActionProxy<>.

    Parameterize with a value type::

        SettingActionProxy[primitives.Float]
        SettingActionProxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SettingActionProxy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.SettingActionProxy<>"

    def __init__(self, action_name: primitives.String | None = None, subsetting_getter: primitives.String | None = None, subsetting_key: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            action_name: Initial value for ActionName.
            subsetting_getter: Initial value for SubsettingGetter.
            subsetting_key: Initial value for SubsettingKey.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if action_name is not None:
            self.action_name = action_name
        if subsetting_getter is not None:
            self.subsetting_getter = subsetting_getter
        if subsetting_key is not None:
            self.subsetting_key = subsetting_key

    @property
    def action_name(self) -> primitives.String | None:
        """The ActionName field value."""
        member = self.get_member("ActionName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @action_name.setter
    def action_name(self, value: primitives.String) -> None:
        """Set the ActionName field value."""
        member = self.get_member("ActionName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActionName", fields.FieldString(value=value)
            )

    @property
    def subsetting_getter(self) -> primitives.String | None:
        """The SubsettingGetter field value."""
        member = self.get_member("SubsettingGetter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsetting_getter.setter
    def subsetting_getter(self, value: primitives.String) -> None:
        """Set the SubsettingGetter field value."""
        member = self.get_member("SubsettingGetter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsettingGetter", fields.FieldString(value=value)
            )

    @property
    def subsetting_key(self) -> primitives.String | None:
        """The SubsettingKey field value."""
        member = self.get_member("SubsettingKey")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsetting_key.setter
    def subsetting_key(self, value: primitives.String) -> None:
        """Set the SubsettingKey field value."""
        member = self.get_member("SubsettingKey")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsettingKey", fields.FieldString(value=value)
            )

    async def trigger(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Trigger sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Trigger", {}, debug,
        )

