"""Generated component: TypeSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_type import SyncType
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeSpatialVariableDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TypeSpatialVariableDriver.

    Category: Data/Spatial/Samplers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeSpatialVariableDriver"

    def __init__(self, drive: str | SyncType | None = None, variable_name: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive: Initial value for Drive.
            variable_name: Initial value for VariableName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive is not None:
            self.drive = drive
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def drive(self) -> str | None:
        """Target ID of the Drive reference (targets SyncType)."""
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | SyncType | None) -> None:
        """Set the Drive reference by target ID or SyncType instance."""
        target_id: str | None = target.id if isinstance(target, SyncType) else target  # type: ignore[assignment]
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncType'),
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
    def default_type(self) -> members.FieldEnum | None:
        """The DefaultType member."""
        member = self.get_member("DefaultType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_type.setter
    def default_type(self, value: members.FieldEnum) -> None:
        """Set the DefaultType member."""
        self.set_member("DefaultType", value)

