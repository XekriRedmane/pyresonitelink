"""Generated component: LinearMapper1D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LinearMapper1D(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Linear Mapper 1D is a component that live maps one range to another, allowing for a reverse mapping of the target range value back to the source range when it is written to.

    Category: Transform/Drivers

    Can be used to keep the fullness of two different containers the same
    percentage wise based on purely the stored units and maximum capacity.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LinearMapper1D"

    def __init__(self, source: str | IValue[primitives.Float] | None = None, target: str | IField[primitives.Float] | None = None, source_min: primitives.Float | None = None, source_max: primitives.Float | None = None, target_min: primitives.Float | None = None, target_max: primitives.Float | None = None, allow_reverse_mapping: primitives.Bool | None = None, clamp: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            source_min: Initial value for SourceMin.
            source_max: Initial value for SourceMax.
            target_min: Initial value for TargetMin.
            target_max: Initial value for TargetMax.
            allow_reverse_mapping: Initial value for AllowReverseMapping.
            clamp: Initial value for Clamp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if source_min is not None:
            self.source_min = source_min
        if source_max is not None:
            self.source_max = source_max
        if target_min is not None:
            self.target_min = target_min
        if target_max is not None:
            self.target_max = target_max
        if allow_reverse_mapping is not None:
            self.allow_reverse_mapping = allow_reverse_mapping
        if clamp is not None:
            self.clamp = clamp

    @property
    def source(self) -> str | None:
        """The value to map from ``SourceMin`` to ``SourceMax`` using ``Target``."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IValue[primitives.Float] | None) -> None:
        """Set the Source reference by target ID or IValue[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<float>'),
            )

    @property
    def target(self) -> str | None:
        """The value to map from ``TargetMin`` to ``TargetMax`` using ``Source``."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def source_min(self) -> primitives.Float | None:
        """The minimum of the range of the ``Source`` value."""
        member = self.get_member("SourceMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_min.setter
    def source_min(self, value: primitives.Float) -> None:
        """Set the SourceMin field value."""
        member = self.get_member("SourceMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceMin", fields.FieldFloat(value=value)
            )

    @property
    def source_max(self) -> primitives.Float | None:
        """The maximum of the range of the ``Source`` value."""
        member = self.get_member("SourceMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_max.setter
    def source_max(self, value: primitives.Float) -> None:
        """Set the SourceMax field value."""
        member = self.get_member("SourceMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceMax", fields.FieldFloat(value=value)
            )

    @property
    def target_min(self) -> primitives.Float | None:
        """The minimum of the range of the ``Target`` value."""
        member = self.get_member("TargetMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_min.setter
    def target_min(self, value: primitives.Float) -> None:
        """Set the TargetMin field value."""
        member = self.get_member("TargetMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetMin", fields.FieldFloat(value=value)
            )

    @property
    def target_max(self) -> primitives.Float | None:
        """The maximum of the range of the ``Target`` value."""
        member = self.get_member("TargetMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_max.setter
    def target_max(self, value: primitives.Float) -> None:
        """Set the TargetMax field value."""
        member = self.get_member("TargetMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetMax", fields.FieldFloat(value=value)
            )

    @property
    def allow_reverse_mapping(self) -> primitives.Bool | None:
        """Allow ``Target`` to map it's value to ``Source``'s ranged value when written to. See write backs."""
        member = self.get_member("AllowReverseMapping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_reverse_mapping.setter
    def allow_reverse_mapping(self, value: primitives.Bool) -> None:
        """Set the AllowReverseMapping field value."""
        member = self.get_member("AllowReverseMapping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowReverseMapping", fields.FieldBool(value=value)
            )

    @property
    def clamp(self) -> primitives.Bool | None:
        """Whether to prevent ``Source`` and ``Target`` from going outside their defined ranges."""
        member = self.get_member("Clamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp.setter
    def clamp(self, value: primitives.Bool) -> None:
        """Set the Clamp field value."""
        member = self.get_member("Clamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Clamp", fields.FieldBool(value=value)
            )

