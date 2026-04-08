"""Generated component: PositionDeltaDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PositionDeltaDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PositionDeltaDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PositionDeltaDriver"

    def __init__(self, origin: str | Slot | None = None, target: str | Slot | None = None, normalized: bool | None = None, vector: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            origin: Initial value for Origin.
            target: Initial value for Target.
            normalized: Initial value for Normalized.
            vector: Initial value for Vector.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if origin is not None:
            self.origin = origin
        if target is not None:
            self.target = target
        if normalized is not None:
            self.normalized = normalized
        if vector is not None:
            self.vector = vector

    @property
    def origin(self) -> str | None:
        """Target ID of the Origin reference (targets Slot)."""
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @origin.setter
    def origin(self, target: str | Slot | None) -> None:
        """Set the Origin reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Origin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets Slot)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def vector_space(self) -> members.SyncObject | None:
        """The VectorSpace member."""
        member = self.get_member("VectorSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @vector_space.setter
    def vector_space(self, value: members.SyncObject) -> None:
        """Set the VectorSpace member."""
        self.set_member("VectorSpace", value)

    @property
    def normalized(self) -> bool | None:
        """The Normalized field value."""
        member = self.get_member("Normalized")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized.setter
    def normalized(self, value: bool) -> None:
        """Set the Normalized field value."""
        member = self.get_member("Normalized")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Normalized", fields.FieldBool(value=value)
            )

    @property
    def vector(self) -> str | None:
        """Target ID of the Vector reference (targets IField[primitives.Float3])."""
        member = self.get_member("Vector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @vector.setter
    def vector(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Vector reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Vector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Vector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

