"""Generated component: BooleanSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanSpatialVariableDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanSpatialVariableDriver.

    Category: Data/Spatial/Samplers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanSpatialVariableDriver"

    def __init__(self, drive: str | IField[bool] | None = None, variable_name: str | None = None, default_value: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive: Initial value for Drive.
            variable_name: Initial value for VariableName.
            default_value: Initial value for DefaultValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive is not None:
            self.drive = drive
        if variable_name is not None:
            self.variable_name = variable_name
        if default_value is not None:
            self.default_value = default_value

    @property
    def drive(self) -> str | None:
        """Target ID of the Drive reference (targets IField[bool])."""
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | IField[bool] | None) -> None:
        """Set the Drive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
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
    def default_value(self) -> bool | None:
        """The DefaultValue field value."""
        member = self.get_member("DefaultValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_value.setter
    def default_value(self, value: bool) -> None:
        """Set the DefaultValue field value."""
        member = self.get_member("DefaultValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultValue", fields.FieldBool(value=value)
            )

