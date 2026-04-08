"""Generated component: ButtonEnumShift."""

from typing import Any

E = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonEnumShift(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonEnumShift<>.

    Category: Common UI/Button Interactions

    Parameterize with a value type::

        ButtonEnumShift[primitives.Float]
        ButtonEnumShift[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonEnumShift<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonEnumShift<>"

    def __init__(self, target_value: str | IField[E] | None = None, shift_delta: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            shift_delta: Initial value for ShiftDelta.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value
        if shift_delta is not None:
            self.shift_delta = shift_delta

    @property
    def target_value(self) -> str | None:
        """Target ID of the TargetValue reference (targets IField[E])."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[E] | None) -> None:
        """Set the TargetValue reference by target ID or IField[E] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<E>'),
            )

    @property
    def shift_delta(self) -> primitives.Int | None:
        """The ShiftDelta field value."""
        member = self.get_member("ShiftDelta")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shift_delta.setter
    def shift_delta(self, value: primitives.Int) -> None:
        """Set the ShiftDelta field value."""
        member = self.get_member("ShiftDelta")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShiftDelta", fields.FieldInt(value=value)
            )

