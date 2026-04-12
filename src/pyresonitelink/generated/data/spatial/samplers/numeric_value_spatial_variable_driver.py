"""Generated component: NumericValueSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.value_spatial_variable_mode import ValueSpatialVariableMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NumericValueSpatialVariableDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The Numeric Value Spatial Variable Driver`1 component works specifically for numeric values and allows for multiple sampling modes.

    Category: Data/Spatial/Samplers

    Attach to a slot and provide a field to drive and a variable name. the
    slot this component is on acts as the position for sampling variable
    values.

    Parameterize with a value type::

        NumericValueSpatialVariableDriver[primitives.Float]
        NumericValueSpatialVariableDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NumericValueSpatialVariableDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.NumericValueSpatialVariableDriver<>"

    def __init__(self, drive: str | IField[T] | None = None, variable_name: primitives.String | None = None, mode: ValueSpatialVariableMode | str | None = None, default_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive: Initial value for Drive.
            variable_name: Initial value for VariableName.
            mode: Initial value for Mode.
            default_value: Initial value for DefaultValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive is not None:
            self.drive = drive
        if variable_name is not None:
            self.variable_name = variable_name
        if mode is not None:
            self.mode = mode
        if default_value is not None:
            self.default_value = default_value

    @property
    def drive(self) -> str | None:
        """The field to drive with the resulting value."""
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | IField[T] | None) -> None:
        """Set the Drive reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def variable_name(self) -> primitives.String | None:
        """The variable name to sample for."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: primitives.String) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def mode(self) -> ValueSpatialVariableMode | None:
        """How to interpret the sampled values."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ValueSpatialVariableMode(member.value)
        return None

    @mode.setter
    def mode(self, value: ValueSpatialVariableMode | str) -> None:
        """Set Mode. How to interpret the sampled values."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
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

