"""Generated component: FootstepSoundPlayer."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifootstep_event_receiver import IFootstepEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepSoundPlayer(GeneratedComponent, IFootstepEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FootstepSoundPlayer.

    Category: Locomotion/Footsteps
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepSoundPlayer"

    @property
    def sound_materials(self) -> members.SyncList | None:
        """The SoundMaterials member."""
        member = self.get_member("SoundMaterials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sound_materials.setter
    def sound_materials(self, value: members.SyncList) -> None:
        """Set the SoundMaterials member."""
        self.set_member("SoundMaterials", value)

