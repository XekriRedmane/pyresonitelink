"""Generated component: AudioZitaReverb+LegacyRangeMapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioZitaReverb+LegacyRangeMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioZitaReverb+LegacyRangeMapper.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioZitaReverb+LegacyRangeMapper"

    def __init__(self, min_distance: np.float32 | None = None, max_distance: np.float32 | None = None, radius: str | IField[np.float32] | None = None, blend_distance: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            radius: Initial value for Radius.
            blend_distance: Initial value for BlendDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if radius is not None:
            self.radius = radius
        if blend_distance is not None:
            self.blend_distance = blend_distance

    @property
    def min_distance(self) -> np.float32 | None:
        """The MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: np.float32) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> np.float32 | None:
        """The MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: np.float32) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

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
    def blend_distance(self) -> str | None:
        """Target ID of the BlendDistance reference (targets IField[np.float32])."""
        member = self.get_member("BlendDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @blend_distance.setter
    def blend_distance(self, target: str | IField[np.float32] | None) -> None:
        """Set the BlendDistance reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BlendDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BlendDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

