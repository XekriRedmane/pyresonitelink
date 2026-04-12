"""Generated component: LegacyRendererSwitcher."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.billboard_particle_renderer import BillboardParticleRenderer
from pyresonitelink.generated._types.mesh_particle_renderer import MeshParticleRenderer
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyRendererSwitcher(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyRendererSwitcher component is used to switch between different rendering types depending on meshes.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyRendererSwitcher"

    def __init__(self, particle_mesh: str | AssetRef[Mesh] | None = None, billboard_renderer: str | BillboardParticleRenderer | None = None, mesh_renderer: str | MeshParticleRenderer | None = None, renderer_drive: str | SyncRef[IParticleRenderer] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            particle_mesh: Initial value for ParticleMesh.
            billboard_renderer: Initial value for BillboardRenderer.
            mesh_renderer: Initial value for MeshRenderer.
            renderer_drive: Initial value for RendererDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if particle_mesh is not None:
            self.particle_mesh = particle_mesh
        if billboard_renderer is not None:
            self.billboard_renderer = billboard_renderer
        if mesh_renderer is not None:
            self.mesh_renderer = mesh_renderer
        if renderer_drive is not None:
            self.renderer_drive = renderer_drive

    @property
    def particle_mesh(self) -> str | None:
        """The particle mesh object when not null will use ``MeshRenderer`` for the renderer."""
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @particle_mesh.setter
    def particle_mesh(self, target: str | AssetRef[Mesh] | None) -> None:
        """Set the ParticleMesh reference by target ID or AssetRef[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParticleMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def billboard_renderer(self) -> str | None:
        """Can be switched to in order to render the particles as squares."""
        member = self.get_member("BillboardRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @billboard_renderer.setter
    def billboard_renderer(self, target: str | BillboardParticleRenderer | None) -> None:
        """Set the BillboardRenderer reference by target ID or BillboardParticleRenderer instance."""
        target_id: str | None = target.id if isinstance(target, BillboardParticleRenderer) else target  # type: ignore[assignment]
        member = self.get_member("BillboardRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BillboardRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.BillboardParticleRenderer'),
            )

    @property
    def mesh_renderer(self) -> str | None:
        """Can be switched to in order to render the particles as meshes."""
        member = self.get_member("MeshRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_renderer.setter
    def mesh_renderer(self, target: str | MeshParticleRenderer | None) -> None:
        """Set the MeshRenderer reference by target ID or MeshParticleRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshParticleRenderer) else target  # type: ignore[assignment]
        member = self.get_member("MeshRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MeshRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.MeshParticleRenderer'),
            )

    @property
    def renderer_drive(self) -> str | None:
        """Drives the target field with ``BillboardRenderer`` or ``MeshRenderer`` depending on if ``ParticleMesh`` is null."""
        member = self.get_member("RendererDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer_drive.setter
    def renderer_drive(self, target: str | SyncRef[IParticleRenderer] | None) -> None:
        """Set the RendererDrive reference by target ID or SyncRef[IParticleRenderer] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("RendererDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RendererDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.PhotonDust.IParticleRenderer>'),
            )

