"""Generated component: ButtonValueCycle."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonValueCycle(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonValueCycle<>.

    Category: Common UI/Button Interactions

    Parameterize with a value type::

        ButtonValueCycle[primitives.Float]
        ButtonValueCycle[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonValueCycle<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonValueCycle<>"

    def __init__(self, target_value: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the TargetValue reference (targets IField[T])."""
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_value.setter
    def target_value(self, target: str | IField[T] | None) -> None:
        """Set the TargetValue reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def values(self) -> members.SyncList | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncList):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncList) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

