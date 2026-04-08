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
    """Wrapper for [FrooxEngine]FrooxEngine.RaycastDriver.

    Category: Transform/Drivers
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
        """Target ID of the IgnoreHierarchy reference (targets Slot)."""
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
        """The FilterDistance field value."""
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
        """Target ID of the Origin reference (targets Slot)."""
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
        """The Offset field value."""
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
        """The Direction field value."""
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
        """The MaxDistance field value."""
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
        """The NoHitDistance field value."""
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
    def rotation_drive(self) -> str | None:
        """Target ID of the _rotationDrive reference (targets IField[primitives.FloatQ])."""
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

