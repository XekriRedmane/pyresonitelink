"""Generated component: VideoExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.video_texture import VideoTexture
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The VideoExportable component is used to export a Video Texture as a video file for your device.

To export using this component, look at the file browser export section.

    Category: Assets/Export

    Using this will allow you to export videos. However, only some types of
    videos can be exported. Videos that were imported from a computer can be
    exported (``.mp3`` and ``.mp4`` file types). Videos that seem to fail
    the exporting process are Youtube videos or streaming videos, as they
    not only fail to export a video file, they instead export a text file
    (which seems to be html).
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoExportable"

    def __init__(self, video: str | IAssetProvider[VideoTexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            video: Initial value for Video.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if video is not None:
            self.video = video

    @property
    def video(self) -> str | None:
        """The video asset to be exported."""
        member = self.get_member("Video")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @video.setter
    def video(self, target: str | IAssetProvider[VideoTexture] | None) -> None:
        """Set the Video reference by target ID or IAssetProvider[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Video")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Video",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.VideoTexture>'),
            )

