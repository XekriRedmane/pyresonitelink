"""Generated component: NotificationPanel."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.userspace_radiant_dash import UserspaceRadiantDash
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NotificationPanel(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NotificationPanel.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NotificationPanel"

    def __init__(self, display_duration: primitives.Float | None = None, dash: str | UserspaceRadiantDash | None = None, canvas: str | Canvas | None = None, notification_clip: str | IAssetProvider[AudioClip] | None = None, contact_request_clip: str | IAssetProvider[AudioClip] | None = None, invite_clip: str | IAssetProvider[AudioClip] | None = None, invite_request_clip: str | IAssetProvider[AudioClip] | None = None, sociable_clip: str | IAssetProvider[AudioClip] | None = None, user_join_clip: str | IAssetProvider[AudioClip] | None = None, user_leave_clip: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_duration: Initial value for DisplayDuration.
            dash: Initial value for Dash.
            canvas: Initial value for _canvas.
            notification_clip: Initial value for _notificationClip.
            contact_request_clip: Initial value for _contactRequestClip.
            invite_clip: Initial value for _inviteClip.
            invite_request_clip: Initial value for _inviteRequestClip.
            sociable_clip: Initial value for _sociableClip.
            user_join_clip: Initial value for _userJoinClip.
            user_leave_clip: Initial value for _userLeaveClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_duration is not None:
            self.display_duration = display_duration
        if dash is not None:
            self.dash = dash
        if canvas is not None:
            self.canvas = canvas
        if notification_clip is not None:
            self.notification_clip = notification_clip
        if contact_request_clip is not None:
            self.contact_request_clip = contact_request_clip
        if invite_clip is not None:
            self.invite_clip = invite_clip
        if invite_request_clip is not None:
            self.invite_request_clip = invite_request_clip
        if sociable_clip is not None:
            self.sociable_clip = sociable_clip
        if user_join_clip is not None:
            self.user_join_clip = user_join_clip
        if user_leave_clip is not None:
            self.user_leave_clip = user_leave_clip

    @property
    def display_duration(self) -> primitives.Float | None:
        """The DisplayDuration field value."""
        member = self.get_member("DisplayDuration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_duration.setter
    def display_duration(self, value: primitives.Float) -> None:
        """Set the DisplayDuration field value."""
        member = self.get_member("DisplayDuration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayDuration", fields.FieldFloat(value=value)
            )

    @property
    def dash(self) -> str | None:
        """Target ID of the Dash reference (targets UserspaceRadiantDash)."""
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | UserspaceRadiantDash | None) -> None:
        """Set the Dash reference by target ID or UserspaceRadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, UserspaceRadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserspaceRadiantDash'),
            )

    @property
    def canvas(self) -> str | None:
        """Target ID of the _canvas reference (targets Canvas)."""
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the _canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def notification_clip(self) -> str | None:
        """Target ID of the _notificationClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_notificationClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @notification_clip.setter
    def notification_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _notificationClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_notificationClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_notificationClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def contact_request_clip(self) -> str | None:
        """Target ID of the _contactRequestClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_contactRequestClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @contact_request_clip.setter
    def contact_request_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _contactRequestClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_contactRequestClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contactRequestClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def invite_clip(self) -> str | None:
        """Target ID of the _inviteClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_inviteClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @invite_clip.setter
    def invite_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _inviteClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_inviteClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inviteClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def invite_request_clip(self) -> str | None:
        """Target ID of the _inviteRequestClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_inviteRequestClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @invite_request_clip.setter
    def invite_request_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _inviteRequestClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_inviteRequestClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inviteRequestClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def sociable_clip(self) -> str | None:
        """Target ID of the _sociableClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_sociableClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sociable_clip.setter
    def sociable_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _sociableClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_sociableClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sociableClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def user_join_clip(self) -> str | None:
        """Target ID of the _userJoinClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_userJoinClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_join_clip.setter
    def user_join_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _userJoinClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_userJoinClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userJoinClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def user_leave_clip(self) -> str | None:
        """Target ID of the _userLeaveClip reference (targets IAssetProvider[AudioClip])."""
        member = self.get_member("_userLeaveClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_leave_clip.setter
    def user_leave_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _userLeaveClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_userLeaveClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userLeaveClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

