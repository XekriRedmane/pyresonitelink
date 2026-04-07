"""Generated component: ItemShelf."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.igrabbable_receiver import IGrabbableReceiver
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iinteraction_target import IInteractionTarget
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ItemShelf(GeneratedComponent, IGrabbableReceiver, IGrabbableReparentBlock, IInteractionTarget, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ItemShelf.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ItemShelf"

    def __init__(self, ignore_grabber: str | Grabber | None = None, min_length: np.float32 | None = None, width: np.float32 | None = None, thickness: np.float32 | None = None, max_item_size: np.float32 | None = None, max_plane_distance: np.float32 | None = None, max_height_distance: np.float32 | None = None, target_length: np.float32 | None = None, visual: str | Slot | None = None, content: str | Slot | None = None, material: str | PBS_RimMetallic | None = None, visual_offset: str | IField[primitives.Float3] | None = None, shelf_mesh: str | BevelStripeMesh | None = None, collider: str | BoxCollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ignore_grabber: Initial value for IgnoreGrabber.
            min_length: Initial value for MinLength.
            width: Initial value for Width.
            thickness: Initial value for Thickness.
            max_item_size: Initial value for MaxItemSize.
            max_plane_distance: Initial value for MaxPlaneDistance.
            max_height_distance: Initial value for MaxHeightDistance.
            target_length: Initial value for _targetLength.
            visual: Initial value for _visual.
            content: Initial value for _content.
            material: Initial value for _material.
            visual_offset: Initial value for _visualOffset.
            shelf_mesh: Initial value for _shelfMesh.
            collider: Initial value for _collider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ignore_grabber is not None:
            self.ignore_grabber = ignore_grabber
        if min_length is not None:
            self.min_length = min_length
        if width is not None:
            self.width = width
        if thickness is not None:
            self.thickness = thickness
        if max_item_size is not None:
            self.max_item_size = max_item_size
        if max_plane_distance is not None:
            self.max_plane_distance = max_plane_distance
        if max_height_distance is not None:
            self.max_height_distance = max_height_distance
        if target_length is not None:
            self.target_length = target_length
        if visual is not None:
            self.visual = visual
        if content is not None:
            self.content = content
        if material is not None:
            self.material = material
        if visual_offset is not None:
            self.visual_offset = visual_offset
        if shelf_mesh is not None:
            self.shelf_mesh = shelf_mesh
        if collider is not None:
            self.collider = collider

    @property
    def grow_direction(self) -> members.FieldEnum | None:
        """The GrowDirection member."""
        member = self.get_member("GrowDirection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @grow_direction.setter
    def grow_direction(self, value: members.FieldEnum) -> None:
        """Set the GrowDirection member."""
        self.set_member("GrowDirection", value)

    @property
    def ignore_grabber(self) -> str | None:
        """Target ID of the IgnoreGrabber reference (targets Grabber)."""
        member = self.get_member("IgnoreGrabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_grabber.setter
    def ignore_grabber(self, target: str | Grabber | None) -> None:
        """Set the IgnoreGrabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreGrabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreGrabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def min_length(self) -> np.float32 | None:
        """The MinLength field value."""
        member = self.get_member("MinLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_length.setter
    def min_length(self, value: np.float32) -> None:
        """Set the MinLength field value."""
        member = self.get_member("MinLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinLength", fields.FieldFloat(value=value)
            )

    @property
    def width(self) -> np.float32 | None:
        """The Width field value."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: np.float32) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> np.float32 | None:
        """The Thickness field value."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: np.float32) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def max_item_size(self) -> np.float32 | None:
        """The MaxItemSize field value."""
        member = self.get_member("MaxItemSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_item_size.setter
    def max_item_size(self, value: np.float32) -> None:
        """Set the MaxItemSize field value."""
        member = self.get_member("MaxItemSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxItemSize", fields.FieldFloat(value=value)
            )

    @property
    def max_plane_distance(self) -> np.float32 | None:
        """The MaxPlaneDistance field value."""
        member = self.get_member("MaxPlaneDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_plane_distance.setter
    def max_plane_distance(self, value: np.float32) -> None:
        """Set the MaxPlaneDistance field value."""
        member = self.get_member("MaxPlaneDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxPlaneDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_height_distance(self) -> np.float32 | None:
        """The MaxHeightDistance field value."""
        member = self.get_member("MaxHeightDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height_distance.setter
    def max_height_distance(self, value: np.float32) -> None:
        """Set the MaxHeightDistance field value."""
        member = self.get_member("MaxHeightDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHeightDistance", fields.FieldFloat(value=value)
            )

    @property
    def target_length(self) -> np.float32 | None:
        """The _targetLength field value."""
        member = self.get_member("_targetLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_length.setter
    def target_length(self, value: np.float32) -> None:
        """Set the _targetLength field value."""
        member = self.get_member("_targetLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_targetLength", fields.FieldFloat(value=value)
            )

    @property
    def visual(self) -> str | None:
        """Target ID of the _visual reference (targets Slot)."""
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | Slot | None) -> None:
        """Set the _visual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def content(self) -> str | None:
        """Target ID of the _content reference (targets Slot)."""
        member = self.get_member("_content")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content.setter
    def content(self, target: str | Slot | None) -> None:
        """Set the _content reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_content")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_content",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets PBS_RimMetallic)."""
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
    def visual_offset(self) -> str | None:
        """Target ID of the _visualOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_visualOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_offset.setter
    def visual_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visualOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def shelf_mesh(self) -> str | None:
        """Target ID of the _shelfMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_shelfMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shelf_mesh.setter
    def shelf_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _shelfMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_shelfMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shelfMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
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

