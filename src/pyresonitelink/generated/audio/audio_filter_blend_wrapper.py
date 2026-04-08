"""Generated component: AudioFilterBlendWrapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.audio_dsp_effect import AudioDSP_Effect
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioFilterBlendWrapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioFilterBlendWrapper.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioFilterBlendWrapper"

    def __init__(self, blend_weight: np.float32 | None = None, nested_filter: str | AudioDSP_Effect | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            blend_weight: Initial value for BlendWeight.
            nested_filter: Initial value for NestedFilter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if blend_weight is not None:
            self.blend_weight = blend_weight
        if nested_filter is not None:
            self.nested_filter = nested_filter

    @property
    def blend_weight(self) -> np.float32 | None:
        """The BlendWeight field value."""
        member = self.get_member("BlendWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_weight.setter
    def blend_weight(self, value: np.float32) -> None:
        """Set the BlendWeight field value."""
        member = self.get_member("BlendWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendWeight", fields.FieldFloat(value=value)
            )

    @property
    def nested_filter(self) -> str | None:
        """Target ID of the NestedFilter reference (targets AudioDSP_Effect)."""
        member = self.get_member("NestedFilter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nested_filter.setter
    def nested_filter(self, target: str | AudioDSP_Effect | None) -> None:
        """Set the NestedFilter reference by target ID or AudioDSP_Effect instance."""
        target_id: str | None = target.id if isinstance(target, AudioDSP_Effect) else target  # type: ignore[assignment]
        member = self.get_member("NestedFilter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NestedFilter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioDSP_Effect'),
            )

