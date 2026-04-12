"""Generated component: UserInspector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.view import View
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.ino_destroy_undo import INoDestroyUndo
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInspector(GeneratedComponent, INoDestroyUndo, IDeveloperInterface, IWorldEventReceiver):
    """The User Inspector component is better described on it's page, User Inspector.

    See User Inspector.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInspector"

    def __init__(self, view_user: str | User | None = None, view_group: View | str | None = None, view_stream_group: primitives.UShort | None = None, current_user: str | User | None = None, current_view_group: View | str | None = None, current_stream_group: primitives.UShort | None = None, user_list_content_root: str | Slot | None = None, workers_content_root: str | Slot | None = None, user_text: str | Sync[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            view_user: Initial value for ViewUser.
            view_group: Initial value for ViewGroup.
            view_stream_group: Initial value for ViewStreamGroup.
            current_user: Initial value for _currentUser.
            current_view_group: Initial value for _currentViewGroup.
            current_stream_group: Initial value for _currentStreamGroup.
            user_list_content_root: Initial value for _userListContentRoot.
            workers_content_root: Initial value for _workersContentRoot.
            user_text: Initial value for _userText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if view_user is not None:
            self.view_user = view_user
        if view_group is not None:
            self.view_group = view_group
        if view_stream_group is not None:
            self.view_stream_group = view_stream_group
        if current_user is not None:
            self.current_user = current_user
        if current_view_group is not None:
            self.current_view_group = current_view_group
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
        """The user this inspector is currently updating through."""
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
    def view_group(self) -> View | None:
        """What kind of information group this is inspecting."""
        member = self.get_member("ViewGroup")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return View(member.value)
        return None

    @view_group.setter
    def view_group(self, value: View | str) -> None:
        """Set ViewGroup. What kind of information group this is inspecting."""
        member = self.get_member("ViewGroup")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ViewGroup",
                members.FieldEnum(value=str(value)),
            )

    @property
    def view_stream_group(self) -> primitives.UShort | None:
        """The kind of value stream group this is viewing."""
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
        """The current user this is viewing."""
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
    def current_view_group(self) -> View | None:
        """What kind of information group this is currently inspecting."""
        member = self.get_member("_currentViewGroup")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return View(member.value)
        return None

    @current_view_group.setter
    def current_view_group(self, value: View | str) -> None:
        """Set _currentViewGroup. What kind of information group this is currently inspecting."""
        member = self.get_member("_currentViewGroup")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_currentViewGroup",
                members.FieldEnum(value=str(value)),
            )

    @property
    def current_stream_group(self) -> primitives.UShort | None:
        """The kind of value stream group this is currently viewing."""
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
        """The slot to place user stream/properties content when viewing a user."""
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
        """The slot to place user worker content when viewing a user."""
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
        """The string field that stores text on the user being viewed."""
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

