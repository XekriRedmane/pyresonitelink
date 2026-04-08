"""Generated component: SlotGizmo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.tube_box_mesh import TubeBoxMesh
from pyresonitelink.generated._types.segment_mesh import SegmentMesh
from pyresonitelink.generated._types.point_anchor import PointAnchor
from pyresonitelink.generated._types.translation_gizmo import TranslationGizmo
from pyresonitelink.generated._types.rotation_gizmo import RotationGizmo
from pyresonitelink.generated._types.scale_gizmo import ScaleGizmo
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlotGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SlotGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SlotGizmo"

    def __init__(self, is_folded: bool | None = None, active_gizmo: str | Worker | None = None, target_slot: str | Slot | None = None, position_drive: str | IField[primitives.Float3] | None = None, scale_drive: str | IField[primitives.Float3] | None = None, bounds_mesh: str | TubeBoxMesh | None = None, bounds_root: str | Slot | None = None, bounds_rotation: str | IField[primitives.FloatQ] | None = None, bounds_offset: str | IField[primitives.Float3] | None = None, bounds_active: str | IField[bool] | None = None, name_text: str | IField[str] | None = None, name_offset: str | IField[primitives.Float3] | None = None, name_rotation: str | IField[primitives.FloatQ] | None = None, name_active: str | IField[bool] | None = None, x_pos_segment: str | SegmentMesh | None = None, y_pos_segment: str | SegmentMesh | None = None, z_pos_segment: str | SegmentMesh | None = None, root_anchor: str | PointAnchor | None = None, translation_gizmo: str | TranslationGizmo | None = None, rotation_gizmo: str | RotationGizmo | None = None, scale_gizmo: str | ScaleGizmo | None = None, is_local_space: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_folded: Initial value for _isFolded.
            active_gizmo: Initial value for _activeGizmo.
            target_slot: Initial value for _targetSlot.
            position_drive: Initial value for _positionDrive.
            scale_drive: Initial value for _scaleDrive.
            bounds_mesh: Initial value for _boundsMesh.
            bounds_root: Initial value for _boundsRoot.
            bounds_rotation: Initial value for _boundsRotation.
            bounds_offset: Initial value for _boundsOffset.
            bounds_active: Initial value for _boundsActive.
            name_text: Initial value for _nameText.
            name_offset: Initial value for _nameOffset.
            name_rotation: Initial value for _nameRotation.
            name_active: Initial value for _nameActive.
            x_pos_segment: Initial value for _xPosSegment.
            y_pos_segment: Initial value for _yPosSegment.
            z_pos_segment: Initial value for _zPosSegment.
            root_anchor: Initial value for _rootAnchor.
            translation_gizmo: Initial value for _translationGizmo.
            rotation_gizmo: Initial value for _rotationGizmo.
            scale_gizmo: Initial value for _scaleGizmo.
            is_local_space: Initial value for IsLocalSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_folded is not None:
            self.is_folded = is_folded
        if active_gizmo is not None:
            self.active_gizmo = active_gizmo
        if target_slot is not None:
            self.target_slot = target_slot
        if position_drive is not None:
            self.position_drive = position_drive
        if scale_drive is not None:
            self.scale_drive = scale_drive
        if bounds_mesh is not None:
            self.bounds_mesh = bounds_mesh
        if bounds_root is not None:
            self.bounds_root = bounds_root
        if bounds_rotation is not None:
            self.bounds_rotation = bounds_rotation
        if bounds_offset is not None:
            self.bounds_offset = bounds_offset
        if bounds_active is not None:
            self.bounds_active = bounds_active
        if name_text is not None:
            self.name_text = name_text
        if name_offset is not None:
            self.name_offset = name_offset
        if name_rotation is not None:
            self.name_rotation = name_rotation
        if name_active is not None:
            self.name_active = name_active
        if x_pos_segment is not None:
            self.x_pos_segment = x_pos_segment
        if y_pos_segment is not None:
            self.y_pos_segment = y_pos_segment
        if z_pos_segment is not None:
            self.z_pos_segment = z_pos_segment
        if root_anchor is not None:
            self.root_anchor = root_anchor
        if translation_gizmo is not None:
            self.translation_gizmo = translation_gizmo
        if rotation_gizmo is not None:
            self.rotation_gizmo = rotation_gizmo
        if scale_gizmo is not None:
            self.scale_gizmo = scale_gizmo
        if is_local_space is not None:
            self.is_local_space = is_local_space

    @property
    def is_folded(self) -> bool | None:
        """The _isFolded field value."""
        member = self.get_member("_isFolded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_folded.setter
    def is_folded(self, value: bool) -> None:
        """Set the _isFolded field value."""
        member = self.get_member("_isFolded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isFolded", fields.FieldBool(value=value)
            )

    @property
    def active_gizmo(self) -> str | None:
        """Target ID of the _activeGizmo reference (targets Worker)."""
        member = self.get_member("_activeGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_gizmo.setter
    def active_gizmo(self, target: str | Worker | None) -> None:
        """Set the _activeGizmo reference by target ID or Worker instance."""
        target_id: str | None = target.id if isinstance(target, Worker) else target  # type: ignore[assignment]
        member = self.get_member("_activeGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Worker'),
            )

    @property
    def target_slot(self) -> str | None:
        """Target ID of the _targetSlot reference (targets Slot)."""
        member = self.get_member("_targetSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_slot.setter
    def target_slot(self, target: str | Slot | None) -> None:
        """Set the _targetSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_targetSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def position_drive(self) -> str | None:
        """Target ID of the _positionDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _positionDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def scale_drive(self) -> str | None:
        """Target ID of the _scaleDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_drive.setter
    def scale_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scaleDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scaleDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def bounds_mesh(self) -> str | None:
        """Target ID of the _boundsMesh reference (targets TubeBoxMesh)."""
        member = self.get_member("_boundsMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds_mesh.setter
    def bounds_mesh(self, target: str | TubeBoxMesh | None) -> None:
        """Set the _boundsMesh reference by target ID or TubeBoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, TubeBoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_boundsMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boundsMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TubeBoxMesh'),
            )

    @property
    def bounds_root(self) -> str | None:
        """Target ID of the _boundsRoot reference (targets Slot)."""
        member = self.get_member("_boundsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds_root.setter
    def bounds_root(self, target: str | Slot | None) -> None:
        """Set the _boundsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_boundsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boundsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def bounds_rotation(self) -> str | None:
        """Target ID of the _boundsRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_boundsRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds_rotation.setter
    def bounds_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _boundsRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_boundsRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boundsRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def bounds_offset(self) -> str | None:
        """Target ID of the _boundsOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_boundsOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds_offset.setter
    def bounds_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _boundsOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_boundsOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boundsOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def bounds_active(self) -> str | None:
        """Target ID of the _boundsActive reference (targets IField[bool])."""
        member = self.get_member("_boundsActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds_active.setter
    def bounds_active(self, target: str | IField[bool] | None) -> None:
        """Set the _boundsActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_boundsActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_boundsActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def name_text(self) -> str | None:
        """Target ID of the _nameText reference (targets IField[str])."""
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_text.setter
    def name_text(self, target: str | IField[str] | None) -> None:
        """Set the _nameText reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def name_offset(self) -> str | None:
        """Target ID of the _nameOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_nameOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_offset.setter
    def name_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _nameOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_nameOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def name_rotation(self) -> str | None:
        """Target ID of the _nameRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_nameRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_rotation.setter
    def name_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _nameRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_nameRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def name_active(self) -> str | None:
        """Target ID of the _nameActive reference (targets IField[bool])."""
        member = self.get_member("_nameActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_active.setter
    def name_active(self, target: str | IField[bool] | None) -> None:
        """Set the _nameActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_nameActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def x_pos_segment(self) -> str | None:
        """Target ID of the _xPosSegment reference (targets SegmentMesh)."""
        member = self.get_member("_xPosSegment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_pos_segment.setter
    def x_pos_segment(self, target: str | SegmentMesh | None) -> None:
        """Set the _xPosSegment reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_xPosSegment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xPosSegment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def y_pos_segment(self) -> str | None:
        """Target ID of the _yPosSegment reference (targets SegmentMesh)."""
        member = self.get_member("_yPosSegment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_pos_segment.setter
    def y_pos_segment(self, target: str | SegmentMesh | None) -> None:
        """Set the _yPosSegment reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_yPosSegment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yPosSegment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def z_pos_segment(self) -> str | None:
        """Target ID of the _zPosSegment reference (targets SegmentMesh)."""
        member = self.get_member("_zPosSegment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_pos_segment.setter
    def z_pos_segment(self, target: str | SegmentMesh | None) -> None:
        """Set the _zPosSegment reference by target ID or SegmentMesh instance."""
        target_id: str | None = target.id if isinstance(target, SegmentMesh) else target  # type: ignore[assignment]
        member = self.get_member("_zPosSegment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zPosSegment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SegmentMesh'),
            )

    @property
    def bounds_anchor_positions(self) -> members.SyncList | None:
        """The _boundsAnchorPositions member."""
        member = self.get_member("_boundsAnchorPositions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bounds_anchor_positions.setter
    def bounds_anchor_positions(self, value: members.SyncList) -> None:
        """Set the _boundsAnchorPositions member."""
        self.set_member("_boundsAnchorPositions", value)

    @property
    def root_anchor(self) -> str | None:
        """Target ID of the _rootAnchor reference (targets PointAnchor)."""
        member = self.get_member("_rootAnchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_anchor.setter
    def root_anchor(self, target: str | PointAnchor | None) -> None:
        """Set the _rootAnchor reference by target ID or PointAnchor instance."""
        target_id: str | None = target.id if isinstance(target, PointAnchor) else target  # type: ignore[assignment]
        member = self.get_member("_rootAnchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootAnchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PointAnchor'),
            )

    @property
    def translation_gizmo(self) -> str | None:
        """Target ID of the _translationGizmo reference (targets TranslationGizmo)."""
        member = self.get_member("_translationGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @translation_gizmo.setter
    def translation_gizmo(self, target: str | TranslationGizmo | None) -> None:
        """Set the _translationGizmo reference by target ID or TranslationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, TranslationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_translationGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_translationGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TranslationGizmo'),
            )

    @property
    def rotation_gizmo(self) -> str | None:
        """Target ID of the _rotationGizmo reference (targets RotationGizmo)."""
        member = self.get_member("_rotationGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_gizmo.setter
    def rotation_gizmo(self, target: str | RotationGizmo | None) -> None:
        """Set the _rotationGizmo reference by target ID or RotationGizmo instance."""
        target_id: str | None = target.id if isinstance(target, RotationGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_rotationGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotationGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RotationGizmo'),
            )

    @property
    def scale_gizmo(self) -> str | None:
        """Target ID of the _scaleGizmo reference (targets ScaleGizmo)."""
        member = self.get_member("_scaleGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_gizmo.setter
    def scale_gizmo(self, target: str | ScaleGizmo | None) -> None:
        """Set the _scaleGizmo reference by target ID or ScaleGizmo instance."""
        target_id: str | None = target.id if isinstance(target, ScaleGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_scaleGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScaleGizmo'),
            )

    @property
    def is_local_space(self) -> bool | None:
        """The IsLocalSpace field value."""
        member = self.get_member("IsLocalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_local_space.setter
    def is_local_space(self, value: bool) -> None:
        """Set the IsLocalSpace field value."""
        member = self.get_member("IsLocalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLocalSpace", fields.FieldBool(value=value)
            )

