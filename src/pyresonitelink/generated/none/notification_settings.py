"""Generated component: NotificationSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.notification_type import NotificationType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class NotificationSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NotificationSettings"

    def __init__(self, user_online: primitives.Bool | None = None, user_online_on_another_build: primitives.Bool | None = None, user_sociable: NotificationType | str | None = None, message: NotificationType | str | None = None, invite: NotificationType | str | None = None, contact_request: NotificationType | str | None = None, invite_request: NotificationType | str | None = None, contact_session_started: NotificationType | str | None = None, public_session_started: NotificationType | str | None = None, user_join_and_leave: NotificationType | str | None = None, permission_changed: NotificationType | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_online: Initial value for UserOnline.
            user_online_on_another_build: Initial value for UserOnlineOnAnotherBuild.
            user_sociable: Initial value for UserSociable.
            message: Initial value for Message.
            invite: Initial value for Invite.
            contact_request: Initial value for ContactRequest.
            invite_request: Initial value for InviteRequest.
            contact_session_started: Initial value for ContactSessionStarted.
            public_session_started: Initial value for PublicSessionStarted.
            user_join_and_leave: Initial value for UserJoinAndLeave.
            permission_changed: Initial value for PermissionChanged.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_online is not None:
            self.user_online = user_online
        if user_online_on_another_build is not None:
            self.user_online_on_another_build = user_online_on_another_build
        if user_sociable is not None:
            self.user_sociable = user_sociable
        if message is not None:
            self.message = message
        if invite is not None:
            self.invite = invite
        if contact_request is not None:
            self.contact_request = contact_request
        if invite_request is not None:
            self.invite_request = invite_request
        if contact_session_started is not None:
            self.contact_session_started = contact_session_started
        if public_session_started is not None:
            self.public_session_started = public_session_started
        if user_join_and_leave is not None:
            self.user_join_and_leave = user_join_and_leave
        if permission_changed is not None:
            self.permission_changed = permission_changed

    @property
    def user_online(self) -> primitives.Bool | None:
        """Whether to show notifications for users coming online."""
        member = self.get_member("UserOnline")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_online.setter
    def user_online(self, value: primitives.Bool) -> None:
        """Set the UserOnline field value."""
        member = self.get_member("UserOnline")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserOnline", fields.FieldBool(value=value)
            )

    @property
    def user_online_on_another_build(self) -> primitives.Bool | None:
        """Whether to show notifications for users coming online while they are on a different version than you."""
        member = self.get_member("UserOnlineOnAnotherBuild")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_online_on_another_build.setter
    def user_online_on_another_build(self, value: primitives.Bool) -> None:
        """Set the UserOnlineOnAnotherBuild field value."""
        member = self.get_member("UserOnlineOnAnotherBuild")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserOnlineOnAnotherBuild", fields.FieldBool(value=value)
            )

    @property
    def user_sociable(self) -> NotificationType | None:
        """How to handle notifications for users turning to sociable mode."""
        member = self.get_member("UserSociable")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @user_sociable.setter
    def user_sociable(self, value: NotificationType | str) -> None:
        """Set UserSociable. How to handle notifications for users turning to sociable mode."""
        member = self.get_member("UserSociable")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "UserSociable",
                members.FieldEnum(value=str(value)),
            )

    @property
    def message(self) -> NotificationType | None:
        """How to handle notifications for messages."""
        member = self.get_member("Message")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @message.setter
    def message(self, value: NotificationType | str) -> None:
        """Set Message. How to handle notifications for messages."""
        member = self.get_member("Message")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Message",
                members.FieldEnum(value=str(value)),
            )

    @property
    def invite(self) -> NotificationType | None:
        """How to handle notifications for invites."""
        member = self.get_member("Invite")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @invite.setter
    def invite(self, value: NotificationType | str) -> None:
        """Set Invite. How to handle notifications for invites."""
        member = self.get_member("Invite")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Invite",
                members.FieldEnum(value=str(value)),
            )

    @property
    def contact_request(self) -> NotificationType | None:
        """How to handle notifications for contact requests."""
        member = self.get_member("ContactRequest")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @contact_request.setter
    def contact_request(self, value: NotificationType | str) -> None:
        """Set ContactRequest. How to handle notifications for contact requests."""
        member = self.get_member("ContactRequest")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ContactRequest",
                members.FieldEnum(value=str(value)),
            )

    @property
    def invite_request(self) -> NotificationType | None:
        """How to handle notifications for invite requests."""
        member = self.get_member("InviteRequest")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @invite_request.setter
    def invite_request(self, value: NotificationType | str) -> None:
        """Set InviteRequest. How to handle notifications for invite requests."""
        member = self.get_member("InviteRequest")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "InviteRequest",
                members.FieldEnum(value=str(value)),
            )

    @property
    def contact_session_started(self) -> NotificationType | None:
        """How to handle notifications for contact session startings."""
        member = self.get_member("ContactSessionStarted")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @contact_session_started.setter
    def contact_session_started(self, value: NotificationType | str) -> None:
        """Set ContactSessionStarted. How to handle notifications for contact session startings."""
        member = self.get_member("ContactSessionStarted")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ContactSessionStarted",
                members.FieldEnum(value=str(value)),
            )

    @property
    def public_session_started(self) -> NotificationType | None:
        """How to handle notifications for public session startings."""
        member = self.get_member("PublicSessionStarted")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @public_session_started.setter
    def public_session_started(self, value: NotificationType | str) -> None:
        """Set PublicSessionStarted. How to handle notifications for public session startings."""
        member = self.get_member("PublicSessionStarted")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PublicSessionStarted",
                members.FieldEnum(value=str(value)),
            )

    @property
    def user_join_and_leave(self) -> NotificationType | None:
        """How to handle notifications for users joining and leaving sessions."""
        member = self.get_member("UserJoinAndLeave")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @user_join_and_leave.setter
    def user_join_and_leave(self, value: NotificationType | str) -> None:
        """Set UserJoinAndLeave. How to handle notifications for users joining and leaving sessions."""
        member = self.get_member("UserJoinAndLeave")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "UserJoinAndLeave",
                members.FieldEnum(value=str(value)),
            )

    @property
    def permission_changed(self) -> NotificationType | None:
        """How to handle notifications for your permissions changing in a world."""
        member = self.get_member("PermissionChanged")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NotificationType(member.value)
        return None

    @permission_changed.setter
    def permission_changed(self, value: NotificationType | str) -> None:
        """Set PermissionChanged. How to handle notifications for your permissions changing in a world."""
        member = self.get_member("PermissionChanged")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PermissionChanged",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

