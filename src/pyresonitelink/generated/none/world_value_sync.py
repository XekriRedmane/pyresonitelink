"""Generated component: WorldValueSync."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldValueSync(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The WorldValueSync component is used to sync values from world space to user space.

    Not used directly by the user.

    Parameterize with a value type::

        WorldValueSync[primitives.Float]
        WorldValueSync[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldValueSync<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.WorldValueSync<>"

    def __init__(self, local_value: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            local_value: Initial value for LocalValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if local_value is not None:
            self.local_value = local_value

    @property
    def local_value(self) -> str | None:
        """The value to sync."""
        member = self.get_member("LocalValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_value.setter
    def local_value(self, target: str | IField[T] | None) -> None:
        """Set the LocalValue reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LocalValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

