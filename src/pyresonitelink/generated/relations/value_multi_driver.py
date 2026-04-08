"""Generated component: ValueMultiDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueMultiDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueMultiDriver<>.

    Category: Relations

    Parameterize with a value type::

        ValueMultiDriver[np.float32]
        ValueMultiDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueMultiDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueMultiDriver<>"

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

    @property
    def drives(self) -> members.SyncList | None:
        """The Drives member."""
        member = self.get_member("Drives")
        if isinstance(member, members.SyncList):
            return member
        return None

    @drives.setter
    def drives(self, value: members.SyncList) -> None:
        """Set the Drives member."""
        self.set_member("Drives", value)

