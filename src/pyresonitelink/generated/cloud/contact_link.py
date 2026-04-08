"""Generated component: ContactLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContactLink(GeneratedComponent, ITouchable, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ContactLink.

    Category: Cloud
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContactLink"

    def __init__(self, user_id: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_id: Initial value for UserId.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_id is not None:
            self.user_id = user_id

    @property
    def user_id(self) -> str | None:
        """The UserId field value."""
        member = self.get_member("UserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_id.setter
    def user_id(self, value: str) -> None:
        """Set the UserId field value."""
        member = self.get_member("UserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserId", fields.FieldString(value=value)
            )

