"""Generated component: LocomotionAnimationHandMetrics."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.locomotion_metrics_space import LocomotionMetricsSpace
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationHandMetrics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocomotionAnimationHandMetrics component can be used to adjust the settings on the hands for an avatar for its rest state.

    Category: Users/Common Avatar System/Animation

    Can be used to adjust the arms rest state so they don't collide with the
    legs or hips too much.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationHandMetrics"

    def __init__(self, space: LocomotionMetricsSpace | str | None = None, shoulder_separation: primitives.Float | None = None, shoulder_height: primitives.Float | None = None, shoulder_offset: primitives.Float | None = None, hand_offset: primitives.Float | None = None, arm_length: primitives.Float | None = None, hand_palm_distance: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            space: Initial value for Space.
            shoulder_separation: Initial value for ShoulderSeparation.
            shoulder_height: Initial value for ShoulderHeight.
            shoulder_offset: Initial value for ShoulderOffset.
            hand_offset: Initial value for HandOffset.
            arm_length: Initial value for ArmLength.
            hand_palm_distance: Initial value for HandPalmDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if space is not None:
            self.space = space
        if shoulder_separation is not None:
            self.shoulder_separation = shoulder_separation
        if shoulder_height is not None:
            self.shoulder_height = shoulder_height
        if shoulder_offset is not None:
            self.shoulder_offset = shoulder_offset
        if hand_offset is not None:
            self.hand_offset = hand_offset
        if arm_length is not None:
            self.arm_length = arm_length
        if hand_palm_distance is not None:
            self.hand_palm_distance = hand_palm_distance

    @property
    def space(self) -> LocomotionMetricsSpace | None:
        """What transform space the metric values are in for this component."""
        member = self.get_member("Space")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LocomotionMetricsSpace(member.value)
        return None

    @space.setter
    def space(self, value: LocomotionMetricsSpace | str) -> None:
        """Set Space. What transform space the metric values are in for this component."""
        member = self.get_member("Space")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Space",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shoulder_separation(self) -> primitives.Float | None:
        """An optional value to specify how apart the shoulders are in local space meters."""
        member = self.get_member("ShoulderSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shoulder_separation.setter
    def shoulder_separation(self, value: primitives.Float) -> None:
        """Set the ShoulderSeparation field value."""
        member = self.get_member("ShoulderSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShoulderSeparation", fields.FieldNullableFloat(value=value)
            )

    @property
    def shoulder_height(self) -> primitives.Float | None:
        """An optional value to specify how far the shoulders are from the ground in local space meters."""
        member = self.get_member("ShoulderHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shoulder_height.setter
    def shoulder_height(self, value: primitives.Float) -> None:
        """Set the ShoulderHeight field value."""
        member = self.get_member("ShoulderHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShoulderHeight", fields.FieldNullableFloat(value=value)
            )

    @property
    def shoulder_offset(self) -> primitives.Float | None:
        """The offset of the shoulders forwards or backwards in meters."""
        member = self.get_member("ShoulderOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shoulder_offset.setter
    def shoulder_offset(self, value: primitives.Float) -> None:
        """Set the ShoulderOffset field value."""
        member = self.get_member("ShoulderOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShoulderOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def hand_offset(self) -> primitives.Float | None:
        """An optional value to specify how far the hands should be offseted from the avatar center in local space meters."""
        member = self.get_member("HandOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_offset.setter
    def hand_offset(self, value: primitives.Float) -> None:
        """Set the HandOffset field value."""
        member = self.get_member("HandOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def arm_length(self) -> primitives.Float | None:
        """An optional value to specify how long the arms are in local space meters."""
        member = self.get_member("ArmLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arm_length.setter
    def arm_length(self, value: primitives.Float) -> None:
        """Set the ArmLength field value."""
        member = self.get_member("ArmLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArmLength", fields.FieldNullableFloat(value=value)
            )

    @property
    def hand_palm_distance(self) -> primitives.Float | None:
        """An optional value to specify how long the palms are in local space meters."""
        member = self.get_member("HandPalmDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_palm_distance.setter
    def hand_palm_distance(self, value: primitives.Float) -> None:
        """Set the HandPalmDistance field value."""
        member = self.get_member("HandPalmDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandPalmDistance", fields.FieldNullableFloat(value=value)
            )

