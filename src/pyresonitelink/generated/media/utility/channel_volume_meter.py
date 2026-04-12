"""Generated component: ChannelVolumeMeter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.volume_meter_method import VolumeMeterMethod
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChannelVolumeMeter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Channel Volume meter is a component that is used to read the volume of an audio source with multiple channels. The amount of channels can vary from 1, 2, and even to beyond 4. Usually this component is used to split the Left and Right audio volumes of an ``.OGG`` clip.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChannelVolumeMeter"

    def __init__(self, smoothing: primitives.Float | None = None, power: primitives.Float | None = None, method: VolumeMeterMethod | str | None = None, source: str | IWorldAudioDataSource | None = None, current_channels: primitives.Int | None = None, do_not_remove_excess_fields: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            smoothing: Initial value for Smoothing.
            power: Initial value for Power.
            method: Initial value for Method.
            source: Initial value for Source.
            current_channels: Initial value for CurrentChannels.
            do_not_remove_excess_fields: Initial value for DoNotRemoveExcessFields.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if smoothing is not None:
            self.smoothing = smoothing
        if power is not None:
            self.power = power
        if method is not None:
            self.method = method
        if source is not None:
            self.source = source
        if current_channels is not None:
            self.current_channels = current_channels
        if do_not_remove_excess_fields is not None:
            self.do_not_remove_excess_fields = do_not_remove_excess_fields

    @property
    def smoothing(self) -> primitives.Float | None:
        """How much to smooth the value changes of the outputs in ``ChannelVolumes``"""
        member = self.get_member("Smoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothing.setter
    def smoothing(self, value: primitives.Float) -> None:
        """Set the Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothing", fields.FieldFloat(value=value)
            )

    @property
    def power(self) -> primitives.Float | None:
        """Raise ``ChannelVolumes`` to this exponent. 1 will leave ``ChannelVolumes`` unchanged."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: primitives.Float) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

    @property
    def method(self) -> VolumeMeterMethod | None:
        """Whether the outputted value should be the current volume, or the change in volume over time (delta)"""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VolumeMeterMethod(member.value)
        return None

    @method.setter
    def method(self, value: VolumeMeterMethod | str) -> None:
        """Set Method. Whether the outputted value should be the current volume, or the change in volume over time (delta)"""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Method",
                members.FieldEnum(value=str(value)),
            )

    @property
    def source(self) -> str | None:
        """The source to read the audio volumes for each channel from."""
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
    def current_channels(self) -> primitives.Int | None:
        """How many channels ``Source`` has."""
        member = self.get_member("CurrentChannels")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_channels.setter
    def current_channels(self, value: primitives.Int) -> None:
        """Set the CurrentChannels field value."""
        member = self.get_member("CurrentChannels")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentChannels", fields.FieldInt(value=value)
            )

    @property
    def channel_volumes(self) -> members.SyncList | None:
        """The output volumes of each channel ``Source`` has."""
        member = self.get_member("ChannelVolumes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @channel_volumes.setter
    def channel_volumes(self, value: members.SyncList) -> None:
        """Set ChannelVolumes. The output volumes of each channel ``Source`` has."""
        self.set_member("ChannelVolumes", value)

    @property
    def do_not_remove_excess_fields(self) -> primitives.Bool | None:
        """Don't remove excess fields whenever a new audio clip is inserted and the fields are outside the amount of channels the audio clip has."""
        member = self.get_member("DoNotRemoveExcessFields")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @do_not_remove_excess_fields.setter
    def do_not_remove_excess_fields(self, value: primitives.Bool) -> None:
        """Set the DoNotRemoveExcessFields field value."""
        member = self.get_member("DoNotRemoveExcessFields")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoNotRemoveExcessFields", fields.FieldBool(value=value)
            )

