"""Generated component: LocomotionAnimationFeetMetrics."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationFeetMetrics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionAnimationFeetMetrics.

    Category: Users/Common Avatar System/Animation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationFeetMetrics"

    def __init__(self, feet_separation: np.float32 | None = None, feet_backwards_offset: np.float32 | None = None, foot_height: np.float32 | None = None, foot_front_offset: np.float32 | None = None, foot_back_offset: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            feet_separation: Initial value for FeetSeparation.
            feet_backwards_offset: Initial value for FeetBackwardsOffset.
            foot_height: Initial value for FootHeight.
            foot_front_offset: Initial value for FootFrontOffset.
            foot_back_offset: Initial value for FootBackOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
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
    def feet_separation(self) -> np.float32 | None:
        """The FeetSeparation field value."""
        member = self.get_member("FeetSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_separation.setter
    def feet_separation(self, value: np.float32) -> None:
        """Set the FeetSeparation field value."""
        member = self.get_member("FeetSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetSeparation", fields.FieldNullableFloat(value=value)
            )

    @property
    def feet_backwards_offset(self) -> np.float32 | None:
        """The FeetBackwardsOffset field value."""
        member = self.get_member("FeetBackwardsOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_backwards_offset.setter
    def feet_backwards_offset(self, value: np.float32) -> None:
        """Set the FeetBackwardsOffset field value."""
        member = self.get_member("FeetBackwardsOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetBackwardsOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_height(self) -> np.float32 | None:
        """The FootHeight field value."""
        member = self.get_member("FootHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_height.setter
    def foot_height(self, value: np.float32) -> None:
        """Set the FootHeight field value."""
        member = self.get_member("FootHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootHeight", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_front_offset(self) -> np.float32 | None:
        """The FootFrontOffset field value."""
        member = self.get_member("FootFrontOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_front_offset.setter
    def foot_front_offset(self, value: np.float32) -> None:
        """Set the FootFrontOffset field value."""
        member = self.get_member("FootFrontOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootFrontOffset", fields.FieldNullableFloat(value=value)
            )

    @property
    def foot_back_offset(self) -> np.float32 | None:
        """The FootBackOffset field value."""
        member = self.get_member("FootBackOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_back_offset.setter
    def foot_back_offset(self, value: np.float32) -> None:
        """Set the FootBackOffset field value."""
        member = self.get_member("FootBackOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootBackOffset", fields.FieldNullableFloat(value=value)
            )

