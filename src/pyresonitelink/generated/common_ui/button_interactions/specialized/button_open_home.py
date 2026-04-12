"""Generated component: ButtonOpenHome."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonOpenHome(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonOpenHome component, when pressed with an IButton, takes the User to their favorite home world (usually the Resonite Cloud Home by default). There is an optional string input for a group home.

}}

    Category: Common UI/Button Interactions/Specialized

    This is an easy way to set up a way to get to your favorite home faster.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonOpenHome"

    def __init__(self, group_owner_id: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            group_owner_id: Initial value for GroupOwnerId.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if group_owner_id is not None:
            self.group_owner_id = group_owner_id

    @property
    def group_owner_id(self) -> primitives.String | None:
        """An optional string input for a group home."""
        member = self.get_member("GroupOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_owner_id.setter
    def group_owner_id(self, value: primitives.String) -> None:
        """Set the GroupOwnerId field value."""
        member = self.get_member("GroupOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupOwnerId", fields.FieldString(value=value)
            )

