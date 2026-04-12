"""Generated component: VibrationDeviceRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivibration_device_component import IVibrationDeviceComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VibrationDeviceRelay(GeneratedComponent, IVibrationDeviceComponent, IWorldEventReceiver):
    """The VibrationDeviceRelay component recieves haptics events and relays them to other vibration recievers.

    Attach to a slot like the hands or other slots that can recieve haptics,
    then specify a target or component that the vibrations should be relayed
    to.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VibrationDeviceRelay"

    def __init__(self, target_component: str | IVibrationDeviceComponent | None = None, dynamic_lookup_target: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_component: Initial value for TargetComponent.
            dynamic_lookup_target: Initial value for DynamicLookupTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_component is not None:
            self.target_component = target_component
        if dynamic_lookup_target is not None:
            self.dynamic_lookup_target = dynamic_lookup_target

    @property
    def target_component(self) -> str | None:
        """The component to relay the vibration event to."""
        member = self.get_member("TargetComponent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_component.setter
    def target_component(self, target: str | IVibrationDeviceComponent | None) -> None:
        """Set the TargetComponent reference by target ID or IVibrationDeviceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IVibrationDeviceComponent) else target  # type: ignore[assignment]
        member = self.get_member("TargetComponent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetComponent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IVibrationDeviceComponent'),
            )

    @property
    def dynamic_lookup_target(self) -> str | None:
        """The slot to look for components in to send the vibration event to."""
        member = self.get_member("DynamicLookupTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dynamic_lookup_target.setter
    def dynamic_lookup_target(self, target: str | Slot | None) -> None:
        """Set the DynamicLookupTarget reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("DynamicLookupTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DynamicLookupTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

