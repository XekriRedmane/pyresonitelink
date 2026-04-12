"""Generated component: AvatarPoseRotationConstraint."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseRotationConstraint(GeneratedComponent, IAvatarPoseFilter, IWorldEventReceiver):
    """The AvatarPoseRotationConstraint component is used to either restrict the rotation direction of the user's arm when using a tooltip, or to restrict the rotation of a particular BodyNode.

    Category: Users/Common Avatar System/Pose Filters

    Used in avatar anchors and in tooltip contraints.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseRotationConstraint"

    def __init__(self, max_twist: primitives.Float | None = None, max_swing: primitives.Float | None = None, axis: primitives.Float3 | None = None, twist_reference_axis: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_twist: Initial value for MaxTwist.
            max_swing: Initial value for MaxSwing.
            axis: Initial value for Axis.
            twist_reference_axis: Initial value for TwistReferenceAxis.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_twist is not None:
            self.max_twist = max_twist
        if max_swing is not None:
            self.max_swing = max_swing
        if axis is not None:
            self.axis = axis
        if twist_reference_axis is not None:
            self.twist_reference_axis = twist_reference_axis

    @property
    def max_twist(self) -> primitives.Float | None:
        """the max twist in degrees allowed for the object being filtered."""
        member = self.get_member("MaxTwist")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_twist.setter
    def max_twist(self, value: primitives.Float) -> None:
        """Set the MaxTwist field value."""
        member = self.get_member("MaxTwist")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTwist", fields.FieldFloat(value=value)
            )

    @property
    def max_swing(self) -> primitives.Float | None:
        """the max swing in degrees allowed for the object being filtered."""
        member = self.get_member("MaxSwing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_swing.setter
    def max_swing(self, value: primitives.Float) -> None:
        """Set the MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSwing", fields.FieldFloat(value=value)
            )

    @property
    def axis(self) -> primitives.Float3 | None:
        """swing axis direction for the object being filtered."""
        member = self.get_member("Axis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis.setter
    def axis(self, value: primitives.Float3) -> None:
        """Set the Axis field value."""
        member = self.get_member("Axis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Axis", fields.FieldFloat3(value=value)
            )

    @property
    def twist_reference_axis(self) -> primitives.Float3 | None:
        """The twist axis direction for the object being filtered."""
        member = self.get_member("TwistReferenceAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @twist_reference_axis.setter
    def twist_reference_axis(self, value: primitives.Float3) -> None:
        """Set the TwistReferenceAxis field value."""
        member = self.get_member("TwistReferenceAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TwistReferenceAxis", fields.FieldFloat3(value=value)
            )

