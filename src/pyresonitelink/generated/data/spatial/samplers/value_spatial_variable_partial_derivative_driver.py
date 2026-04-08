"""Generated component: ValueSpatialVariablePartialDerivativeDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueSpatialVariablePartialDerivativeDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueSpatialVariablePartialDerivativeDriver<>.

    Category: Data/Spatial/Samplers

    Parameterize with a value type::

        ValueSpatialVariablePartialDerivativeDriver[primitives.Float]
        ValueSpatialVariablePartialDerivativeDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueSpatialVariablePartialDerivativeDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueSpatialVariablePartialDerivativeDriver<>"

    def __init__(self, drive_x: str | IField[T] | None = None, drive_y: str | IField[T] | None = None, drive_z: str | IField[T] | None = None, variable_name: primitives.String | None = None, default_value: T | None = None, sampling_distance: primitives.Float | None = None, compute_in_local_space: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive_x: Initial value for DriveX.
            drive_y: Initial value for DriveY.
            drive_z: Initial value for DriveZ.
            variable_name: Initial value for VariableName.
            default_value: Initial value for DefaultValue.
            sampling_distance: Initial value for SamplingDistance.
            compute_in_local_space: Initial value for ComputeInLocalSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive_x is not None:
            self.drive_x = drive_x
        if drive_y is not None:
            self.drive_y = drive_y
        if drive_z is not None:
            self.drive_z = drive_z
        if variable_name is not None:
            self.variable_name = variable_name
        if default_value is not None:
            self.default_value = default_value
        if sampling_distance is not None:
            self.sampling_distance = sampling_distance
        if compute_in_local_space is not None:
            self.compute_in_local_space = compute_in_local_space

    @property
    def drive_x(self) -> str | None:
        """Target ID of the DriveX reference (targets IField[T])."""
        member = self.get_member("DriveX")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_x.setter
    def drive_x(self, target: str | IField[T] | None) -> None:
        """Set the DriveX reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveX")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveX",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def drive_y(self) -> str | None:
        """Target ID of the DriveY reference (targets IField[T])."""
        member = self.get_member("DriveY")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_y.setter
    def drive_y(self, target: str | IField[T] | None) -> None:
        """Set the DriveY reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveY")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveY",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def drive_z(self) -> str | None:
        """Target ID of the DriveZ reference (targets IField[T])."""
        member = self.get_member("DriveZ")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_z.setter
    def drive_z(self, target: str | IField[T] | None) -> None:
        """Set the DriveZ reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveZ")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveZ",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def variable_name(self) -> primitives.String | None:
        """The VariableName field value."""
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
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

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
    def sampling_distance(self) -> primitives.Float | None:
        """The SamplingDistance field value."""
        member = self.get_member("SamplingDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sampling_distance.setter
    def sampling_distance(self, value: primitives.Float) -> None:
        """Set the SamplingDistance field value."""
        member = self.get_member("SamplingDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SamplingDistance", fields.FieldFloat(value=value)
            )

    @property
    def compute_in_local_space(self) -> primitives.Bool | None:
        """The ComputeInLocalSpace field value."""
        member = self.get_member("ComputeInLocalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @compute_in_local_space.setter
    def compute_in_local_space(self, value: primitives.Bool) -> None:
        """Set the ComputeInLocalSpace field value."""
        member = self.get_member("ComputeInLocalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ComputeInLocalSpace", fields.FieldBool(value=value)
            )

