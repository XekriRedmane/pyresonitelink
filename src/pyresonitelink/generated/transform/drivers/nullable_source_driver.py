"""Generated component: NullableSourceDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.nullable import Nullable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NullableSourceDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The NullableSourceDriver component allows for getting info from a ``Source`` nullable and driving a set of split fields with content from the nullable. Changes to driven fields by this component can also be reverse written back to ``Source``.

    Category: Transform/Drivers

    Can be used to extract data from nullables or write to them using a
    component only solution.

    Parameterize with a value type::

        NullableSourceDriver[primitives.Float]
        NullableSourceDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NullableSourceDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.NullableSourceDriver<>"

    def __init__(self, source: str | IField[Nullable[T]] | None = None, value: str | IField[T] | None = None, has_value: str | IField[primitives.Bool] | None = None, default_value: T | None = None, write_back: primitives.Bool | None = None, update_default_value: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            value: Initial value for Value.
            has_value: Initial value for HasValue.
            default_value: Initial value for DefaultValue.
            write_back: Initial value for WriteBack.
            update_default_value: Initial value for UpdateDefaultValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if value is not None:
            self.value = value
        if has_value is not None:
            self.has_value = has_value
        if default_value is not None:
            self.default_value = default_value
        if write_back is not None:
            self.write_back = write_back
        if update_default_value is not None:
            self.update_default_value = update_default_value

    @property
    def source(self) -> str | None:
        """The field to get nullable data from."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[Nullable[T]] | None) -> None:
        """Set the Source reference by target ID or IField[Nullable[T]] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Nullable<T>>'),
            )

    @property
    def value(self) -> str | None:
        """The field to drive with the value for ``Source`` if it has a value, or instead drive with ``DefaultValue``."""
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

    @property
    def has_value(self) -> str | None:
        """The field to drive with whether ``Source`` has a value."""
        member = self.get_member("HasValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_value.setter
    def has_value(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasValue reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def default_value(self) -> T | None:
        """The DefaultValue field value (type depends on type parameter)."""
        member = self.get_member("DefaultValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_value.setter
    def default_value(self, value: T) -> None:
        """Set the DefaultValue field value."""
        member = self.get_member("DefaultValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "DefaultValue", self._type_info.field_class(value=value)
            )

    @property
    def write_back(self) -> primitives.Bool | None:
        """Whether writes to the fields driven by this component will update the value of ``Source``. See write backs."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

    @property
    def update_default_value(self) -> primitives.Bool | None:
        """Whether the default value gets updated when using write back and ``Source`` has no value."""
        member = self.get_member("UpdateDefaultValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_default_value.setter
    def update_default_value(self, value: primitives.Bool) -> None:
        """Set the UpdateDefaultValue field value."""
        member = self.get_member("UpdateDefaultValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateDefaultValue", fields.FieldBool(value=value)
            )

