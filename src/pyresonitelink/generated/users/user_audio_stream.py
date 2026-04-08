"""Generated component: UserAudioStream."""

from typing import Any

S = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.audio_stream import AudioStream
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserAudioStream(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserAudioStream<>.

    Category: Users

    Parameterize with a value type::

        UserAudioStream[np.float32]
        UserAudioStream[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserAudioStream<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UserAudioStream<>"

    def __init__(self, stream: str | AudioStream[S] | None = None, use_filtered_data: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stream: Initial value for Stream.
            use_filtered_data: Initial value for UseFilteredData.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stream is not None:
            self.stream = stream
        if use_filtered_data is not None:
            self.use_filtered_data = use_filtered_data

    @property
    def stream(self) -> str | None:
        """Target ID of the Stream reference (targets AudioStream[S])."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | AudioStream[S] | None) -> None:
        """Set the Stream reference by target ID or AudioStream[S] instance."""
        target_id: str | None = target.id if isinstance(target, AudioStream) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioStream<S>'),
            )

    @property
    def use_filtered_data(self) -> bool | None:
        """The UseFilteredData field value."""
        member = self.get_member("UseFilteredData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_filtered_data.setter
    def use_filtered_data(self, value: bool) -> None:
        """Set the UseFilteredData field value."""
        member = self.get_member("UseFilteredData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFilteredData", fields.FieldBool(value=value)
            )

