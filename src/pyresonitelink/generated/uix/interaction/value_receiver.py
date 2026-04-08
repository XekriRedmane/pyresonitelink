"""Generated component: ValueReceiver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.ivalue_receiver import IValueReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueReceiver(GenericComponent[T], IUIGrabReceiver, IValueReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ValueReceiver<>.

    Category: UIX/Interaction

    Parameterize with a value type::

        ValueReceiver[np.float32]
        ValueReceiver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ValueReceiver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ValueReceiver<>"

    def __init__(self, field: str | IField[T] | None = None, undoable: bool | None = None, try_convert_values: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            field: Initial value for Field.
            undoable: Initial value for Undoable.
            try_convert_values: Initial value for TryConvertValues.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if field is not None:
            self.field = field
        if undoable is not None:
            self.undoable = undoable
        if try_convert_values is not None:
            self.try_convert_values = try_convert_values

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

    @property
    def undoable(self) -> bool | None:
        """The Undoable field value."""
        member = self.get_member("Undoable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undoable.setter
    def undoable(self, value: bool) -> None:
        """Set the Undoable field value."""
        member = self.get_member("Undoable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Undoable", fields.FieldBool(value=value)
            )

    @property
    def try_convert_values(self) -> bool | None:
        """The TryConvertValues field value."""
        member = self.get_member("TryConvertValues")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @try_convert_values.setter
    def try_convert_values(self, value: bool) -> None:
        """Set the TryConvertValues field value."""
        member = self.get_member("TryConvertValues")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TryConvertValues", fields.FieldBool(value=value)
            )

