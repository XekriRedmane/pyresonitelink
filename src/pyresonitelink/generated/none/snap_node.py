"""Generated component: SnapNode."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapNode(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SnapNode component does nothing.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapNode"

    def __init__(self, snap_radius: primitives.Float | None = None, collider_radius: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            snap_radius: Initial value for SnapRadius.
            collider_radius: Initial value for _colliderRadius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if snap_radius is not None:
            self.snap_radius = snap_radius
        if collider_radius is not None:
            self.collider_radius = collider_radius

    @property
    def snap_radius(self) -> primitives.Float | None:
        """Radius."""
        member = self.get_member("SnapRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_radius.setter
    def snap_radius(self, value: primitives.Float) -> None:
        """Set the SnapRadius field value."""
        member = self.get_member("SnapRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapRadius", fields.FieldFloat(value=value)
            )

    @property
    def collider_radius(self) -> str | None:
        """Collider radius field to drive."""
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_radius.setter
    def collider_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _colliderRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

