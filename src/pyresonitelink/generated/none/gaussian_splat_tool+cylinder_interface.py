"""Generated component: GaussianSplatTool+CylinderInterface."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatTool+CylinderInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatTool+CylinderInterface.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatTool+CylinderInterface"

    def __init__(self, radius: str | IField[np.float32] | None = None, height: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            height: Initial value for Height.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if height is not None:
            self.height = height

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

    @property
    def height(self) -> str | None:
        """Target ID of the Height reference (targets IField[np.float32])."""
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height.setter
    def height(self, target: str | IField[np.float32] | None) -> None:
        """Set the Height reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Height",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

