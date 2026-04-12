"""Generated component: ButtonValueSet."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonValueSet(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonValueSet component takes in a Value Type and a ``TargetValue``. When an IButton is pressed while this component is on the same slot, this will send the value to the provided ``TargetValue``.

}}

    Category: Common UI/Button Interactions

    This is similar to the Write ProtoFlux node but as a component instead.

    Parameterize with a value type::

        ButtonValueSet[primitives.Float]
        ButtonValueSet[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonValueSet<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonValueSet<>"

    def __init__(self, target_value: str | IField[T] | None = None, set_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            set_value: Initial value for SetValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value
        if set_value is not None:
            self.set_value = set_value

    @property
    def target_value(self) -> str | None:
        """The target to send the value outwards."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[T] | None) -> None:
        """Set the TargetValue reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def set_value(self) -> T | None:
        """The SetValue field value (type depends on type parameter)."""
        member = self.get_member("SetValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_value.setter
    def set_value(self, value: T) -> None:
        """Set the SetValue field value."""
        member = self.get_member("SetValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "SetValue", self._type_info.field_class(value=value)
            )

