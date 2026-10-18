"""Generated component: VideoStreamSpawner."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoStreamSpawner(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Utility.Tools.VideoStreamSpawner.

    Category: Utility/Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Utility.Tools.VideoStreamSpawner"

    def __init__(self, stream_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stream_active: Initial value for StreamActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stream_active is not None:
            self.stream_active = stream_active

    @property
    def stream_active(self) -> primitives.Bool | None:
        """The StreamActive field value."""
        member = self.get_member("StreamActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stream_active.setter
    def stream_active(self, value: primitives.Bool) -> None:
        """Set the StreamActive field value."""
        member = self.get_member("StreamActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StreamActive", fields.FieldBool(value=value)
            )

