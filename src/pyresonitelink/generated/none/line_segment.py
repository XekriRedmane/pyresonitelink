"""Generated component: LineSegment."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.cylinder_mesh import CylinderMesh
from pyresonitelink.generated._types.cylinder_collider import CylinderCollider
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LineSegment(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LineSegment.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LineSegment"

    def __init__(self, radius: primitives.Float | None = None, sides: primitives.Int | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, anchor0: str | Slot | None = None, anchor1: str | Slot | None = None, cylinder: str | CylinderMesh | None = None, collider: str | CylinderCollider | None = None, offset: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, visual_scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            sides: Initial value for Sides.
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            anchor0: Initial value for Anchor0.
            anchor1: Initial value for Anchor1.
            cylinder: Initial value for _cylinder.
            collider: Initial value for _collider.
            offset: Initial value for _offset.
            rotation: Initial value for _rotation.
            visual_scale: Initial value for _visualScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if sides is not None:
            self.sides = sides
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if anchor0 is not None:
            self.anchor0 = anchor0
        if anchor1 is not None:
            self.anchor1 = anchor1
        if cylinder is not None:
            self.cylinder = cylinder
        if collider is not None:
            self.collider = collider
        if offset is not None:
            self.offset = offset
        if rotation is not None:
            self.rotation = rotation
        if visual_scale is not None:
            self.visual_scale = visual_scale

    @property
    def radius(self) -> primitives.Float | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def sides(self) -> primitives.Int | None:
        """The Sides field value."""
        member = self.get_member("Sides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sides.setter
    def sides(self, value: primitives.Int) -> None:
        """Set the Sides field value."""
        member = self.get_member("Sides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Sides", fields.FieldInt(value=value)
            )

    @property
    def point0(self) -> primitives.Float3 | None:
        """The Point0 field value."""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Float3) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldFloat3(value=value)
            )

    @property
    def point1(self) -> primitives.Float3 | None:
        """The Point1 field value."""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Float3) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldFloat3(value=value)
            )

    @property
    def anchor0(self) -> str | None:
        """Target ID of the Anchor0 reference (targets Slot)."""
        member = self.get_member("Anchor0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor0.setter
    def anchor0(self, target: str | Slot | None) -> None:
        """Set the Anchor0 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Anchor0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def anchor1(self) -> str | None:
        """Target ID of the Anchor1 reference (targets Slot)."""
        member = self.get_member("Anchor1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor1.setter
    def anchor1(self, target: str | Slot | None) -> None:
        """Set the Anchor1 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Anchor1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def cylinder(self) -> str | None:
        """Target ID of the _cylinder reference (targets CylinderMesh)."""
        member = self.get_member("_cylinder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder.setter
    def cylinder(self, target: str | CylinderMesh | None) -> None:
        """Set the _cylinder reference by target ID or CylinderMesh instance."""
        target_id: str | None = target.id if isinstance(target, CylinderMesh) else target  # type: ignore[assignment]
        member = self.get_member("_cylinder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cylinder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CylinderMesh'),
            )

    @property
    def collider(self) -> str | None:
        """Target ID of the _collider reference (targets CylinderCollider)."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | CylinderCollider | None) -> None:
        """Set the _collider reference by target ID or CylinderCollider instance."""
        target_id: str | None = target.id if isinstance(target, CylinderCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CylinderCollider'),
            )

    @property
    def offset(self) -> str | None:
        """Target ID of the _offset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset.setter
    def offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _offset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation(self) -> str | None:
        """Target ID of the _rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def visual_scale(self) -> str | None:
        """Target ID of the _visualScale reference (targets IField[primitives.Float3])."""
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

