"""Generated component: MultiUserAvatarAnchor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiUserAvatarAnchor(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.MultiUserAvatarAnchor.

    Category: Users/Common Avatar System/Anchors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.MultiUserAvatarAnchor"

    def __init__(self, anchor_point_snap: str | IPointSnappable | None = None, max_users: primitives.Int | None = None, min_distance: primitives.Float | None = None, template: str | IAvatarAnchor | None = None, anchors_root: str | Slot | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor_point_snap: Initial value for AnchorPointSnap.
            max_users: Initial value for MaxUsers.
            min_distance: Initial value for MinDistance.
            template: Initial value for Template.
            anchors_root: Initial value for AnchorsRoot.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor_point_snap is not None:
            self.anchor_point_snap = anchor_point_snap
        if max_users is not None:
            self.max_users = max_users
        if min_distance is not None:
            self.min_distance = min_distance
        if template is not None:
            self.template = template
        if anchors_root is not None:
            self.anchors_root = anchors_root
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch

    @property
    def anchor_point_snap(self) -> str | None:
        """Target ID of the AnchorPointSnap reference (targets IPointSnappable)."""
        member = self.get_member("AnchorPointSnap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor_point_snap.setter
    def anchor_point_snap(self, target: str | IPointSnappable | None) -> None:
        """Set the AnchorPointSnap reference by target ID or IPointSnappable instance."""
        target_id: str | None = target.id if isinstance(target, IPointSnappable) else target  # type: ignore[assignment]
        member = self.get_member("AnchorPointSnap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnchorPointSnap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPointSnappable'),
            )

    @property
    def max_users(self) -> primitives.Int | None:
        """The MaxUsers field value."""
        member = self.get_member("MaxUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_users.setter
    def max_users(self, value: primitives.Int) -> None:
        """Set the MaxUsers field value."""
        member = self.get_member("MaxUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxUsers", fields.FieldInt(value=value)
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """The MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def template(self) -> str | None:
        """Target ID of the Template reference (targets IAvatarAnchor)."""
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template.setter
    def template(self, target: str | IAvatarAnchor | None) -> None:
        """Set the Template reference by target ID or IAvatarAnchor instance."""
        target_id: str | None = target.id if isinstance(target, IAvatarAnchor) else target  # type: ignore[assignment]
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Template",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAvatarAnchor'),
            )

    @property
    def anchors_root(self) -> str | None:
        """Target ID of the AnchorsRoot reference (targets Slot)."""
        member = self.get_member("AnchorsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchors_root.setter
    def anchors_root(self, target: str | Slot | None) -> None:
        """Set the AnchorsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("AnchorsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AnchorsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

