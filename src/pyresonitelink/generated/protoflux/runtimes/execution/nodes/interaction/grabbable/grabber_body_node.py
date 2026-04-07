"""Generated component: GrabberBodyNode."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabberBodyNode(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.GrabberBodyNode.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Grabbable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.GrabberBodyNode"

    def __init__(self, grabber: str | INodeObjectOutput[Grabber] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grabber: Initial value for Grabber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grabber is not None:
            self.grabber = grabber

    @property
    def grabber(self) -> str | None:
        """Target ID of the Grabber reference (targets INodeObjectOutput[Grabber])."""
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

