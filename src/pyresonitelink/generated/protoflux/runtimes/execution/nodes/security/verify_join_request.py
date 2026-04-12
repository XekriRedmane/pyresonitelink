"""Generated component: VerifyJoinRequest."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VerifyJoinRequest(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Verify Join Request node listens for join requests when users join a world with an enabled join verification system, firing an event when it happens. This node returns a set of information that contains info of the joining user. This node can be combined with the Allow Join, Deny Join, and Assign Role nodes.

To activate a join verification system, a user needs to open the node in a Scene Inspector and go to the VerifyJoinRequest component. The bottom of the component has a button labeled "Set as custom join request verifier" and a warning letting users know that this feature does not prevent tampering of worlds that use this feature.

The following is the exact warning inside this node:

    Category: ProtoFlux/Runtimes/Execution/Nodes/Security
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.VerifyJoinRequest"

    def __init__(self, verify: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            verify: Initial value for Verify.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if verify is not None:
            self.verify = verify

    @property
    def verify(self) -> str | None:
        """Fires when a user is wanting to join the world."""
        member = self.get_member("Verify")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @verify.setter
    def verify(self, target: str | INodeOperation | None) -> None:
        """Set the Verify reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Verify")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Verify",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
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
    def user_session_id(self) -> members.EmptyElement | None:
        """The UserSessionId member."""
        member = self.get_member("UserSessionId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @user_session_id.setter
    def user_session_id(self, value: members.EmptyElement) -> None:
        """Set the UserSessionId member."""
        self.set_member("UserSessionId", value)

    @property
    def machine_id(self) -> members.EmptyElement | None:
        """The MachineId member."""
        member = self.get_member("MachineId")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @machine_id.setter
    def machine_id(self, value: members.EmptyElement) -> None:
        """Set the MachineId member."""
        self.set_member("MachineId", value)

    @property
    def username(self) -> members.EmptyElement | None:
        """The username that is wanting to join the world."""
        member = self.get_member("Username")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @username.setter
    def username(self, value: members.EmptyElement) -> None:
        """Set Username. The username that is wanting to join the world."""
        self.set_member("Username", value)

    @property
    def head_output_device(self) -> members.EmptyElement | None:
        """The joining user's head output device."""
        member = self.get_member("HeadOutputDevice")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @head_output_device.setter
    def head_output_device(self, value: members.EmptyElement) -> None:
        """Set HeadOutputDevice. The joining user's head output device."""
        self.set_member("HeadOutputDevice", value)

    @property
    def platform(self) -> members.EmptyElement | None:
        """The joining user's platform."""
        member = self.get_member("Platform")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @platform.setter
    def platform(self, value: members.EmptyElement) -> None:
        """Set Platform. The joining user's platform."""
        self.set_member("Platform", value)

    @property
    def is_invited(self) -> members.EmptyElement | None:
        """Returns if this joining user was invited."""
        member = self.get_member("IsInvited")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_invited.setter
    def is_invited(self, value: members.EmptyElement) -> None:
        """Set IsInvited. Returns if this joining user was invited."""
        self.set_member("IsInvited", value)

    @property
    def is_contact(self) -> members.EmptyElement | None:
        """Returns if this joining user is in the host's contacts list."""
        member = self.get_member("IsContact")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_contact.setter
    def is_contact(self, value: members.EmptyElement) -> None:
        """Set IsContact. Returns if this joining user is in the host's contacts list."""
        self.set_member("IsContact", value)

    @property
    def is_in_kiosk_mode(self) -> members.EmptyElement | None:
        """Returns if this joining user is in kiosk mode."""
        member = self.get_member("IsInKioskMode")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_in_kiosk_mode.setter
    def is_in_kiosk_mode(self, value: members.EmptyElement) -> None:
        """Set IsInKioskMode. Returns if this joining user is in kiosk mode."""
        self.set_member("IsInKioskMode", value)

    @property
    def is_spectator_banned(self) -> members.EmptyElement | None:
        """Returns if this joining user was banned as a spectator."""
        member = self.get_member("IsSpectatorBanned")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_spectator_banned.setter
    def is_spectator_banned(self, value: members.EmptyElement) -> None:
        """Set IsSpectatorBanned. Returns if this joining user was banned as a spectator."""
        self.set_member("IsSpectatorBanned", value)

    @property
    def is_mute_banned(self) -> members.EmptyElement | None:
        """Returns if this joining user was banned and muted."""
        member = self.get_member("IsMuteBanned")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_mute_banned.setter
    def is_mute_banned(self, value: members.EmptyElement) -> None:
        """Set IsMuteBanned. Returns if this joining user was banned and muted."""
        self.set_member("IsMuteBanned", value)

    @property
    def handle(self) -> members.EmptyElement | None:
        """Returns this join request as a type."""
        member = self.get_member("Handle")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @handle.setter
    def handle(self, value: members.EmptyElement) -> None:
        """Set Handle. Returns this join request as a type."""
        self.set_member("Handle", value)

