"""Generated component: TwitchChatMessageEvent."""

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


class TwitchChatMessageEvent(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides Twitch chat message information from a TwitchInterface. 

Note that all outputs are generated on a new Twitch chat message, and will not display any information when connected to a display node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Twitch
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchChatMessageEvent"

    def __init__(self, interface: str | IGlobalValueProxy[TwitchInterface] | None = None, on_message: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interface: Initial value for Interface.
            on_message: Initial value for OnMessage.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interface is not None:
            self.interface = interface
        if on_message is not None:
            self.on_message = on_message

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
    def on_message(self) -> str | None:
        """Fires on receiving a new Twitch chat message."""
        member = self.get_member("OnMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_message.setter
    def on_message(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnMessage reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def message(self) -> members.EmptyElement | None:
        """Outputs the contents of the message as a text string."""
        member = self.get_member("Message")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @message.setter
    def message(self, value: members.EmptyElement) -> None:
        """Set Message. Outputs the contents of the message as a text string."""
        self.set_member("Message", value)

    @property
    def user_id(self) -> members.EmptyElement | None:
        """Outputs the Twitch Channel ID of the message sender."""
        member = self.get_member("UserId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user_id.setter
    def user_id(self, value: members.EmptyElement) -> None:
        """Set UserId. Outputs the Twitch Channel ID of the message sender."""
        self.set_member("UserId", value)

    @property
    def display_name(self) -> members.EmptyElement | None:
        """Outputs the Twitch username of the message sender."""
        member = self.get_member("DisplayName")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @display_name.setter
    def display_name(self, value: members.EmptyElement) -> None:
        """Set DisplayName. Outputs the Twitch username of the message sender."""
        self.set_member("DisplayName", value)

    @property
    def color(self) -> members.EmptyElement | None:
        """Outputs the Twitch chat color of the message sender."""
        member = self.get_member("Color")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @color.setter
    def color(self, value: members.EmptyElement) -> None:
        """Set Color. Outputs the Twitch chat color of the message sender."""
        self.set_member("Color", value)

    @property
    def is_highlighted(self) -> members.EmptyElement | None:
        """Shows if the chat message is highlighted."""
        member = self.get_member("IsHighlighted")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_highlighted.setter
    def is_highlighted(self, value: members.EmptyElement) -> None:
        """Set IsHighlighted. Shows if the chat message is highlighted."""
        self.set_member("IsHighlighted", value)

    @property
    def is_subscriber(self) -> members.EmptyElement | None:
        """Shows if the chat message sender is subscribed to the Twitch channel."""
        member = self.get_member("IsSubscriber")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_subscriber.setter
    def is_subscriber(self, value: members.EmptyElement) -> None:
        """Set IsSubscriber. Shows if the chat message sender is subscribed to the Twitch channel."""
        self.set_member("IsSubscriber", value)

    @property
    def is_moderator(self) -> members.EmptyElement | None:
        """Shows if the chat message sender is a moderator of the Twitch channel."""
        member = self.get_member("IsModerator")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_moderator.setter
    def is_moderator(self, value: members.EmptyElement) -> None:
        """Set IsModerator. Shows if the chat message sender is a moderator of the Twitch channel."""
        self.set_member("IsModerator", value)

    @property
    def is_broadcaster(self) -> members.EmptyElement | None:
        """Shows if the chat message sender is from the Twitch channel, or broadcaster."""
        member = self.get_member("IsBroadcaster")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_broadcaster.setter
    def is_broadcaster(self, value: members.EmptyElement) -> None:
        """Set IsBroadcaster. Shows if the chat message sender is from the Twitch channel, or broadcaster."""
        self.set_member("IsBroadcaster", value)

    @property
    def is_turbo(self) -> members.EmptyElement | None:
        """Shows if the chat message sender is subscribed to Twitch Turbo."""
        member = self.get_member("IsTurbo")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_turbo.setter
    def is_turbo(self, value: members.EmptyElement) -> None:
        """Set IsTurbo. Shows if the chat message sender is subscribed to Twitch Turbo."""
        self.set_member("IsTurbo", value)

    @property
    def is_vip(self) -> members.EmptyElement | None:
        """Shows if the chat message sender is a VIP in the Twitch channel."""
        member = self.get_member("IsVIP")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_vip.setter
    def is_vip(self, value: members.EmptyElement) -> None:
        """Set IsVIP. Shows if the chat message sender is a VIP in the Twitch channel."""
        self.set_member("IsVIP", value)

    @property
    def cheer_badge(self) -> members.EmptyElement | None:
        """Shows the current cheer chat badge of the chat message sender."""
        member = self.get_member("CheerBadge")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @cheer_badge.setter
    def cheer_badge(self, value: members.EmptyElement) -> None:
        """Set CheerBadge. Shows the current cheer chat badge of the chat message sender."""
        self.set_member("CheerBadge", value)

    @property
    def cheer_amount(self) -> members.EmptyElement | None:
        """Shows the cheer amount if the chat message includes any bits."""
        member = self.get_member("CheerAmount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @cheer_amount.setter
    def cheer_amount(self, value: members.EmptyElement) -> None:
        """Set CheerAmount. Shows the cheer amount if the chat message includes any bits."""
        self.set_member("CheerAmount", value)

    @property
    def bits(self) -> members.EmptyElement | None:
        """Shows the bit amount if the chat message includes any."""
        member = self.get_member("Bits")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bits.setter
    def bits(self, value: members.EmptyElement) -> None:
        """Set Bits. Shows the bit amount if the chat message includes any."""
        self.set_member("Bits", value)

    @property
    def bits_dollars(self) -> members.EmptyElement | None:
        """Shows the bit amount in USD (United States Dollars), as a double value."""
        member = self.get_member("BitsDollars")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bits_dollars.setter
    def bits_dollars(self, value: members.EmptyElement) -> None:
        """Set BitsDollars. Shows the bit amount in USD (United States Dollars), as a double value."""
        self.set_member("BitsDollars", value)

    @property
    def subscribed_month_count(self) -> members.EmptyElement | None:
        """Shows the amount of months the chat message sender is subscribed to the channel."""
        member = self.get_member("SubscribedMonthCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @subscribed_month_count.setter
    def subscribed_month_count(self, value: members.EmptyElement) -> None:
        """Set SubscribedMonthCount. Shows the amount of months the chat message sender is subscribed to the channel."""
        self.set_member("SubscribedMonthCount", value)

    @property
    def custom_reward_id(self) -> members.EmptyElement | None:
        """If the chat message was sent with a custom reward redeem, shows the ID of the custom reward.
This will only output the custom reward ID if the redeem has the "Require Viewer to Enter Text" option enabled."""
        member = self.get_member("CustomRewardId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @custom_reward_id.setter
    def custom_reward_id(self, value: members.EmptyElement) -> None:
        """Set CustomRewardId. If the chat message was sent with a custom reward redeem, shows the ID of the custom reward.
This will only output the custom reward ID if the redeem has the "Require Viewer to Enter Text" option enabled."""
        self.set_member("CustomRewardId", value)

