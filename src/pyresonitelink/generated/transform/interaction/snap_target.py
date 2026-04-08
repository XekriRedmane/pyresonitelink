"""Generated component: SnapTarget."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sphere_collider import SphereCollider
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapTarget(GeneratedComponent, IGrabbableReparentBlock, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapTarget.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapTarget"

    def __init__(self, direct_snap_only: primitives.Bool | None = None, maximum_snap_distance: primitives.Float | None = None, maximum_angle_deviation: primitives.Float | None = None, animation_time: primitives.Float | None = None, auto_snap: primitives.Bool | None = None, snap_collider_radius: str | IField[primitives.Float] | None = None, proxy_sphere: str | SphereCollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            direct_snap_only: Initial value for DirectSnapOnly.
            maximum_snap_distance: Initial value for MaximumSnapDistance.
            maximum_angle_deviation: Initial value for MaximumAngleDeviation.
            animation_time: Initial value for AnimationTime.
            auto_snap: Initial value for AutoSnap.
            snap_collider_radius: Initial value for _snapColliderRadius.
            proxy_sphere: Initial value for proxySphere.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if direct_snap_only is not None:
            self.direct_snap_only = direct_snap_only
        if maximum_snap_distance is not None:
            self.maximum_snap_distance = maximum_snap_distance
        if maximum_angle_deviation is not None:
            self.maximum_angle_deviation = maximum_angle_deviation
        if animation_time is not None:
            self.animation_time = animation_time
        if auto_snap is not None:
            self.auto_snap = auto_snap
        if snap_collider_radius is not None:
            self.snap_collider_radius = snap_collider_radius
        if proxy_sphere is not None:
            self.proxy_sphere = proxy_sphere

    @property
    def snapper_whitelist(self) -> members.SyncList | None:
        """The SnapperWhitelist member."""
        member = self.get_member("SnapperWhitelist")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snapper_whitelist.setter
    def snapper_whitelist(self, value: members.SyncList) -> None:
        """Set the SnapperWhitelist member."""
        self.set_member("SnapperWhitelist", value)

    @property
    def snapper_keyword_whitelist(self) -> members.SyncList | None:
        """The SnapperKeywordWhitelist member."""
        member = self.get_member("SnapperKeywordWhitelist")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snapper_keyword_whitelist.setter
    def snapper_keyword_whitelist(self, value: members.SyncList) -> None:
        """Set the SnapperKeywordWhitelist member."""
        self.set_member("SnapperKeywordWhitelist", value)

    @property
    def direct_snap_only(self) -> primitives.Bool | None:
        """The DirectSnapOnly field value."""
        member = self.get_member("DirectSnapOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_snap_only.setter
    def direct_snap_only(self, value: primitives.Bool) -> None:
        """Set the DirectSnapOnly field value."""
        member = self.get_member("DirectSnapOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectSnapOnly", fields.FieldBool(value=value)
            )

    @property
    def maximum_snap_distance(self) -> primitives.Float | None:
        """The MaximumSnapDistance field value."""
        member = self.get_member("MaximumSnapDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_snap_distance.setter
    def maximum_snap_distance(self, value: primitives.Float) -> None:
        """Set the MaximumSnapDistance field value."""
        member = self.get_member("MaximumSnapDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumSnapDistance", fields.FieldFloat(value=value)
            )

    @property
    def maximum_angle_deviation(self) -> primitives.Float | None:
        """The MaximumAngleDeviation field value."""
        member = self.get_member("MaximumAngleDeviation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_angle_deviation.setter
    def maximum_angle_deviation(self, value: primitives.Float) -> None:
        """Set the MaximumAngleDeviation field value."""
        member = self.get_member("MaximumAngleDeviation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumAngleDeviation", fields.FieldFloat(value=value)
            )

    @property
    def animation_time(self) -> primitives.Float | None:
        """The AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_time.setter
    def animation_time(self, value: primitives.Float) -> None:
        """Set the AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationTime", fields.FieldFloat(value=value)
            )

    @property
    def auto_snap(self) -> primitives.Bool | None:
        """The AutoSnap field value."""
        member = self.get_member("AutoSnap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_snap.setter
    def auto_snap(self, value: primitives.Bool) -> None:
        """Set the AutoSnap field value."""
        member = self.get_member("AutoSnap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoSnap", fields.FieldBool(value=value)
            )

    @property
    def snap_collider_radius(self) -> str | None:
        """Target ID of the _snapColliderRadius reference (targets IField[primitives.Float])."""
        member = self.get_member("_snapColliderRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @snap_collider_radius.setter
    def snap_collider_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _snapColliderRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_snapColliderRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_snapColliderRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def proxy_sphere(self) -> str | None:
        """Target ID of the proxySphere reference (targets SphereCollider)."""
        member = self.get_member("proxySphere")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @proxy_sphere.setter
    def proxy_sphere(self, target: str | SphereCollider | None) -> None:
        """Set the proxySphere reference by target ID or SphereCollider instance."""
        target_id: str | None = target.id if isinstance(target, SphereCollider) else target  # type: ignore[assignment]
        member = self.get_member("proxySphere")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "proxySphere",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SphereCollider'),
            )

