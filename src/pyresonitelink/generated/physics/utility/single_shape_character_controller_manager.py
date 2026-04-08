"""Generated component: SingleShapeCharacterControllerManager."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SingleShapeCharacterControllerManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SingleShapeCharacterControllerManager.

    Category: Physics/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SingleShapeCharacterControllerManager"

    def __init__(self, use_user_head_height_when_available: bool | None = None, head_height_offset: np.float32 | None = None, crouch_target_width: np.float32 | None = None, crouch_start: np.float32 | None = None, crouch_end: np.float32 | None = None, default_height: np.float32 | None = None, default_width: np.float32 | None = None, root_at_bottom: bool | None = None, target_height: str | IField[np.float32] | None = None, target_width: str | IField[np.float32] | None = None, target_offset: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
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
    def use_user_head_height_when_available(self) -> bool | None:
        """The UseUserHeadHeightWhenAvailable field value."""
        member = self.get_member("UseUserHeadHeightWhenAvailable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_user_head_height_when_available.setter
    def use_user_head_height_when_available(self, value: bool) -> None:
        """Set the UseUserHeadHeightWhenAvailable field value."""
        member = self.get_member("UseUserHeadHeightWhenAvailable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseUserHeadHeightWhenAvailable", fields.FieldBool(value=value)
            )

    @property
    def head_height_offset(self) -> np.float32 | None:
        """The HeadHeightOffset field value."""
        member = self.get_member("HeadHeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_height_offset.setter
    def head_height_offset(self, value: np.float32) -> None:
        """Set the HeadHeightOffset field value."""
        member = self.get_member("HeadHeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadHeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def crouch_target_width(self) -> np.float32 | None:
        """The CrouchTargetWidth field value."""
        member = self.get_member("CrouchTargetWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_target_width.setter
    def crouch_target_width(self, value: np.float32) -> None:
        """Set the CrouchTargetWidth field value."""
        member = self.get_member("CrouchTargetWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchTargetWidth", fields.FieldFloat(value=value)
            )

    @property
    def crouch_start(self) -> np.float32 | None:
        """The CrouchStart field value."""
        member = self.get_member("CrouchStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_start.setter
    def crouch_start(self, value: np.float32) -> None:
        """Set the CrouchStart field value."""
        member = self.get_member("CrouchStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchStart", fields.FieldFloat(value=value)
            )

    @property
    def crouch_end(self) -> np.float32 | None:
        """The CrouchEnd field value."""
        member = self.get_member("CrouchEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crouch_end.setter
    def crouch_end(self, value: np.float32) -> None:
        """Set the CrouchEnd field value."""
        member = self.get_member("CrouchEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrouchEnd", fields.FieldFloat(value=value)
            )

    @property
    def default_height(self) -> np.float32 | None:
        """The DefaultHeight field value."""
        member = self.get_member("DefaultHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_height.setter
    def default_height(self, value: np.float32) -> None:
        """Set the DefaultHeight field value."""
        member = self.get_member("DefaultHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultHeight", fields.FieldFloat(value=value)
            )

    @property
    def default_width(self) -> np.float32 | None:
        """The DefaultWidth field value."""
        member = self.get_member("DefaultWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_width.setter
    def default_width(self, value: np.float32) -> None:
        """Set the DefaultWidth field value."""
        member = self.get_member("DefaultWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultWidth", fields.FieldFloat(value=value)
            )

    @property
    def root_at_bottom(self) -> bool | None:
        """The RootAtBottom field value."""
        member = self.get_member("RootAtBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_at_bottom.setter
    def root_at_bottom(self, value: bool) -> None:
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
        """Target ID of the TargetHeight reference (targets IField[np.float32])."""
        member = self.get_member("TargetHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_height.setter
    def target_height(self, target: str | IField[np.float32] | None) -> None:
        """Set the TargetHeight reference by target ID or IField[np.float32] instance."""
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
        """Target ID of the TargetWidth reference (targets IField[np.float32])."""
        member = self.get_member("TargetWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_width.setter
    def target_width(self, target: str | IField[np.float32] | None) -> None:
        """Set the TargetWidth reference by target ID or IField[np.float32] instance."""
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
        """Target ID of the TargetOffset reference (targets IField[primitives.Float3])."""
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

