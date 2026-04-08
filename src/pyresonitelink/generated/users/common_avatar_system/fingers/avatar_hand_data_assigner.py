"""Generated component: AvatarHandDataAssigner."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.tip_touch_source import TipTouchSource
from pyresonitelink.generated._types.vibration_device_relay import VibrationDeviceRelay
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarHandDataAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarHandDataAssigner.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarHandDataAssigner"

    def __init__(self, target_reference: str | SyncRef[IFingerPoseSourceComponent] | None = None, touch_source: str | TipTouchSource | None = None, vibration_relay: str | VibrationDeviceRelay | None = None, equipping_slot: str | AvatarObjectSlot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            touch_source: Initial value for TouchSource.
            vibration_relay: Initial value for VibrationRelay.
            equipping_slot: Initial value for _equippingSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference
        if touch_source is not None:
            self.touch_source = touch_source
        if vibration_relay is not None:
            self.vibration_relay = vibration_relay
        if equipping_slot is not None:
            self.equipping_slot = equipping_slot

    @property
    def target_reference(self) -> str | None:
        """Target ID of the TargetReference reference (targets SyncRef[IFingerPoseSourceComponent])."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[IFingerPoseSourceComponent] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[IFingerPoseSourceComponent] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent>'),
            )

    @property
    def touch_source(self) -> str | None:
        """Target ID of the TouchSource reference (targets TipTouchSource)."""
        member = self.get_member("TouchSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @touch_source.setter
    def touch_source(self, target: str | TipTouchSource | None) -> None:
        """Set the TouchSource reference by target ID or TipTouchSource instance."""
        target_id: str | None = target.id if isinstance(target, TipTouchSource) else target  # type: ignore[assignment]
        member = self.get_member("TouchSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TouchSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TipTouchSource'),
            )

    @property
    def vibration_relay(self) -> str | None:
        """Target ID of the VibrationRelay reference (targets VibrationDeviceRelay)."""
        member = self.get_member("VibrationRelay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @vibration_relay.setter
    def vibration_relay(self, target: str | VibrationDeviceRelay | None) -> None:
        """Set the VibrationRelay reference by target ID or VibrationDeviceRelay instance."""
        target_id: str | None = target.id if isinstance(target, VibrationDeviceRelay) else target  # type: ignore[assignment]
        member = self.get_member("VibrationRelay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VibrationRelay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VibrationDeviceRelay'),
            )

    @property
    def chirality(self) -> members.FieldEnum | None:
        """The Chirality member."""
        member = self.get_member("Chirality")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @chirality.setter
    def chirality(self, value: members.FieldEnum) -> None:
        """Set the Chirality member."""
        self.set_member("Chirality", value)

    @property
    def equipping_slot(self) -> str | None:
        """Target ID of the _equippingSlot reference (targets AvatarObjectSlot)."""
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipping_slot.setter
    def equipping_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the _equippingSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_equippingSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

