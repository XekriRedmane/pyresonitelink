"""Generated component: OSC_Value."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.osc_handler import OSC_Handler


class OSC_Value(GenericComponent[T]):
    """Wrapper for [FrooxEngine]FrooxEngine.OSC_Value<>.

    Category: Network/OSC

    Parameterize with a value type::

        OSC_Value[primitives.Float]
        OSC_Value[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OSC_Value<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.OSC_Value<>"

    def __init__(self, handler: str | OSC_Handler | None = None, path: primitives.String | None = None, argument_index: primitives.Int | None = None, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            handler: Initial value for Handler.
            path: Initial value for Path.
            argument_index: Initial value for ArgumentIndex.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if handler is not None:
            self.handler = handler
        if path is not None:
            self.path = path
        if argument_index is not None:
            self.argument_index = argument_index
        if value is not None:
            self.value = value

    @property
    def handler(self) -> str | None:
        """Target ID of the Handler reference (targets OSC_Handler)."""
        member = self.get_member("Handler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handler.setter
    def handler(self, target: str | OSC_Handler | None) -> None:
        """Set the Handler reference by target ID or OSC_Handler instance."""
        target_id: str | None = target.id if isinstance(target, OSC_Handler) else target  # type: ignore[assignment]
        member = self.get_member("Handler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Handler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OSC_Handler'),
            )

    @property
    def path(self) -> primitives.String | None:
        """The Path field value."""
        member = self.get_member("Path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the Path field value."""
        member = self.get_member("Path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Path", fields.FieldString(value=value)
            )

    @property
    def argument_index(self) -> primitives.Int | None:
        """The ArgumentIndex field value."""
        member = self.get_member("ArgumentIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @argument_index.setter
    def argument_index(self, value: primitives.Int) -> None:
        """Set the ArgumentIndex field value."""
        member = self.get_member("ArgumentIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArgumentIndex", fields.FieldInt(value=value)
            )

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

