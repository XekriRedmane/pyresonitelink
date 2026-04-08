"""Generated component: LinearMapper4D."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LinearMapper4D(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LinearMapper4D.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LinearMapper4D"

    def __init__(self, source: str | IValue[np.float32] | None = None, target: str | IField[primitives.Float4] | None = None, source_min: np.float32 | None = None, source_max: np.float32 | None = None, target_min: primitives.Float4 | None = None, target_max: primitives.Float4 | None = None, allow_reverse_mapping: bool | None = None, clamp: bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Source reference (targets IValue[np.float32])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IValue[np.float32] | None) -> None:
        """Set the Source reference by target ID or IValue[np.float32] instance."""
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
        """Target ID of the Target reference (targets IField[primitives.Float4])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float4] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float4>'),
            )

    @property
    def source_min(self) -> np.float32 | None:
        """The SourceMin field value."""
        member = self.get_member("SourceMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_min.setter
    def source_min(self, value: np.float32) -> None:
        """Set the SourceMin field value."""
        member = self.get_member("SourceMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceMin", fields.FieldFloat(value=value)
            )

    @property
    def source_max(self) -> np.float32 | None:
        """The SourceMax field value."""
        member = self.get_member("SourceMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_max.setter
    def source_max(self, value: np.float32) -> None:
        """Set the SourceMax field value."""
        member = self.get_member("SourceMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceMax", fields.FieldFloat(value=value)
            )

    @property
    def target_min(self) -> primitives.Float4 | None:
        """The TargetMin field value."""
        member = self.get_member("TargetMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_min.setter
    def target_min(self, value: primitives.Float4) -> None:
        """Set the TargetMin field value."""
        member = self.get_member("TargetMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetMin", fields.FieldFloat4(value=value)
            )

    @property
    def target_max(self) -> primitives.Float4 | None:
        """The TargetMax field value."""
        member = self.get_member("TargetMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_max.setter
    def target_max(self, value: primitives.Float4) -> None:
        """Set the TargetMax field value."""
        member = self.get_member("TargetMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetMax", fields.FieldFloat4(value=value)
            )

    @property
    def allow_reverse_mapping(self) -> bool | None:
        """The AllowReverseMapping field value."""
        member = self.get_member("AllowReverseMapping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_reverse_mapping.setter
    def allow_reverse_mapping(self, value: bool) -> None:
        """Set the AllowReverseMapping field value."""
        member = self.get_member("AllowReverseMapping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowReverseMapping", fields.FieldBool(value=value)
            )

    @property
    def clamp(self) -> bool | None:
        """The Clamp field value."""
        member = self.get_member("Clamp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp.setter
    def clamp(self, value: bool) -> None:
        """Set the Clamp field value."""
        member = self.get_member("Clamp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Clamp", fields.FieldBool(value=value)
            )

