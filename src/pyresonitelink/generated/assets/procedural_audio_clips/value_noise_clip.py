"""Generated component: ValueNoiseClip."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueNoiseClip(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The ValueNoiseClip component takes completely random noise and turns it into audio data. The best way to describe the noise would be like TV static.

    Category: Assets/Procedural Audio Clips

    Attach to a slot and provide a ``Frequency`` and ``Amplitude``, then
    insert into a AudioClipPlayer to hear it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueNoiseClip"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, duration: primitives.Float | None = None, seed: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            duration: Initial value for Duration.
            seed: Initial value for Seed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if duration is not None:
            self.duration = duration
        if seed is not None:
            self.seed = seed

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
    def duration(self) -> primitives.Float | None:
        """How long the clip is."""
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
    def seed(self) -> primitives.Int | None:
        """The seed for the random audio noise."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: primitives.Int) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    async def bake_clip(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Turns the audio into a StaticAudioClip.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeClip", {}, debug,
        )

