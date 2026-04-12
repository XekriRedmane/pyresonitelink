"""Generated component: Rotation3DEulerRangeInitializer."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Rotation3DEulerRangeInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Rotation3DEulerRangeInitializer component makes particles have a random rotation between a pair of Euler angles.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.Rotation3DEulerRangeInitializer"

    def __init__(self, min_value: primitives.Float3 | None = None, max_value: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def min_value(self) -> primitives.Float3 | None:
        """The minimum euler angle rotation a particle can have."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: primitives.Float3) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat3(value=value)
            )

    @property
    def max_value(self) -> primitives.Float3 | None:
        """The maximum euler angle rotation a particle can have."""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: primitives.Float3) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat3(value=value)
            )

