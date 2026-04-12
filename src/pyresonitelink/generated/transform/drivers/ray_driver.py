"""Generated component: RayDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RayDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """A ray driver is a component that takes a start origin and a direction and drives point A and B via a RayCast, keeping the distance between the two below MaxDistance.

    Category: Transform/Drivers

    * LaserPointer Tool with RayDriver by ProbablePrime

    **Related Components**: RaycastDriver component
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RayDriver"

    def __init__(self, max_distance: primitives.Float | None = None, point_a: str | Sync[primitives.Float3] | None = None, point_b: str | Sync[primitives.Float3] | None = None, local_origin: primitives.Float3 | None = None, local_direction: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_distance: Initial value for MaxDistance.
            point_a: Initial value for PointA.
            point_b: Initial value for PointB.
            local_origin: Initial value for LocalOrigin.
            local_direction: Initial value for LocalDirection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_distance is not None:
            self.max_distance = max_distance
        if point_a is not None:
            self.point_a = point_a
        if point_b is not None:
            self.point_b = point_b
        if local_origin is not None:
            self.local_origin = local_origin
        if local_direction is not None:
            self.local_direction = local_direction

    @property
    def max_distance(self) -> primitives.Float | None:
        """the max distance that A and B can be from each other"""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def point_a(self) -> str | None:
        """what to drive with the local space start position of the Raycast"""
        member = self.get_member("PointA")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_a.setter
    def point_a(self, target: str | Sync[primitives.Float3] | None) -> None:
        """Set the PointA reference by target ID or Sync[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("PointA")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PointA",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float3>'),
            )

    @property
    def point_b(self) -> str | None:
        """what to drive with the local space end point of the raycast"""
        member = self.get_member("PointB")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_b.setter
    def point_b(self, target: str | Sync[primitives.Float3] | None) -> None:
        """Set the PointB reference by target ID or Sync[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("PointB")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PointB",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float3>'),
            )

    @property
    def local_origin(self) -> primitives.Float3 | None:
        """the local space start point of the raycast"""
        member = self.get_member("LocalOrigin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_origin.setter
    def local_origin(self, value: primitives.Float3) -> None:
        """Set the LocalOrigin field value."""
        member = self.get_member("LocalOrigin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalOrigin", fields.FieldFloat3(value=value)
            )

    @property
    def local_direction(self) -> primitives.Float3 | None:
        """the direction in local space to fire the raycast in."""
        member = self.get_member("LocalDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_direction.setter
    def local_direction(self, value: primitives.Float3) -> None:
        """Set the LocalDirection field value."""
        member = self.get_member("LocalDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalDirection", fields.FieldFloat3(value=value)
            )

