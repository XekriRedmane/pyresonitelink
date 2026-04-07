"""Generated component: RelayTouchSource."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.func import Func
from pyresonitelink.generated._types.relay_touch_source import RelayTouchSource
from pyresonitelink.generated._types.touch_type import TouchType
from pyresonitelink.generated._types.touchable_getter import TouchableGetter
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RelayTouchSource(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RelayTouchSource.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RelayTouchSource"

    def __init__(self, auto_update_user: str | User | None = None, tip_position_getter: str | Func[RelayTouchSource, primitives.Float3] | None = None, tip_direction_getter: str | Func[RelayTouchSource, primitives.Float3] | None = None, touch_type_getter: str | Func[RelayTouchSource, TouchType] | None = None, touchable_getter: str | TouchableGetter | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_update_user: Initial value for AutoUpdateUser.
            tip_position_getter: Initial value for TipPositionGetter.
            tip_direction_getter: Initial value for TipDirectionGetter.
            touch_type_getter: Initial value for TouchTypeGetter.
            touchable_getter: Initial value for TouchableGetter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_update_user is not None:
            self.auto_update_user = auto_update_user
        if tip_position_getter is not None:
            self.tip_position_getter = tip_position_getter
        if tip_direction_getter is not None:
            self.tip_direction_getter = tip_direction_getter
        if touch_type_getter is not None:
            self.touch_type_getter = touch_type_getter
        if touchable_getter is not None:
            self.touchable_getter = touchable_getter

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
    def tip_position_getter(self) -> str | None:
        """Target ID of the TipPositionGetter reference (targets Func[RelayTouchSource, primitives.Float3])."""
        member = self.get_member("TipPositionGetter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_position_getter.setter
    def tip_position_getter(self, target: str | Func[RelayTouchSource, primitives.Float3] | None) -> None:
        """Set the TipPositionGetter reference by target ID or Func[RelayTouchSource, primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Func) else target  # type: ignore[assignment]
        member = self.get_member("TipPositionGetter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipPositionGetter",
                members.Reference(targetId=target_id, targetType='Func<[FrooxEngine]FrooxEngine.RelayTouchSource,float3>'),
            )

    @property
    def tip_direction_getter(self) -> str | None:
        """Target ID of the TipDirectionGetter reference (targets Func[RelayTouchSource, primitives.Float3])."""
        member = self.get_member("TipDirectionGetter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_direction_getter.setter
    def tip_direction_getter(self, target: str | Func[RelayTouchSource, primitives.Float3] | None) -> None:
        """Set the TipDirectionGetter reference by target ID or Func[RelayTouchSource, primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, Func) else target  # type: ignore[assignment]
        member = self.get_member("TipDirectionGetter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipDirectionGetter",
                members.Reference(targetId=target_id, targetType='Func<[FrooxEngine]FrooxEngine.RelayTouchSource,float3>'),
            )

    @property
    def touch_type_getter(self) -> str | None:
        """Target ID of the TouchTypeGetter reference (targets Func[RelayTouchSource, TouchType])."""
        member = self.get_member("TouchTypeGetter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @touch_type_getter.setter
    def touch_type_getter(self, target: str | Func[RelayTouchSource, TouchType] | None) -> None:
        """Set the TouchTypeGetter reference by target ID or Func[RelayTouchSource, TouchType] instance."""
        target_id: str | None = target.id if isinstance(target, Func) else target  # type: ignore[assignment]
        member = self.get_member("TouchTypeGetter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TouchTypeGetter",
                members.Reference(targetId=target_id, targetType='Func<[FrooxEngine]FrooxEngine.RelayTouchSource,[FrooxEngine]FrooxEngine.TouchType>'),
            )

    @property
    def touchable_getter(self) -> str | None:
        """Target ID of the TouchableGetter reference (targets TouchableGetter)."""
        member = self.get_member("TouchableGetter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @touchable_getter.setter
    def touchable_getter(self, target: str | TouchableGetter | None) -> None:
        """Set the TouchableGetter reference by target ID or TouchableGetter instance."""
        target_id: str | None = target.id if isinstance(target, TouchableGetter) else target  # type: ignore[assignment]
        member = self.get_member("TouchableGetter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TouchableGetter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TouchableGetter'),
            )

