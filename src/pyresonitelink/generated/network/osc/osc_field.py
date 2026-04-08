"""Generated component: OSC_Field."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.osc_handler import OSC_Handler
from pyresonitelink.generated._types.ifield import IField


class OSC_Field(GenericComponent[T]):
    """Wrapper for [FrooxEngine]FrooxEngine.OSC_Field<>.

    Category: Network/OSC

    Parameterize with a value type::

        OSC_Field[np.float32]
        OSC_Field[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OSC_Field<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.OSC_Field<>"

    def __init__(self, handler: str | OSC_Handler | None = None, path: str | None = None, argument_index: np.int32 | None = None, field: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            handler: Initial value for Handler.
            path: Initial value for Path.
            argument_index: Initial value for ArgumentIndex.
            field: Initial value for Field.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if handler is not None:
            self.handler = handler
        if path is not None:
            self.path = path
        if argument_index is not None:
            self.argument_index = argument_index
        if field is not None:
            self.field = field

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
    def path(self) -> str | None:
        """The Path field value."""
        member = self.get_member("Path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: str) -> None:
        """Set the Path field value."""
        member = self.get_member("Path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Path", fields.FieldString(value=value)
            )

    @property
    def argument_index(self) -> np.int32 | None:
        """The ArgumentIndex field value."""
        member = self.get_member("ArgumentIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @argument_index.setter
    def argument_index(self, value: np.int32) -> None:
        """Set the ArgumentIndex field value."""
        member = self.get_member("ArgumentIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArgumentIndex", fields.FieldInt(value=value)
            )

    @property
    def field(self) -> str | None:
        """Target ID of the Field reference (targets IField[T])."""
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @field.setter
    def field(self, target: str | IField[T] | None) -> None:
        """Set the Field reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Field")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Field",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

