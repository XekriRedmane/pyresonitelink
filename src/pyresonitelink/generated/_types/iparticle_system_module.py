"""Generated type: IParticleSystemModule."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iparticle_system_subsystem import IParticleSystemSubsystem

M = TypeVar('M')


class IParticleSystemModule(IParticleSystemSubsystem, Generic[M]):
    """Interface: [FrooxEngine]FrooxEngine.PhotonDust.IParticleSystemModule<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.PhotonDust.IParticleSystemModule<>"

