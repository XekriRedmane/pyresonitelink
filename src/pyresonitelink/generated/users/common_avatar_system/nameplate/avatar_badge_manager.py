"""Generated component: AvatarBadgeManager."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarBadgeManager(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarBadgeManager.

    Category: Users/Common Avatar System/Nameplate
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarBadgeManager"

    def __init__(self, badge_size: np.float32 | None = None, badge_separation: np.float32 | None = None, max_row_size: np.int32 | None = None, badges_root: str | Slot | None = None, badges_offset: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            badge_size: Initial value for BadgeSize.
            badge_separation: Initial value for BadgeSeparation.
            max_row_size: Initial value for MaxRowSize.
            badges_root: Initial value for _badgesRoot.
            badges_offset: Initial value for _badgesOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if badge_size is not None:
            self.badge_size = badge_size
        if badge_separation is not None:
            self.badge_separation = badge_separation
        if max_row_size is not None:
            self.max_row_size = max_row_size
        if badges_root is not None:
            self.badges_root = badges_root
        if badges_offset is not None:
            self.badges_offset = badges_offset

    @property
    def badge_size(self) -> np.float32 | None:
        """The BadgeSize field value."""
        member = self.get_member("BadgeSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @badge_size.setter
    def badge_size(self, value: np.float32) -> None:
        """Set the BadgeSize field value."""
        member = self.get_member("BadgeSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BadgeSize", fields.FieldFloat(value=value)
            )

    @property
    def badge_separation(self) -> np.float32 | None:
        """The BadgeSeparation field value."""
        member = self.get_member("BadgeSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @badge_separation.setter
    def badge_separation(self, value: np.float32) -> None:
        """Set the BadgeSeparation field value."""
        member = self.get_member("BadgeSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BadgeSeparation", fields.FieldFloat(value=value)
            )

    @property
    def max_row_size(self) -> np.int32 | None:
        """The MaxRowSize field value."""
        member = self.get_member("MaxRowSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_row_size.setter
    def max_row_size(self, value: np.int32) -> None:
        """Set the MaxRowSize field value."""
        member = self.get_member("MaxRowSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRowSize", fields.FieldInt(value=value)
            )

    @property
    def badges_root(self) -> str | None:
        """Target ID of the _badgesRoot reference (targets Slot)."""
        member = self.get_member("_badgesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @badges_root.setter
    def badges_root(self, target: str | Slot | None) -> None:
        """Set the _badgesRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_badgesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_badgesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def badges_offset(self) -> str | None:
        """Target ID of the _badgesOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_badgesOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @badges_offset.setter
    def badges_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _badgesOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_badgesOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_badgesOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

