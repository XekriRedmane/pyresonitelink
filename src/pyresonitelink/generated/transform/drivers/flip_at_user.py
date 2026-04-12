"""Generated component: FlipAtUser."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FlipAtUser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The FlipAtUser component can be used to make an object face towards positive or negative Z, depending on what side of it the local user is.

    Category: Transform/Drivers

    **Related Components**: Look At User
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FlipAtUser"

    def __init__(self, rotation: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rotation: Initial value for _rotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rotation is not None:
            self.rotation = rotation

    @property
    def up_space(self) -> members.SyncObject | None:
        """the coordinate space that is used when calculating what is "up". If set to local user space, then the up direction of this component is the up direction of the slot the user is parented under, which is usually up for that user. This can be useful if a user is in a gravity direction which doesn't match the world's up direction, and will make this orient to that user's direction for a better reading experience for example."""
        member = self.get_member("UpSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @up_space.setter
    def up_space(self, value: members.SyncObject) -> None:
        """Set UpSpace. the coordinate space that is used when calculating what is "up". If set to local user space, then the up direction of this component is the up direction of the slot the user is parented under, which is usually up for that user. This can be useful if a user is in a gravity direction which doesn't match the world's up direction, and will make this orient to that user's direction for a better reading experience for example."""
        self.set_member("UpSpace", value)

    @property
    def rotation(self) -> str | None:
        """The field that is driven to make the object rotate to the user. This is automatically set to the Rotation field of the slot this component is added to."""
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

