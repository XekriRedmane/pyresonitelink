"""Generated component: UserInspectorItem."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.expander import Expander
from pyresonitelink.generated._types.text_expand_indicator import TextExpandIndicator
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInspectorItem(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserInspectorItem component is used to display user items of the User Inspector.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInspectorItem"

    def __init__(self, user: str | User | None = None, user_name_text: str | Text | None = None, expander: str | Expander | None = None, expander_indicator: str | TextExpandIndicator | None = None, child_container: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for _user.
            user_name_text: Initial value for _userNameText.
            expander: Initial value for _expander.
            expander_indicator: Initial value for _expanderIndicator.
            child_container: Initial value for _childContainer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if user_name_text is not None:
            self.user_name_text = user_name_text
        if expander is not None:
            self.expander = expander
        if expander_indicator is not None:
            self.expander_indicator = expander_indicator
        if child_container is not None:
            self.child_container = child_container

    @property
    def user(self) -> str | None:
        """The user this item points to."""
        member = self.get_member("_user")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the _user reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_user")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_user",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def user_name_text(self) -> str | None:
        """The text field to display the user's name."""
        member = self.get_member("_userNameText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_name_text.setter
    def user_name_text(self, target: str | Text | None) -> None:
        """Set the _userNameText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_userNameText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userNameText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def expander(self) -> str | None:
        """The component used to expand items under the user like stream groups."""
        member = self.get_member("_expander")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expander.setter
    def expander(self, target: str | Expander | None) -> None:
        """Set the _expander reference by target ID or Expander instance."""
        target_id: str | None = target.id if isinstance(target, Expander) else target  # type: ignore[assignment]
        member = self.get_member("_expander")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expander",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Expander'),
            )

    @property
    def expander_indicator(self) -> str | None:
        """The indicator component used to show the expand/collapse arrow."""
        member = self.get_member("_expanderIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expander_indicator.setter
    def expander_indicator(self, target: str | TextExpandIndicator | None) -> None:
        """Set the _expanderIndicator reference by target ID or TextExpandIndicator instance."""
        target_id: str | None = target.id if isinstance(target, TextExpandIndicator) else target  # type: ignore[assignment]
        member = self.get_member("_expanderIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expanderIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextExpandIndicator'),
            )

    @property
    def child_container(self) -> str | None:
        """The slot to display child items of this user item."""
        member = self.get_member("_childContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @child_container.setter
    def child_container(self, target: str | Slot | None) -> None:
        """Set the _childContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_childContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_childContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

