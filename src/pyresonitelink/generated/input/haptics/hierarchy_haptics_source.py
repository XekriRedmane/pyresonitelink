"""Generated component: HierarchyHapticsSource."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HierarchyHapticsSource(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HierarchyHapticsSource.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HierarchyHapticsSource"

    def __init__(self, target_hierarchy: str | Slot | None = None, interval: np.float32 | None = None, relative_intensity: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_hierarchy: Initial value for TargetHierarchy.
            interval: Initial value for Interval.
            relative_intensity: Initial value for RelativeIntensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_hierarchy is not None:
            self.target_hierarchy = target_hierarchy
        if interval is not None:
            self.interval = interval
        if relative_intensity is not None:
            self.relative_intensity = relative_intensity

    @property
    def target_hierarchy(self) -> str | None:
        """Target ID of the TargetHierarchy reference (targets Slot)."""
        member = self.get_member("TargetHierarchy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_hierarchy.setter
    def target_hierarchy(self, target: str | Slot | None) -> None:
        """Set the TargetHierarchy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetHierarchy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetHierarchy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def interval(self) -> np.float32 | None:
        """The Interval field value."""
        member = self.get_member("Interval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interval.setter
    def interval(self, value: np.float32) -> None:
        """Set the Interval field value."""
        member = self.get_member("Interval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Interval", fields.FieldFloat(value=value)
            )

    @property
    def relative_intensity(self) -> np.float32 | None:
        """The RelativeIntensity field value."""
        member = self.get_member("RelativeIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @relative_intensity.setter
    def relative_intensity(self, value: np.float32) -> None:
        """Set the RelativeIntensity field value."""
        member = self.get_member("RelativeIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RelativeIntensity", fields.FieldFloat(value=value)
            )

