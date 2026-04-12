"""Generated component: TouchController."""

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


class TouchController(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """* User: User: Equipee of the controller. should not be null. * Node: Chirality: The side of the controller. should not be null.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers

    **Input**: * User: User: Equipee of the controller. should not be null.
* Node: Chirality: The side of the controller. should not be null.

    **Output**: * IsActive: Bool: is controller active?
* Type: Type: The internal class for handling device I/O. Defaults to null.
* BatteryLevel: Float: How its battery is charged? Default to -1 if it cannot be retrieved.
* IsBatteryCharging: Bool
* Model: Model
* Start: Bool
* ButtonYB: Bool: are they pressed?
* ButtonXA: Bool: are they pressed?
* ButtonYB_Touch: are they touched?
* ButtonXA_Touch: are they touched?
* ThumbRestTouch: are there touched input key where touchable by thumb other than buttons and joysticks? (Requires verification: does this include joystick touch?)
* Grip: Float: press strength of grip. Between 0 (not gripped) and 1 (completely gripped).
* GripClick: Bool: is grip pressed?
* Joystick: Float2: reports rotation amount by each axis.
* JoystickTouch: Bool: is joystick touched?
* JoystickClick: Bool: is joystick clicked down?
* Trigger: Float: press strength of trigger. Same as Grip.
* TriggerTouch: Bool: is trigger touched?
* TriggerClick: Bool: is trigger clicked?
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.TouchController"

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
    def model(self) -> members.EmptyElement | None:
        """The Model member."""
        member = self.get_member("Model")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @model.setter
    def model(self, value: members.EmptyElement) -> None:
        """Set the Model member."""
        self.set_member("Model", value)

    @property
    def start(self) -> members.EmptyElement | None:
        """The Start member."""
        member = self.get_member("Start")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @start.setter
    def start(self, value: members.EmptyElement) -> None:
        """Set the Start member."""
        self.set_member("Start", value)

    @property
    def button_yb(self) -> members.EmptyElement | None:
        """The ButtonYB member."""
        member = self.get_member("ButtonYB")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_yb.setter
    def button_yb(self, value: members.EmptyElement) -> None:
        """Set the ButtonYB member."""
        self.set_member("ButtonYB", value)

    @property
    def button_xa(self) -> members.EmptyElement | None:
        """The ButtonXA member."""
        member = self.get_member("ButtonXA")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_xa.setter
    def button_xa(self, value: members.EmptyElement) -> None:
        """Set the ButtonXA member."""
        self.set_member("ButtonXA", value)

    @property
    def button_yb_touch(self) -> members.EmptyElement | None:
        """The ButtonYB_Touch member."""
        member = self.get_member("ButtonYB_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_yb_touch.setter
    def button_yb_touch(self, value: members.EmptyElement) -> None:
        """Set the ButtonYB_Touch member."""
        self.set_member("ButtonYB_Touch", value)

    @property
    def button_xa_touch(self) -> members.EmptyElement | None:
        """The ButtonXA_Touch member."""
        member = self.get_member("ButtonXA_Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @button_xa_touch.setter
    def button_xa_touch(self, value: members.EmptyElement) -> None:
        """Set the ButtonXA_Touch member."""
        self.set_member("ButtonXA_Touch", value)

    @property
    def thumb_rest_touch(self) -> members.EmptyElement | None:
        """The ThumbRestTouch member."""
        member = self.get_member("ThumbRestTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @thumb_rest_touch.setter
    def thumb_rest_touch(self, value: members.EmptyElement) -> None:
        """Set the ThumbRestTouch member."""
        self.set_member("ThumbRestTouch", value)

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

