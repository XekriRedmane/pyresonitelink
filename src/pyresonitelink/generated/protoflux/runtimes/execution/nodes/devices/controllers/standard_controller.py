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
    """This node provides information for generic controllers.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers

    The standard controller node allows one to interact with the players
    virtual reality controller as well as generic inputs on Desktop mode.
    Say you want to get the user's grip and trigger strength, just feed it a
    user and a "Chirality input" for the left or right controller and volla!
    Just pull an output from the grip boolean and the strength float value
    and now you have the users grip and trigger on/off and strength!
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
        """The user to get controller information from."""
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
        """The controller side to get information from."""
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
        """Is this controller actively being used right now."""
        member = self.get_member("IsActive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_active.setter
    def is_active(self, value: members.EmptyElement) -> None:
        """Set IsActive. Is this controller actively being used right now."""
        self.set_member("IsActive", value)

    @property
    def type_(self) -> members.EmptyElement | None:
        """The controller type being used. (a subtype of IStandardController if a controller exists or ``null``)"""
        member = self.get_member("Type")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @type_.setter
    def type_(self, value: members.EmptyElement) -> None:
        """Set Type. The controller type being used. (a subtype of IStandardController if a controller exists or ``null``)"""
        self.set_member("Type", value)

    @property
    def battery_level(self) -> members.EmptyElement | None:
        """The battery level of this controller. (``1``: full, ``0``: empty, ``-1``: battery level not available)"""
        member = self.get_member("BatteryLevel")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @battery_level.setter
    def battery_level(self, value: members.EmptyElement) -> None:
        """Set BatteryLevel. The battery level of this controller. (``1``: full, ``0``: empty, ``-1``: battery level not available)"""
        self.set_member("BatteryLevel", value)

    @property
    def is_battery_charging(self) -> members.EmptyElement | None:
        """Is this controller currently charging."""
        member = self.get_member("IsBatteryCharging")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_battery_charging.setter
    def is_battery_charging(self, value: members.EmptyElement) -> None:
        """Set IsBatteryCharging. Is this controller currently charging."""
        self.set_member("IsBatteryCharging", value)

    @property
    def primary(self) -> members.EmptyElement | None:
        """Is primary pressed right now."""
        member = self.get_member("Primary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary.setter
    def primary(self, value: members.EmptyElement) -> None:
        """Set Primary. Is primary pressed right now."""
        self.set_member("Primary", value)

    @property
    def secondary(self) -> members.EmptyElement | None:
        """Is secondary pressed right now."""
        member = self.get_member("Secondary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary.setter
    def secondary(self, value: members.EmptyElement) -> None:
        """Set Secondary. Is secondary pressed right now."""
        self.set_member("Secondary", value)

    @property
    def grab(self) -> members.EmptyElement | None:
        """Is the controller's grip button pressed right now."""
        member = self.get_member("Grab")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grab.setter
    def grab(self, value: members.EmptyElement) -> None:
        """Set Grab. Is the controller's grip button pressed right now."""
        self.set_member("Grab", value)

    @property
    def menu(self) -> members.EmptyElement | None:
        """Is the menu button being pressed right now."""
        member = self.get_member("Menu")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @menu.setter
    def menu(self, value: members.EmptyElement) -> None:
        """Set Menu. Is the menu button being pressed right now."""
        self.set_member("Menu", value)

    @property
    def strength(self) -> members.EmptyElement | None:
        """How much the trigger is pressed currently. (from ``0`` to ``1``)"""
        member = self.get_member("Strength")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @strength.setter
    def strength(self, value: members.EmptyElement) -> None:
        """Set Strength. How much the trigger is pressed currently. (from ``0`` to ``1``)"""
        self.set_member("Strength", value)

    @property
    def axis(self) -> members.EmptyElement | None:
        """The position of this controller's joystick or touchpad depending on controller type. (``[-1; -1]``: bottom left, ``[+1; +1]``: top right, ``[0; 0]`` for touchpads that are untouched)

Index Controllers have both types of input. ``Axis`` returns the touchpad position."""
        member = self.get_member("Axis")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @axis.setter
    def axis(self, value: members.EmptyElement) -> None:
        """Set Axis. The position of this controller's joystick or touchpad depending on controller type. (``[-1; -1]``: bottom left, ``[+1; +1]``: top right, ``[0; 0]`` for touchpads that are untouched)

Index Controllers have both types of input. ``Axis`` returns the touchpad position."""
        self.set_member("Axis", value)

