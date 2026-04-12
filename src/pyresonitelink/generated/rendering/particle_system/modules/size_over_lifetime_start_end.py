"""Generated component: SizeOverLifetimeStartEnd."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SizeOverLifetimeStartEnd(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SizeOverLifetimeStartEnd component makes particles in a particle system change size as their lifetime duration progresses.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SizeOverLifetimeStartEnd"

    def __init__(self, start_size: primitives.Float3 | None = None, end_size: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_size: Initial value for StartSize.
            end_size: Initial value for EndSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_size is not None:
            self.start_size = start_size
        if end_size is not None:
            self.end_size = end_size

    @property
    def start_size(self) -> primitives.Float3 | None:
        """The size particles will have at the beginning of their lifetime."""
        member = self.get_member("StartSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_size.setter
    def start_size(self, value: primitives.Float3) -> None:
        """Set the StartSize field value."""
        member = self.get_member("StartSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartSize", fields.FieldFloat3(value=value)
            )

    @property
    def end_size(self) -> primitives.Float3 | None:
        """The size particles will have at the end or their lifetime."""
        member = self.get_member("EndSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_size.setter
    def end_size(self, value: primitives.Float3) -> None:
        """Set the EndSize field value."""
        member = self.get_member("EndSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndSize", fields.FieldFloat3(value=value)
            )

