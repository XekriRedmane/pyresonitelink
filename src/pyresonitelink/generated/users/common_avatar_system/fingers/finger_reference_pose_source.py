"""Generated component: FingerReferencePoseSource."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerReferencePoseSource(GeneratedComponent, IFingerPoseSourceComponent, ICustomInspector, IWorldEventReceiver):
    """The FingerReferencePoseSource component is used to read and generate Pose data from the user or its already created bone hiearchy Template. The Slots used in the ``Bones`` list need to not be null. Every time the Pose data is read from this component as a Finger Pose Source, the current positions and rotations of the slots in ``Bones`` are used. This component in itself is a IFingerPoseSourceComponent.

For more information on finger pose sources, please see Finger Posing System.

    Category: Users/Common Avatar System/Fingers

    Attach to a slot and use either the generate visuals button or assign
    from biped rig to make a reference armature. Then, it can either be set
    from the current hand pose of the user (useful for Index Controller
    users) or can be adjusted manually. The component can then be used as a
    IFingerPoseSourceComponent.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerReferencePoseSource"

    @property
    def bones(self) -> members.SyncDictionary | None:
        """A list of bones mapped to Fingers to use as the Finger pose source data for this component. The Fingers need to be in the default hand structure."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncDictionary) -> None:
        """Set Bones. A list of bones mapped to Fingers to use as the Finger pose source data for this component. The Fingers need to be in the default hand structure."""
        self.set_member("Bones", value)

