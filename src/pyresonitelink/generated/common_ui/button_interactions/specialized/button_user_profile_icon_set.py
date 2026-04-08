"""Generated component: ButtonUserProfileIconSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonUserProfileIconSet(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonUserProfileIconSet.

    Category: Common UI/Button Interactions/Specialized
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonUserProfileIconSet"

    def __init__(self, is_updating: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_updating: Initial value for IsUpdating.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_updating is not None:
            self.is_updating = is_updating

    @property
    def is_updating(self) -> bool | None:
        """The IsUpdating field value."""
        member = self.get_member("IsUpdating")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_updating.setter
    def is_updating(self, value: bool) -> None:
        """Set the IsUpdating field value."""
        member = self.get_member("IsUpdating")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsUpdating", fields.FieldBool(value=value)
            )

