"""Generated component: RectTransformLerp."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectTransformLerp(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.RectTransformLerp.

    Category: UIX/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectTransformLerp"

    def __init__(self, lerp: np.float32 | None = None, source_rect: str | RectTransform | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            lerp: Initial value for Lerp.
            source_rect: Initial value for SourceRect.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if lerp is not None:
            self.lerp = lerp
        if source_rect is not None:
            self.source_rect = source_rect

    @property
    def lerp(self) -> np.float32 | None:
        """The Lerp field value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: np.float32) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
            )

    @property
    def source_rect(self) -> str | None:
        """Target ID of the SourceRect reference (targets RectTransform)."""
        member = self.get_member("SourceRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_rect.setter
    def source_rect(self, target: str | RectTransform | None) -> None:
        """Set the SourceRect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("SourceRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

