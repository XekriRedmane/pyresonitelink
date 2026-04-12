"""Generated component: TwitchRewardRedeemEvent."""

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


class TwitchRewardRedeemEvent(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node provides Twitch reward redeem information from a TwitchInterface. 

Note that all outputs are generated on a new Twitch reward redeem, and will not display any information when connected to a display node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Twitch

    **Legacy Twitch API**: Due to the depreciation of the Twitch V5 API that Resonite currently uses, this node will fail to pulse on a redeem event from Twitch. This means currently that this node is inoperable, and should be considered unusable until updated.

The issue is marked as a bug on the Resonite GitHub under Issue 68.
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchRewardRedeemEvent"

    def __init__(self, interface: str | IGlobalValueProxy[TwitchInterface] | None = None, on_redeem: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interface: Initial value for Interface.
            on_redeem: Initial value for OnRedeem.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interface is not None:
            self.interface = interface
        if on_redeem is not None:
            self.on_redeem = on_redeem

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
    def on_redeem(self) -> str | None:
        """Target ID of the OnRedeem reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnRedeem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_redeem.setter
    def on_redeem(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnRedeem reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnRedeem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRedeem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

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
    def time_stamp(self) -> members.EmptyElement | None:
        """The TimeStamp member."""
        member = self.get_member("TimeStamp")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @time_stamp.setter
    def time_stamp(self, value: members.EmptyElement) -> None:
        """Set the TimeStamp member."""
        self.set_member("TimeStamp", value)

    @property
    def reward_id(self) -> members.EmptyElement | None:
        """The RewardId member."""
        member = self.get_member("RewardId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reward_id.setter
    def reward_id(self, value: members.EmptyElement) -> None:
        """Set the RewardId member."""
        self.set_member("RewardId", value)

    @property
    def reward_title(self) -> members.EmptyElement | None:
        """The RewardTitle member."""
        member = self.get_member("RewardTitle")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reward_title.setter
    def reward_title(self, value: members.EmptyElement) -> None:
        """Set the RewardTitle member."""
        self.set_member("RewardTitle", value)

    @property
    def reward_prompt(self) -> members.EmptyElement | None:
        """The RewardPrompt member."""
        member = self.get_member("RewardPrompt")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reward_prompt.setter
    def reward_prompt(self, value: members.EmptyElement) -> None:
        """Set the RewardPrompt member."""
        self.set_member("RewardPrompt", value)

    @property
    def status(self) -> members.EmptyElement | None:
        """The Status member."""
        member = self.get_member("Status")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @status.setter
    def status(self, value: members.EmptyElement) -> None:
        """Set the Status member."""
        self.set_member("Status", value)

    @property
    def reward_cost(self) -> members.EmptyElement | None:
        """The RewardCost member."""
        member = self.get_member("RewardCost")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reward_cost.setter
    def reward_cost(self, value: members.EmptyElement) -> None:
        """Set the RewardCost member."""
        self.set_member("RewardCost", value)

