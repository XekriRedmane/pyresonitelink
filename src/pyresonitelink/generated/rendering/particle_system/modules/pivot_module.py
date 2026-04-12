"""Generated component: PivotModule."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PivotModule(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Pivot Module component

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.PivotModule"

    pass

