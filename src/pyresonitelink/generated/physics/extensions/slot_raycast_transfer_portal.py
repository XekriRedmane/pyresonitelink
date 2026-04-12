"""Generated component: SlotRaycastTransferPortal."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.filter_combine_mode import FilterCombineMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iraycast_portal import IRaycastPortal
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlotRaycastTransferPortal(GeneratedComponent, IRaycastPortal, IWorldEventReceiver):
    """The SlotRaycastTransferPortal acts very similarly to the MeshUVRaycastPortal except that it works on colliders hitting a slot hiearchy to another slot rather than just a mesh and a camera.

    Category: Physics/Extensions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SlotRaycastTransferPortal"

    def __init__(self, exit: str | Slot | None = None, override_hit_triggers: primitives.Bool | None = None, filter_mode: FilterCombineMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            exit: Initial value for Exit.
            override_hit_triggers: Initial value for OverrideHitTriggers.
            filter_mode: Initial value for FilterMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if exit is not None:
            self.exit = exit
        if override_hit_triggers is not None:
            self.override_hit_triggers = override_hit_triggers
        if filter_mode is not None:
            self.filter_mode = filter_mode

    @property
    def exit(self) -> str | None:
        """The slot to send the raycast through if it hits this slot's hierarchy, converting the hit point / direction in this component slot's local space to the space of the slot specified here."""
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
    def override_hit_triggers(self) -> primitives.Bool | None:
        """Whether to override if a laser coming through will hit triggers and what to override it with."""
        member = self.get_member("OverrideHitTriggers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_hit_triggers.setter
    def override_hit_triggers(self, value: primitives.Bool) -> None:
        """Set the OverrideHitTriggers field value."""
        member = self.get_member("OverrideHitTriggers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideHitTriggers", fields.FieldNullableBool(value=value)
            )

    @property
    def filter_mode(self) -> FilterCombineMode | None:
        """If a raycast being transfered has its own filter, how should we combine it with ``Filter`` if it exists?."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return FilterCombineMode(member.value)
        return None

    @filter_mode.setter
    def filter_mode(self, value: FilterCombineMode | str) -> None:
        """Set FilterMode. If a raycast being transfered has its own filter, how should we combine it with ``Filter`` if it exists?."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "FilterMode",
                members.FieldEnum(value=str(value)),
            )

