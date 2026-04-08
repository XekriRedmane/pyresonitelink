"""Generated component: BillboardParticleRenderer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BillboardParticleRenderer(GeneratedComponent, IParticleRenderer, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.BillboardParticleRenderer.

    Category: Rendering/Particle System/Renderers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.BillboardParticleRenderer"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, min_billboard_screen_size: np.float32 | None = None, max_billboard_screen_size: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            min_billboard_screen_size: Initial value for MinBillboardScreenSize.
            max_billboard_screen_size: Initial value for MaxBillboardScreenSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if min_billboard_screen_size is not None:
            self.min_billboard_screen_size = min_billboard_screen_size
        if max_billboard_screen_size is not None:
            self.max_billboard_screen_size = max_billboard_screen_size

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

    @property
    def min_billboard_screen_size(self) -> np.float32 | None:
        """The MinBillboardScreenSize field value."""
        member = self.get_member("MinBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_billboard_screen_size.setter
    def min_billboard_screen_size(self, value: np.float32) -> None:
        """Set the MinBillboardScreenSize field value."""
        member = self.get_member("MinBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinBillboardScreenSize", fields.FieldFloat(value=value)
            )

    @property
    def max_billboard_screen_size(self) -> np.float32 | None:
        """The MaxBillboardScreenSize field value."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_billboard_screen_size.setter
    def max_billboard_screen_size(self, value: np.float32) -> None:
        """Set the MaxBillboardScreenSize field value."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxBillboardScreenSize", fields.FieldFloat(value=value)
            )

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

