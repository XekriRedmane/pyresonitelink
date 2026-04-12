"""Generated component: SizeOffsetByVelocity."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SizeOffsetByVelocity(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SizeOffsetByVelocity component changes the size of particles in a particle system based on their velocity.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SizeOffsetByVelocity"

    def __init__(self, velocity_multiplier: primitives.Float3 | None = None, offset_clamp_min: primitives.Float3 | None = None, offset_clamp_max: primitives.Float3 | None = None, result_clamp_min: primitives.Float3 | None = None, result_clamp_max: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            velocity_multiplier: Initial value for VelocityMultiplier.
            offset_clamp_min: Initial value for OffsetClampMin.
            offset_clamp_max: Initial value for OffsetClampMax.
            result_clamp_min: Initial value for ResultClampMin.
            result_clamp_max: Initial value for ResultClampMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if velocity_multiplier is not None:
            self.velocity_multiplier = velocity_multiplier
        if offset_clamp_min is not None:
            self.offset_clamp_min = offset_clamp_min
        if offset_clamp_max is not None:
            self.offset_clamp_max = offset_clamp_max
        if result_clamp_min is not None:
            self.result_clamp_min = result_clamp_min
        if result_clamp_max is not None:
            self.result_clamp_max = result_clamp_max

    @property
    def velocity_multiplier(self) -> primitives.Float3 | None:
        """How much velocity should multiply the size of the particle."""
        member = self.get_member("VelocityMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_multiplier.setter
    def velocity_multiplier(self, value: primitives.Float3) -> None:
        """Set the VelocityMultiplier field value."""
        member = self.get_member("VelocityMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocityMultiplier", fields.FieldFloat3(value=value)
            )

    @property
    def offset_clamp_min(self) -> primitives.Float3 | None:
        """The minimum value for the clamping of the offset."""
        member = self.get_member("OffsetClampMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_clamp_min.setter
    def offset_clamp_min(self, value: primitives.Float3) -> None:
        """Set the OffsetClampMin field value."""
        member = self.get_member("OffsetClampMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetClampMin", fields.FieldFloat3(value=value)
            )

    @property
    def offset_clamp_max(self) -> primitives.Float3 | None:
        """The maximum value for the clamping of the offset."""
        member = self.get_member("OffsetClampMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_clamp_max.setter
    def offset_clamp_max(self, value: primitives.Float3) -> None:
        """Set the OffsetClampMax field value."""
        member = self.get_member("OffsetClampMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetClampMax", fields.FieldFloat3(value=value)
            )

    @property
    def result_clamp_min(self) -> primitives.Float3 | None:
        """The minimum value for the clamping of the result."""
        member = self.get_member("ResultClampMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @result_clamp_min.setter
    def result_clamp_min(self, value: primitives.Float3) -> None:
        """Set the ResultClampMin field value."""
        member = self.get_member("ResultClampMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResultClampMin", fields.FieldFloat3(value=value)
            )

    @property
    def result_clamp_max(self) -> primitives.Float3 | None:
        """The maximum value for the clamping of the result."""
        member = self.get_member("ResultClampMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @result_clamp_max.setter
    def result_clamp_max(self, value: primitives.Float3) -> None:
        """Set the ResultClampMax field value."""
        member = self.get_member("ResultClampMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResultClampMax", fields.FieldFloat3(value=value)
            )

