"""Generated component: TrailLifetimeFromSizeInitializer."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrailLifetimeFromSizeInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The TrailLifetimeFromSizeInitializer component will give trails a lifetime depending on how much more or less size they have compared to a ref size.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TrailLifetimeFromSizeInitializer"

    def __init__(self, reference_size: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference_size: Initial value for ReferenceSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference_size is not None:
            self.reference_size = reference_size

    @property
    def reference_size(self) -> primitives.Float | None:
        """The size to reference a trail size against when making a trail's lifetime."""
        member = self.get_member("ReferenceSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_size.setter
    def reference_size(self, value: primitives.Float) -> None:
        """Set the ReferenceSize field value."""
        member = self.get_member("ReferenceSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceSize", fields.FieldFloat(value=value)
            )

