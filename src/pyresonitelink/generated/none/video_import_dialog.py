"""Generated component: VideoImportDialog."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.video_type import VideoType
from pyresonitelink.generated._enums.stereo_layout import StereoLayout
from pyresonitelink.generated._enums.depth_preset import DepthPreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoImportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The VideoImportDialog component is better explained in the Importing page.

    See Importing.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoImportDialog"

    def __init__(self, content_root: str | Slot | None = None, video_type: VideoType | str | None = None, stereo_layout: StereoLayout | str | None = None, depth_preset: DepthPreset | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            video_type: Initial value for _videoType.
            stereo_layout: Initial value for _stereoLayout.
            depth_preset: Initial value for _depthPreset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root
        if video_type is not None:
            self.video_type = video_type
        if stereo_layout is not None:
            self.stereo_layout = stereo_layout
        if depth_preset is not None:
            self.depth_preset = depth_preset

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def video_type(self) -> VideoType | None:
        """The type of video being imported."""
        member = self.get_member("_videoType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VideoType(member.value)
        return None

    @video_type.setter
    def video_type(self, value: VideoType | str) -> None:
        """Set _videoType. The type of video being imported."""
        member = self.get_member("_videoType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_videoType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def stereo_layout(self) -> StereoLayout | None:
        """The kind of video stereo layout the video being imported has."""
        member = self.get_member("_stereoLayout")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StereoLayout(member.value)
        return None

    @stereo_layout.setter
    def stereo_layout(self, value: StereoLayout | str) -> None:
        """Set _stereoLayout. The kind of video stereo layout the video being imported has."""
        member = self.get_member("_stereoLayout")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_stereoLayout",
                members.FieldEnum(value=str(value)),
            )

    @property
    def depth_preset(self) -> DepthPreset | None:
        """The kind of depth the video being imported has."""
        member = self.get_member("_depthPreset")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DepthPreset(member.value)
        return None

    @depth_preset.setter
    def depth_preset(self, value: DepthPreset | str) -> None:
        """Set _depthPreset. The kind of depth the video being imported has."""
        member = self.get_member("_depthPreset")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_depthPreset",
                members.FieldEnum(value=str(value)),
            )

