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

    **Outputs**: === IsActive (Bool) ===

Bool for showing if the device is active. Useful for troubleshooting if your controller is not responding.
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
    def button_a(self) -> members.EmptyElement | None:
        """The ButtonA member."""
        member = self.get_member("ButtonA")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_a.setter
    def button_a(self, value: members.EmptyElement) -> None:
        """Set the ButtonA member."""
        self.set_member("ButtonA", value)

    @property
    def button_b(self) -> members.EmptyElement | None:
        """The ButtonB member."""
        member = self.get_member("ButtonB")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_b.setter
    def button_b(self, value: members.EmptyElement) -> None:
        """Set the ButtonB member."""
        self.set_member("ButtonB", value)

    @property
    def button_a_touch(self) -> members.EmptyElement | None:
        """The ButtonA_Touch member."""
        member = self.get_member("ButtonA_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_a_touch.setter
    def button_a_touch(self, value: members.EmptyElement) -> None:
        """Set the ButtonA_Touch member."""
        self.set_member("ButtonA_Touch", value)

    @property
    def button_b_touch(self) -> members.EmptyElement | None:
        """The ButtonB_Touch member."""
        member = self.get_member("ButtonB_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_b_touch.setter
    def button_b_touch(self, value: members.EmptyElement) -> None:
        """Set the ButtonB_Touch member."""
        self.set_member("ButtonB_Touch", value)

    @property
    def grip(self) -> members.EmptyElement | None:
        """The Grip member."""
        member = self.get_member("Grip")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip.setter
    def grip(self, value: members.EmptyElement) -> None:
        """Set the Grip member."""
        self.set_member("Grip", value)

    @property
    def grip_touch(self) -> members.EmptyElement | None:
        """The GripTouch member."""
        member = self.get_member("GripTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip_touch.setter
    def grip_touch(self, value: members.EmptyElement) -> None:
        """Set the GripTouch member."""
        self.set_member("GripTouch", value)

    @property
    def grip_click(self) -> members.EmptyElement | None:
        """The GripClick member."""
        member = self.get_member("GripClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip_click.setter
    def grip_click(self, value: members.EmptyElement) -> None:
        """Set the GripClick member."""
        self.set_member("GripClick", value)

    @property
    def joystick(self) -> members.EmptyElement | None:
        """The Joystick member."""
        member = self.get_member("Joystick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick.setter
    def joystick(self, value: members.EmptyElement) -> None:
        """Set the Joystick member."""
        self.set_member("Joystick", value)

    @property
    def joystick_touch(self) -> members.EmptyElement | None:
        """The JoystickTouch member."""
        member = self.get_member("JoystickTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick_touch.setter
    def joystick_touch(self, value: members.EmptyElement) -> None:
        """Set the JoystickTouch member."""
        self.set_member("JoystickTouch", value)

    @property
    def joystick_click(self) -> members.EmptyElement | None:
        """The JoystickClick member."""
        member = self.get_member("JoystickClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @joystick_click.setter
    def joystick_click(self, value: members.EmptyElement) -> None:
        """Set the JoystickClick member."""
        self.set_member("JoystickClick", value)

    @property
    def trigger(self) -> members.EmptyElement | None:
        """The Trigger member."""
        member = self.get_member("Trigger")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.EmptyElement) -> None:
        """Set the Trigger member."""
        self.set_member("Trigger", value)

    @property
    def trigger_touch(self) -> members.EmptyElement | None:
        """The TriggerTouch member."""
        member = self.get_member("TriggerTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_touch.setter
    def trigger_touch(self, value: members.EmptyElement) -> None:
        """Set the TriggerTouch member."""
        self.set_member("TriggerTouch", value)

    @property
    def trigger_click(self) -> members.EmptyElement | None:
        """The TriggerClick member."""
        member = self.get_member("TriggerClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_click.setter
    def trigger_click(self, value: members.EmptyElement) -> None:
        """Set the TriggerClick member."""
        self.set_member("TriggerClick", value)

    @property
    def touchpad(self) -> members.EmptyElement | None:
        """The Touchpad member."""
        member = self.get_member("Touchpad")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad.setter
    def touchpad(self, value: members.EmptyElement) -> None:
        """Set the Touchpad member."""
        self.set_member("Touchpad", value)

    @property
    def touchpad_touch(self) -> members.EmptyElement | None:
        """The TouchpadTouch member."""
        member = self.get_member("TouchpadTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_touch.setter
    def touchpad_touch(self, value: members.EmptyElement) -> None:
        """Set the TouchpadTouch member."""
        self.set_member("TouchpadTouch", value)

    @property
    def touchpad_press(self) -> members.EmptyElement | None:
        """The TouchpadPress member."""
        member = self.get_member("TouchpadPress")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_press.setter
    def touchpad_press(self, value: members.EmptyElement) -> None:
        """Set the TouchpadPress member."""
        self.set_member("TouchpadPress", value)

    @property
    def touchpad_force(self) -> members.EmptyElement | None:
        """The TouchpadForce member."""
        member = self.get_member("TouchpadForce")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_force.setter
    def touchpad_force(self, value: members.EmptyElement) -> None:
        """Set the TouchpadForce member."""
        self.set_member("TouchpadForce", value)

