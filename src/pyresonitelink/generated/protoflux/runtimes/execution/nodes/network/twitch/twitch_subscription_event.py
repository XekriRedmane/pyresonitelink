"""Generated component: TwitchSubscriptionEvent."""

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


class TwitchSubscriptionEvent(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchSubscriptionEvent.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Twitch
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchSubscriptionEvent"

    def __init__(self, interface: str | IGlobalValueProxy[TwitchInterface] | None = None, on_subscription: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interface: Initial value for Interface.
            on_subscription: Initial value for OnSubscription.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interface is not None:
            self.interface = interface
        if on_subscription is not None:
            self.on_subscription = on_subscription

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
    def on_subscription(self) -> str | None:
        """Target ID of the OnSubscription reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnSubscription")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_subscription.setter
    def on_subscription(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnSubscription reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSubscription")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSubscription",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def user_id(self) -> members.EmptyElement | None:
        """The UserId member."""
        member = self.get_member("UserId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user_id.setter
    def user_id(self, value: members.EmptyElement) -> None:
        """Set the UserId member."""
        self.set_member("UserId", value)

    @property
    def display_name(self) -> members.EmptyElement | None:
        """The DisplayName member."""
        member = self.get_member("DisplayName")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @display_name.setter
    def display_name(self, value: members.EmptyElement) -> None:
        """Set the DisplayName member."""
        self.set_member("DisplayName", value)

    @property
    def message(self) -> members.EmptyElement | None:
        """The Message member."""
        member = self.get_member("Message")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @message.setter
    def message(self, value: members.EmptyElement) -> None:
        """Set the Message member."""
        self.set_member("Message", value)

    @property
    def months(self) -> members.EmptyElement | None:
        """The Months member."""
        member = self.get_member("Months")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @months.setter
    def months(self, value: members.EmptyElement) -> None:
        """Set the Months member."""
        self.set_member("Months", value)

    @property
    def plan(self) -> members.EmptyElement | None:
        """The Plan member."""
        member = self.get_member("Plan")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @plan.setter
    def plan(self, value: members.EmptyElement) -> None:
        """Set the Plan member."""
        self.set_member("Plan", value)

    @property
    def is_resub(self) -> members.EmptyElement | None:
        """The IsResub member."""
        member = self.get_member("IsResub")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_resub.setter
    def is_resub(self, value: members.EmptyElement) -> None:
        """Set the IsResub member."""
        self.set_member("IsResub", value)

    @property
    def is_gifted(self) -> members.EmptyElement | None:
        """The IsGifted member."""
        member = self.get_member("IsGifted")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_gifted.setter
    def is_gifted(self, value: members.EmptyElement) -> None:
        """Set the IsGifted member."""
        self.set_member("IsGifted", value)

    @property
    def gifted_by(self) -> members.EmptyElement | None:
        """The GiftedBy member."""
        member = self.get_member("GiftedBy")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gifted_by.setter
    def gifted_by(self, value: members.EmptyElement) -> None:
        """Set the GiftedBy member."""
        self.set_member("GiftedBy", value)

    @property
    def is_anonymous(self) -> members.EmptyElement | None:
        """The IsAnonymous member."""
        member = self.get_member("IsAnonymous")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_anonymous.setter
    def is_anonymous(self, value: members.EmptyElement) -> None:
        """Set the IsAnonymous member."""
        self.set_member("IsAnonymous", value)

