"""Generated component: AvatarControllerInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarControllerInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarControllerInfo.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarControllerInfo"

    def __init__(self, target_user: str | User | None = None, controller_device_model: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            controller_device_model: Initial value for ControllerDeviceModel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if controller_device_model is not None:
            self.controller_device_model = controller_device_model

    @property
    def target_user(self) -> str | None:
        """Target ID of the TargetUser reference (targets User)."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_user.setter
    def target_user(self, target: str | User | None) -> None:
        """Set the TargetUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def controller_side(self) -> members.FieldEnum | None:
        """The ControllerSide member."""
        member = self.get_member("ControllerSide")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @controller_side.setter
    def controller_side(self, value: members.FieldEnum) -> None:
        """Set the ControllerSide member."""
        self.set_member("ControllerSide", value)

    @property
    def controller_type(self) -> members.FieldEnum | None:
        """The ControllerType member."""
        member = self.get_member("ControllerType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @controller_type.setter
    def controller_type(self, value: members.FieldEnum) -> None:
        """Set the ControllerType member."""
        self.set_member("ControllerType", value)

    @property
    def controller_device_model(self) -> str | None:
        """The ControllerDeviceModel field value."""
        member = self.get_member("ControllerDeviceModel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @controller_device_model.setter
    def controller_device_model(self, value: str) -> None:
        """Set the ControllerDeviceModel field value."""
        member = self.get_member("ControllerDeviceModel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ControllerDeviceModel", fields.FieldString(value=value)
            )

