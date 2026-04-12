"""Generated component: WorldCloseAction."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.close_action import CloseAction
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldCloseAction(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The WorldCloseAction component is used to handle the leaving of a world after the user confirms leaving. This component only works on user space.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldCloseAction"

    def __init__(self, action: CloseAction | str | None = None, waiting_confirm: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            action: Initial value for Action.
            waiting_confirm: Initial value for WaitingConfirm.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if action is not None:
            self.action = action
        if waiting_confirm is not None:
            self.waiting_confirm = waiting_confirm

    @property
    def action(self) -> CloseAction | None:
        """The kind of action this Button Events recieving Component is doing to a world."""
        member = self.get_member("Action")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CloseAction(member.value)
        return None

    @action.setter
    def action(self, value: CloseAction | str) -> None:
        """Set Action. The kind of action this Button Events recieving Component is doing to a world."""
        member = self.get_member("Action")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Action",
                members.FieldEnum(value=str(value)),
            )

    @property
    def waiting_confirm(self) -> primitives.Bool | None:
        """Whether the game is waiting on confirmation via double click, which is 2 clicks within a 2 second time frame."""
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

