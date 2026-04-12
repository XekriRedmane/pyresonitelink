"""Generated component: ColorByThreadDiagnosticModule."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorByThreadDiagnosticModule(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The ColorByThreadDiagnosticModule component makes particles colored based on what the thread is doing and/or what thread they are a part of as part of the Photon Dust Simulation.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorByThreadDiagnosticModule"

    pass

