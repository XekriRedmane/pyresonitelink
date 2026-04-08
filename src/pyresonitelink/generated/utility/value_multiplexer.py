"""Generated component: ValueMultiplexer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueMultiplexer(GenericComponent[T], IValue[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueMultiplexer<>.

    Category: Utility

    Parameterize with a value type::

        ValueMultiplexer[np.float32]
        ValueMultiplexer[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueMultiplexer<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueMultiplexer<>"

    def __init__(self, target: str | IField[T] | None = None, index: np.int32 | None = None, allow_write_back: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            index: Initial value for Index.
            allow_write_back: Initial value for AllowWriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if index is not None:
            self.index = index
        if allow_write_back is not None:
            self.allow_write_back = allow_write_back

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
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
    def index(self) -> np.int32 | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: np.int32) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def values(self) -> members.SyncList | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncList):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncList) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

    @property
    def allow_write_back(self) -> bool | None:
        """The AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_back.setter
    def allow_write_back(self, value: bool) -> None:
        """Set the AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteBack", fields.FieldBool(value=value)
            )

