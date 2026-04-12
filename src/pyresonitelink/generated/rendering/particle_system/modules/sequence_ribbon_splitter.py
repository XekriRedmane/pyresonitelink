"""Generated component: SequenceRibbonSplitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SequenceRibbonSplitter(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SequenceRibbonSplitter splits ribbons based on how long they are at random.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SequenceRibbonSplitter"

    def __init__(self, min_sequence_count: primitives.Int | None = None, max_sequence_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_sequence_count: Initial value for MinSequenceCount.
            max_sequence_count: Initial value for MaxSequenceCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_sequence_count is not None:
            self.min_sequence_count = min_sequence_count
        if max_sequence_count is not None:
            self.max_sequence_count = max_sequence_count

    @property
    def min_sequence_count(self) -> primitives.Int | None:
        """The minimum ribbon sequence length a ribbon has to be before it is split."""
        member = self.get_member("MinSequenceCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_sequence_count.setter
    def min_sequence_count(self, value: primitives.Int) -> None:
        """Set the MinSequenceCount field value."""
        member = self.get_member("MinSequenceCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSequenceCount", fields.FieldInt(value=value)
            )

    @property
    def max_sequence_count(self) -> primitives.Int | None:
        """The maximum ribbon sequence length a ribbon can be before it is split forcibly."""
        member = self.get_member("MaxSequenceCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_sequence_count.setter
    def max_sequence_count(self, value: primitives.Int) -> None:
        """Set the MaxSequenceCount field value."""
        member = self.get_member("MaxSequenceCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSequenceCount", fields.FieldInt(value=value)
            )

