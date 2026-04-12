"""Generated component: SnapSphere."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapSphere(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """A snap sphere is a component that is able to generate a point in a sphere shape along the outer shell when given a point by another component. Usually this is used in components like the Multi User Avatar Anchor Component to determine where to place the anchors upon clicking (click point is used in such case)

How the snapper determines a point is as such:
# the snapper component will reduce the distance from the provided point to the center of the snapper to a distance of 1.
# It then takes the number and aligns it to the closest point on the shape. since this is a sphere snapper, it doesn't need this step.
# the snapper will then multiply the normalized point by the snapper's size in all 3 axes, and then return the result.

The functionality of this component is internal, and cannot be used by ProtoFlux to snap points using in game code.

    Category: Transform/Snapping

    Used as an anchor point generator in the Multi User Avatar Anchor
    Component and drawing tools.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapSphere"

    def __init__(self, radius: primitives.Float | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def radius(self) -> primitives.Float | None:
        """the radius of the sphere"""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def snap_parent(self) -> str | None:
        """where the objects to be snapped should go, if they are slots."""
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @snap_parent.setter
    def snap_parent(self, target: str | Slot | None) -> None:
        """Set the SnapParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SnapParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

