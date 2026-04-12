"""Generated component: BillboardParticleRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.billboard_alignment import BillboardAlignment
from pyresonitelink.generated._enums.motion_vector_mode import MotionVectorMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BillboardParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """The BillboardParticleRenderer component is a rendering style component for Particle systems that give them the default square tile based particles.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Renderers

    Attach to a slot, add to the renderer slot in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.BillboardParticleRenderer"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, alignment: BillboardAlignment | str | None = None, min_billboard_screen_size: primitives.Float | None = None, max_billboard_screen_size: primitives.Float | None = None, motion_vector_mode: MotionVectorMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            alignment: Initial value for Alignment.
            min_billboard_screen_size: Initial value for MinBillboardScreenSize.
            max_billboard_screen_size: Initial value for MaxBillboardScreenSize.
            motion_vector_mode: Initial value for MotionVectorMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if alignment is not None:
            self.alignment = alignment
        if min_billboard_screen_size is not None:
            self.min_billboard_screen_size = min_billboard_screen_size
        if max_billboard_screen_size is not None:
            self.max_billboard_screen_size = max_billboard_screen_size
        if motion_vector_mode is not None:
            self.motion_vector_mode = motion_vector_mode

    @property
    def material(self) -> str | None:
        """The material to use to render the particles."""
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
    def alignment(self) -> BillboardAlignment | None:
        """How to align the particles."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BillboardAlignment(member.value)
        return None

    @alignment.setter
    def alignment(self, value: BillboardAlignment | str) -> None:
        """Set Alignment. How to align the particles."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Alignment",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_billboard_screen_size(self) -> primitives.Float | None:
        """The minimum size a particle can be on the screen."""
        member = self.get_member("MinBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_billboard_screen_size.setter
    def min_billboard_screen_size(self, value: primitives.Float) -> None:
        """Set the MinBillboardScreenSize field value."""
        member = self.get_member("MinBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinBillboardScreenSize", fields.FieldFloat(value=value)
            )

    @property
    def max_billboard_screen_size(self) -> primitives.Float | None:
        """The maximum size a particle can be on the screen."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_billboard_screen_size.setter
    def max_billboard_screen_size(self, value: primitives.Float) -> None:
        """Set the MaxBillboardScreenSize field value."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxBillboardScreenSize", fields.FieldFloat(value=value)
            )

    @property
    def motion_vector_mode(self) -> MotionVectorMode | None:
        """How to handle rendering particles when it comes to their motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MotionVectorMode(member.value)
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: MotionVectorMode | str) -> None:
        """Set MotionVectorMode. How to handle rendering particles when it comes to their motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MotionVectorMode",
                members.FieldEnum(value=str(value)),
            )

