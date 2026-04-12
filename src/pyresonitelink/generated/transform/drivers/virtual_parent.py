"""Generated component: VirtualParent."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualParent(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Virtual Parent Component is used to make a Slot act as the child of another Slot without needing to be in the normal hierarchy order. This can be useful when you need it to respond in a certain way using transforms of the overriding parent.

    Category: Transform/Drivers

    **Description**: The Virtual Parent Component is used to make a Slot act as the child of another Slot without needing to be in the normal hierarchy order. This can be useful when you need it to respond in a certain way using transforms of the overriding parent.

The different ways to force this Slot (that has the Virtual Parent Component on it) to update its own transform, is to move it by grabbing it, using other components to move it, or using Flux.

You can use the provided local offset fields to then further position this slot from its virtual parent.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualParent"

    def __init__(self, override_parent: str | Slot | None = None, target_pos: str | IField[primitives.Float3] | None = None, target_rot: str | IField[primitives.FloatQ] | None = None, target_scl: str | IField[primitives.Float3] | None = None, local_position: primitives.Float3 | None = None, local_rotation: primitives.FloatQ | None = None, local_scale: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override_parent: Initial value for OverrideParent.
            target_pos: Initial value for _targetPos.
            target_rot: Initial value for _targetRot.
            target_scl: Initial value for _targetScl.
            local_position: Initial value for LocalPosition.
            local_rotation: Initial value for LocalRotation.
            local_scale: Initial value for LocalScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override_parent is not None:
            self.override_parent = override_parent
        if target_pos is not None:
            self.target_pos = target_pos
        if target_rot is not None:
            self.target_rot = target_rot
        if target_scl is not None:
            self.target_scl = target_scl
        if local_position is not None:
            self.local_position = local_position
        if local_rotation is not None:
            self.local_rotation = local_rotation
        if local_scale is not None:
            self.local_scale = local_scale

    @property
    def override_parent(self) -> str | None:
        """If not null, the slot that the object gets reparented to"""
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_parent.setter
    def override_parent(self, target: str | Slot | None) -> None:
        """Set the OverrideParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_pos(self) -> str | None:
        """Position to be driven by parent's position."""
        member = self.get_member("_targetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_pos.setter
    def target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _targetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_rot(self) -> str | None:
        """Rotation to be driven by parent's rotation."""
        member = self.get_member("_targetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_rot.setter
    def target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _targetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def target_scl(self) -> str | None:
        """Scale to be driven by parent's scale."""
        member = self.get_member("_targetScl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_scl.setter
    def target_scl(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _targetScl reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetScl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetScl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def local_position(self) -> primitives.Float3 | None:
        """Object's position relative to parent."""
        member = self.get_member("LocalPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_position.setter
    def local_position(self, value: primitives.Float3) -> None:
        """Set the LocalPosition field value."""
        member = self.get_member("LocalPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPosition", fields.FieldFloat3(value=value)
            )

    @property
    def local_rotation(self) -> primitives.FloatQ | None:
        """Object's rotation relative to parent."""
        member = self.get_member("LocalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation.setter
    def local_rotation(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotation field value."""
        member = self.get_member("LocalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def local_scale(self) -> primitives.Float3 | None:
        """Object's scale relative to parent."""
        member = self.get_member("LocalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_scale.setter
    def local_scale(self, value: primitives.Float3) -> None:
        """Set the LocalScale field value."""
        member = self.get_member("LocalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalScale", fields.FieldFloat3(value=value)
            )

