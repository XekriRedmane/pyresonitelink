"""Generated component: UserInspector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.ino_destroy_undo import INoDestroyUndo
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInspector(GeneratedComponent, INoDestroyUndo, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserInspector.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInspector"

    def __init__(self, view_user: str | User | None = None, view_stream_group: primitives.UShort | None = None, current_user: str | User | None = None, current_stream_group: primitives.UShort | None = None, user_list_content_root: str | Slot | None = None, workers_content_root: str | Slot | None = None, user_text: str | Sync[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            view_user: Initial value for ViewUser.
            view_stream_group: Initial value for ViewStreamGroup.
            current_user: Initial value for _currentUser.
            current_stream_group: Initial value for _currentStreamGroup.
            user_list_content_root: Initial value for _userListContentRoot.
            workers_content_root: Initial value for _workersContentRoot.
            user_text: Initial value for _userText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if view_user is not None:
            self.view_user = view_user
        if view_stream_group is not None:
            self.view_stream_group = view_stream_group
        if current_user is not None:
            self.current_user = current_user
        if current_stream_group is not None:
            self.current_stream_group = current_stream_group
        if user_list_content_root is not None:
            self.user_list_content_root = user_list_content_root
        if workers_content_root is not None:
            self.workers_content_root = workers_content_root
        if user_text is not None:
            self.user_text = user_text

    @property
    def view_user(self) -> str | None:
        """Target ID of the ViewUser reference (targets User)."""
        member = self.get_member("ViewUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @view_user.setter
    def view_user(self, target: str | User | None) -> None:
        """Set the ViewUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("ViewUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ViewUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def view_group(self) -> members.FieldEnum | None:
        """The ViewGroup member."""
        member = self.get_member("ViewGroup")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @view_group.setter
    def view_group(self, value: members.FieldEnum) -> None:
        """Set the ViewGroup member."""
        self.set_member("ViewGroup", value)

    @property
    def view_stream_group(self) -> primitives.UShort | None:
        """The ViewStreamGroup field value."""
        member = self.get_member("ViewStreamGroup")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @view_stream_group.setter
    def view_stream_group(self, value: primitives.UShort) -> None:
        """Set the ViewStreamGroup field value."""
        member = self.get_member("ViewStreamGroup")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViewStreamGroup", fields.FieldUshort(value=value)
            )

    @property
    def current_user(self) -> str | None:
        """Target ID of the _currentUser reference (targets User)."""
        member = self.get_member("_currentUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_user.setter
    def current_user(self, target: str | User | None) -> None:
        """Set the _currentUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_currentUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def current_view_group(self) -> members.FieldEnum | None:
        """The _currentViewGroup member."""
        member = self.get_member("_currentViewGroup")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @current_view_group.setter
    def current_view_group(self, value: members.FieldEnum) -> None:
        """Set the _currentViewGroup member."""
        self.set_member("_currentViewGroup", value)

    @property
    def current_stream_group(self) -> primitives.UShort | None:
        """The _currentStreamGroup field value."""
        member = self.get_member("_currentStreamGroup")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_stream_group.setter
    def current_stream_group(self, value: primitives.UShort) -> None:
        """Set the _currentStreamGroup field value."""
        member = self.get_member("_currentStreamGroup")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_currentStreamGroup", fields.FieldUshort(value=value)
            )

    @property
    def user_list_content_root(self) -> str | None:
        """Target ID of the _userListContentRoot reference (targets Slot)."""
        member = self.get_member("_userListContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_list_content_root.setter
    def user_list_content_root(self, target: str | Slot | None) -> None:
        """Set the _userListContentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_userListContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userListContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def workers_content_root(self) -> str | None:
        """Target ID of the _workersContentRoot reference (targets Slot)."""
        member = self.get_member("_workersContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @workers_content_root.setter
    def workers_content_root(self, target: str | Slot | None) -> None:
        """Set the _workersContentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_workersContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_workersContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def user_text(self) -> str | None:
        """Target ID of the _userText reference (targets Sync[primitives.String])."""
        member = self.get_member("_userText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_text.setter
    def user_text(self, target: str | Sync[primitives.String] | None) -> None:
        """Set the _userText reference by target ID or Sync[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_userText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<string>'),
            )

