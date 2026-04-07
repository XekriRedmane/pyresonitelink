"""Generated component: ReferenceSpatialVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceSpatialVariableDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceSpatialVariableDriver<>.

    Category: Data/Spatial/Samplers

    Parameterize with a value type::

        ReferenceSpatialVariableDriver[np.float32]
        ReferenceSpatialVariableDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceSpatialVariableDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceSpatialVariableDriver<>"

    def __init__(self, drive: str | SyncRef[T] | None = None, variable_name: str | None = None, default_target: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drive: Initial value for Drive.
            variable_name: Initial value for VariableName.
            default_target: Initial value for DefaultTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drive is not None:
            self.drive = drive
        if variable_name is not None:
            self.variable_name = variable_name
        if default_target is not None:
            self.default_target = default_target

    @property
    def drive(self) -> str | None:
        """Target ID of the Drive reference (targets SyncRef[T])."""
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | SyncRef[T] | None) -> None:
        """Set the Drive reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
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
    def default_target(self) -> str | None:
        """Target ID of the DefaultTarget reference (targets T)."""
        member = self.get_member("DefaultTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_target.setter
    def default_target(self, target: str | T | None) -> None:
        """Set the DefaultTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("DefaultTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

