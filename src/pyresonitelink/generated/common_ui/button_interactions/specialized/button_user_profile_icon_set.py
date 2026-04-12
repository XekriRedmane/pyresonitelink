"""Generated component: ButtonUserProfileIconSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonUserProfileIconSet(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonUserProfileIconSet component only works in Userspace. This is the component that handles the setting of a user profile icon in the game.

    Category: Common UI/Button Interactions/Specialized

    Put this beside a button component on an slot or facet and press the
    button to set your profile icon via the button.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonUserProfileIconSet"

    def __init__(self, is_updating: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_updating: Initial value for IsUpdating.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_updating is not None:
            self.is_updating = is_updating

    @property
    def is_updating(self) -> primitives.Bool | None:
        """Whether or not the component is sending to the cloud your new icon url and/or asset."""
        member = self.get_member("IsUpdating")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_updating.setter
    def is_updating(self, value: primitives.Bool) -> None:
        """Set the IsUpdating field value."""
        member = self.get_member("IsUpdating")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsUpdating", fields.FieldBool(value=value)
            )

