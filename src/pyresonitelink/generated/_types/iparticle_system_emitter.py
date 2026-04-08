"""Generated type: IParticleSystemEmitter."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iparticle_system_subsystem import IParticleSystemSubsystem

E = TypeVar('E')


class IParticleSystemEmitter(IParticleSystemSubsystem, Generic[E]):
    """Interface: [FrooxEngine]FrooxEngine.PhotonDust.IParticleSystemEmitter<>."""

