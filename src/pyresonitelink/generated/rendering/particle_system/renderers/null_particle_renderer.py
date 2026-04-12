"""Generated component: NullParticleRenderer."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NullParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """The Null Particle Renderer component is used with Photon Dust to render zero geometry particles.

    Category: Rendering/Particle System/Renderers

    Used for debugging.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.NullParticleRenderer"

    pass

