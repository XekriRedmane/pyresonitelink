"""Generated component: RotationSimulatorModule."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RotationSimulatorModule(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The RotationSimulatorModule component is the second most essential particle simulator module. Without it, particles will not have orientation, or have Angular velocity.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.RotationSimulatorModule"

    pass

