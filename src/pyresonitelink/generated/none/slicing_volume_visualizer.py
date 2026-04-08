"""Generated component: SlicingVolumeVisualizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.volume_unlit_material import VolumeUnlitMaterial
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.box_mesh import BoxMesh
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_list import SyncList
from pyresonitelink.generated._types.slice_plane import SlicePlane
from pyresonitelink.generated._types.highlight import Highlight
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlicingVolumeVisualizer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SlicingVolumeVisualizer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SlicingVolumeVisualizer"

    def __init__(self, material: str | VolumeUnlitMaterial | None = None, auto_scale: primitives.Bool | None = None, renderer: str | MeshRenderer | None = None, mesh: str | BoxMesh | None = None, collider: str | BoxCollider | None = None, scale: str | IField[primitives.Float3] | None = None, slice_planes: str | SyncList[SlicePlane] | None = None, highlights: str | SyncList[Highlight] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            auto_scale: Initial value for AutoScale.
            renderer: Initial value for _renderer.
            mesh: Initial value for _mesh.
            collider: Initial value for _collider.
            scale: Initial value for _scale.
            slice_planes: Initial value for _slicePlanes.
            highlights: Initial value for _highlights.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if auto_scale is not None:
            self.auto_scale = auto_scale
        if renderer is not None:
            self.renderer = renderer
        if mesh is not None:
            self.mesh = mesh
        if collider is not None:
            self.collider = collider
        if scale is not None:
            self.scale = scale
        if slice_planes is not None:
            self.slice_planes = slice_planes
        if highlights is not None:
            self.highlights = highlights

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets VolumeUnlitMaterial)."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | VolumeUnlitMaterial | None) -> None:
        """Set the Material reference by target ID or VolumeUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, VolumeUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VolumeUnlitMaterial'),
            )

    @property
    def auto_scale(self) -> primitives.Bool | None:
        """The AutoScale field value."""
        member = self.get_member("AutoScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_scale.setter
    def auto_scale(self, value: primitives.Bool) -> None:
        """Set the AutoScale field value."""
        member = self.get_member("AutoScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoScale", fields.FieldBool(value=value)
            )

    @property
    def renderer(self) -> str | None:
        """Target ID of the _renderer reference (targets MeshRenderer)."""
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the _renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def mesh(self) -> str | None:
        """Target ID of the _mesh reference (targets BoxMesh)."""
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | BoxMesh | None) -> None:
        """Set the _mesh reference by target ID or BoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, BoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxMesh'),
            )

    @property
    def collider(self) -> str | None:
        """Target ID of the _collider reference (targets BoxCollider)."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | BoxCollider | None) -> None:
        """Set the _collider reference by target ID or BoxCollider instance."""
        target_id: str | None = target.id if isinstance(target, BoxCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxCollider'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the _scale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def slicers(self) -> members.SyncList | None:
        """The Slicers member."""
        member = self.get_member("Slicers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @slicers.setter
    def slicers(self, value: members.SyncList) -> None:
        """Set the Slicers member."""
        self.set_member("Slicers", value)

    @property
    def slice_planes(self) -> str | None:
        """Target ID of the _slicePlanes reference (targets SyncList[SlicePlane])."""
        member = self.get_member("_slicePlanes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slice_planes.setter
    def slice_planes(self, target: str | SyncList[SlicePlane] | None) -> None:
        """Set the _slicePlanes reference by target ID or SyncList[SlicePlane] instance."""
        target_id: str | None = target.id if isinstance(target, SyncList) else target  # type: ignore[assignment]
        member = self.get_member("_slicePlanes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slicePlanes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncList<[FrooxEngine]FrooxEngine.VolumeUnlitMaterial+SlicePlane>'),
            )

    @property
    def highlights(self) -> str | None:
        """Target ID of the _highlights reference (targets SyncList[Highlight])."""
        member = self.get_member("_highlights")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @highlights.setter
    def highlights(self, target: str | SyncList[Highlight] | None) -> None:
        """Set the _highlights reference by target ID or SyncList[Highlight] instance."""
        target_id: str | None = target.id if isinstance(target, SyncList) else target  # type: ignore[assignment]
        member = self.get_member("_highlights")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_highlights",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncList<[FrooxEngine]FrooxEngine.VolumeUnlitMaterial+Highlight>'),
            )

