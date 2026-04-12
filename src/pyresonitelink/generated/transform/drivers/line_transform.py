"""Generated component: LineTransform."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.position_type import PositionType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LineTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LineTransform component is a transform driver component used to position an object between two points or slots.

    Category: Transform/Drivers

    Can be used to position an object along a track like a slider.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LineTransform"

    def __init__(self, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, point0_anchor: str | Slot | None = None, point1_anchor: str | Slot | None = None, line_position_type: PositionType | str | None = None, plane_position_type: PositionType | str | None = None, line_point: primitives.Float | None = None, offset_point: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, allow_repositioning: primitives.Bool | None = None, reposition_offset: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            point0_anchor: Initial value for Point0Anchor.
            point1_anchor: Initial value for Point1Anchor.
            line_position_type: Initial value for LinePositionType.
            plane_position_type: Initial value for PlanePositionType.
            line_point: Initial value for LinePoint.
            offset_point: Initial value for OffsetPoint.
            rotation_offset: Initial value for RotationOffset.
            position: Initial value for _position.
            rotation: Initial value for _rotation.
            allow_repositioning: Initial value for AllowRepositioning.
            reposition_offset: Initial value for RepositionOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if point0_anchor is not None:
            self.point0_anchor = point0_anchor
        if point1_anchor is not None:
            self.point1_anchor = point1_anchor
        if line_position_type is not None:
            self.line_position_type = line_position_type
        if plane_position_type is not None:
            self.plane_position_type = plane_position_type
        if line_point is not None:
            self.line_point = line_point
        if offset_point is not None:
            self.offset_point = offset_point
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if allow_repositioning is not None:
            self.allow_repositioning = allow_repositioning
        if reposition_offset is not None:
            self.reposition_offset = reposition_offset

    @property
    def point0(self) -> primitives.Float3 | None:
        """The point in local space to transform from."""
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
        """The point in local space to transform to."""
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
    def point0_anchor(self) -> str | None:
        """acts as a slot to offset ``Point0`` in global space."""
        member = self.get_member("Point0Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point0_anchor.setter
    def point0_anchor(self, target: str | Slot | None) -> None:
        """Set the Point0Anchor reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Point0Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point0Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def point1_anchor(self) -> str | None:
        """acts as a slot to offset ``Point1`` in global space."""
        member = self.get_member("Point1Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point1_anchor.setter
    def point1_anchor(self, target: str | Slot | None) -> None:
        """Set the Point1Anchor reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Point1Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point1Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def line_position_type(self) -> PositionType | None:
        """How to calculate the position on the line using ``LinePoint`` for the slot this component is on."""
        member = self.get_member("LinePositionType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PositionType(member.value)
        return None

    @line_position_type.setter
    def line_position_type(self, value: PositionType | str) -> None:
        """Set LinePositionType. How to calculate the position on the line using ``LinePoint`` for the slot this component is on."""
        member = self.get_member("LinePositionType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "LinePositionType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def plane_position_type(self) -> PositionType | None:
        """How to calculate the position on the line using ``LinePoint`` for the slot this component is on."""
        member = self.get_member("PlanePositionType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PositionType(member.value)
        return None

    @plane_position_type.setter
    def plane_position_type(self, value: PositionType | str) -> None:
        """Set PlanePositionType. How to calculate the position on the line using ``LinePoint`` for the slot this component is on."""
        member = self.get_member("PlanePositionType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PlanePositionType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def line_point(self) -> primitives.Float | None:
        """Where on the line specified by ``Point0`` and ``Point1`` in percentage or relative distance that the slot this component is on should be positioned."""
        member = self.get_member("LinePoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_point.setter
    def line_point(self, value: primitives.Float) -> None:
        """Set the LinePoint field value."""
        member = self.get_member("LinePoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LinePoint", fields.FieldFloat(value=value)
            )

    @property
    def offset_point(self) -> primitives.Float3 | None:
        """The offset from the point found by ``LinePoint`` slot this component is on should be."""
        member = self.get_member("OffsetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_point.setter
    def offset_point(self, value: primitives.Float3) -> None:
        """Set the OffsetPoint field value."""
        member = self.get_member("OffsetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """The rotation offset from looking along the line."""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def position(self) -> str | None:
        """drives the target field with the position found by ``LinePoint`` plus ``OffsetPoint`` rotated by ``RotationOffset`` and "looking down the line rotation" around the point found by ``LinePoint``."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation(self) -> str | None:
        """drives the target field with ``RotationOffset`` and "looking down the line rotation"."""
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
    def allow_repositioning(self) -> primitives.Bool | None:
        """Allow grabbing of the slot this component is on to move the object and change ``LinePoint``"""
        member = self.get_member("AllowRepositioning")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_repositioning.setter
    def allow_repositioning(self, value: primitives.Bool) -> None:
        """Set the AllowRepositioning field value."""
        member = self.get_member("AllowRepositioning")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowRepositioning", fields.FieldBool(value=value)
            )

    @property
    def reposition_offset(self) -> primitives.Bool | None:
        """Whether grabbing changes ``OffsetPoint`` as well."""
        member = self.get_member("RepositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reposition_offset.setter
    def reposition_offset(self, value: primitives.Bool) -> None:
        """Set the RepositionOffset field value."""
        member = self.get_member("RepositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RepositionOffset", fields.FieldBool(value=value)
            )

