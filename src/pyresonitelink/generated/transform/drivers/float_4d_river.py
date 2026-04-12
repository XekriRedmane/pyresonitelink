"""Generated component: Float4Driver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Float4Driver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Float4Driver component can be used to drive a foat4 value, based on an X, Y, Z and a W value.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Float4Driver"

    def __init__(self, x: str | Sync[primitives.Float] | None = None, y: str | Sync[primitives.Float] | None = None, z: str | Sync[primitives.Float] | None = None, w: str | Sync[primitives.Float] | None = None, target: str | IField[primitives.Float4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x: Initial value for X.
            y: Initial value for Y.
            z: Initial value for Z.
            w: Initial value for W.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if w is not None:
            self.w = w
        if target is not None:
            self.target = target

    @property
    def x(self) -> str | None:
        """The field that holds the X value for the float4. If null, the X component of the float4 will be 0."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | Sync[primitives.Float] | None) -> None:
        """Set the X reference by target ID or Sync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

    @property
    def y(self) -> str | None:
        """The field that holds the Y value for the float4. If null, the Y component of the float4 will be 0."""
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y.setter
    def y(self, target: str | Sync[primitives.Float] | None) -> None:
        """Set the Y reference by target ID or Sync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Y",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

    @property
    def z(self) -> str | None:
        """The field that holds the Z value for the float4. If null, the Z component of the float4 will be 0."""
        member = self.get_member("Z")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z.setter
    def z(self, target: str | Sync[primitives.Float] | None) -> None:
        """Set the Z reference by target ID or Sync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("Z")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Z",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

    @property
    def w(self) -> str | None:
        """The field that holds the W value for the float4. If null, the W component of the float4 will be 0."""
        member = self.get_member("W")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @w.setter
    def w(self, target: str | Sync[primitives.Float] | None) -> None:
        """Set the W reference by target ID or Sync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("W")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "W",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

    @property
    def target(self) -> str | None:
        """The field that is driven to the constructed float4."""
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

