"""Generated component: SnapNode."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapNode(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapNode.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapNode"

    def __init__(self, snap_radius: np.float32 | None = None, collider_radius: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
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
    def snap_radius(self) -> np.float32 | None:
        """The SnapRadius field value."""
        member = self.get_member("SnapRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_radius.setter
    def snap_radius(self, value: np.float32) -> None:
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
        """Target ID of the _colliderRadius reference (targets IField[np.float32])."""
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_radius.setter
    def collider_radius(self, target: str | IField[np.float32] | None) -> None:
        """Set the _colliderRadius reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

