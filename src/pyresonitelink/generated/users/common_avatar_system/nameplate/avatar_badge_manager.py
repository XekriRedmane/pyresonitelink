"""Generated component: AvatarBadgeManager."""

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
    """The AvatarBadgeManager component initializes the user's badges under the ``Badges Root`` slot.

}}

    Category: Users/Common Avatar System/Nameplate

    This is used to help with organizing badges on a user's Nameplate,
    including custom badges. The user badge manager does this internally to
    help assign badges accordingly. If an avatar contains this component
    when equipped, the user's default badges will be hidden for those who
    have custom nameplates enabled.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarBadgeManager"

    def __init__(self, badge_size: primitives.Float | None = None, badge_separation: primitives.Float | None = None, max_row_size: primitives.Int | None = None, badges_root: str | Slot | None = None, badges_offset: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
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
    def badge_size(self) -> primitives.Float | None:
        """The size of the generated badges in local space."""
        member = self.get_member("BadgeSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @badge_size.setter
    def badge_size(self, value: primitives.Float) -> None:
        """Set the BadgeSize field value."""
        member = self.get_member("BadgeSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BadgeSize", fields.FieldFloat(value=value)
            )

    @property
    def badge_separation(self) -> primitives.Float | None:
        """The separation in meters between the badges in local space"""
        member = self.get_member("BadgeSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @badge_separation.setter
    def badge_separation(self, value: primitives.Float) -> None:
        """Set the BadgeSeparation field value."""
        member = self.get_member("BadgeSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BadgeSeparation", fields.FieldFloat(value=value)
            )

    @property
    def max_row_size(self) -> primitives.Int | None:
        """The maximum amount of badges on one row before moving to the next."""
        member = self.get_member("MaxRowSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_row_size.setter
    def max_row_size(self, value: primitives.Int) -> None:
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
        """The slot to put the badges under."""
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
        """The position of the ``_badgesRoot`` slot, which is used to move the badges away from the user's name tag and keep them positioned properly."""
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

