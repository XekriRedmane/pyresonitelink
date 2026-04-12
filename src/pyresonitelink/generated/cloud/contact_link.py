"""Generated component: ContactLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContactLink(GeneratedComponent, ITouchable, IButtonPressReceiver, IWorldEventReceiver):
    """The ContactLink component allows a slot to be clicked on by a user to open their Dash Menu to the Contacts Menu of a specific user (by using a provided ``UserId``).

    Category: Cloud

    Add the ContactLink component to an object, clicking on that object will
    open up the Contacts Menu and will show the User page of the user
    defined in the ``UserId`` field. When you attach it, your own User ID
    will be automatically filled in. For UIX, a button component is required
    to click and take the user to that contact page. Otherwise, a collider
    works just fine without a button for this component to work.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContactLink"

    def __init__(self, user_id: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_id: Initial value for UserId.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_id is not None:
            self.user_id = user_id

    @property
    def user_id(self) -> primitives.String | None:
        """The User ID of the User whose contact page will be opened upon clicking the object."""
        member = self.get_member("UserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_id.setter
    def user_id(self, value: primitives.String) -> None:
        """Set the UserId field value."""
        member = self.get_member("UserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserId", fields.FieldString(value=value)
            )

