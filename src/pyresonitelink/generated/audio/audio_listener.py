"""Generated component: AudioListener."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioListener(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioListener.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioListener"

    def __init__(self, active_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            active_user: Initial value for ActiveUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if active_user is not None:
            self.active_user = active_user

    @property
    def active_user(self) -> str | None:
        """Target ID of the ActiveUser reference (targets User)."""
        member = self.get_member("ActiveUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the ActiveUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("ActiveUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def target_output(self) -> members.FieldEnum | None:
        """The TargetOutput member."""
        member = self.get_member("TargetOutput")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @target_output.setter
    def target_output(self, value: members.FieldEnum) -> None:
        """Set the TargetOutput member."""
        self.set_member("TargetOutput", value)

    @property
    def effects(self) -> members.SyncList | None:
        """The Effects member."""
        member = self.get_member("Effects")
        if isinstance(member, members.SyncList):
            return member
        return None

    @effects.setter
    def effects(self, value: members.SyncList) -> None:
        """Set the Effects member."""
        self.set_member("Effects", value)

