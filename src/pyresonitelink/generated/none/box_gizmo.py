"""Generated component: BoxGizmo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.ico_sphere_mesh import IcoSphereMesh
from pyresonitelink.generated._types.tube_box_mesh import TubeBoxMesh
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxGizmo(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """The BoxGizmo component is used to make the handles and visual for editing a box mesh or collider, and also handles the interaction with the handles.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxGizmo"

    def __init__(self, target_slot: str | Slot | None = None, box_size: str | IField[primitives.Float3] | None = None, box_center: str | IField[primitives.Float3] | None = None, lock_offset: primitives.Bool | None = None, material: str | OverlayFresnelMaterial | None = None, handle_sphere: str | IcoSphereMesh | None = None, visual_root: str | Slot | None = None, visual_position: str | IField[primitives.Float3] | None = None, visual_rotation: str | IField[primitives.FloatQ] | None = None, visual_scale: str | IField[primitives.Float3] | None = None, tube_box: str | TubeBoxMesh | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_slot: Initial value for TargetSlot.
            box_size: Initial value for BoxSize.
            box_center: Initial value for BoxCenter.
            lock_offset: Initial value for LockOffset.
            material: Initial value for _material.
            handle_sphere: Initial value for _handleSphere.
            visual_root: Initial value for _visualRoot.
            visual_position: Initial value for _visualPosition.
            visual_rotation: Initial value for _visualRotation.
            visual_scale: Initial value for _visualScale.
            tube_box: Initial value for _tubeBox.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_slot is not None:
            self.target_slot = target_slot
        if box_size is not None:
            self.box_size = box_size
        if box_center is not None:
            self.box_center = box_center
        if lock_offset is not None:
            self.lock_offset = lock_offset
        if material is not None:
            self.material = material
        if handle_sphere is not None:
            self.handle_sphere = handle_sphere
        if visual_root is not None:
            self.visual_root = visual_root
        if visual_position is not None:
            self.visual_position = visual_position
        if visual_rotation is not None:
            self.visual_rotation = visual_rotation
        if visual_scale is not None:
            self.visual_scale = visual_scale
        if tube_box is not None:
            self.tube_box = tube_box

    @property
    def target_slot(self) -> str | None:
        """The slot of the box to edit."""
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_slot.setter
    def target_slot(self, target: str | Slot | None) -> None:
        """Set the TargetSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def box_center_space(self) -> members.SyncObject | None:
        """The coordinate space to transform by when making the result of ``BoxCenter``"""
        member = self.get_member("BoxCenterSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @box_center_space.setter
    def box_center_space(self, value: members.SyncObject) -> None:
        """Set BoxCenterSpace. The coordinate space to transform by when making the result of ``BoxCenter``"""
        self.set_member("BoxCenterSpace", value)

    @property
    def box_size_space(self) -> members.SyncObject | None:
        """The coordinate space to transform by when making the result of ``BoxSize``"""
        member = self.get_member("BoxSizeSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @box_size_space.setter
    def box_size_space(self, value: members.SyncObject) -> None:
        """Set BoxSizeSpace. The coordinate space to transform by when making the result of ``BoxSize``"""
        self.set_member("BoxSizeSpace", value)

    @property
    def box_size(self) -> str | None:
        """The field to edit for the box size."""
        member = self.get_member("BoxSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @box_size.setter
    def box_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the BoxSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BoxSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BoxSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def box_center(self) -> str | None:
        """The field to drive for the box center."""
        member = self.get_member("BoxCenter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @box_center.setter
    def box_center(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the BoxCenter reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BoxCenter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BoxCenter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def lock_offset(self) -> primitives.Bool | None:
        """Whether to lock the offset of the box so it's center stays the same."""
        member = self.get_member("LockOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lock_offset.setter
    def lock_offset(self, value: primitives.Bool) -> None:
        """Set the LockOffset field value."""
        member = self.get_member("LockOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LockOffset", fields.FieldBool(value=value)
            )

    @property
    def vertices(self) -> members.SyncList | None:
        """A list of fields to drive for the vertex positions of the cube gizmo visual."""
        member = self.get_member("_vertices")
        if isinstance(member, members.SyncList):
            return member
        return None

    @vertices.setter
    def vertices(self, value: members.SyncList) -> None:
        """Set _vertices. A list of fields to drive for the vertex positions of the cube gizmo visual."""
        self.set_member("_vertices", value)

    @property
    def edges(self) -> members.SyncList | None:
        """A list of fields to drive for the edge positions of the cube gizmo visual."""
        member = self.get_member("_edges")
        if isinstance(member, members.SyncList):
            return member
        return None

    @edges.setter
    def edges(self, value: members.SyncList) -> None:
        """Set _edges. A list of fields to drive for the edge positions of the cube gizmo visual."""
        self.set_member("_edges", value)

    @property
    def faces(self) -> members.SyncList | None:
        """A list of fields to drive for the face positions of the cube gizmo visual."""
        member = self.get_member("_faces")
        if isinstance(member, members.SyncList):
            return member
        return None

    @faces.setter
    def faces(self, value: members.SyncList) -> None:
        """Set _faces. A list of fields to drive for the face positions of the cube gizmo visual."""
        self.set_member("_faces", value)

    @property
    def sphere_collider_radii(self) -> members.SyncList | None:
        """A list of fields to drive for the sphere rotations of the cube gizmo visual."""
        member = self.get_member("_sphereColliderRadii")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sphere_collider_radii.setter
    def sphere_collider_radii(self, value: members.SyncList) -> None:
        """Set _sphereColliderRadii. A list of fields to drive for the sphere rotations of the cube gizmo visual."""
        self.set_member("_sphereColliderRadii", value)

    @property
    def material(self) -> str | None:
        """The material being used for the gizmo visual."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _material reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def handle_sphere(self) -> str | None:
        """The mesh being used for the handles of the gizmo like corners or faces."""
        member = self.get_member("_handleSphere")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_sphere.setter
    def handle_sphere(self, target: str | IcoSphereMesh | None) -> None:
        """Set the _handleSphere reference by target ID or IcoSphereMesh instance."""
        target_id: str | None = target.id if isinstance(target, IcoSphereMesh) else target  # type: ignore[assignment]
        member = self.get_member("_handleSphere")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleSphere",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IcoSphereMesh'),
            )

    @property
    def visual_root(self) -> str | None:
        """The slot of the visual root."""
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_root.setter
    def visual_root(self, target: str | Slot | None) -> None:
        """Set the _visualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def visual_position(self) -> str | None:
        """The field to drive for the visual position."""
        member = self.get_member("_visualPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_position.setter
    def visual_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visualPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def visual_rotation(self) -> str | None:
        """The field to drive for the visual rotation."""
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_rotation.setter
    def visual_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _visualRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def visual_scale(self) -> str | None:
        """The field to drive for the visual scale."""
        member = self.get_member("_visualScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_scale.setter
    def visual_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visualScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def tube_box(self) -> str | None:
        """The tube box mesh being used for the gizmo visual."""
        member = self.get_member("_tubeBox")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tube_box.setter
    def tube_box(self, target: str | TubeBoxMesh | None) -> None:
        """Set the _tubeBox reference by target ID or TubeBoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, TubeBoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_tubeBox")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tubeBox",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TubeBoxMesh'),
            )

