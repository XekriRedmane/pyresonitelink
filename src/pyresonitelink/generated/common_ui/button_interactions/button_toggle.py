"""Generated component: ButtonToggle."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonToggle(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonToggle.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonToggle"

    def __init__(self, target_value: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_value: Initial value for TargetValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_value is not None:
            self.target_value = target_value

    @property
    def target_value(self) -> str | None:
        """Target ID of the TargetValue reference (targets IField[bool])."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[bool] | None) -> None:
        """Set the TargetValue reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

