"""Generated component: ButtonStringErase."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonStringErase(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonStringErase.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonStringErase"

    def __init__(self, target_string: str | IField[primitives.String] | None = None, count: primitives.Int | None = None, erase_from_beginning: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_string: Initial value for TargetString.
            count: Initial value for Count.
            erase_from_beginning: Initial value for EraseFromBeginning.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_string is not None:
            self.target_string = target_string
        if count is not None:
            self.count = count
        if erase_from_beginning is not None:
            self.erase_from_beginning = erase_from_beginning

    @property
    def target_string(self) -> str | None:
        """Target ID of the TargetString reference (targets IField[primitives.String])."""
        member = self.get_member("TargetString")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_string.setter
    def target_string(self, target: str | IField[primitives.String] | None) -> None:
        """Set the TargetString reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetString")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetString",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def count(self) -> primitives.Int | None:
        """The Count field value."""
        member = self.get_member("Count")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @count.setter
    def count(self, value: primitives.Int) -> None:
        """Set the Count field value."""
        member = self.get_member("Count")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Count", fields.FieldInt(value=value)
            )

    @property
    def erase_from_beginning(self) -> primitives.Bool | None:
        """The EraseFromBeginning field value."""
        member = self.get_member("EraseFromBeginning")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @erase_from_beginning.setter
    def erase_from_beginning(self, value: primitives.Bool) -> None:
        """Set the EraseFromBeginning field value."""
        member = self.get_member("EraseFromBeginning")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EraseFromBeginning", fields.FieldBool(value=value)
            )

