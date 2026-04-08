"""Generated component: ParticleRibbonsModule."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleRibbonsModule(GeneratedComponent, IParticleSystemModule, IParticleRenderer, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleRibbonsModule.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleRibbonsModule"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, generate_lighting_data: bool | None = None, ribbon_point_ratio: np.float32 | None = None, max_ribbon_points: np.int32 | None = None, interweaved_ribbon_count: np.int32 | None = None, use_particle_color: bool | None = None, use_particle_size: bool | None = None, shuffle_interweaved_ribbons: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            generate_lighting_data: Initial value for GenerateLightingData.
            ribbon_point_ratio: Initial value for RibbonPointRatio.
            max_ribbon_points: Initial value for MaxRibbonPoints.
            interweaved_ribbon_count: Initial value for InterweavedRibbonCount.
            use_particle_color: Initial value for UseParticleColor.
            use_particle_size: Initial value for UseParticleSize.
            shuffle_interweaved_ribbons: Initial value for ShuffleInterweavedRibbons.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if generate_lighting_data is not None:
            self.generate_lighting_data = generate_lighting_data
        if ribbon_point_ratio is not None:
            self.ribbon_point_ratio = ribbon_point_ratio
        if max_ribbon_points is not None:
            self.max_ribbon_points = max_ribbon_points
        if interweaved_ribbon_count is not None:
            self.interweaved_ribbon_count = interweaved_ribbon_count
        if use_particle_color is not None:
            self.use_particle_color = use_particle_color
        if use_particle_size is not None:
            self.use_particle_size = use_particle_size
        if shuffle_interweaved_ribbons is not None:
            self.shuffle_interweaved_ribbons = shuffle_interweaved_ribbons

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
    def texture_mode(self) -> members.FieldEnum | None:
        """The TextureMode member."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_mode.setter
    def texture_mode(self, value: members.FieldEnum) -> None:
        """Set the TextureMode member."""
        self.set_member("TextureMode", value)

    @property
    def motion_vector_mode(self) -> members.FieldEnum | None:
        """The MotionVectorMode member."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: members.FieldEnum) -> None:
        """Set the MotionVectorMode member."""
        self.set_member("MotionVectorMode", value)

    @property
    def generate_lighting_data(self) -> bool | None:
        """The GenerateLightingData field value."""
        member = self.get_member("GenerateLightingData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_lighting_data.setter
    def generate_lighting_data(self, value: bool) -> None:
        """Set the GenerateLightingData field value."""
        member = self.get_member("GenerateLightingData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GenerateLightingData", fields.FieldBool(value=value)
            )

    @property
    def ribbon_point_ratio(self) -> np.float32 | None:
        """The RibbonPointRatio field value."""
        member = self.get_member("RibbonPointRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ribbon_point_ratio.setter
    def ribbon_point_ratio(self, value: np.float32) -> None:
        """Set the RibbonPointRatio field value."""
        member = self.get_member("RibbonPointRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RibbonPointRatio", fields.FieldFloat(value=value)
            )

    @property
    def distribution(self) -> members.FieldEnum | None:
        """The Distribution member."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @distribution.setter
    def distribution(self, value: members.FieldEnum) -> None:
        """Set the Distribution member."""
        self.set_member("Distribution", value)

    @property
    def max_ribbon_points(self) -> np.int32 | None:
        """The MaxRibbonPoints field value."""
        member = self.get_member("MaxRibbonPoints")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_ribbon_points.setter
    def max_ribbon_points(self, value: np.int32) -> None:
        """Set the MaxRibbonPoints field value."""
        member = self.get_member("MaxRibbonPoints")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRibbonPoints", fields.FieldInt(value=value)
            )

    @property
    def interweaved_ribbon_count(self) -> np.int32 | None:
        """The InterweavedRibbonCount field value."""
        member = self.get_member("InterweavedRibbonCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interweaved_ribbon_count.setter
    def interweaved_ribbon_count(self, value: np.int32) -> None:
        """Set the InterweavedRibbonCount field value."""
        member = self.get_member("InterweavedRibbonCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterweavedRibbonCount", fields.FieldInt(value=value)
            )

    @property
    def use_particle_color(self) -> bool | None:
        """The UseParticleColor field value."""
        member = self.get_member("UseParticleColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_particle_color.setter
    def use_particle_color(self, value: bool) -> None:
        """Set the UseParticleColor field value."""
        member = self.get_member("UseParticleColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseParticleColor", fields.FieldBool(value=value)
            )

    @property
    def use_particle_size(self) -> bool | None:
        """The UseParticleSize field value."""
        member = self.get_member("UseParticleSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_particle_size.setter
    def use_particle_size(self, value: bool) -> None:
        """Set the UseParticleSize field value."""
        member = self.get_member("UseParticleSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseParticleSize", fields.FieldBool(value=value)
            )

    @property
    def shuffle_interweaved_ribbons(self) -> bool | None:
        """The ShuffleInterweavedRibbons field value."""
        member = self.get_member("ShuffleInterweavedRibbons")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shuffle_interweaved_ribbons.setter
    def shuffle_interweaved_ribbons(self, value: bool) -> None:
        """Set the ShuffleInterweavedRibbons field value."""
        member = self.get_member("ShuffleInterweavedRibbons")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShuffleInterweavedRibbons", fields.FieldBool(value=value)
            )

    @property
    def size_inheritance_mode(self) -> members.FieldEnum | None:
        """The SizeInheritanceMode member."""
        member = self.get_member("SizeInheritanceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @size_inheritance_mode.setter
    def size_inheritance_mode(self, value: members.FieldEnum) -> None:
        """Set the SizeInheritanceMode member."""
        self.set_member("SizeInheritanceMode", value)

