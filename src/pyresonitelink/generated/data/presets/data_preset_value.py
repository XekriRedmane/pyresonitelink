"""Generated component: DataPresetValue."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.idata_preset_entry import IDataPresetEntry
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataPresetValue(GenericComponent[T], IDataPresetEntry, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DataPresetValue<>.

    Category: Data/Presets

    Parameterize with a value type::

        DataPresetValue[np.float32]
        DataPresetValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataPresetValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DataPresetValue<>"

    def __init__(self, preset_value: T | None = None, target_field: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            preset_value: Initial value for PresetValue.
            target_field: Initial value for TargetField.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if preset_value is not None:
            self.preset_value = preset_value
        if target_field is not None:
            self.target_field = target_field

    @property
    def preset_value(self) -> T | None:
        """The PresetValue field value (type depends on type parameter)."""
        member = self.get_member("PresetValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preset_value.setter
    def preset_value(self, value: T) -> None:
        """Set the PresetValue field value."""
        member = self.get_member("PresetValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "PresetValue", self._type_info.field_class(value=value)
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

