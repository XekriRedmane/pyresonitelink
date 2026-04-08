"""Generated component: VideoImportDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoImportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VideoImportDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoImportDialog"

    def __init__(self, content_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root

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
    def video_type(self) -> members.FieldEnum | None:
        """The _videoType member."""
        member = self.get_member("_videoType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @video_type.setter
    def video_type(self, value: members.FieldEnum) -> None:
        """Set the _videoType member."""
        self.set_member("_videoType", value)

    @property
    def stereo_layout(self) -> members.FieldEnum | None:
        """The _stereoLayout member."""
        member = self.get_member("_stereoLayout")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @stereo_layout.setter
    def stereo_layout(self, value: members.FieldEnum) -> None:
        """Set the _stereoLayout member."""
        self.set_member("_stereoLayout", value)

    @property
    def depth_preset(self) -> members.FieldEnum | None:
        """The _depthPreset member."""
        member = self.get_member("_depthPreset")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @depth_preset.setter
    def depth_preset(self, value: members.FieldEnum) -> None:
        """Set the _depthPreset member."""
        self.set_member("_depthPreset", value)

