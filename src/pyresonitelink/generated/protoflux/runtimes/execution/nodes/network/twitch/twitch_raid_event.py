"""Generated component: TwitchRaidEvent."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.twitch_interface import TwitchInterface
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TwitchRaidEvent(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides Twitch raid information from a TwitchInterface. 

Note that all outputs are generated on a new Twitch raid event, and will not display any information when connected to a display node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Twitch
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchRaidEvent"

    def __init__(self, interface: str | IGlobalValueProxy[TwitchInterface] | None = None, on_raid: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interface: Initial value for Interface.
            on_raid: Initial value for OnRaid.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interface is not None:
            self.interface = interface
        if on_raid is not None:
            self.on_raid = on_raid

    @property
    def interface(self) -> str | None:
        """Target ID of the Interface reference (targets IGlobalValueProxy[TwitchInterface])."""
        member = self.get_member("Interface")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interface.setter
    def interface(self, target: str | IGlobalValueProxy[TwitchInterface] | None) -> None:
        """Set the Interface reference by target ID or IGlobalValueProxy[TwitchInterface] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Interface")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Interface",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.TwitchInterface>'),
            )

    @property
    def on_raid(self) -> str | None:
        """Fires on receiving a new Twitch raid."""
        member = self.get_member("OnRaid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_raid.setter
    def on_raid(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnRaid reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnRaid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRaid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def user_id(self) -> members.EmptyElement | None:
        """Outputs the Twitch Channel ID of the raider."""
        member = self.get_member("UserId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user_id.setter
    def user_id(self, value: members.EmptyElement) -> None:
        """Set UserId. Outputs the Twitch Channel ID of the raider."""
        self.set_member("UserId", value)

    @property
    def display_name(self) -> members.EmptyElement | None:
        """Outputs the Twitch username of the raider."""
        member = self.get_member("DisplayName")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @display_name.setter
    def display_name(self, value: members.EmptyElement) -> None:
        """Set DisplayName. Outputs the Twitch username of the raider."""
        self.set_member("DisplayName", value)

    @property
    def color(self) -> members.EmptyElement | None:
        """Outputs the Twitch chat color of the raider."""
        member = self.get_member("Color")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @color.setter
    def color(self, value: members.EmptyElement) -> None:
        """Set Color. Outputs the Twitch chat color of the raider."""
        self.set_member("Color", value)

    @property
    def viewer_count(self) -> members.EmptyElement | None:
        """Shows the amount of viewers who are raiding with the raider."""
        member = self.get_member("ViewerCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @viewer_count.setter
    def viewer_count(self, value: members.EmptyElement) -> None:
        """Set ViewerCount. Shows the amount of viewers who are raiding with the raider."""
        self.set_member("ViewerCount", value)

    @property
    def is_subscriber(self) -> members.EmptyElement | None:
        """Shows if the raider is subscribed to the Twitch channel."""
        member = self.get_member("IsSubscriber")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_subscriber.setter
    def is_subscriber(self, value: members.EmptyElement) -> None:
        """Set IsSubscriber. Shows if the raider is subscribed to the Twitch channel."""
        self.set_member("IsSubscriber", value)

