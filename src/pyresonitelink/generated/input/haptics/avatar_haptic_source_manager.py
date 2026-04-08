"""Generated component: AvatarHapticSourceManager."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarHapticSourceManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AvatarHapticSourceManager.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarHapticSourceManager"

    @property
    def haptic_volume_active_states(self) -> members.SyncList | None:
        """The HapticVolumeActiveStates member."""
        member = self.get_member("HapticVolumeActiveStates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @haptic_volume_active_states.setter
    def haptic_volume_active_states(self, value: members.SyncList) -> None:
        """Set the HapticVolumeActiveStates member."""
        self.set_member("HapticVolumeActiveStates", value)

