"""Generated component: GaussianSplatTool+SphereInterface."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatTool+SphereInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatTool+SphereInterface.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatTool+SphereInterface"

    def __init__(self, radius: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius

    @property
    def radius(self) -> str | None:
        """Target ID of the Radius reference (targets IField[np.float32])."""
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @radius.setter
    def radius(self, target: str | IField[np.float32] | None) -> None:
        """Set the Radius reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Radius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

