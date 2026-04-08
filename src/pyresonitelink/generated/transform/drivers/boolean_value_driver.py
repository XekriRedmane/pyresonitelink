"""Generated component: BooleanValueDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanValueDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanValueDriver<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        BooleanValueDriver[primitives.Float]
        BooleanValueDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanValueDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BooleanValueDriver<>"

    def __init__(self, state: primitives.Bool | None = None, target_field: str | IField[T] | None = None, false_value: T | None = None, true_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            target_field: Initial value for TargetField.
            false_value: Initial value for FalseValue.
            true_value: Initial value for TrueValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if target_field is not None:
            self.target_field = target_field
        if false_value is not None:
            self.false_value = false_value
        if true_value is not None:
            self.true_value = true_value

    @property
    def state(self) -> primitives.Bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

    @property
    def target_field(self) -> str | None:
        """Target ID of the TargetField reference (targets IField[T])."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[T] | None) -> None:
        """Set the TargetField reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def false_value(self) -> T | None:
        """The FalseValue field value (type depends on type parameter)."""
        member = self.get_member("FalseValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @false_value.setter
    def false_value(self, value: T) -> None:
        """Set the FalseValue field value."""
        member = self.get_member("FalseValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "FalseValue", self._type_info.field_class(value=value)
            )

    @property
    def true_value(self) -> T | None:
        """The TrueValue field value (type depends on type parameter)."""
        member = self.get_member("TrueValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @true_value.setter
    def true_value(self, value: T) -> None:
        """Set the TrueValue field value."""
        member = self.get_member("TrueValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "TrueValue", self._type_info.field_class(value=value)
            )

