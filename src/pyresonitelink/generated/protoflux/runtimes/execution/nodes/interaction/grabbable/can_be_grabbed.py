"""Generated component: CanBeGrabbed."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CanBeGrabbed(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Can Be Grabbed`` node takes in a slot and a grabber from a user, and checks if this slot can be grabbed using that provided grabber. It will not check if it is being grabbed, only if it could be grabbed.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Grabbable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.CanBeGrabbed"

    def __init__(self, slot: str | INodeObjectOutput[Slot] | None = None, grabber: str | INodeObjectOutput[Grabber] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            slot: Initial value for Slot.
            grabber: Initial value for Grabber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if slot is not None:
            self.slot = slot
        if grabber is not None:
            self.grabber = grabber

    @property
    def slot(self) -> str | None:
        """The Slot to check if it can be grabbed."""
        member = self.get_member("Slot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slot.setter
    def slot(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Slot reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Slot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Slot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def grabber(self) -> str | None:
        """The grabber on a user (``LeftHand`` or ``RightHand``)."""
        member = self.get_member("Grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | INodeObjectOutput[Grabber] | None) -> None:
        """Set the Grabber reference by target ID or INodeObjectOutput[Grabber] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Grabber>'),
            )

