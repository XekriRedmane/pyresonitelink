"""Generated component: ViveController."""

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


class ViveController(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides information provided by HTC Vive wand controllers.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Controllers
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.ViveController"

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
    def grip(self) -> members.EmptyElement | None:
        """Is the controller's grip clicked down right now."""
        member = self.get_member("Grip")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @grip.setter
    def grip(self, value: members.EmptyElement) -> None:
        """Set Grip. Is the controller's grip clicked down right now."""
        self.set_member("Grip", value)

    @property
    def app(self) -> members.EmptyElement | None:
        """Is the app button pressed right now."""
        member = self.get_member("App")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @app.setter
    def app(self, value: members.EmptyElement) -> None:
        """Set App. Is the app button pressed right now."""
        self.set_member("App", value)

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
    def trigger_hair(self) -> members.EmptyElement | None:
        """Is the controller's trigger hair being used right now."""
        member = self.get_member("TriggerHair")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @trigger_hair.setter
    def trigger_hair(self, value: members.EmptyElement) -> None:
        """Set TriggerHair. Is the controller's trigger hair being used right now."""
        self.set_member("TriggerHair", value)

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

    @property
    def touchpad(self) -> members.EmptyElement | None:
        """The position of this controller's touchpad."""
        member = self.get_member("Touchpad")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad.setter
    def touchpad(self, value: members.EmptyElement) -> None:
        """Set Touchpad. The position of this controller's touchpad."""
        self.set_member("Touchpad", value)

    @property
    def touchpad_touch(self) -> members.EmptyElement | None:
        """Is the controller's touchpad being touched right now."""
        member = self.get_member("TouchpadTouch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_touch.setter
    def touchpad_touch(self, value: members.EmptyElement) -> None:
        """Set TouchpadTouch. Is the controller's touchpad being touched right now."""
        self.set_member("TouchpadTouch", value)

    @property
    def touchpad_click(self) -> members.EmptyElement | None:
        """Is the controller's touchpad clicked down right now."""
        member = self.get_member("TouchpadClick")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touchpad_click.setter
    def touchpad_click(self, value: members.EmptyElement) -> None:
        """Set TouchpadClick. Is the controller's touchpad clicked down right now."""
        self.set_member("TouchpadClick", value)

