"""Generated component: DebugQuadMeshRenderer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugQuadMeshRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """The DebugQuadMeshRenderer component renders particles via a QuadArrayMesh.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Renderers

    Attach to a slot, add to the renderer slot in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.DebugQuadMeshRenderer"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material

    @property
    def material(self) -> str | None:
        """The material to use for the mesh."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

