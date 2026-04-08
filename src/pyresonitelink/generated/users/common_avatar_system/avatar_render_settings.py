"""Generated component: AvatarRenderSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irender_settings_source import IRenderSettingsSource
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarRenderSettings(GeneratedComponent, IRenderSettingsSource, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarRenderSettings.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarRenderSettings"

    def __init__(self, near_clip: np.float32 | None = None, far_clip: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if near_clip is not None:
            self.near_clip = near_clip
        if far_clip is not None:
            self.far_clip = far_clip

    @property
    def near_clip(self) -> np.float32 | None:
        """The NearClip field value."""
        member = self.get_member("NearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clip.setter
    def near_clip(self, value: np.float32) -> None:
        """Set the NearClip field value."""
        member = self.get_member("NearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClip", fields.FieldNullableFloat(value=value)
            )

    @property
    def far_clip(self) -> np.float32 | None:
        """The FarClip field value."""
        member = self.get_member("FarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clip.setter
    def far_clip(self, value: np.float32) -> None:
        """Set the FarClip field value."""
        member = self.get_member("FarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClip", fields.FieldNullableFloat(value=value)
            )

