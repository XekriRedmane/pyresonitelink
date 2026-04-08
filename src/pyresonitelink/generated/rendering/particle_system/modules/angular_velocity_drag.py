"""Generated component: AngularVelocityDrag."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AngularVelocityDrag(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.AngularVelocityDrag.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.AngularVelocityDrag"

    def __init__(self, drag: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drag: Initial value for Drag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drag is not None:
            self.drag = drag

    @property
    def drag(self) -> primitives.Float | None:
        """The Drag field value."""
        member = self.get_member("Drag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drag.setter
    def drag(self, value: primitives.Float) -> None:
        """Set the Drag field value."""
        member = self.get_member("Drag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Drag", fields.FieldFloat(value=value)
            )

