"""Generated component: WorldCloseAction."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldCloseAction(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldCloseAction.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldCloseAction"

    def __init__(self, waiting_confirm: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            waiting_confirm: Initial value for WaitingConfirm.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if waiting_confirm is not None:
            self.waiting_confirm = waiting_confirm

    @property
    def action(self) -> members.FieldEnum | None:
        """The Action member."""
        member = self.get_member("Action")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @action.setter
    def action(self, value: members.FieldEnum) -> None:
        """Set the Action member."""
        self.set_member("Action", value)

    @property
    def waiting_confirm(self) -> primitives.Bool | None:
        """The WaitingConfirm field value."""
        member = self.get_member("WaitingConfirm")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @waiting_confirm.setter
    def waiting_confirm(self, value: primitives.Bool) -> None:
        """Set the WaitingConfirm field value."""
        member = self.get_member("WaitingConfirm")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WaitingConfirm", fields.FieldBool(value=value)
            )

