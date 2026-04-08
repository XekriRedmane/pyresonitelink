"""Generated component: TrailLifetimeFromSizeInitializer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrailLifetimeFromSizeInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.TrailLifetimeFromSizeInitializer.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.TrailLifetimeFromSizeInitializer"

    def __init__(self, reference_size: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference_size: Initial value for ReferenceSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference_size is not None:
            self.reference_size = reference_size

    @property
    def reference_size(self) -> np.float32 | None:
        """The ReferenceSize field value."""
        member = self.get_member("ReferenceSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_size.setter
    def reference_size(self, value: np.float32) -> None:
        """Set the ReferenceSize field value."""
        member = self.get_member("ReferenceSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceSize", fields.FieldFloat(value=value)
            )

