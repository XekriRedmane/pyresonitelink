"""Generated component: LocomotionAnimationHandMetrics."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationHandMetrics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionAnimationHandMetrics.

    Category: Users/Common Avatar System/Animation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationHandMetrics"

    def __init__(self, shoulder_separation: primitives.Float | None = None, shoulder_height: primitives.Float | None = None, shoulder_offset: primitives.Float | None = None, hand_offset: primitives.Float | None = None, arm_length: primitives.Float | None = None, hand_palm_distance: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            shoulder_separation: Initial value for ShoulderSeparation.
            shoulder_height: Initial value for ShoulderHeight.
            shoulder_offset: Initial value for ShoulderOffset.
            hand_offset: Initial value for HandOffset.
            arm_length: Initial value for ArmLength.
            hand_palm_distance: Initial value for HandPalmDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
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
    def space(self) -> members.FieldEnum | None:
        """The Space member."""
        member = self.get_member("Space")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @space.setter
    def space(self, value: members.FieldEnum) -> None:
        """Set the Space member."""
        self.set_member("Space", value)

    @property
    def shoulder_separation(self) -> primitives.Float | None:
        """The ShoulderSeparation field value."""
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
        """The ShoulderHeight field value."""
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
        """The ShoulderOffset field value."""
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
        """The HandOffset field value."""
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
        """The ArmLength field value."""
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
        """The HandPalmDistance field value."""
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

