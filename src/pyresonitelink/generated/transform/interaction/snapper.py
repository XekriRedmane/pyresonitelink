"""Generated component: Snapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Snapper(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """The Snapper component allows a slot to parent to Snap Target slots.

    Category: Transform/Interaction

    **Behavior**: Allows the slot in which this component resides in to snap to a Snap Target in another slot. The SnapTargetWhitelist allows you to specify a list of SnapTargets that this component will link to in case you want to limit its snapability. The keywords list allows you to provide a list of words which the Snap Target can use to filter for specific types of snappers.

It is important to have this in a slot shared with a Grabbable component in the root link of the object you wish to snap. Snapped components will become children of the snap target.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Snapper"

    def __init__(self, use_bounding_box_center: primitives.Bool | None = None, snap_check_radius: primitives.Float | None = None, check_static_colliders: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_bounding_box_center: Initial value for UseBoundingBoxCenter.
            snap_check_radius: Initial value for SnapCheckRadius.
            check_static_colliders: Initial value for CheckStaticColliders.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_bounding_box_center is not None:
            self.use_bounding_box_center = use_bounding_box_center
        if snap_check_radius is not None:
            self.snap_check_radius = snap_check_radius
        if check_static_colliders is not None:
            self.check_static_colliders = check_static_colliders

    @property
    def use_bounding_box_center(self) -> primitives.Bool | None:
        """The UseBoundingBoxCenter field value."""
        member = self.get_member("UseBoundingBoxCenter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_bounding_box_center.setter
    def use_bounding_box_center(self, value: primitives.Bool) -> None:
        """Set the UseBoundingBoxCenter field value."""
        member = self.get_member("UseBoundingBoxCenter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseBoundingBoxCenter", fields.FieldBool(value=value)
            )

    @property
    def snap_check_radius(self) -> primitives.Float | None:
        """The SnapCheckRadius field value."""
        member = self.get_member("SnapCheckRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_check_radius.setter
    def snap_check_radius(self, value: primitives.Float) -> None:
        """Set the SnapCheckRadius field value."""
        member = self.get_member("SnapCheckRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapCheckRadius", fields.FieldFloat(value=value)
            )

    @property
    def check_static_colliders(self) -> primitives.Bool | None:
        """Allows the Snapper to look for colliders that are set to Static rather then Trigger."""
        member = self.get_member("CheckStaticColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @check_static_colliders.setter
    def check_static_colliders(self, value: primitives.Bool) -> None:
        """Set the CheckStaticColliders field value."""
        member = self.get_member("CheckStaticColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckStaticColliders", fields.FieldBool(value=value)
            )

    @property
    def snap_target_whitelist(self) -> members.SyncList | None:
        """List of Snap Targets that the slot can attach to"""
        member = self.get_member("SnapTargetWhitelist")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snap_target_whitelist.setter
    def snap_target_whitelist(self, value: members.SyncList) -> None:
        """Set SnapTargetWhitelist. List of Snap Targets that the slot can attach to"""
        self.set_member("SnapTargetWhitelist", value)

    @property
    def keywords(self) -> members.SyncList | None:
        """List of keywords to match against a corresponding Snap Targets. Can have multiple keywords to snap to multiple Snap Targets"""
        member = self.get_member("Keywords")
        if isinstance(member, members.SyncList):
            return member
        return None

    @keywords.setter
    def keywords(self, value: members.SyncList) -> None:
        """Set Keywords. List of keywords to match against a corresponding Snap Targets. Can have multiple keywords to snap to multiple Snap Targets"""
        self.set_member("Keywords", value)

