"""Generated component: Laser."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.ray_driver import RayDriver
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Laser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Laser component creates a simple red laser when attached that raycasts the enviroment.

When added to a slot the Laser component creates a MeshRenderer, a SegmentMesh, a RayDriver, and a red PBS RimMetallic.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Laser"

    def __init__(self, material: str | PBS_RimMetallic | None = None, ray_driver: str | RayDriver | None = None, mesh_renderer: str | MeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for _material.
            ray_driver: Initial value for _rayDriver.
            mesh_renderer: Initial value for _meshRenderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if ray_driver is not None:
            self.ray_driver = ray_driver
        if mesh_renderer is not None:
            self.mesh_renderer = mesh_renderer

    @property
    def material(self) -> str | None:
        """The material to use for the laser."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _material reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def ray_driver(self) -> str | None:
        """The ray driver driving the generated segment mesh."""
        member = self.get_member("_rayDriver")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ray_driver.setter
    def ray_driver(self, target: str | RayDriver | None) -> None:
        """Set the _rayDriver reference by target ID or RayDriver instance."""
        target_id: str | None = target.id if isinstance(target, RayDriver) else target  # type: ignore[assignment]
        member = self.get_member("_rayDriver")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rayDriver",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RayDriver'),
            )

    @property
    def mesh_renderer(self) -> str | None:
        """The mesh renderer rendering the segment mesh for this laser pointer type component."""
        member = self.get_member("_meshRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_renderer.setter
    def mesh_renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the _meshRenderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_meshRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_meshRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

