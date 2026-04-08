"""Generated component: ColliderEventRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icollider import ICollider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColliderEventRelay(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColliderEventRelay.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColliderEventRelay"

    def __init__(self, collider: str | ICollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collider: Initial value for Collider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collider is not None:
            self.collider = collider

    @property
    def collider(self) -> str | None:
        """Target ID of the Collider reference (targets ICollider)."""
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | ICollider | None) -> None:
        """Set the Collider reference by target ID or ICollider instance."""
        target_id: str | None = target.id if isinstance(target, ICollider) else target  # type: ignore[assignment]
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ICollider'),
            )

