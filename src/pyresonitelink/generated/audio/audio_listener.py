"""Generated component: AudioListener."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.listener_target import ListenerTarget
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioListener(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """The Audio Listener component can hear audio from the world around it and relay it back. It can also be used as a source for audio data for AudioOutput, working as a virtual microphone (This only works on listeners that aren't bound to specific user - ActiveUser must be null)

    Category: Audio

    Audio Reverb zones and other effects can be dynamically assigned to the
    list of ``Effects`` using spatial variables. The default variable for
    such is "Resonite.Audio.Filters" of type AudioDSP_Effect. Using
    SphereConstantReferenceSpatialVariables of the same type can be used to
    designate areas with reverbs using the Spatial variables system. For
    audio reverb, the AudioDSP_Effect the sphere spatial variable component
    points to needs to be a AudioFilterBlendWrapper with a AudioZitaReverb
    in it The list of effects on this component can be driven using the
    ReferenceSpatialVariableDriver and will change depending on what audio
    effects at it's location it can sample from surrounding
    SphereConstantReferenceSpatialVariables
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioListener"

    def __init__(self, active_user: str | User | None = None, target_output: ListenerTarget | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            active_user: Initial value for ActiveUser.
            target_output: Initial value for TargetOutput.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if active_user is not None:
            self.active_user = active_user
        if target_output is not None:
            self.target_output = target_output

    @property
    def active_user(self) -> str | None:
        """Position the audio source to this user."""
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
    def target_output(self) -> ListenerTarget | None:
        """The TargetOutput enum value."""
        member = self.get_member("TargetOutput")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ListenerTarget(member.value)
        return None

    @target_output.setter
    def target_output(self, value: ListenerTarget | str) -> None:
        """Set the TargetOutput enum value."""
        member = self.get_member("TargetOutput")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TargetOutput",
                members.FieldEnum(value=str(value)),
            )

    @property
    def effects(self) -> members.SyncList | None:
        """The list of affects to apply to the audio this recieves."""
        member = self.get_member("Effects")
        if isinstance(member, members.SyncList):
            return member
        return None

    @effects.setter
    def effects(self, value: members.SyncList) -> None:
        """Set Effects. The list of affects to apply to the audio this recieves."""
        self.set_member("Effects", value)

