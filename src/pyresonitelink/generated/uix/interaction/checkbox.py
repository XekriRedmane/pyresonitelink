"""Generated component: Checkbox."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Checkbox(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The Checkbox component is a UIX element used with a Button component to provide a toggling state whenever the button is pressed.

}}

    Category: UIX/Interaction

    Checkboxes are great for settings and options in your designs.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Checkbox"

    def __init__(self, state: primitives.Bool | None = None, target_state: str | IField[primitives.Bool] | None = None, check_visual: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state: Initial value for State.
            target_state: Initial value for TargetState.
            check_visual: Initial value for CheckVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state is not None:
            self.state = state
        if target_state is not None:
            self.target_state = target_state
        if check_visual is not None:
            self.check_visual = check_visual

    @property
    def state(self) -> primitives.Bool | None:
        """The current state of thie check box."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

    @property
    def target_state(self) -> str | None:
        """The Bool field to drive with the state of the checkbox."""
        member = self.get_member("TargetState")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_state.setter
    def target_state(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the TargetState reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetState")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetState",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def check_visual(self) -> str | None:
        """The Bool field controlling visibility of the visual to display when the checkbox is in the checked state."""
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_visual.setter
    def check_visual(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the CheckVisual reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheckVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

