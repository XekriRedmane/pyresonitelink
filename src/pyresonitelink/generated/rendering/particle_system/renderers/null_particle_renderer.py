"""Generated component: NullParticleRenderer."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NullParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.NullParticleRenderer.

    Category: Rendering/Particle System/Renderers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.NullParticleRenderer"

    pass

