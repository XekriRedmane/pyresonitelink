"""Generated component: IsPlayingDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IsPlayingDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The IsPlayingDriver component checks if a particular SyncPlayback is currently playing, and drives a set of Bool to reflect this status.

    Category: Media/Utility

    Attach to a slot and provide a value for ``Playback`` then any boolean
    in the list of ``Targets`` will drive to whether or not ``Playback`` is
    currently playing.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.IsPlayingDriver"

    def __init__(self, playback: str | SyncPlayback | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for Playback.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback

    @property
    def playback(self) -> str | None:
        """The playback to check if it is playing"""
        member = self.get_member("Playback")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback.setter
    def playback(self, target: str | SyncPlayback | None) -> None:
        """Set the Playback reference by target ID or SyncPlayback instance."""
        target_id: str | None = target.id if isinstance(target, SyncPlayback) else target  # type: ignore[assignment]
        member = self.get_member("Playback")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Playback",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncPlayback'),
            )

    @property
    def targets(self) -> members.SyncList | None:
        """The set of booleans to drive to whether or not ``Playback`` is playing or not."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The set of booleans to drive to whether or not ``Playback`` is playing or not."""
        self.set_member("Targets", value)

