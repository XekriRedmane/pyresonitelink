"""Generated component: MeshParticleRenderer."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.mesh_alignment import MeshAlignment
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """The MeshParticleRenderer component is a particle renderer that makes all particle instances in a particle system render as a specific mesh.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Renderers

    Attach to a slot, add to the renderer slot in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.MeshParticleRenderer"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, mesh: str | IAssetProvider[Mesh] | None = None, alignment: MeshAlignment | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            mesh: Initial value for Mesh.
            alignment: Initial value for Alignment.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if mesh is not None:
            self.mesh = mesh
        if alignment is not None:
            self.alignment = alignment

    @property
    def material(self) -> str | None:
        """The material the particles should have."""
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

    @property
    def mesh(self) -> str | None:
        """The mesh object to GPU instance to all particle points and render."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | IAssetProvider[Mesh] | None) -> None:
        """Set the Mesh reference by target ID or IAssetProvider[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def alignment(self) -> MeshAlignment | None:
        """How to align the meshes with the particle transforms."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MeshAlignment(member.value)
        return None

    @alignment.setter
    def alignment(self, value: MeshAlignment | str) -> None:
        """Set Alignment. How to align the meshes with the particle transforms."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Alignment",
                members.FieldEnum(value=str(value)),
            )

