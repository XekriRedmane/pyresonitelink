"""Generated component: PositionSimulatorModule."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PositionSimulatorModule(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The PositionSimulatorModule component is the most essential particle simulator module. Without it, particles will not move, and won't have velocity.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.PositionSimulatorModule"

    def __init__(self, collisions: primitives.Bool | None = None, collision_lifetime_loss_ratio: primitives.Float | None = None, collision_bounce_ratio: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collisions: Initial value for Collisions.
            collision_lifetime_loss_ratio: Initial value for CollisionLifetimeLossRatio.
            collision_bounce_ratio: Initial value for CollisionBounceRatio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collisions is not None:
            self.collisions = collisions
        if collision_lifetime_loss_ratio is not None:
            self.collision_lifetime_loss_ratio = collision_lifetime_loss_ratio
        if collision_bounce_ratio is not None:
            self.collision_bounce_ratio = collision_bounce_ratio

    @property
    def collisions(self) -> primitives.Bool | None:
        """Whether particles should have collisions."""
        member = self.get_member("Collisions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collisions.setter
    def collisions(self, value: primitives.Bool) -> None:
        """Set the Collisions field value."""
        member = self.get_member("Collisions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Collisions", fields.FieldBool(value=value)
            )

    @property
    def collision_lifetime_loss_ratio(self) -> primitives.Float | None:
        """How much lifetime percentage from 01 should particles loose when hitting a surface?"""
        member = self.get_member("CollisionLifetimeLossRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collision_lifetime_loss_ratio.setter
    def collision_lifetime_loss_ratio(self, value: primitives.Float) -> None:
        """Set the CollisionLifetimeLossRatio field value."""
        member = self.get_member("CollisionLifetimeLossRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollisionLifetimeLossRatio", fields.FieldFloat(value=value)
            )

    @property
    def collision_bounce_ratio(self) -> primitives.Float | None:
        """How much velocity should particles retain as a percentage from 01 when bouncing off of a surface?"""
        member = self.get_member("CollisionBounceRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collision_bounce_ratio.setter
    def collision_bounce_ratio(self, value: primitives.Float) -> None:
        """Set the CollisionBounceRatio field value."""
        member = self.get_member("CollisionBounceRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollisionBounceRatio", fields.FieldFloat(value=value)
            )

    @property
    def collision_sub_emission(self) -> members.SyncObject | None:
        """The CollisionSubEmission member."""
        member = self.get_member("CollisionSubEmission")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @collision_sub_emission.setter
    def collision_sub_emission(self, value: members.SyncObject) -> None:
        """Set the CollisionSubEmission member."""
        self.set_member("CollisionSubEmission", value)

