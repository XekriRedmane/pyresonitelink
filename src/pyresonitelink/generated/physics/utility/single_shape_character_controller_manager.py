"""Generated component: SingleShapeCharacterControllerManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SingleShapeCharacterControllerManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SingleShapeCharacterControllerManager component is used by locomotions to change the shape of a Capsule Collider based on a user's standing height and current height.

    Category: Physics/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SingleShapeCharacterControllerManager"

    def __init__(self, use_user_head_height_when_available: primitives.Bool | None = None, head_height_offset: primitives.Float | None = None, crouch_target_width: primitives.Float | None = None, crouch_start: primitives.Float | None = None, crouch_end: primitives.Float | None = None, default_height: primitives.Float | None = None, default_width: primitives.Float | None = None, root_at_bottom: primitives.Bool | None = None, target_height: str | IField[primitives.Float] | None = None, target_width: str | IField[primitives.Float] | None = None, target_offset: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_user_head_height_when_available: Initial value for UseUserHeadHeightWhenAvailable.
            head_height_offset: Initial value for HeadHeightOffset.
            crouch_target_width: Initial value for CrouchTargetWidth.
            crouch_start: Initial value for CrouchStart.
            crouch_end: Initial value for CrouchEnd.
            default_height: Initial value for DefaultHeight.
            default_width: Initial value for DefaultWidth.
            root_at_bottom: Initial value for RootAtBottom.
            target_height: Initial value for TargetHeight.
            target_width: Initial value for TargetWidth.
            target_offset: Initial value for TargetOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_user_head_height_when_available is not None:
            self.use_user_head_height_when_available = use_user_head_height_when_available
        if head_height_offset is not None:
            self.head_height_offset = head_height_offset
        if crouch_target_width is not None:
            self.crouch_target_width = crouch_target_width
        if crouch_start is not None:
            self.crouch_start = crouch_start
        if crouch_end is not None:
            self.crouch_end = crouch_end
        if default_height is not None:
            self.default_height = default_height
        if default_width is not None:
            self.default_width = default_width
        if root_at_bottom is not None:
            self.root_at_bottom = root_at_bottom
        if target_height is not None:
            self.target_height = target_height
        if target_width is not None:
            self.target_width = target_width
        if target_offset is not None:
            self.target_offset = target_offset

    @property
    def use_user_head_height_when_available(self) -> primitives.Bool | None:
        """Whether to use the user's head height to do calculations when possible."""
        member = self.get_member("UseUserHeadHeightWhenAvailable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_user_head_height_when_available.setter
    def use_user_head_height_when_available(self, value: primitives.Bool) -> None:
        """Set the UseUserHeadHeightWhenAvailable field value."""
        member = self.get_member("UseUserHeadHeightWhenAvailable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseUserHeadHeightWhenAvailable", fields.FieldBool(value=value)
            )

    @property
    def head_height_offset(self) -> primitives.Float | None:
        """How much to add/subtract from the user's head to make the top of the capsule."""
        member = self.get_member("HeadHeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_height_offset.setter
    def head_height_offset(self, value: primitives.Float) -> None:
        """Set the HeadHeightOffset field value."""
        member = self.get_member("HeadHeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadHeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def crouch_target_width(self) -> primitives.Float | None:
        """How wide the capsule should become when crouching."""
        member = self.get_member("CrouchTargetWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_target_width.setter
    def crouch_target_width(self, value: primitives.Float) -> None:
        """Set the CrouchTargetWidth field value."""
        member = self.get_member("CrouchTargetWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchTargetWidth", fields.FieldFloat(value=value)
            )

    @property
    def crouch_start(self) -> primitives.Float | None:
        """The maximum height the user's head has to be for them to be crouching."""
        member = self.get_member("CrouchStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_start.setter
    def crouch_start(self, value: primitives.Float) -> None:
        """Set the CrouchStart field value."""
        member = self.get_member("CrouchStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchStart", fields.FieldFloat(value=value)
            )

    @property
    def crouch_end(self) -> primitives.Float | None:
        """The minimum height the user's head has to be for them to be crouching."""
        member = self.get_member("CrouchEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_end.setter
    def crouch_end(self, value: primitives.Float) -> None:
        """Set the CrouchEnd field value."""
        member = self.get_member("CrouchEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchEnd", fields.FieldFloat(value=value)
            )

    @property
    def default_height(self) -> primitives.Float | None:
        """The user's default head height."""
        member = self.get_member("DefaultHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_height.setter
    def default_height(self, value: primitives.Float) -> None:
        """Set the DefaultHeight field value."""
        member = self.get_member("DefaultHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultHeight", fields.FieldFloat(value=value)
            )

    @property
    def default_width(self) -> primitives.Float | None:
        """The collider's width when standing."""
        member = self.get_member("DefaultWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_width.setter
    def default_width(self, value: primitives.Float) -> None:
        """Set the DefaultWidth field value."""
        member = self.get_member("DefaultWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultWidth", fields.FieldFloat(value=value)
            )

    @property
    def root_at_bottom(self) -> primitives.Bool | None:
        """Whether the bottom end of the capsule should be at the slot rather than the slot being at the middle."""
        member = self.get_member("RootAtBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_at_bottom.setter
    def root_at_bottom(self, value: primitives.Bool) -> None:
        """Set the RootAtBottom field value."""
        member = self.get_member("RootAtBottom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RootAtBottom", fields.FieldBool(value=value)
            )

    @property
    def target_height(self) -> str | None:
        """The slot to drive to influence the capsule collider's height."""
        member = self.get_member("TargetHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_height.setter
    def target_height(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetHeight reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def target_width(self) -> str | None:
        """The slot to drive to influence the capsule collider's radius."""
        member = self.get_member("TargetWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_width.setter
    def target_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TargetWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def target_offset(self) -> str | None:
        """The slot to drive to influence the capsule collider's center offset."""
        member = self.get_member("TargetOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_offset.setter
    def target_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the TargetOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

