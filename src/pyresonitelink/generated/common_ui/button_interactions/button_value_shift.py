"""Generated component: ButtonValueShift."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonValueShift(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonValueShift<>.

    Category: Common UI/Button Interactions

    Parameterize with a value type::

        ButtonValueShift[np.float32]
        ButtonValueShift[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonValueShift<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonValueShift<>"

    def __init__(self, target_value: str | IField[T] | None = None, delta: T | None = None, min: T | None = None, max: T | None = None, wrap_around: bool | None = None, max_is_exclusive: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            delta: Initial value for Delta.
            min: Initial value for Min.
            max: Initial value for Max.
            wrap_around: Initial value for WrapAround.
            max_is_exclusive: Initial value for MaxIsExclusive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value
        if delta is not None:
            self.delta = delta
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if wrap_around is not None:
            self.wrap_around = wrap_around
        if max_is_exclusive is not None:
            self.max_is_exclusive = max_is_exclusive

    @property
    def target_value(self) -> str | None:
        """Target ID of the TargetValue reference (targets IField[T])."""
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
    def delta(self) -> T | None:
        """The Delta field value (type depends on type parameter)."""
        member = self.get_member("Delta")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @delta.setter
    def delta(self, value: T) -> None:
        """Set the Delta field value."""
        member = self.get_member("Delta")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Delta", self._type_info.field_class(value=value)
            )

    @property
    def min(self) -> T | None:
        """The Min field value (type depends on type parameter)."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: T) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Min", self._type_info.field_class(value=value)
            )

    @property
    def max(self) -> T | None:
        """The Max field value (type depends on type parameter)."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: T) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Max", self._type_info.field_class(value=value)
            )

    @property
    def wrap_around(self) -> bool | None:
        """The WrapAround field value."""
        member = self.get_member("WrapAround")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wrap_around.setter
    def wrap_around(self, value: bool) -> None:
        """Set the WrapAround field value."""
        member = self.get_member("WrapAround")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WrapAround", fields.FieldBool(value=value)
            )

    @property
    def max_is_exclusive(self) -> bool | None:
        """The MaxIsExclusive field value."""
        member = self.get_member("MaxIsExclusive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_is_exclusive.setter
    def max_is_exclusive(self, value: bool) -> None:
        """Set the MaxIsExclusive field value."""
        member = self.get_member("MaxIsExclusive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIsExclusive", fields.FieldBool(value=value)
            )

