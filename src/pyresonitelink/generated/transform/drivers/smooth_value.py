"""Generated component: SmoothValue."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SmoothValue(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SmoothValue<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        SmoothValue[np.float32]
        SmoothValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SmoothValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.SmoothValue<>"

    def __init__(self, target_value: T | None = None, speed: np.float32 | None = None, write_back: bool | None = None, value: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            speed: Initial value for Speed.
            write_back: Initial value for WriteBack.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value
        if speed is not None:
            self.speed = speed
        if write_back is not None:
            self.write_back = write_back
        if value is not None:
            self.value = value

    @property
    def target_value(self) -> T | None:
        """The TargetValue field value (type depends on type parameter)."""
        member = self.get_member("TargetValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_value.setter
    def target_value(self, value: T) -> None:
        """Set the TargetValue field value."""
        member = self.get_member("TargetValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "TargetValue", self._type_info.field_class(value=value)
            )

    @property
    def speed(self) -> np.float32 | None:
        """The Speed field value."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: np.float32) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat(value=value)
            )

    @property
    def write_back(self) -> bool | None:
        """The WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets IField[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | IField[T] | None) -> None:
        """Set the Value reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

