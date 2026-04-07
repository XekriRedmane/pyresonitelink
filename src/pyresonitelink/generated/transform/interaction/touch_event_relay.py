"""Generated component: TouchEventRelay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.touch_event import TouchEvent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchEventRelay(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchEventRelay.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchEventRelay"

    def __init__(self, touched: str | TouchEvent | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            touched: Initial value for Touched.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if touched is not None:
            self.touched = touched

    @property
    def accept_out_of_sight_touch(self) -> bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def touchable_targets(self) -> members.SyncList | None:
        """The TouchableTargets member."""
        member = self.get_member("TouchableTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @touchable_targets.setter
    def touchable_targets(self, value: members.SyncList) -> None:
        """Set the TouchableTargets member."""
        self.set_member("TouchableTargets", value)

    @property
    def touched(self) -> str | None:
        """Target ID of the Touched reference (targets TouchEvent)."""
        member = self.get_member("Touched")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @touched.setter
    def touched(self, target: str | TouchEvent | None) -> None:
        """Set the Touched reference by target ID or TouchEvent instance."""
        target_id: str | None = target.id if isinstance(target, TouchEvent) else target  # type: ignore[assignment]
        member = self.get_member("Touched")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Touched",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TouchEvent'),
            )

