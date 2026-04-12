"""Generated component: LocomotionAnimationFeetMetrics."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.locomotion_metrics_space import LocomotionMetricsSpace
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationFeetMetrics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocomotionAnimationFeetMetrics component is used to adjust the settings for an avatar's feet.

    Category: Users/Common Avatar System/Animation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationFeetMetrics"

    def __init__(self, space: LocomotionMetricsSpace | str | None = None, feet_separation: primitives.Float | None = None, feet_backwards_offset: primitives.Float | None = None, foot_height: primitives.Float | None = None, foot_front_offset: primitives.Float | None = None, foot_back_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            space: Initial value for Space.
            feet_separation: Initial value for FeetSeparation.
            feet_backwards_offset: Initial value for FeetBackwardsOffset.
            foot_height: Initial value for FootHeight.
            foot_front_offset: Initial value for FootFrontOffset.
            foot_back_offset: Initial value for FootBackOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if space is not None:
            self.space = space
        if feet_separation is not None:
            self.feet_separation = feet_separation
        if feet_backwards_offset is not None:
            self.feet_backwards_offset = feet_backwards_offset
        if foot_height is not None:
            self.foot_height = foot_height
        if foot_front_offset is not None:
            self.foot_front_offset = foot_front_offset
        if foot_back_offset is not None:
            self.foot_back_offset = foot_back_offset

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
    def feet_separation(self) -> primitives.Float | None:
        """How far apart the feet should be placed from each other."""
        member = self.get_member("FeetSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_separation.setter
    def feet_separation(self, value: primitives.Float) -> None:
        """Set the FeetSeparation field value."""
        member = self.get_member("FeetSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetSeparation", fields.FieldNullableFloat(value=value)
            )

    @property
    def feet_backwards_offset(self) -> primitives.Float | None:
        """How much the foot should be shifted forwards or backwards."""
        member = self.get_member("FeetBackwardsOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_backwards_offset.setter
    def feet_backwards_offset(self, value: primitives.Float) -> None:
        """Set the FeetBackwardsOffset field value."""
        member = self.get_member("FeetBackwardsOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetBackwardsOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_height(self) -> primitives.Float | None:
        """The distance from the floor to the foot bone for the whole foot."""
        member = self.get_member("FootHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_height.setter
    def foot_height(self, value: primitives.Float) -> None:
        """Set the FootHeight field value."""
        member = self.get_member("FootHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootHeight", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_front_offset(self) -> primitives.Float | None:
        """An optional value to influence the foot front distance from floor value."""
        member = self.get_member("FootFrontOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_front_offset.setter
    def foot_front_offset(self, value: primitives.Float) -> None:
        """Set the FootFrontOffset field value."""
        member = self.get_member("FootFrontOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootFrontOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_back_offset(self) -> primitives.Float | None:
        """An optional value to influence the foot back distance from floor value."""
        member = self.get_member("FootBackOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_back_offset.setter
    def foot_back_offset(self, value: primitives.Float) -> None:
        """Set the FootBackOffset field value."""
        member = self.get_member("FootBackOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootBackOffset", fields.FieldNullableFloat(value=value)
            )

