"""Generated component: RandomAudioClipPlayer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomAudioClipPlayer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RandomAudioClipPlayer component is able to play a random audio file all the way through from a list of ``Clips`` and parent the resulting one shots under a slot.

    Category: Media

    Attach to a slot and give the component some ``Clips`` to play. This
    component can be trigged via it's sync delegates or by button events
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RandomAudioClipPlayer"

    def __init__(self, parent_under: str | Slot | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, ignore_audio_effects: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_under is not None:
            self.parent_under = parent_under
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects

    @property
    def parent_under(self) -> str | None:
        """The slot to parent the one shot objects under."""
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_under.setter
    def parent_under(self, target: str | Slot | None) -> None:
        """Set the ParentUnder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """the distance in meters in the audio's set transform space where the audio's perceived volume stops increasing and stays constant all the way to the center."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """the maximum distance in meters in the audio's set transform space in meters before it cannot be heard."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def rolloff_mode(self) -> members.FieldEnum | None:
        """An optional AudioRolloffMode"""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: members.FieldEnum) -> None:
        """Set RolloffMode. An optional AudioRolloffMode"""
        self.set_member("RolloffMode", value)

    @property
    def ignore_audio_effects(self) -> primitives.Bool | None:
        """The IgnoreAudioEffects field value."""
        member = self.get_member("IgnoreAudioEffects")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_audio_effects.setter
    def ignore_audio_effects(self, value: primitives.Bool) -> None:
        """Set the IgnoreAudioEffects field value."""
        member = self.get_member("IgnoreAudioEffects")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreAudioEffects", fields.FieldBool(value=value)
            )

    @property
    def clips(self) -> members.SyncList | None:
        """The list of ClipData to choose from, randomly with weights."""
        member = self.get_member("Clips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @clips.setter
    def clips(self, value: members.SyncList) -> None:
        """Set Clips. The list of ClipData to choose from, randomly with weights."""
        self.set_member("Clips", value)

    async def play(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Plays a random audio clip at it's current position

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Play", {}, debug,
        )

    async def play_at_point(self, resolink: protocols.ResoniteLinkClient, point: primitives.Float3, debug: bool = False) -> dict:
        """Plays a random audio clip at the provided position.

        Args:
            resolink: Connected ResoniteLink client.
            point: The point parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PlayAtPoint", {"point": point}, debug,
        )

