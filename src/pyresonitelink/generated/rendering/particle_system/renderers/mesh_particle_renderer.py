"""Generated component: MeshParticleRenderer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.MeshParticleRenderer.

    Category: Rendering/Particle System/Renderers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.MeshParticleRenderer"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, mesh: str | IAssetProvider[Mesh] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            mesh: Initial value for Mesh.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if mesh is not None:
            self.mesh = mesh

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets IAssetProvider[Material])."""
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
        """Target ID of the Mesh reference (targets IAssetProvider[Mesh])."""
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
    def alignment(self) -> members.FieldEnum | None:
        """The Alignment member."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @alignment.setter
    def alignment(self, value: members.FieldEnum) -> None:
        """Set the Alignment member."""
        self.set_member("Alignment", value)

