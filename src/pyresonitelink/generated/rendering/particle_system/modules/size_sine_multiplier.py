"""Generated component: SizeSineMultiplier."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SizeSineMultiplier(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SizeSineMultiplier component makes particles multiply their size on start with a value sampled from a Sine Wave based on the time they were emitted in a particle system. 

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SizeSineMultiplier"

    def __init__(self, speed: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, min_multiplier: primitives.Float3 | None = None, max_multiplier: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            speed: Initial value for Speed.
            offset: Initial value for Offset.
            min_multiplier: Initial value for MinMultiplier.
            max_multiplier: Initial value for MaxMultiplier.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if speed is not None:
            self.speed = speed
        if offset is not None:
            self.offset = offset
        if min_multiplier is not None:
            self.min_multiplier = min_multiplier
        if max_multiplier is not None:
            self.max_multiplier = max_multiplier

    @property
    def speed(self) -> primitives.Float3 | None:
        """The speed that the Sine Wave changes."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: primitives.Float3) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat3(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The initial offset of the Sine Wave function."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def min_multiplier(self) -> primitives.Float3 | None:
        """The minimum value outputted by the sinewave function."""
        member = self.get_member("MinMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_multiplier.setter
    def min_multiplier(self, value: primitives.Float3) -> None:
        """Set the MinMultiplier field value."""
        member = self.get_member("MinMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinMultiplier", fields.FieldFloat3(value=value)
            )

    @property
    def max_multiplier(self) -> primitives.Float3 | None:
        """The maximum value outputted by the sinewave function."""
        member = self.get_member("MaxMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_multiplier.setter
    def max_multiplier(self, value: primitives.Float3) -> None:
        """Set the MaxMultiplier field value."""
        member = self.get_member("MaxMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxMultiplier", fields.FieldFloat3(value=value)
            )

