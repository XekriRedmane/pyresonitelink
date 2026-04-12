"""Generated component: RaycastDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RaycastDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RaycastDriver component drives the position of the Slot it is attached to to the location of the hit point of a raycast and aligns its rotation to the normal of the hit object.

    Category: Transform/Drivers

    When placed on a slot, ``_positionDrive`` and ``_rotationDrive`` are
    automatically filled to the slot's position and rotation. These fields
    are not actually effective, as this component always writes to the
    position/rotation of the slot it is on. However, if either of these
    fields are omitted, the respective functionality of the raycast is not
    performed. The raycast is constructed in the local coordinate space of
    ``Origin``, where ``Offset`` controls the origin of the ray relative to
    the origin and ``Direction`` controls the direction of the ray relative
    to the origin. ``MaxDistance`` controls the maximum distance that the
    raycast will travel. If a raycast is unable to make contact with a
    collider within this distance, the position of the slot will be set to
    ``NoHitDistance`` in the direction of the raycast. These two distances
    are in global scale, and are not affected by either the slot's local
    scale or the scale of the ``Origin`` slot. If the ray hits a collider,
    the rotation of the slot will be aligned to the normal of the hit point.
    This rotation can be transformed into the normal vector by using the Get
    Forward node on the RaycastDriver slot. If the raycast does not hit a
    collider, the rotation will be set to ``(0, 0, 0)``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RaycastDriver"

    def __init__(self, ignore_hierarchy: str | Slot | None = None, filter_distance: primitives.Float | None = None, origin: str | Slot | None = None, offset: primitives.Float3 | None = None, direction: primitives.Float3 | None = None, max_distance: primitives.Float | None = None, no_hit_distance: primitives.Float | None = None, position_drive: str | IField[primitives.Float3] | None = None, rotation_drive: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ignore_hierarchy: Initial value for IgnoreHierarchy.
            filter_distance: Initial value for FilterDistance.
            origin: Initial value for Origin.
            offset: Initial value for Offset.
            direction: Initial value for Direction.
            max_distance: Initial value for MaxDistance.
            no_hit_distance: Initial value for NoHitDistance.
            position_drive: Initial value for _positionDrive.
            rotation_drive: Initial value for _rotationDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ignore_hierarchy is not None:
            self.ignore_hierarchy = ignore_hierarchy
        if filter_distance is not None:
            self.filter_distance = filter_distance
        if origin is not None:
            self.origin = origin
        if offset is not None:
            self.offset = offset
        if direction is not None:
            self.direction = direction
        if max_distance is not None:
            self.max_distance = max_distance
        if no_hit_distance is not None:
            self.no_hit_distance = no_hit_distance
        if position_drive is not None:
            self.position_drive = position_drive
        if rotation_drive is not None:
            self.rotation_drive = rotation_drive

    @property
    def ignore_hierarchy(self) -> str | None:
        """a hiearchy of slots which to ignore the colliders for"""
        member = self.get_member("IgnoreHierarchy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_hierarchy.setter
    def ignore_hierarchy(self, target: str | Slot | None) -> None:
        """Set the IgnoreHierarchy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreHierarchy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreHierarchy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def filter_distance(self) -> primitives.Float | None:
        """ignore hit detections before this distance."""
        member = self.get_member("FilterDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filter_distance.setter
    def filter_distance(self, value: primitives.Float) -> None:
        """Set the FilterDistance field value."""
        member = self.get_member("FilterDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FilterDistance", fields.FieldFloat(value=value)
            )

    @property
    def origin(self) -> str | None:
        """The slot to start the raycast from."""
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @origin.setter
    def origin(self, target: str | Slot | None) -> None:
        """Set the Origin reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Origin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The offset from ``Origin`` before starting the raycast."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def direction(self) -> primitives.Float3 | None:
        """The direction in ``Origin``'s local space to shoot in."""
        member = self.get_member("Direction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction.setter
    def direction(self, value: primitives.Float3) -> None:
        """Set the Direction field value."""
        member = self.get_member("Direction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction", fields.FieldFloat3(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """The maximum distance to raycast for."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def no_hit_distance(self) -> primitives.Float | None:
        """How far to raycast shoot for in meters till reporting no hit."""
        member = self.get_member("NoHitDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @no_hit_distance.setter
    def no_hit_distance(self, value: primitives.Float) -> None:
        """Set the NoHitDistance field value."""
        member = self.get_member("NoHitDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoHitDistance", fields.FieldFloat(value=value)
            )

    @property
    def position_drive(self) -> str | None:
        """The position field to drive. This does not actually affect the field that is driven, but if it is not filled, the component will not function."""
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
    def rotation_drive(self) -> str | None:
        """The rotation field to drive. This does not actually affect the field that is driven, but if it is not filled, the rotation of the slot is not changed. Aligns itself to the normal of the surface this raycast hit, or ``(0,0,0)``."""
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_drive.setter
    def rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

