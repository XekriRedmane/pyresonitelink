"""Generated component: CosmosController."""

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


class CosmosController(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides information provided by HTC Vive Cosmos controllers.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.CosmosController"

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
        """The user we are getting controller information from."""
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
        """The controller type being used."""
        member = self.get_member("Type")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @type_.setter
    def type_(self, value: members.EmptyElement) -> None:
        """Set Type. The controller type being used."""
        self.set_member("Type", value)

    @property
    def battery_level(self) -> members.EmptyElement | None:
        """The battery level of this controller."""
        member = self.get_member("BatteryLevel")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @battery_level.setter
    def battery_level(self, value: members.EmptyElement) -> None:
        """Set BatteryLevel. The battery level of this controller."""
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
    def menu(self) -> members.EmptyElement | None:
        """Is the menu button pressed right now."""
        member = self.get_member("Menu")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @menu.setter
    def menu(self, value: members.EmptyElement) -> None:
        """Set Menu. Is the menu button pressed right now."""
        self.set_member("Menu", value)

    @property
    def button_by(self) -> members.EmptyElement | None:
        """Is the Button BY pressed right now."""
        member = self.get_member("ButtonBY")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_by.setter
    def button_by(self, value: members.EmptyElement) -> None:
        """Set ButtonBY. Is the Button BY pressed right now."""
        self.set_member("ButtonBY", value)

    @property
    def button_ax(self) -> members.EmptyElement | None:
        """Is the Button AX pressed right now."""
        member = self.get_member("ButtonAX")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_ax.setter
    def button_ax(self, value: members.EmptyElement) -> None:
        """Set ButtonAX. Is the Button AX pressed right now."""
        self.set_member("ButtonAX", value)

    @property
    def grip_click(self) -> members.EmptyElement | None:
        """Is the controller's grip clicked down right now."""
        member = self.get_member("GripClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip_click.setter
    def grip_click(self, value: members.EmptyElement) -> None:
        """Set GripClick. Is the controller's grip clicked down right now."""
        self.set_member("GripClick", value)

    @property
    def bumper(self) -> members.EmptyElement | None:
        """Is the controller's bumper pressed right now."""
        member = self.get_member("Bumper")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bumper.setter
    def bumper(self, value: members.EmptyElement) -> None:
        """Set Bumper. Is the controller's bumper pressed right now."""
        self.set_member("Bumper", value)

    @property
    def joystick(self) -> members.EmptyElement | None:
        """The position of this controller's joystick."""
        member = self.get_member("Joystick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick.setter
    def joystick(self, value: members.EmptyElement) -> None:
        """Set Joystick. The position of this controller's joystick."""
        self.set_member("Joystick", value)

    @property
    def joystick_touch(self) -> members.EmptyElement | None:
        """Is the controller's joystick being touched right now."""
        member = self.get_member("JoystickTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick_touch.setter
    def joystick_touch(self, value: members.EmptyElement) -> None:
        """Set JoystickTouch. Is the controller's joystick being touched right now."""
        self.set_member("JoystickTouch", value)

    @property
    def joystick_click(self) -> members.EmptyElement | None:
        """Is the controller's joystick clicked down right now."""
        member = self.get_member("JoystickClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick_click.setter
    def joystick_click(self, value: members.EmptyElement) -> None:
        """Set JoystickClick. Is the controller's joystick clicked down right now."""
        self.set_member("JoystickClick", value)

    @property
    def trigger(self) -> members.EmptyElement | None:
        """The amount of how far this controller's trigger is being pressed down currently."""
        member = self.get_member("Trigger")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.EmptyElement) -> None:
        """Set Trigger. The amount of how far this controller's trigger is being pressed down currently."""
        self.set_member("Trigger", value)

    @property
    def trigger_touch(self) -> members.EmptyElement | None:
        """Is the controller's trigger being touched right now."""
        member = self.get_member("TriggerTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_touch.setter
    def trigger_touch(self, value: members.EmptyElement) -> None:
        """Set TriggerTouch. Is the controller's trigger being touched right now."""
        self.set_member("TriggerTouch", value)

    @property
    def trigger_click(self) -> members.EmptyElement | None:
        """Is the controller's trigger being clicked down right now."""
        member = self.get_member("TriggerClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_click.setter
    def trigger_click(self, value: members.EmptyElement) -> None:
        """Set TriggerClick. Is the controller's trigger being clicked down right now."""
        self.set_member("TriggerClick", value)

