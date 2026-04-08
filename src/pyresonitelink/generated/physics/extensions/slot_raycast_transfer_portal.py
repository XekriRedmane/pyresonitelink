"""Generated component: SlotRaycastTransferPortal."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iraycast_portal import IRaycastPortal
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlotRaycastTransferPortal(GeneratedComponent, IRaycastPortal, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SlotRaycastTransferPortal.

    Category: Physics/Extensions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SlotRaycastTransferPortal"

    def __init__(self, exit: str | Slot | None = None, override_hit_triggers: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            exit: Initial value for Exit.
            override_hit_triggers: Initial value for OverrideHitTriggers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if exit is not None:
            self.exit = exit
        if override_hit_triggers is not None:
            self.override_hit_triggers = override_hit_triggers

    @property
    def exit(self) -> str | None:
        """Target ID of the Exit reference (targets Slot)."""
        member = self.get_member("Exit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exit.setter
    def exit(self, target: str | Slot | None) -> None:
        """Set the Exit reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Exit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Exit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def override_hit_triggers(self) -> bool | None:
        """The OverrideHitTriggers field value."""
        member = self.get_member("OverrideHitTriggers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_hit_triggers.setter
    def override_hit_triggers(self, value: bool) -> None:
        """Set the OverrideHitTriggers field value."""
        member = self.get_member("OverrideHitTriggers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideHitTriggers", fields.FieldNullableBool(value=value)
            )

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

