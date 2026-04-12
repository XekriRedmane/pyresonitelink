"""Generated component: GrabbableReceiverSurface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable_receiver import IGrabbableReceiver
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableReceiverSurface(GeneratedComponent, IGrabbableReceiver, IGrabbableReparentBlock, IWorldEventReceiver):
    """The GrabbableReceiverSurface component allows you to set up an object so that Grabbable objects snap to its surface when a user releases the Grabbable object within range of it. For a volume based alternative, see Grabbable Parenter.

Add Component Path: Transform > Interaction > GrabbableReceiverSurface.
= Fields =
}}

= Behavior =
When a GrabbableReceiverSurface is setup on an object, it will become visible to Grabbable objects when they are released from a user's grab. When this occurs the Surface will carry out some checks and if these pass the object will snap to the GrabbableReceiverSurface. If the ``ParentPlaced`` checkbox is enable the Grabbable will be parented to the surface or the slot specified in ``OverrideParent``

    Category: Transform/Interaction

    **Explanation of the Checks**: These are a little complicated but if you want to fully understand what happens it is provided.

When a user is holding a Grabbable object and lets go (releases it):
# The Grabbable object will look around it in its vicinity using a sphere collider based on the Object's bounding box plus a radius defined on the User's Hand. The hand radius is defined by a sphere made from a Bounding box of all the released objects.
# If this collider overlaps with any objects which have GrabbableRecieverSurface attached to them then the Grabbable will perform some checks on each surface.
# First it asks the Surface to check its distance from the Grabbable object.
## The distance check first calculates if a Raycast from the released object towards the surface would hit in the directions specified in the component. 
## If the Raycast would hit a distance is then calculated.
## This distance varies depending on the directions specified in the component's properties.
##* For example, placing an object on top of a cube from above has a shorter distance to the top of the Cube than the bottom of a cube because the distance from above the cube to the bottom face of the cube is greater.
# If this distance is to great as specified in the component's properties a second check using the released object's bounding box corners is also computed
# After both distance checks a final distance value is provided.
# The Grabbable then selects the surface with the smallest distance and tells the Surface to receive it.
# The Surface will then position the Grabbable upon the surface using an Animation of a ``Tween Time`` value is set.
# The Surface will then parent the Grabbable to itself or the ``OverrideParent`` location if the ``ParentPlaced`` checkbox is checked.

= Examples =

ProbablePrime's tutorial on GrabbleReceiverSurface:

9IZI3ui-RLY

= Frequently Asked Questions =

    **Can objects which are not grabbed be received?**: No, this component only works with Grabbable objects which are released by a user.

    **Can this be used with objects that are not Grabbable?**: No, It cannot be used with objects that do not have a Grabbable component.

= See Also =
* Grabbable for what this receives. 
* Grabbable Parenter For a volume alternative
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableReceiverSurface"

    def __init__(self, parent_placed: primitives.Bool | None = None, override_parent: str | Slot | None = None, tween_time: primitives.Float | None = None, max_distance: primitives.Float | None = None, offset: primitives.Float | None = None, check_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_placed: Initial value for ParentPlaced.
            override_parent: Initial value for OverrideParent.
            tween_time: Initial value for TweenTime.
            max_distance: Initial value for MaxDistance.
            offset: Initial value for Offset.
            check_offset: Initial value for CheckOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_placed is not None:
            self.parent_placed = parent_placed
        if override_parent is not None:
            self.override_parent = override_parent
        if tween_time is not None:
            self.tween_time = tween_time
        if max_distance is not None:
            self.max_distance = max_distance
        if offset is not None:
            self.offset = offset
        if check_offset is not None:
            self.check_offset = check_offset

    @property
    def parent_placed(self) -> primitives.Bool | None:
        """Whether the Grabbable object gets reparented to this object's Slot or the Slot specified in OverrideParent."""
        member = self.get_member("ParentPlaced")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_placed.setter
    def parent_placed(self, value: primitives.Bool) -> None:
        """Set the ParentPlaced field value."""
        member = self.get_member("ParentPlaced")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentPlaced", fields.FieldBool(value=value)
            )

    @property
    def override_parent(self) -> str | None:
        """If not null, the slot that the Grabbable object gets reparented to, if ParentPlaced is true."""
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_parent.setter
    def override_parent(self, target: str | Slot | None) -> None:
        """Set the OverrideParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def tween_time(self) -> primitives.Float | None:
        """The amount of time in seconds for the animation effect when the object snaps to the surface."""
        member = self.get_member("TweenTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tween_time.setter
    def tween_time(self, value: primitives.Float) -> None:
        """Set the TweenTime field value."""
        member = self.get_member("TweenTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TweenTime", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """How far away in meters something released gets grabbed."""
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
    def offset(self) -> primitives.Float | None:
        """The distance from the surface that the Grabbable object will stop at."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def check_offset(self) -> primitives.Float | None:
        """How far away from the surface that the object ignores before it starts looking for released objects."""
        member = self.get_member("CheckOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @check_offset.setter
    def check_offset(self, value: primitives.Float) -> None:
        """Set the CheckOffset field value."""
        member = self.get_member("CheckOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckOffset", fields.FieldFloat(value=value)
            )

    @property
    def directions(self) -> members.SyncList | None:
        """List of directions a Grabbable object can be received from."""
        member = self.get_member("Directions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @directions.setter
    def directions(self, value: members.SyncList) -> None:
        """Set Directions. List of directions a Grabbable object can be received from."""
        self.set_member("Directions", value)

    @property
    def tag_filter(self) -> members.SyncObject | None:
        """A filter that limits what can be picked up by this surface."""
        member = self.get_member("TagFilter")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tag_filter.setter
    def tag_filter(self, value: members.SyncObject) -> None:
        """Set TagFilter. A filter that limits what can be picked up by this surface."""
        self.set_member("TagFilter", value)

