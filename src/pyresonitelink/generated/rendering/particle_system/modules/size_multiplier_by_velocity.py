"""Generated component: SizeMultiplierByVelocity."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SizeMultiplierByVelocity(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Size Multiplier By Velocity component is used in Photon Dust systems to make particles change size on any given axies based on velocity.

    Category: Rendering/Particle System/Modules

    Used in particle systems to change particle size by velocity.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SizeMultiplierByVelocity"

    def __init__(self, velocity_multiplier: primitives.Float3 | None = None, velocity_mask: primitives.Bool3 | None = None, multiplier_clamp_min: primitives.Float3 | None = None, multiplier_clamp_max: primitives.Float3 | None = None, result_clamp_min: primitives.Float3 | None = None, result_clamp_max: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            velocity_multiplier: Initial value for VelocityMultiplier.
            velocity_mask: Initial value for VelocityMask.
            multiplier_clamp_min: Initial value for MultiplierClampMin.
            multiplier_clamp_max: Initial value for MultiplierClampMax.
            result_clamp_min: Initial value for ResultClampMin.
            result_clamp_max: Initial value for ResultClampMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if velocity_multiplier is not None:
            self.velocity_multiplier = velocity_multiplier
        if velocity_mask is not None:
            self.velocity_mask = velocity_mask
        if multiplier_clamp_min is not None:
            self.multiplier_clamp_min = multiplier_clamp_min
        if multiplier_clamp_max is not None:
            self.multiplier_clamp_max = multiplier_clamp_max
        if result_clamp_min is not None:
            self.result_clamp_min = result_clamp_min
        if result_clamp_max is not None:
            self.result_clamp_max = result_clamp_max

    @property
    def velocity_multiplier(self) -> primitives.Float3 | None:
        """The amount to multiply velocity of a particle by before using it as a multiplier."""
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
    def velocity_mask(self) -> primitives.Bool3 | None:
        """Which axies should be included in or excluded from this scaling effect."""
        member = self.get_member("VelocityMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_mask.setter
    def velocity_mask(self, value: primitives.Bool3) -> None:
        """Set the VelocityMask field value."""
        member = self.get_member("VelocityMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocityMask", fields.FieldBool3(value=value)
            )

    @property
    def multiplier_clamp_min(self) -> primitives.Float3 | None:
        """the minimum value to clamp the current velocity of a particle to before it is used as a scale multiplier."""
        member = self.get_member("MultiplierClampMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiplier_clamp_min.setter
    def multiplier_clamp_min(self, value: primitives.Float3) -> None:
        """Set the MultiplierClampMin field value."""
        member = self.get_member("MultiplierClampMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiplierClampMin", fields.FieldFloat3(value=value)
            )

    @property
    def multiplier_clamp_max(self) -> primitives.Float3 | None:
        """the maximum value to clamp the current velocity of a particle to before it is used as a scale multiplier."""
        member = self.get_member("MultiplierClampMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiplier_clamp_max.setter
    def multiplier_clamp_max(self, value: primitives.Float3) -> None:
        """Set the MultiplierClampMax field value."""
        member = self.get_member("MultiplierClampMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiplierClampMax", fields.FieldFloat3(value=value)
            )

    @property
    def result_clamp_min(self) -> primitives.Float3 | None:
        """the minimum scale the particle is allowed to be as a final scale."""
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
        """the maximum scale the particle is allowed to be as a final scale."""
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

