"""Generated component: LegacyRotation3DAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyRotation3DAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LegacyRotation3DAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyRotation3DAdapter"

    def __init__(self, target: str | IField[primitives.Float3] | None = None, value: primitives.Float3 | None = None, particle_mesh: str | AssetRef[Mesh] | None = None, using_stretch: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            value: Initial value for Value.
            particle_mesh: Initial value for ParticleMesh.
            using_stretch: Initial value for UsingStretch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if value is not None:
            self.value = value
        if particle_mesh is not None:
            self.particle_mesh = particle_mesh
        if using_stretch is not None:
            self.using_stretch = using_stretch

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Float3])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def value(self) -> primitives.Float3 | None:
        """The Value field value."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: primitives.Float3) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Value", fields.FieldFloat3(value=value)
            )

    @property
    def particle_mesh(self) -> str | None:
        """Target ID of the ParticleMesh reference (targets AssetRef[Mesh])."""
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @particle_mesh.setter
    def particle_mesh(self, target: str | AssetRef[Mesh] | None) -> None:
        """Set the ParticleMesh reference by target ID or AssetRef[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("ParticleMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParticleMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def using_stretch(self) -> str | None:
        """Target ID of the UsingStretch reference (targets IField[primitives.Bool])."""
        member = self.get_member("UsingStretch")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @using_stretch.setter
    def using_stretch(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the UsingStretch reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UsingStretch")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UsingStretch",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

