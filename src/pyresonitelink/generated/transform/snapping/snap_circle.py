"""Generated component: SnapCircle."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapCircle(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapCircle.

    Category: Transform/Snapping
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapCircle"

    def __init__(self, radius: np.float32 | None = None, normal: primitives.Float3 | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            normal: Initial value for Normal.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if normal is not None:
            self.normal = normal
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def normal(self) -> primitives.Float3 | None:
        """The Normal field value."""
        member = self.get_member("Normal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal.setter
    def normal(self, value: primitives.Float3) -> None:
        """Set the Normal field value."""
        member = self.get_member("Normal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Normal", fields.FieldFloat3(value=value)
            )

    @property
    def snap_parent(self) -> str | None:
        """Target ID of the SnapParent reference (targets Slot)."""
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @snap_parent.setter
    def snap_parent(self, target: str | Slot | None) -> None:
        """Set the SnapParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SnapParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

