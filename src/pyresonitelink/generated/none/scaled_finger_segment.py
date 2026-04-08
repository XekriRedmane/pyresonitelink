"""Generated component: ScaledFingerSegment."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaledFingerSegment(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaledFingerSegment.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaledFingerSegment"

    def __init__(self, scale: str | IField[primitives.Float3] | None = None, offset: str | IField[primitives.Float3] | None = None, next_joint: str | Slot | None = None, width: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale: Initial value for _scale.
            offset: Initial value for _offset.
            next_joint: Initial value for _nextJoint.
            width: Initial value for Width.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale is not None:
            self.scale = scale
        if offset is not None:
            self.offset = offset
        if next_joint is not None:
            self.next_joint = next_joint
        if width is not None:
            self.width = width

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
    def next_joint(self) -> str | None:
        """Target ID of the _nextJoint reference (targets Slot)."""
        member = self.get_member("_nextJoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next_joint.setter
    def next_joint(self, target: str | Slot | None) -> None:
        """Set the _nextJoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_nextJoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nextJoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def body_node(self) -> members.FieldEnum | None:
        """The _bodyNode member."""
        member = self.get_member("_bodyNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @body_node.setter
    def body_node(self, value: members.FieldEnum) -> None:
        """Set the _bodyNode member."""
        self.set_member("_bodyNode", value)

    @property
    def width(self) -> primitives.Float | None:
        """The Width field value."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

