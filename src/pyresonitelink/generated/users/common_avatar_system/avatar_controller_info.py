"""Generated component: AvatarControllerInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarControllerInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Reads the controller FrooxEngine class type and it's model identifier for a User for a hand Side.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarControllerInfo"

    def __init__(self, target_user: str | User | None = None, controller_side: Chirality | str | None = None, controller_type: Type | str | None = None, controller_device_model: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            controller_side: Initial value for ControllerSide.
            controller_type: Initial value for ControllerType.
            controller_device_model: Initial value for ControllerDeviceModel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if controller_side is not None:
            self.controller_side = controller_side
        if controller_type is not None:
            self.controller_type = controller_type
        if controller_device_model is not None:
            self.controller_device_model = controller_device_model

    @property
    def target_user(self) -> str | None:
        """The user this component is reading controller info from"""
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
    def controller_side(self) -> Chirality | None:
        """The side (left or right) controller this component is reading info from."""
        member = self.get_member("ControllerSide")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @controller_side.setter
    def controller_side(self, value: Chirality | str) -> None:
        """Set ControllerSide. The side (left or right) controller this component is reading info from."""
        member = self.get_member("ControllerSide")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ControllerSide",
                members.FieldEnum(value=str(value)),
            )

    @property
    def controller_type(self) -> Type | None:
        """The type of the controller ``TargetUser`` is using on their ``ControllerSide`` hand."""
        member = self.get_member("ControllerType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @controller_type.setter
    def controller_type(self, value: Type | str) -> None:
        """Set ControllerType. The type of the controller ``TargetUser`` is using on their ``ControllerSide`` hand."""
        member = self.get_member("ControllerType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ControllerType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def controller_device_model(self) -> primitives.String | None:
        """The device model of the controller ``TargetUser`` is using on their ``ControllerSide`` hand."""
        member = self.get_member("ControllerDeviceModel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @controller_device_model.setter
    def controller_device_model(self, value: primitives.String) -> None:
        """Set the ControllerDeviceModel field value."""
        member = self.get_member("ControllerDeviceModel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ControllerDeviceModel", fields.FieldString(value=value)
            )

