"""Generated component: LegacyAudioOutputIgnoreReverbAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAudioOutputIgnoreReverbAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyAudioOutputIgnoreReverbAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyAudioOutputIgnoreReverbAdapter"

    def __init__(self, target: str | IField[primitives.Bool] | None = None, value: primitives.Bool | None = None, spatialize: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value: Initial value for Value.
            spatialize: Initial value for Spatialize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value is not None:
            self.value = value
        if spatialize is not None:
            self.spatialize = spatialize

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Bool])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def value(self) -> primitives.Bool | None:
        """The Value field value."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: primitives.Bool) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Value", fields.FieldBool(value=value)
            )

    @property
    def spatialize(self) -> str | None:
        """Target ID of the Spatialize reference (targets IField[primitives.Bool])."""
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatialize.setter
    def spatialize(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Spatialize reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Spatialize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

