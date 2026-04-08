"""Generated component: TrackedDevicePositioner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.user_pose_controller import UserPoseController
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrackedDevicePositioner(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TrackedDevicePositioner.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackedDevicePositioner"

    def __init__(self, device_index: primitives.Int | None = None, always_render_model: primitives.Bool | None = None, reference_model: str | Slot | None = None, body_node_root: str | Slot | None = None, object_slot: str | AvatarObjectSlot | None = None, is_tracking: primitives.Bool | None = None, is_active: primitives.Bool | None = None, is_simulated: primitives.Bool | None = None, create_avatar_object_slot: primitives.Bool | None = None, pose_filter: str | UserPoseController | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_index: Initial value for DeviceIndex.
            always_render_model: Initial value for AlwaysRenderModel.
            reference_model: Initial value for ReferenceModel.
            body_node_root: Initial value for BodyNodeRoot.
            object_slot: Initial value for ObjectSlot.
            is_tracking: Initial value for IsTracking.
            is_active: Initial value for IsActive.
            is_simulated: Initial value for IsSimulated.
            create_avatar_object_slot: Initial value for CreateAvatarObjectSlot.
            pose_filter: Initial value for PoseFilter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if device_index is not None:
            self.device_index = device_index
        if always_render_model is not None:
            self.always_render_model = always_render_model
        if reference_model is not None:
            self.reference_model = reference_model
        if body_node_root is not None:
            self.body_node_root = body_node_root
        if object_slot is not None:
            self.object_slot = object_slot
        if is_tracking is not None:
            self.is_tracking = is_tracking
        if is_active is not None:
            self.is_active = is_active
        if is_simulated is not None:
            self.is_simulated = is_simulated
        if create_avatar_object_slot is not None:
            self.create_avatar_object_slot = create_avatar_object_slot
        if pose_filter is not None:
            self.pose_filter = pose_filter

    @property
    def device_index(self) -> primitives.Int | None:
        """The DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_index.setter
    def device_index(self, value: primitives.Int) -> None:
        """Set the DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def corresponding_body_node(self) -> members.FieldEnum | None:
        """The CorrespondingBodyNode member."""
        member = self.get_member("CorrespondingBodyNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @corresponding_body_node.setter
    def corresponding_body_node(self, value: members.FieldEnum) -> None:
        """Set the CorrespondingBodyNode member."""
        self.set_member("CorrespondingBodyNode", value)

    @property
    def auto_body_node(self) -> members.FieldEnum | None:
        """The AutoBodyNode member."""
        member = self.get_member("AutoBodyNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @auto_body_node.setter
    def auto_body_node(self, value: members.FieldEnum) -> None:
        """Set the AutoBodyNode member."""
        self.set_member("AutoBodyNode", value)

    @property
    def always_render_model(self) -> primitives.Bool | None:
        """The AlwaysRenderModel field value."""
        member = self.get_member("AlwaysRenderModel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_render_model.setter
    def always_render_model(self, value: primitives.Bool) -> None:
        """Set the AlwaysRenderModel field value."""
        member = self.get_member("AlwaysRenderModel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysRenderModel", fields.FieldBool(value=value)
            )

    @property
    def reference_model(self) -> str | None:
        """Target ID of the ReferenceModel reference (targets Slot)."""
        member = self.get_member("ReferenceModel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_model.setter
    def reference_model(self, target: str | Slot | None) -> None:
        """Set the ReferenceModel reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ReferenceModel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReferenceModel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def body_node_root(self) -> str | None:
        """Target ID of the BodyNodeRoot reference (targets Slot)."""
        member = self.get_member("BodyNodeRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @body_node_root.setter
    def body_node_root(self, target: str | Slot | None) -> None:
        """Set the BodyNodeRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("BodyNodeRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BodyNodeRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def object_slot(self) -> str | None:
        """Target ID of the ObjectSlot reference (targets AvatarObjectSlot)."""
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot.setter
    def object_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the ObjectSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ObjectSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

    @property
    def is_tracking(self) -> primitives.Bool | None:
        """The IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_tracking.setter
    def is_tracking(self, value: primitives.Bool) -> None:
        """Set the IsTracking field value."""
        member = self.get_member("IsTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsTracking", fields.FieldBool(value=value)
            )

    @property
    def is_active(self) -> primitives.Bool | None:
        """The IsActive field value."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: primitives.Bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    @property
    def is_simulated(self) -> primitives.Bool | None:
        """The IsSimulated field value."""
        member = self.get_member("IsSimulated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_simulated.setter
    def is_simulated(self, value: primitives.Bool) -> None:
        """Set the IsSimulated field value."""
        member = self.get_member("IsSimulated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSimulated", fields.FieldBool(value=value)
            )

    @property
    def create_avatar_object_slot(self) -> primitives.Bool | None:
        """The CreateAvatarObjectSlot field value."""
        member = self.get_member("CreateAvatarObjectSlot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @create_avatar_object_slot.setter
    def create_avatar_object_slot(self, value: primitives.Bool) -> None:
        """Set the CreateAvatarObjectSlot field value."""
        member = self.get_member("CreateAvatarObjectSlot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreateAvatarObjectSlot", fields.FieldBool(value=value)
            )

    @property
    def pose_filter(self) -> str | None:
        """Target ID of the PoseFilter reference (targets UserPoseController)."""
        member = self.get_member("PoseFilter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pose_filter.setter
    def pose_filter(self, target: str | UserPoseController | None) -> None:
        """Set the PoseFilter reference by target ID or UserPoseController instance."""
        target_id: str | None = target.id if isinstance(target, UserPoseController) else target  # type: ignore[assignment]
        member = self.get_member("PoseFilter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PoseFilter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserPoseController'),
            )

