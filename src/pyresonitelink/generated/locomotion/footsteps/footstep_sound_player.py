"""Generated component: FootstepSoundPlayer."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifootstep_event_receiver import IFootstepEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepSoundPlayer(GeneratedComponent, IFootstepEventReceiver, IWorldEventReceiver):
    """The FootstepSoundPlayer component triggers a list of IFootstepSoundMaterials when a player walks on a collider on the same slot.

    Category: Locomotion/Footsteps

    Used to make an entire collider like a tile floor play sounds when a
    player walks on it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepSoundPlayer"

    @property
    def sound_materials(self) -> members.SyncList | None:
        """usually a list of FootstepSoundDefinitions."""
        member = self.get_member("SoundMaterials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sound_materials.setter
    def sound_materials(self, value: members.SyncList) -> None:
        """Set SoundMaterials. usually a list of FootstepSoundDefinitions."""
        self.set_member("SoundMaterials", value)

