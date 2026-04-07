"""Generated component: StandardController."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StandardController(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.StandardController.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.StandardController"

    def __init__(self, user: str | INodeObjectOutput[User] | None = None, node: str | INodeValueOutput[Chirality] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            node: Initial value for Node.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if node is not None:
            self.node = node

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
    def node(self) -> str | None:
        """Target ID of the Node reference (targets INodeValueOutput[Chirality])."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Node reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
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
    def type_(self) -> members.EmptyElement | None:
        """The Type member."""
        member = self.get_member("Type")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @type_.setter
    def type_(self, value: members.EmptyElement) -> None:
        """Set the Type member."""
        self.set_member("Type", value)

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

    @property
    def primary(self) -> members.EmptyElement | None:
        """The Primary member."""
        member = self.get_member("Primary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary.setter
    def primary(self, value: members.EmptyElement) -> None:
        """Set the Primary member."""
        self.set_member("Primary", value)

    @property
    def secondary(self) -> members.EmptyElement | None:
        """The Secondary member."""
        member = self.get_member("Secondary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary.setter
    def secondary(self, value: members.EmptyElement) -> None:
        """Set the Secondary member."""
        self.set_member("Secondary", value)

    @property
    def grab(self) -> members.EmptyElement | None:
        """The Grab member."""
        member = self.get_member("Grab")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grab.setter
    def grab(self, value: members.EmptyElement) -> None:
        """Set the Grab member."""
        self.set_member("Grab", value)

    @property
    def menu(self) -> members.EmptyElement | None:
        """The Menu member."""
        member = self.get_member("Menu")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @menu.setter
    def menu(self, value: members.EmptyElement) -> None:
        """Set the Menu member."""
        self.set_member("Menu", value)

    @property
    def strength(self) -> members.EmptyElement | None:
        """The Strength member."""
        member = self.get_member("Strength")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @strength.setter
    def strength(self, value: members.EmptyElement) -> None:
        """Set the Strength member."""
        self.set_member("Strength", value)

    @property
    def axis(self) -> members.EmptyElement | None:
        """The Axis member."""
        member = self.get_member("Axis")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @axis.setter
    def axis(self, value: members.EmptyElement) -> None:
        """Set the Axis member."""
        self.set_member("Axis", value)

