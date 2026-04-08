"""Generated component: SphereEmitter+LegacyTransformConverter."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sphere_emitter import SphereEmitter
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereEmitter+LegacyTransformConverter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.SphereEmitter+LegacyTransformConverter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SphereEmitter+LegacyTransformConverter"

    def __init__(self, transform: str | IField[primitives.Float3x3] | None = None, emitter: str | SphereEmitter | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            transform: Initial value for Transform.
            emitter: Initial value for Emitter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if transform is not None:
            self.transform = transform
        if emitter is not None:
            self.emitter = emitter

    @property
    def transform(self) -> str | None:
        """Target ID of the Transform reference (targets IField[primitives.Float3x3])."""
        member = self.get_member("Transform")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @transform.setter
    def transform(self, target: str | IField[primitives.Float3x3] | None) -> None:
        """Set the Transform reference by target ID or IField[primitives.Float3x3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Transform")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Transform",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3x3>'),
            )

    @property
    def emitter(self) -> str | None:
        """Target ID of the Emitter reference (targets SphereEmitter)."""
        member = self.get_member("Emitter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emitter.setter
    def emitter(self, target: str | SphereEmitter | None) -> None:
        """Set the Emitter reference by target ID or SphereEmitter instance."""
        target_id: str | None = target.id if isinstance(target, SphereEmitter) else target  # type: ignore[assignment]
        member = self.get_member("Emitter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Emitter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.SphereEmitter'),
            )

