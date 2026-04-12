"""Generated component: SetValue."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetValue(GenericComponent[T], IUndoable, IWorldEventReceiver):
    """Set Value is a component that is part of the undo system.

    Parameterize with a value type::

        SetValue[primitives.Float]
        SetValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SetValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.Undo.SetValue<>"

    def __init__(self, target: str | IField[T] | None = None, value_before: T | None = None, value_after: T | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value_before: Initial value for ValueBefore.
            value_after: Initial value for ValueAfter.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value_before is not None:
            self.value_before = value_before
        if value_after is not None:
            self.value_after = value_after
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """The field edited by the user."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def value_before(self) -> T | None:
        """The ValueBefore field value (type depends on type parameter)."""
        member = self.get_member("ValueBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_before.setter
    def value_before(self, value: T) -> None:
        """Set the ValueBefore field value."""
        member = self.get_member("ValueBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "ValueBefore", self._type_info.field_class(value=value)
            )

    @property
    def value_after(self) -> T | None:
        """The ValueAfter field value (type depends on type parameter)."""
        member = self.get_member("ValueAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_after.setter
    def value_after(self, value: T) -> None:
        """Set the ValueAfter field value."""
        member = self.get_member("ValueAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "ValueAfter", self._type_info.field_class(value=value)
            )

    @property
    def performed(self) -> primitives.Bool | None:
        """Whether this has been done or has been undone instead."""
        member = self.get_member("_performed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @performed.setter
    def performed(self, value: primitives.Bool) -> None:
        """Set the _performed field value."""
        member = self.get_member("_performed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_performed", fields.FieldBool(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The description of this undo step."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
            )

