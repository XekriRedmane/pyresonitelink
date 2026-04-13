"""Generated component: FingerPosePreset."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.preset import Preset
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPosePreset(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """The FingerPosePreset component is itself a IFingerPoseSourceComponent type component that it's finger pose data is determined by the preset selected in ``PresetPose``.

For more information on finger pose sources, please see Finger Posing System.

    Category: Users/Common Avatar System/Fingers

    Select a Preset for ``PresetPose``. This component can now be used as a
    IFingerPoseSourceComponent in other components that mix or use such
    data.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPosePreset"

    def __init__(self, preset_pose: Preset | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            preset_pose: Initial value for PresetPose.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if preset_pose is not None:
            self.preset_pose = preset_pose

    @property
    def preset_pose(self) -> Preset | None:
        """The Finger pose data this component's finger pose data should be."""
        member = self.get_member("PresetPose")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Preset(member.value)
        return None

    @preset_pose.setter
    def preset_pose(self, value: Preset | str) -> None:
        """Set PresetPose. The Finger pose data this component's finger pose data should be."""
        member = self.get_member("PresetPose")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PresetPose",
                members.FieldEnum(value=str(value)),
            )

