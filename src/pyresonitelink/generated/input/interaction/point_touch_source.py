"""Generated component: PointTouchSource."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointTouchSource(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PointTouchSource.

    Category: Input/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointTouchSource"

    def __init__(self, auto_update_user: str | User | None = None, out_of_sight_angle: np.float32 | None = None, max_touch_penetration_distance: np.float32 | None = None, offset: primitives.Float3 | None = None, direction: primitives.Float3 | None = None, max_distance: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_update_user: Initial value for AutoUpdateUser.
            out_of_sight_angle: Initial value for OutOfSightAngle.
            max_touch_penetration_distance: Initial value for MaxTouchPenetrationDistance.
            offset: Initial value for Offset.
            direction: Initial value for Direction.
            max_distance: Initial value for MaxDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_update_user is not None:
            self.auto_update_user = auto_update_user
        if out_of_sight_angle is not None:
            self.out_of_sight_angle = out_of_sight_angle
        if max_touch_penetration_distance is not None:
            self.max_touch_penetration_distance = max_touch_penetration_distance
        if offset is not None:
            self.offset = offset
        if direction is not None:
            self.direction = direction
        if max_distance is not None:
            self.max_distance = max_distance

    @property
    def auto_update_user(self) -> str | None:
        """Target ID of the AutoUpdateUser reference (targets User)."""
        member = self.get_member("AutoUpdateUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_update_user.setter
    def auto_update_user(self, target: str | User | None) -> None:
        """Set the AutoUpdateUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("AutoUpdateUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AutoUpdateUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def out_of_sight_angle(self) -> np.float32 | None:
        """The OutOfSightAngle field value."""
        member = self.get_member("OutOfSightAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @out_of_sight_angle.setter
    def out_of_sight_angle(self, value: np.float32) -> None:
        """Set the OutOfSightAngle field value."""
        member = self.get_member("OutOfSightAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutOfSightAngle", fields.FieldFloat(value=value)
            )

    @property
    def max_touch_penetration_distance(self) -> np.float32 | None:
        """The MaxTouchPenetrationDistance field value."""
        member = self.get_member("MaxTouchPenetrationDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_touch_penetration_distance.setter
    def max_touch_penetration_distance(self, value: np.float32) -> None:
        """Set the MaxTouchPenetrationDistance field value."""
        member = self.get_member("MaxTouchPenetrationDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTouchPenetrationDistance", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def direction(self) -> primitives.Float3 | None:
        """The Direction field value."""
        member = self.get_member("Direction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction.setter
    def direction(self, value: primitives.Float3) -> None:
        """Set the Direction field value."""
        member = self.get_member("Direction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction", fields.FieldFloat3(value=value)
            )

    @property
    def max_distance(self) -> np.float32 | None:
        """The MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: np.float32) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

