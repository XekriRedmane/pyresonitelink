"""Generated component: ChannelVolumeMeter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChannelVolumeMeter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ChannelVolumeMeter.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChannelVolumeMeter"

    def __init__(self, smoothing: primitives.Float | None = None, power: primitives.Float | None = None, source: str | IWorldAudioDataSource | None = None, current_channels: primitives.Int | None = None, do_not_remove_excess_fields: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            smoothing: Initial value for Smoothing.
            power: Initial value for Power.
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
        if source is not None:
            self.source = source
        if current_channels is not None:
            self.current_channels = current_channels
        if do_not_remove_excess_fields is not None:
            self.do_not_remove_excess_fields = do_not_remove_excess_fields

    @property
    def smoothing(self) -> primitives.Float | None:
        """The Smoothing field value."""
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
        """The Power field value."""
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
    def current_channels(self) -> primitives.Int | None:
        """The CurrentChannels field value."""
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
        """The ChannelVolumes member."""
        member = self.get_member("ChannelVolumes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @channel_volumes.setter
    def channel_volumes(self, value: members.SyncList) -> None:
        """Set the ChannelVolumes member."""
        self.set_member("ChannelVolumes", value)

    @property
    def do_not_remove_excess_fields(self) -> primitives.Bool | None:
        """The DoNotRemoveExcessFields field value."""
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

