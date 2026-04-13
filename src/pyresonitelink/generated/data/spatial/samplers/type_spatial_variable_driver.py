"""Generated component: TypeSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_type import SyncType
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeSpatialVariableDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Type Spatial Variable Driver component is part of the Spatial variables system. It will drive a field with value sampled at the current global position of the slot it's on. The value used is one with highest priority

    Category: Data/Spatial/Samplers

    Attach to a slot and provide a field to drive and a variable name. the
    slot this component is on acts as the position for sampling variable
    values.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeSpatialVariableDriver"

    def __init__(self, drive: str | SyncType | None = None, variable_name: primitives.String | None = None, default_type: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive: Initial value for Drive.
            variable_name: Initial value for VariableName.
            default_type: Initial value for DefaultType.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive is not None:
            self.drive = drive
        if variable_name is not None:
            self.variable_name = variable_name
        if default_type is not None:
            self.default_type = default_type

    @property
    def drive(self) -> str | None:
        """The field to drive with the sampled value."""
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
    def default_type(self) -> Type | None:
        """The value to default to if no variable is found from sampling at the point of the slot this component is on."""
        member = self.get_member("DefaultType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @default_type.setter
    def default_type(self, value: Type | str) -> None:
        """Set DefaultType. The value to default to if no variable is found from sampling at the point of the slot this component is on."""
        member = self.get_member("DefaultType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DefaultType",
                members.FieldEnum(value=str(value)),
            )

