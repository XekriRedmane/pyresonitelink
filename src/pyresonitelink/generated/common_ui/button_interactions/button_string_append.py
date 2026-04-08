"""Generated component: ButtonStringAppend."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonStringAppend(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonStringAppend.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonStringAppend"

    def __init__(self, target_string: str | IField[primitives.String] | None = None, append_string: primitives.String | None = None, append_in_front: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_string: Initial value for TargetString.
            append_string: Initial value for AppendString.
            append_in_front: Initial value for AppendInFront.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_string is not None:
            self.target_string = target_string
        if append_string is not None:
            self.append_string = append_string
        if append_in_front is not None:
            self.append_in_front = append_in_front

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
    def append_string(self) -> primitives.String | None:
        """The AppendString field value."""
        member = self.get_member("AppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @append_string.setter
    def append_string(self, value: primitives.String) -> None:
        """Set the AppendString field value."""
        member = self.get_member("AppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppendString", fields.FieldString(value=value)
            )

    @property
    def append_in_front(self) -> primitives.Bool | None:
        """The AppendInFront field value."""
        member = self.get_member("AppendInFront")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @append_in_front.setter
    def append_in_front(self, value: primitives.Bool) -> None:
        """Set the AppendInFront field value."""
        member = self.get_member("AppendInFront")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppendInFront", fields.FieldBool(value=value)
            )

