"""Generated component: SimplexNoiseClip."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexNoiseClip(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The SimplexNoiseClip component samples from simplex noise in order to get a pseudo-random frequency chart. Like a constantly random smooth changing whistle pitch.

    Category: Assets/Procedural Audio Clips

    Attach to a slot and provide a ``Frequency`` and ``Amplitude``, then
    insert into a AudioClipPlayer to hear it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimplexNoiseClip"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, frequency: primitives.Float | None = None, amplitude: primitives.Float | None = None, duration: primitives.Float | None = None, offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            frequency: Initial value for Frequency.
            amplitude: Initial value for Amplitude.
            duration: Initial value for Duration.
            offset: Initial value for Offset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if frequency is not None:
            self.frequency = frequency
        if amplitude is not None:
            self.amplitude = amplitude
        if duration is not None:
            self.duration = duration
        if offset is not None:
            self.offset = offset

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def frequency(self) -> primitives.Float | None:
        """The pitch of the clip."""
        member = self.get_member("Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frequency.setter
    def frequency(self, value: primitives.Float) -> None:
        """Set the Frequency field value."""
        member = self.get_member("Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frequency", fields.FieldFloat(value=value)
            )

    @property
    def amplitude(self) -> primitives.Float | None:
        """The loudness of the clip."""
        member = self.get_member("Amplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @amplitude.setter
    def amplitude(self, value: primitives.Float) -> None:
        """Set the Amplitude field value."""
        member = self.get_member("Amplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Amplitude", fields.FieldFloat(value=value)
            )

    @property
    def duration(self) -> primitives.Float | None:
        """How long the clip is and its duration of how much of simplex noise it samples."""
        member = self.get_member("Duration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @duration.setter
    def duration(self, value: primitives.Float) -> None:
        """Set the Duration field value."""
        member = self.get_member("Duration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Duration", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float | None:
        """Where in the simplex noise algorithm this clip starts sampling from."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    async def bake_clip(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Turns the audio into a StaticAudioClip.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeClip", {}, debug,
        )

