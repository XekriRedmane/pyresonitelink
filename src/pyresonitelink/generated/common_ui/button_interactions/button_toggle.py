"""Generated component: ButtonToggle."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonToggle(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonValueToggle component can be used to make an IButton that switches a boolean value between ``true`` and ``false`` every time the button is pressed.

    Category: Common UI/Button Interactions

    To function, the component simply needs to be attached to a slot that
    also has a button component attached to it. From then on, pressing that
    button will activate the ButtonToggle, making it toggle its
    ``TargetValue`` from true to false or the other way round.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonToggle"

    def __init__(self, target_value: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The boolean to invert whenever the button is pressed."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the TargetValue reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

