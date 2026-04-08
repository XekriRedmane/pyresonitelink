"""Generated component: OnLocomotionGripEnd."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.physical_locomotion import PhysicalLocomotion
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnLocomotionGripEnd(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The On Locomotion Grip End node takes in a global reference from a user's PhysicalLocomotion. And fires when a grip ends that relates to that locomotion along with the data of the slot, position in 3D space, and what side of the user's grip it was.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics/Events
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.OnLocomotionGripEnd"

    def __init__(self, locomotion: str | IGlobalValueProxy[PhysicalLocomotion] | None = None, on_event: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locomotion: Initial value for Locomotion.
            on_event: Initial value for OnEvent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locomotion is not None:
            self.locomotion = locomotion
        if on_event is not None:
            self.on_event = on_event

    @property
    def locomotion(self) -> str | None:
        """Target ID of the Locomotion reference (targets IGlobalValueProxy[PhysicalLocomotion])."""
        member = self.get_member("Locomotion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion.setter
    def locomotion(self, target: str | IGlobalValueProxy[PhysicalLocomotion] | None) -> None:
        """Set the Locomotion reference by target ID or IGlobalValueProxy[PhysicalLocomotion] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Locomotion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Locomotion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.PhysicalLocomotion>'),
            )

    @property
    def on_event(self) -> str | None:
        """Target ID of the OnEvent reference (targets ISyncNodeOperation)."""
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
    def gripped_slot(self) -> members.EmptyElement | None:
        """The GrippedSlot member."""
        member = self.get_member("GrippedSlot")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gripped_slot.setter
    def gripped_slot(self, value: members.EmptyElement) -> None:
        """Set the GrippedSlot member."""
        self.set_member("GrippedSlot", value)

    @property
    def gripped_point(self) -> members.EmptyElement | None:
        """The GrippedPoint member."""
        member = self.get_member("GrippedPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gripped_point.setter
    def gripped_point(self, value: members.EmptyElement) -> None:
        """Set the GrippedPoint member."""
        self.set_member("GrippedPoint", value)

    @property
    def gripping_hand(self) -> members.EmptyElement | None:
        """The GrippingHand member."""
        member = self.get_member("GrippingHand")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gripping_hand.setter
    def gripping_hand(self, value: members.EmptyElement) -> None:
        """Set the GrippingHand member."""
        self.set_member("GrippingHand", value)

