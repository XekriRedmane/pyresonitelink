"""Generated component: ProgressBar."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProgressBar(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ProgressBar.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ProgressBar"

    def __init__(self, progress: np.float32 | None = None, anchor_min_offset: primitives.Float2 | None = None, anchor_max_offset: primitives.Float2 | None = None, anchor_min: str | IField[primitives.Float2] | None = None, anchor_max: str | IField[primitives.Float2] | None = None, power: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            progress: Initial value for Progress.
            anchor_min_offset: Initial value for AnchorMinOffset.
            anchor_max_offset: Initial value for AnchorMaxOffset.
            anchor_min: Initial value for AnchorMin.
            anchor_max: Initial value for AnchorMax.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if progress is not None:
            self.progress = progress
        if anchor_min_offset is not None:
            self.anchor_min_offset = anchor_min_offset
        if anchor_max_offset is not None:
            self.anchor_max_offset = anchor_max_offset
        if anchor_min is not None:
            self.anchor_min = anchor_min
        if anchor_max is not None:
            self.anchor_max = anchor_max
        if power is not None:
            self.power = power

    @property
    def progress(self) -> np.float32 | None:
        """The Progress field value."""
        member = self.get_member("Progress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress.setter
    def progress(self, value: np.float32) -> None:
        """Set the Progress field value."""
        member = self.get_member("Progress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Progress", fields.FieldFloat(value=value)
            )

    @property
    def anchor_min_offset(self) -> primitives.Float2 | None:
        """The AnchorMinOffset field value."""
        member = self.get_member("AnchorMinOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_min_offset.setter
    def anchor_min_offset(self, value: primitives.Float2) -> None:
        """Set the AnchorMinOffset field value."""
        member = self.get_member("AnchorMinOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorMinOffset", fields.FieldFloat2(value=value)
            )

    @property
    def anchor_max_offset(self) -> primitives.Float2 | None:
        """The AnchorMaxOffset field value."""
        member = self.get_member("AnchorMaxOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_max_offset.setter
    def anchor_max_offset(self, value: primitives.Float2) -> None:
        """Set the AnchorMaxOffset field value."""
        member = self.get_member("AnchorMaxOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorMaxOffset", fields.FieldFloat2(value=value)
            )

    @property
    def anchor_min(self) -> str | None:
        """Target ID of the AnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("AnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor_min.setter
    def anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the AnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def anchor_max(self) -> str | None:
        """Target ID of the AnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("AnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor_max.setter
    def anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the AnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def power(self) -> np.float32 | None:
        """The Power field value."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: np.float32) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

