"""Generated component: CallbackValueArgument."""

from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CallbackValueArgument(GenericComponent[T], IComponent, IWorldEventReceiver):
    """This isn't very often used by the user, since there aren't many Sync Delegates in the game that match this component's requirements.

    Parameterize with a value type::

        CallbackValueArgument[primitives.Float]
        CallbackValueArgument[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CallbackValueArgument<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CallbackValueArgument<>"

    def __init__(self, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value

    @property
    def value(self) -> T | None:
        """The Value field value (type depends on type parameter)."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: T) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value", self._type_info.field_class(value=value)
            )

    async def call(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call ``Callback`` sync delegate and provide it ``Value``.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Call", {}, debug,
        )

    async def call_and_destroy(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Do ``Call()`` and then destroy this component.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "CallAndDestroy", {}, debug,
        )

