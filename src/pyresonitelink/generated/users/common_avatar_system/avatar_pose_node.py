"""Generated component: AvatarPoseNode."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iavatar_object import IAvatarObject
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseNode(GeneratedComponent, IAvatarObject, IInputUpdateReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode"

    def __init__(self, equip_order_priority: primitives.Int | None = None, run_after_input_update: primitives.Bool | None = None, is_tracking: primitives.Bool | None = None, source_is_tracking: primitives.Bool | None = None, source_is_active: primitives.Bool | None = None, source_is_simulated: primitives.Bool | None = None, object_slot: str | AvatarObjectSlot | None = None, source: str | Slot | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, scale: str | IField[primitives.Float3] | None = None, active: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            equip_order_priority: Initial value for EquipOrderPriority.
            run_after_input_update: Initial value for RunAfterInputUpdate.
            is_tracking: Initial value for IsTracking.
            source_is_tracking: Initial value for SourceIsTracking.
            source_is_active: Initial value for SourceIsActive.
            source_is_simulated: Initial value for SourceIsSimulated.
            object_slot: Initial value for _objectSlot.
            source: Initial value for _source.
            position: Initial value for _position.
            rotation: Initial value for _rotation.
            scale: Initial value for _scale.
            active: Initial value for _active.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if equip_order_priority is not None:
            self.equip_order_priority = equip_order_priority
        if run_after_input_update is not None:
            self.run_after_input_update = run_after_input_update
        if is_tracking is not None:
            self.is_tracking = is_tracking
        if source_is_tracking is not None:
            self.source_is_tracking = source_is_tracking
        if source_is_active is not None:
            self.source_is_active = source_is_active
        if source_is_simulated is not None:
            self.source_is_simulated = source_is_simulated
        if object_slot is not None:
            self.object_slot = object_slot
        if source is not None:
            self.source = source
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if scale is not None:
            self.scale = scale
        if active is not None:
            self.active = active

    @property
    def node(self) -> members.FieldEnum | None:
        """The Node member."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @node.setter
    def node(self, value: members.FieldEnum) -> None:
        """Set the Node member."""
        self.set_member("Node", value)

    @property
    def equip_order_priority(self) -> primitives.Int | None:
        """The EquipOrderPriority field value."""
        member = self.get_member("EquipOrderPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_order_priority.setter
    def equip_order_priority(self, value: primitives.Int) -> None:
        """Set the EquipOrderPriority field value."""
        member = self.get_member("EquipOrderPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipOrderPriority", fields.FieldInt(value=value)
            )

    @property
    def run_after_input_update(self) -> primitives.Bool | None:
        """The RunAfterInputUpdate field value."""
        member = self.get_member("RunAfterInputUpdate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @run_after_input_update.setter
    def run_after_input_update(self, value: primitives.Bool) -> None:
        """Set the RunAfterInputUpdate field value."""
        member = self.get_member("RunAfterInputUpdate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RunAfterInputUpdate", fields.FieldBool(value=value)
            )

    @property
    def mutually_exclusive_nodes(self) -> members.SyncList | None:
        """The MutuallyExclusiveNodes member."""
        member = self.get_member("MutuallyExclusiveNodes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @mutually_exclusive_nodes.setter
    def mutually_exclusive_nodes(self, value: members.SyncList) -> None:
        """Set the MutuallyExclusiveNodes member."""
        self.set_member("MutuallyExclusiveNodes", value)

    @property
    def is_tracking(self) -> primitives.Bool | None:
        """The IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: primitives.Bool) -> None:
        """Set the IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsTracking", fields.FieldBool(value=value)
            )

    @property
    def source_is_tracking(self) -> primitives.Bool | None:
        """The SourceIsTracking field value."""
        member = self.get_member("SourceIsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_is_tracking.setter
    def source_is_tracking(self, value: primitives.Bool) -> None:
        """Set the SourceIsTracking field value."""
        member = self.get_member("SourceIsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceIsTracking", fields.FieldBool(value=value)
            )

    @property
    def source_is_active(self) -> primitives.Bool | None:
        """The SourceIsActive field value."""
        member = self.get_member("SourceIsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_is_active.setter
    def source_is_active(self, value: primitives.Bool) -> None:
        """Set the SourceIsActive field value."""
        member = self.get_member("SourceIsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceIsActive", fields.FieldBool(value=value)
            )

    @property
    def source_is_simulated(self) -> primitives.Bool | None:
        """The SourceIsSimulated field value."""
        member = self.get_member("SourceIsSimulated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_is_simulated.setter
    def source_is_simulated(self, value: primitives.Bool) -> None:
        """Set the SourceIsSimulated field value."""
        member = self.get_member("SourceIsSimulated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceIsSimulated", fields.FieldBool(value=value)
            )

    @property
    def object_slot(self) -> str | None:
        """Target ID of the _objectSlot reference (targets AvatarObjectSlot)."""
        member = self.get_member("_objectSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot.setter
    def object_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the _objectSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("_objectSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_objectSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

    @property
    def source(self) -> str | None:
        """Target ID of the _source reference (targets Slot)."""
        member = self.get_member("_source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | Slot | None) -> None:
        """Set the _source reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
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
    def active(self) -> str | None:
        """Target ID of the _active reference (targets IField[primitives.Bool])."""
        member = self.get_member("_active")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active.setter
    def active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _active reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_active")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_active",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

