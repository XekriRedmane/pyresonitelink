"""Generated component: RandomValueInitializer_byte."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomValueInitializer_byte(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RandomValueInitializer_byte.

    Category: Utility/Random Value Initializer
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RandomValueInitializer_byte"

    def __init__(self, target: str | IField[primitives.Byte] | None = None, min: primitives.Byte | None = None, max: primitives.Byte | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            min: Initial value for Min.
            max: Initial value for Max.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Byte])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Byte] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Byte] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<byte>'),
            )

    @property
    def min(self) -> primitives.Byte | None:
        """The Min field value."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: primitives.Byte) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Min", fields.FieldByte(value=value)
            )

    @property
    def max(self) -> primitives.Byte | None:
        """The Max field value."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: primitives.Byte) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Max", fields.FieldByte(value=value)
            )

