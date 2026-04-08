"""Generated component: TextCountdownClock."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextCountdownClock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextCountdownClock.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextCountdownClock"

    def __init__(self, countdown_time: np.float64 | None = None, allow_negative: bool | None = None, text_target: str | IField[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            countdown_time: Initial value for CountdownTime.
            allow_negative: Initial value for AllowNegative.
            text_target: Initial value for TextTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if countdown_time is not None:
            self.countdown_time = countdown_time
        if allow_negative is not None:
            self.allow_negative = allow_negative
        if text_target is not None:
            self.text_target = text_target

    @property
    def countdown_time(self) -> np.float64 | None:
        """The CountdownTime field value."""
        member = self.get_member("CountdownTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @countdown_time.setter
    def countdown_time(self, value: np.float64) -> None:
        """Set the CountdownTime field value."""
        member = self.get_member("CountdownTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CountdownTime", fields.FieldDouble(value=value)
            )

    @property
    def allow_negative(self) -> bool | None:
        """The AllowNegative field value."""
        member = self.get_member("AllowNegative")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_negative.setter
    def allow_negative(self, value: bool) -> None:
        """Set the AllowNegative field value."""
        member = self.get_member("AllowNegative")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowNegative", fields.FieldBool(value=value)
            )

    @property
    def text_target(self) -> str | None:
        """Target ID of the TextTarget reference (targets IField[str])."""
        member = self.get_member("TextTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_target.setter
    def text_target(self, target: str | IField[str] | None) -> None:
        """Set the TextTarget reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TextTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

