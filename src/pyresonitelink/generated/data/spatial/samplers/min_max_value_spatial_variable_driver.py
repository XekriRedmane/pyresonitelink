"""Generated component: MinMaxValueSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MinMaxValueSpatialVariableDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MinMaxValueSpatialVariableDriver<>.

    Category: Data/Spatial/Samplers

    Parameterize with a value type::

        MinMaxValueSpatialVariableDriver[np.float32]
        MinMaxValueSpatialVariableDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MinMaxValueSpatialVariableDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.MinMaxValueSpatialVariableDriver<>"

    def __init__(self, min_drive: str | IField[T] | None = None, max_drive: str | IField[T] | None = None, variable_name: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_drive: Initial value for MinDrive.
            max_drive: Initial value for MaxDrive.
            variable_name: Initial value for VariableName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_drive is not None:
            self.min_drive = min_drive
        if max_drive is not None:
            self.max_drive = max_drive
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def min_drive(self) -> str | None:
        """Target ID of the MinDrive reference (targets IField[T])."""
        member = self.get_member("MinDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_drive.setter
    def min_drive(self, target: str | IField[T] | None) -> None:
        """Set the MinDrive reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MinDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MinDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def max_drive(self) -> str | None:
        """Target ID of the MaxDrive reference (targets IField[T])."""
        member = self.get_member("MaxDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_drive.setter
    def max_drive(self, target: str | IField[T] | None) -> None:
        """Set the MaxDrive reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("MaxDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaxDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def variable_name(self) -> str | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: str) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

