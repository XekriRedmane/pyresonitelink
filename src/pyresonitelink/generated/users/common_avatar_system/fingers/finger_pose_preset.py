"""Generated component: FingerPosePreset."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPosePreset(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FingerPosePreset.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPosePreset"

    @property
    def preset_pose(self) -> members.FieldEnum | None:
        """The PresetPose member."""
        member = self.get_member("PresetPose")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preset_pose.setter
    def preset_pose(self, value: members.FieldEnum) -> None:
        """Set the PresetPose member."""
        self.set_member("PresetPose", value)

