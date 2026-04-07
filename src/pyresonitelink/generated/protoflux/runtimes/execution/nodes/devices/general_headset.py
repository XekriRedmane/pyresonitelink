"""Generated component: GeneralHeadset."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GeneralHeadset(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Headsets.GeneralHeadset.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Headsets.GeneralHeadset"

    def __init__(self, user: str | INodeObjectOutput[User] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user

    @property
    def user(self) -> str | None:
        """Target ID of the User reference (targets INodeObjectOutput[User])."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the User reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def is_active(self) -> members.EmptyElement | None:
        """The IsActive member."""
        member = self.get_member("IsActive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_active.setter
    def is_active(self, value: members.EmptyElement) -> None:
        """Set the IsActive member."""
        self.set_member("IsActive", value)

    @property
    def battery_level(self) -> members.EmptyElement | None:
        """The BatteryLevel member."""
        member = self.get_member("BatteryLevel")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @battery_level.setter
    def battery_level(self, value: members.EmptyElement) -> None:
        """Set the BatteryLevel member."""
        self.set_member("BatteryLevel", value)

    @property
    def is_battery_charging(self) -> members.EmptyElement | None:
        """The IsBatteryCharging member."""
        member = self.get_member("IsBatteryCharging")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_battery_charging.setter
    def is_battery_charging(self, value: members.EmptyElement) -> None:
        """Set the IsBatteryCharging member."""
        self.set_member("IsBatteryCharging", value)

