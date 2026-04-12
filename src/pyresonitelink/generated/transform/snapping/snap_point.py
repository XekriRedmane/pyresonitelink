"""Generated component: SnapPoint."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapPoint(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """A snap point is a component that when called by another component always returns the point of the slot it is on (0,0,0). Usually this is used in components like the Multi User Avatar Anchor Component to determine where to place the anchors upon clicking (click point is used in such case). This component will take a given point by another component and return the position the slot is on, acting as a nullifier of incoming data.

The functionality of this component is internal, and cannot be used by ProtoFlux to snap points using in game code.

    Category: Transform/Snapping

    Used as an anchor point generator in the Multi User Avatar Anchor
    Component and drawing tools.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapPoint"

    def __init__(self, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def snap_parent(self) -> str | None:
        """Where to put slots if the component is being used for slot placement."""
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

