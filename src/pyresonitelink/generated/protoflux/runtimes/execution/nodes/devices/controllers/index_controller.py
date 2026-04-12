"""Generated component: IndexController."""

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


class IndexController(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides information provided by Index controllers.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.IndexController"

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
        """Bool for showing if the device is active. Useful for troubleshooting if your controller is not responding."""
        member = self.get_member("IsActive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_active.setter
    def is_active(self, value: members.EmptyElement) -> None:
        """Set IsActive. Bool for showing if the device is active. Useful for troubleshooting if your controller is not responding."""
        self.set_member("IsActive", value)

    @property
    def type_(self) -> members.EmptyElement | None:
        """The controller type being used. (type of IndexController if exists or ``null``)"""
        member = self.get_member("Type")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @type_.setter
    def type_(self, value: members.EmptyElement) -> None:
        """Set Type. The controller type being used. (type of IndexController if exists or ``null``)"""
        self.set_member("Type", value)

    @property
    def battery_level(self) -> members.EmptyElement | None:
        """The battery level of this controller. (``1``: full, ``0``: empty)"""
        member = self.get_member("BatteryLevel")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @battery_level.setter
    def battery_level(self, value: members.EmptyElement) -> None:
        """Set BatteryLevel. The battery level of this controller. (``1``: full, ``0``: empty)"""
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
    def button_a(self) -> members.EmptyElement | None:
        """Shows if the A button is being pressed."""
        member = self.get_member("ButtonA")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_a.setter
    def button_a(self, value: members.EmptyElement) -> None:
        """Set ButtonA. Shows if the A button is being pressed."""
        self.set_member("ButtonA", value)

    @property
    def button_b(self) -> members.EmptyElement | None:
        """Shows if the B button is being pressed."""
        member = self.get_member("ButtonB")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_b.setter
    def button_b(self, value: members.EmptyElement) -> None:
        """Set ButtonB. Shows if the B button is being pressed."""
        self.set_member("ButtonB", value)

    @property
    def button_a_touch(self) -> members.EmptyElement | None:
        """Shows if the capacitive touch is being pressed on A button."""
        member = self.get_member("ButtonA_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_a_touch.setter
    def button_a_touch(self, value: members.EmptyElement) -> None:
        """Set ButtonA_Touch. Shows if the capacitive touch is being pressed on A button."""
        self.set_member("ButtonA_Touch", value)

    @property
    def button_b_touch(self) -> members.EmptyElement | None:
        """Shows if the capacitive touch is being pressed on B button."""
        member = self.get_member("ButtonB_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_b_touch.setter
    def button_b_touch(self, value: members.EmptyElement) -> None:
        """Set ButtonB_Touch. Shows if the capacitive touch is being pressed on B button."""
        self.set_member("ButtonB_Touch", value)

    @property
    def grip(self) -> members.EmptyElement | None:
        """Shows the strength of the grip on the device. (from ``0`` to ``1``)"""
        member = self.get_member("Grip")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip.setter
    def grip(self, value: members.EmptyElement) -> None:
        """Set Grip. Shows the strength of the grip on the device. (from ``0`` to ``1``)"""
        self.set_member("Grip", value)

    @property
    def grip_touch(self) -> members.EmptyElement | None:
        """Shows if the grip is being touched."""
        member = self.get_member("GripTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip_touch.setter
    def grip_touch(self, value: members.EmptyElement) -> None:
        """Set GripTouch. Shows if the grip is being touched."""
        self.set_member("GripTouch", value)

    @property
    def grip_click(self) -> members.EmptyElement | None:
        """Shows if the grip is being gripped enough to trigger a grab action."""
        member = self.get_member("GripClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip_click.setter
    def grip_click(self, value: members.EmptyElement) -> None:
        """Set GripClick. Shows if the grip is being gripped enough to trigger a grab action."""
        self.set_member("GripClick", value)

    @property
    def joystick(self) -> members.EmptyElement | None:
        """The position of this controller's joystick. (``[-1; -1]``: backward left, ``[+1; +1]``: forward right, ``[0; 0]``: resting position)"""
        member = self.get_member("Joystick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick.setter
    def joystick(self, value: members.EmptyElement) -> None:
        """Set Joystick. The position of this controller's joystick. (``[-1; -1]``: backward left, ``[+1; +1]``: forward right, ``[0; 0]``: resting position)"""
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
        """Shows the strength of the trigger while pressed. (from ``0`` to ``1``)"""
        member = self.get_member("Trigger")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.EmptyElement) -> None:
        """Set Trigger. Shows the strength of the trigger while pressed. (from ``0`` to ``1``)"""
        self.set_member("Trigger", value)

    @property
    def trigger_touch(self) -> members.EmptyElement | None:
        """Shows if the trigger is being touched."""
        member = self.get_member("TriggerTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_touch.setter
    def trigger_touch(self, value: members.EmptyElement) -> None:
        """Set TriggerTouch. Shows if the trigger is being touched."""
        self.set_member("TriggerTouch", value)

    @property
    def trigger_click(self) -> members.EmptyElement | None:
        """Shows if the trigger is pushed enough to trigger a click action."""
        member = self.get_member("TriggerClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_click.setter
    def trigger_click(self, value: members.EmptyElement) -> None:
        """Set TriggerClick. Shows if the trigger is pushed enough to trigger a click action."""
        self.set_member("TriggerClick", value)

    @property
    def touchpad(self) -> members.EmptyElement | None:
        """Shows the X and Y of the area where the Touchpad is touched. (``[-1; -1]``: bottom left, ``[+1; +1]``: top right, ``[0; 0]`` when untouched)"""
        member = self.get_member("Touchpad")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad.setter
    def touchpad(self, value: members.EmptyElement) -> None:
        """Set Touchpad. Shows the X and Y of the area where the Touchpad is touched. (``[-1; -1]``: bottom left, ``[+1; +1]``: top right, ``[0; 0]`` when untouched)"""
        self.set_member("Touchpad", value)

    @property
    def touchpad_touch(self) -> members.EmptyElement | None:
        """Shows if the touchpad being touched."""
        member = self.get_member("TouchpadTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_touch.setter
    def touchpad_touch(self, value: members.EmptyElement) -> None:
        """Set TouchpadTouch. Shows if the touchpad being touched."""
        self.set_member("TouchpadTouch", value)

    @property
    def touchpad_press(self) -> members.EmptyElement | None:
        """Shows if the touchpad being touched enough to trigger a click action."""
        member = self.get_member("TouchpadPress")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_press.setter
    def touchpad_press(self, value: members.EmptyElement) -> None:
        """Set TouchpadPress. Shows if the touchpad being touched enough to trigger a click action."""
        self.set_member("TouchpadPress", value)

    @property
    def touchpad_force(self) -> members.EmptyElement | None:
        """Shows the strength of the touch on the touchpad. (from ``0`` to ``1``)"""
        member = self.get_member("TouchpadForce")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_force.setter
    def touchpad_force(self, value: members.EmptyElement) -> None:
        """Set TouchpadForce. Shows the strength of the touch on the touchpad. (from ``0`` to ``1``)"""
        self.set_member("TouchpadForce", value)

