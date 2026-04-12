"""Generated component: PointCloudParticleRenderer."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointCloudParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """The PointCloudParticleRenderer component is used to render particles as dots with size using a material

    Category: Rendering/Particle System/Renderers

    Used with particle systems.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.PointCloudParticleRenderer"

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
        """The material to render with."""
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

