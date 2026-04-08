"""Generated component: NotificationSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class NotificationSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.NotificationSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NotificationSettings"

    def __init__(self, user_online: bool | None = None, user_online_on_another_build: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_online: Initial value for UserOnline.
            user_online_on_another_build: Initial value for UserOnlineOnAnotherBuild.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_online is not None:
            self.user_online = user_online
        if user_online_on_another_build is not None:
            self.user_online_on_another_build = user_online_on_another_build

    @property
    def user_online(self) -> bool | None:
        """The UserOnline field value."""
        member = self.get_member("UserOnline")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_online.setter
    def user_online(self, value: bool) -> None:
        """Set the UserOnline field value."""
        member = self.get_member("UserOnline")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserOnline", fields.FieldBool(value=value)
            )

    @property
    def user_online_on_another_build(self) -> bool | None:
        """The UserOnlineOnAnotherBuild field value."""
        member = self.get_member("UserOnlineOnAnotherBuild")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_online_on_another_build.setter
    def user_online_on_another_build(self, value: bool) -> None:
        """Set the UserOnlineOnAnotherBuild field value."""
        member = self.get_member("UserOnlineOnAnotherBuild")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserOnlineOnAnotherBuild", fields.FieldBool(value=value)
            )

    @property
    def user_sociable(self) -> members.FieldEnum | None:
        """The UserSociable member."""
        member = self.get_member("UserSociable")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @user_sociable.setter
    def user_sociable(self, value: members.FieldEnum) -> None:
        """Set the UserSociable member."""
        self.set_member("UserSociable", value)

    @property
    def message(self) -> members.FieldEnum | None:
        """The Message member."""
        member = self.get_member("Message")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @message.setter
    def message(self, value: members.FieldEnum) -> None:
        """Set the Message member."""
        self.set_member("Message", value)

    @property
    def invite(self) -> members.FieldEnum | None:
        """The Invite member."""
        member = self.get_member("Invite")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @invite.setter
    def invite(self, value: members.FieldEnum) -> None:
        """Set the Invite member."""
        self.set_member("Invite", value)

    @property
    def contact_request(self) -> members.FieldEnum | None:
        """The ContactRequest member."""
        member = self.get_member("ContactRequest")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @contact_request.setter
    def contact_request(self, value: members.FieldEnum) -> None:
        """Set the ContactRequest member."""
        self.set_member("ContactRequest", value)

    @property
    def invite_request(self) -> members.FieldEnum | None:
        """The InviteRequest member."""
        member = self.get_member("InviteRequest")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @invite_request.setter
    def invite_request(self, value: members.FieldEnum) -> None:
        """Set the InviteRequest member."""
        self.set_member("InviteRequest", value)

    @property
    def contact_session_started(self) -> members.FieldEnum | None:
        """The ContactSessionStarted member."""
        member = self.get_member("ContactSessionStarted")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @contact_session_started.setter
    def contact_session_started(self, value: members.FieldEnum) -> None:
        """Set the ContactSessionStarted member."""
        self.set_member("ContactSessionStarted", value)

    @property
    def public_session_started(self) -> members.FieldEnum | None:
        """The PublicSessionStarted member."""
        member = self.get_member("PublicSessionStarted")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @public_session_started.setter
    def public_session_started(self, value: members.FieldEnum) -> None:
        """Set the PublicSessionStarted member."""
        self.set_member("PublicSessionStarted", value)

    @property
    def user_join_and_leave(self) -> members.FieldEnum | None:
        """The UserJoinAndLeave member."""
        member = self.get_member("UserJoinAndLeave")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @user_join_and_leave.setter
    def user_join_and_leave(self, value: members.FieldEnum) -> None:
        """Set the UserJoinAndLeave member."""
        self.set_member("UserJoinAndLeave", value)

    @property
    def permission_changed(self) -> members.FieldEnum | None:
        """The PermissionChanged member."""
        member = self.get_member("PermissionChanged")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @permission_changed.setter
    def permission_changed(self, value: members.FieldEnum) -> None:
        """Set the PermissionChanged member."""
        self.set_member("PermissionChanged", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

