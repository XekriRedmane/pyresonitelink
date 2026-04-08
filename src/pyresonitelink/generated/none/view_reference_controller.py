"""Generated component: ViewReferenceController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ViewReferenceController(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ViewReferenceController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ViewReferenceController"

    def __init__(self, position_stream: str | ValueStream[primitives.Float3] | None = None, rotation_stream: str | ValueStream[primitives.FloatQ] | None = None, object_slot: str | AvatarObjectSlot | None = None, should_voice_be_active: bool | None = None, object_slot_scale: str | IField[primitives.Float3] | None = None, object_slot_active: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_stream: Initial value for PositionStream.
            rotation_stream: Initial value for RotationStream.
            object_slot: Initial value for ObjectSlot.
            should_voice_be_active: Initial value for ShouldVoiceBeActive.
            object_slot_scale: Initial value for _objectSlotScale.
            object_slot_active: Initial value for _objectSlotActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_stream is not None:
            self.position_stream = position_stream
        if rotation_stream is not None:
            self.rotation_stream = rotation_stream
        if object_slot is not None:
            self.object_slot = object_slot
        if should_voice_be_active is not None:
            self.should_voice_be_active = should_voice_be_active
        if object_slot_scale is not None:
            self.object_slot_scale = object_slot_scale
        if object_slot_active is not None:
            self.object_slot_active = object_slot_active

    @property
    def position_stream(self) -> str | None:
        """Target ID of the PositionStream reference (targets ValueStream[primitives.Float3])."""
        member = self.get_member("PositionStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_stream.setter
    def position_stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the PositionStream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("PositionStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def rotation_stream(self) -> str | None:
        """Target ID of the RotationStream reference (targets ValueStream[primitives.FloatQ])."""
        member = self.get_member("RotationStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_stream.setter
    def rotation_stream(self, target: str | ValueStream[primitives.FloatQ] | None) -> None:
        """Set the RotationStream reference by target ID or ValueStream[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("RotationStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<floatQ>'),
            )

    @property
    def object_slot(self) -> str | None:
        """Target ID of the ObjectSlot reference (targets AvatarObjectSlot)."""
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot.setter
    def object_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the ObjectSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ObjectSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

    @property
    def should_voice_be_active(self) -> bool | None:
        """The ShouldVoiceBeActive field value."""
        member = self.get_member("ShouldVoiceBeActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @should_voice_be_active.setter
    def should_voice_be_active(self, value: bool) -> None:
        """Set the ShouldVoiceBeActive field value."""
        member = self.get_member("ShouldVoiceBeActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShouldVoiceBeActive", fields.FieldBool(value=value)
            )

    @property
    def object_slot_scale(self) -> str | None:
        """Target ID of the _objectSlotScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_objectSlotScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot_scale.setter
    def object_slot_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _objectSlotScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_objectSlotScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_objectSlotScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def object_slot_active(self) -> str | None:
        """Target ID of the _objectSlotActive reference (targets IField[bool])."""
        member = self.get_member("_objectSlotActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot_active.setter
    def object_slot_active(self, target: str | IField[bool] | None) -> None:
        """Set the _objectSlotActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_objectSlotActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_objectSlotActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

