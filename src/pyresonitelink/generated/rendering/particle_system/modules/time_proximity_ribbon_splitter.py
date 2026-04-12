"""Generated component: TimeProximityRibbonSplitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.time_split_mode import TimeSplitMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TimeProximityRibbonSplitter(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The TimeProximityRibbonSplitter component splits ribbons based on how long the ribbons have been living for.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TimeProximityRibbonSplitter"

    def __init__(self, interval: primitives.Float | None = None, mode: TimeSplitMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interval: Initial value for Interval.
            mode: Initial value for Mode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interval is not None:
            self.interval = interval
        if mode is not None:
            self.mode = mode

    @property
    def interval(self) -> primitives.Float | None:
        """The time interval to split acords"""
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
    def mode(self) -> TimeSplitMode | None:
        """How to split the ribbons based on the lifetime of Ribbon segments."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TimeSplitMode(member.value)
        return None

    @mode.setter
    def mode(self, value: TimeSplitMode | str) -> None:
        """Set Mode. How to split the ribbons based on the lifetime of Ribbon segments."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

