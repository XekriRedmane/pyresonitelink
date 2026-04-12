"""Generated component: ButtonValueActionTrigger."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonValueActionTrigger(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonValueActionTrigger component receives any Button Event and uses it to trigger a Sync Delegate and sends a value to it.

    Category: Common UI/Button Interactions

    Attach to a slot with a button, or a slot targeted by a ButtonRelay or
    related. Then, find a Sync Delegate to trigger using this component.
    Lastly, put the sync delegate into any ``OnPressed``, ``OnPressing``,
    and/or ``OnReleased``; then provide ``Value``

    Parameterize with a value type::

        ButtonValueActionTrigger[primitives.Float]
        ButtonValueActionTrigger[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonValueActionTrigger<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonValueActionTrigger<>"

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

