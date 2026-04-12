"""Generated component: OrientAtPoint."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OrientAtPoint(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Orient At Point component makes particles in a particle system orient at a point in a specified transform space.

    Category: Rendering/Particle System/Modules

    used with Photon Dust systems.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.OrientAtPoint"

    def __init__(self, target_point: primitives.Float3 | None = None, up: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_point: Initial value for TargetPoint.
            up: Initial value for Up.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_point is not None:
            self.target_point = target_point
        if up is not None:
            self.up = up

    @property
    def point_space(self) -> members.SyncObject | None:
        """The tranform space ``TargetPoint`` and ``Up`` are in."""
        member = self.get_member("PointSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @point_space.setter
    def point_space(self, value: members.SyncObject) -> None:
        """Set PointSpace. The tranform space ``TargetPoint`` and ``Up`` are in."""
        self.set_member("PointSpace", value)

    @property
    def target_point(self) -> primitives.Float3 | None:
        """The point that particles should point at."""
        member = self.get_member("TargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_point.setter
    def target_point(self, value: primitives.Float3) -> None:
        """Set the TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def up(self) -> primitives.Float3 | None:
        """The direction that should be up locally for each particle."""
        member = self.get_member("Up")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up.setter
    def up(self, value: primitives.Float3) -> None:
        """Set the Up field value."""
        member = self.get_member("Up")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Up", fields.FieldFloat3(value=value)
            )

