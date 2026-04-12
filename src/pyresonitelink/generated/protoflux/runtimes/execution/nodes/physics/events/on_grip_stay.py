"""Generated component: OnGripStay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.locomotion_grip import LocomotionGrip
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnGripStay(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The On Grip Stay node takes in a global reference of a LocomotionGrip, and fires an event when the grip is happening per frame, as well as information of the locomotion module and the body node that is gripping.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics/Events
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.OnGripStay"

    def __init__(self, grip: str | IGlobalValueProxy[LocomotionGrip] | None = None, on_event: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grip: Initial value for Grip.
            on_event: Initial value for OnEvent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grip is not None:
            self.grip = grip
        if on_event is not None:
            self.on_event = on_event

    @property
    def grip(self) -> str | None:
        """Target ID of the Grip reference (targets IGlobalValueProxy[LocomotionGrip])."""
        member = self.get_member("Grip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grip.setter
    def grip(self, target: str | IGlobalValueProxy[LocomotionGrip] | None) -> None:
        """Set the Grip reference by target ID or IGlobalValueProxy[LocomotionGrip] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Grip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Grip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.LocomotionGrip>'),
            )

    @property
    def on_event(self) -> str | None:
        """Fires when the grip is being used by the user."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_event.setter
    def on_event(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnEvent reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnEvent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def module(self) -> members.EmptyElement | None:
        """Returns the module that is gripping."""
        member = self.get_member("Module")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @module.setter
    def module(self, value: members.EmptyElement) -> None:
        """Set Module. Returns the module that is gripping."""
        self.set_member("Module", value)

    @property
    def gripping_body_node(self) -> members.EmptyElement | None:
        """Returns the body node that is gripping."""
        member = self.get_member("GrippingBodyNode")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gripping_body_node.setter
    def gripping_body_node(self, value: members.EmptyElement) -> None:
        """Set GrippingBodyNode. Returns the body node that is gripping."""
        self.set_member("GrippingBodyNode", value)

