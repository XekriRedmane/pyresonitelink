"""Generated component: Checkbox."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Checkbox(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Checkbox.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Checkbox"

    def __init__(self, state: bool | None = None, target_state: str | IField[bool] | None = None, check_visual: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
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
    def state(self) -> bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: bool) -> None:
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
        """Target ID of the TargetState reference (targets IField[bool])."""
        member = self.get_member("TargetState")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_state.setter
    def target_state(self, target: str | IField[bool] | None) -> None:
        """Set the TargetState reference by target ID or IField[bool] instance."""
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
        """Target ID of the CheckVisual reference (targets IField[bool])."""
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_visual.setter
    def check_visual(self, target: str | IField[bool] | None) -> None:
        """Set the CheckVisual reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheckVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

