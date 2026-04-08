"""Generated component: ViolentAprilFoolsExplosion."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ViolentAprilFoolsExplosion(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ViolentAprilFoolsExplosion.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ViolentAprilFoolsExplosion"

    def __init__(self, bloat_magnitude: np.float32 | None = None, bloating_clip: str | IAssetProvider[AudioClip] | None = None, explosion_clip: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bloat_magnitude: Initial value for BloatMagnitude.
            bloating_clip: Initial value for _bloatingClip.
            explosion_clip: Initial value for _explosionClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bloat_magnitude is not None:
            self.bloat_magnitude = bloat_magnitude
        if bloating_clip is not None:
            self.bloating_clip = bloating_clip
        if explosion_clip is not None:
            self.explosion_clip = explosion_clip

    @property
    def bloat_magnitude(self) -> np.float32 | None:
        """The BloatMagnitude field value."""
        member = self.get_member("BloatMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bloat_magnitude.setter
    def bloat_magnitude(self, value: np.float32) -> None:
        """Set the BloatMagnitude field value."""
        member = self.get_member("BloatMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BloatMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def bloating_clip(self) -> str | None:
        """Target ID of the _bloatingClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_bloatingClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bloating_clip.setter
    def bloating_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _bloatingClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_bloatingClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bloatingClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def explosion_clip(self) -> str | None:
        """Target ID of the _explosionClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_explosionClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @explosion_clip.setter
    def explosion_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _explosionClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_explosionClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_explosionClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

