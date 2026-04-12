"""Generated component: SessionCaptureThumbnailSource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.isession_thumbnail_source import ISessionThumbnailSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionCaptureThumbnailSource(GeneratedComponent, ISessionThumbnailSource, IWorldEventReceiver):
    """The SessionCaptureThumbnailSource component sets the slot it is on as a source for capturing the session thumbnail, or the preview image used for the currently active session.

    Category: World

    Place this component on a slot. The slot's position will then be used as
    the capture source for the session thumbnail. If multiple slots have
    this component on it, the capture will be taken via a weighted random
    pick, where slots with a lower average user distance from them will be
    more likely to be captured.

    **See also**: * WorldCaptureThumbnailSource for capturing the world preview that shows up without an active session.
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
        """An overlay image to superimpose over the normal session capture. This image must have an average alpha channel value under 25% or else it will not be applied."""
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

