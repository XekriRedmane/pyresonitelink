"""Generated component: AvatarHapticSourceManager."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarHapticSourceManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AvatarHapticSourceManager component allows you to override the injected haptic points that Resonite puts on fullbody avatars and to specify custom Haptic Volumes on your body.

Overriding your injected haptic points can be useful in situations where your avatar's proportions exaggerate the automatic haptic points that other users feel is too large or too small.

Requires the avatar to be equipped again to turn off the injected haptics.

Despite the component asking for the haptic volume active state, it is suggested to instead use the active state of the haptic collider, this allows the Avatar Haptic Source Manager to disable the colliders on the active user and allow culling behavior. The reason for this is that disabling haptic volumes does not disable the haptics itself.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarHapticSourceManager"

    @property
    def haptic_volume_active_states(self) -> members.SyncList | None:
        """Drives the boolean field put in the list to be disabled when noclipping usually"""
        member = self.get_member("HapticVolumeActiveStates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @haptic_volume_active_states.setter
    def haptic_volume_active_states(self, value: members.SyncList) -> None:
        """Set HapticVolumeActiveStates. Drives the boolean field put in the list to be disabled when noclipping usually"""
        self.set_member("HapticVolumeActiveStates", value)

