"""Generated component: MirrorTransform."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MirrorTransform(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MirrorTransform.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MirrorTransform"

    def __init__(self, mirror_source: str | Slot | None = None, mirror_plane: str | Slot | None = None, mirror_offset: primitives.Float3 | None = None, mirror_normal: primitives.Float3 | None = None, allow_write_back: primitives.Bool | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mirror_source: Initial value for MirrorSource.
            mirror_plane: Initial value for MirrorPlane.
            mirror_offset: Initial value for MirrorOffset.
            mirror_normal: Initial value for MirrorNormal.
            allow_write_back: Initial value for AllowWriteBack.
            position: Initial value for _position.
            rotation: Initial value for _rotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mirror_source is not None:
            self.mirror_source = mirror_source
        if mirror_plane is not None:
            self.mirror_plane = mirror_plane
        if mirror_offset is not None:
            self.mirror_offset = mirror_offset
        if mirror_normal is not None:
            self.mirror_normal = mirror_normal
        if allow_write_back is not None:
            self.allow_write_back = allow_write_back
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation

    @property
    def mirror_source(self) -> str | None:
        """Target ID of the MirrorSource reference (targets Slot)."""
        member = self.get_member("MirrorSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mirror_source.setter
    def mirror_source(self, target: str | Slot | None) -> None:
        """Set the MirrorSource reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("MirrorSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MirrorSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def mirror_plane(self) -> str | None:
        """Target ID of the MirrorPlane reference (targets Slot)."""
        member = self.get_member("MirrorPlane")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mirror_plane.setter
    def mirror_plane(self, target: str | Slot | None) -> None:
        """Set the MirrorPlane reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("MirrorPlane")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MirrorPlane",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def mirror_offset(self) -> primitives.Float3 | None:
        """The MirrorOffset field value."""
        member = self.get_member("MirrorOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror_offset.setter
    def mirror_offset(self, value: primitives.Float3) -> None:
        """Set the MirrorOffset field value."""
        member = self.get_member("MirrorOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MirrorOffset", fields.FieldFloat3(value=value)
            )

    @property
    def mirror_normal(self) -> primitives.Float3 | None:
        """The MirrorNormal field value."""
        member = self.get_member("MirrorNormal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror_normal.setter
    def mirror_normal(self, value: primitives.Float3) -> None:
        """Set the MirrorNormal field value."""
        member = self.get_member("MirrorNormal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MirrorNormal", fields.FieldFloat3(value=value)
            )

    @property
    def allow_write_back(self) -> primitives.Bool | None:
        """The AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_back.setter
    def allow_write_back(self, value: primitives.Bool) -> None:
        """Set the AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteBack", fields.FieldBool(value=value)
            )

    @property
    def position(self) -> str | None:
        """Target ID of the _position reference (targets IField[primitives.Float3])."""
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

