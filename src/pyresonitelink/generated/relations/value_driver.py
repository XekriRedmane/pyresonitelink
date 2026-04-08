"""Generated component: ValueDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueDriver<>.

    Category: Relations

    Parameterize with a value type::

        ValueDriver[np.float32]
        ValueDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueDriver<>"

    def __init__(self, value_source: str | IValue[T] | None = None, drive_target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value_source: Initial value for ValueSource.
            drive_target: Initial value for DriveTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value_source is not None:
            self.value_source = value_source
        if drive_target is not None:
            self.drive_target = drive_target

    @property
    def value_source(self) -> str | None:
        """Target ID of the ValueSource reference (targets IValue[T])."""
        member = self.get_member("ValueSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value_source.setter
    def value_source(self, target: str | IValue[T] | None) -> None:
        """Set the ValueSource reference by target ID or IValue[T] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("ValueSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ValueSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<T>'),
            )

    @property
    def drive_target(self) -> str | None:
        """Target ID of the DriveTarget reference (targets IField[T])."""
        member = self.get_member("DriveTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_target.setter
    def drive_target(self, target: str | IField[T] | None) -> None:
        """Set the DriveTarget reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

