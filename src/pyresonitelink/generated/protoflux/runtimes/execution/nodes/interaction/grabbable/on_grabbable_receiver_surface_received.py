"""Generated component: OnGrabbableReceiverSurfaceReceived."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.grabbable_receiver_surface import GrabbableReceiverSurface
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnGrabbableReceiverSurfaceReceived(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """On Grabbable Receiver Surface Received is a ProtoFlux node that monitors a Reciever for when a grabbable is let go of and is received by the Source (GrabbableReceiverSurface). The node then sends an Impulse.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Grabbable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReceiverSurfaceReceived"

    def __init__(self, source: str | IGlobalValueProxy[GrabbableReceiverSurface] | None = None, on_received: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            on_received: Initial value for OnReceived.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if on_received is not None:
            self.on_received = on_received

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IGlobalValueProxy[GrabbableReceiverSurface])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IGlobalValueProxy[GrabbableReceiverSurface] | None) -> None:
        """Set the Source reference by target ID or IGlobalValueProxy[GrabbableReceiverSurface] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.GrabbableReceiverSurface>'),
            )

    @property
    def on_received(self) -> str | None:
        """Sends an impulse when Grabbable (IGrabbable) is let go of and is received by the Source (GrabbableReceiverSurface)."""
        member = self.get_member("OnReceived")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_received.setter
    def on_received(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnReceived reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReceived")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReceived",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def received_grabbable(self) -> members.EmptyElement | None:
        """The ReceivedGrabbable member."""
        member = self.get_member("ReceivedGrabbable")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @received_grabbable.setter
    def received_grabbable(self, value: members.EmptyElement) -> None:
        """Set the ReceivedGrabbable member."""
        self.set_member("ReceivedGrabbable", value)

    @property
    def from_grabber(self) -> members.EmptyElement | None:
        """The grabber that let go of the RecievedGrabbable (IGrabbable)."""
        member = self.get_member("FromGrabber")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @from_grabber.setter
    def from_grabber(self, value: members.EmptyElement) -> None:
        """Set FromGrabber. The grabber that let go of the RecievedGrabbable (IGrabbable)."""
        self.set_member("FromGrabber", value)

