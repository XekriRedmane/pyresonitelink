"""Generated component: FingerReferencePoseSource."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerReferencePoseSource(GeneratedComponent, IFingerPoseSourceComponent, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FingerReferencePoseSource.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerReferencePoseSource"

    @property
    def bones(self) -> members.SyncDictionary | None:
        """The Bones member."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncDictionary) -> None:
        """Set the Bones member."""
        self.set_member("Bones", value)

