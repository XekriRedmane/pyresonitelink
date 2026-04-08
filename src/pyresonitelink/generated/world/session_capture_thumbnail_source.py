"""Generated component: SessionCaptureThumbnailSource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.isession_thumbnail_source import ISessionThumbnailSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionCaptureThumbnailSource(GeneratedComponent, ISessionThumbnailSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SessionCaptureThumbnailSource.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionCaptureThumbnailSource"

    def __init__(self, overlay: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            overlay: Initial value for Overlay.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if overlay is not None:
            self.overlay = overlay

    @property
    def overlay(self) -> str | None:
        """Target ID of the Overlay reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("Overlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overlay.setter
    def overlay(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Overlay reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Overlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Overlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

