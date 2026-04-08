"""Generated component: TimeProximityRibbonSplitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeProximityRibbonSplitter(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.TimeProximityRibbonSplitter.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TimeProximityRibbonSplitter"

    def __init__(self, interval: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interval: Initial value for Interval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interval is not None:
            self.interval = interval

    @property
    def interval(self) -> primitives.Float | None:
        """The Interval field value."""
        member = self.get_member("Interval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interval.setter
    def interval(self, value: primitives.Float) -> None:
        """Set the Interval field value."""
        member = self.get_member("Interval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Interval", fields.FieldFloat(value=value)
            )

    @property
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

