"""Generated component: VolumeMeter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VolumeMeter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VolumeMeter.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumeMeter"

    def __init__(self, smoothing: np.float32 | None = None, power: np.float32 | None = None, source: str | IWorldAudioDataSource | None = None, volume: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            smoothing: Initial value for Smoothing.
            power: Initial value for Power.
            source: Initial value for Source.
            volume: Initial value for Volume.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if smoothing is not None:
            self.smoothing = smoothing
        if power is not None:
            self.power = power
        if source is not None:
            self.source = source
        if volume is not None:
            self.volume = volume

    @property
    def smoothing(self) -> np.float32 | None:
        """The Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothing.setter
    def smoothing(self, value: np.float32) -> None:
        """Set the Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothing", fields.FieldFloat(value=value)
            )

    @property
    def power(self) -> np.float32 | None:
        """The Power field value."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: np.float32) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

    @property
    def method(self) -> members.FieldEnum | None:
        """The Method member."""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @method.setter
    def method(self, value: members.FieldEnum) -> None:
        """Set the Method member."""
        self.set_member("Method", value)

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IWorldAudioDataSource)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IWorldAudioDataSource | None) -> None:
        """Set the Source reference by target ID or IWorldAudioDataSource instance."""
        target_id: str | None = target.id if isinstance(target, IWorldAudioDataSource) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldAudioDataSource'),
            )

    @property
    def volume(self) -> np.float32 | None:
        """The Volume field value."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: np.float32) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

