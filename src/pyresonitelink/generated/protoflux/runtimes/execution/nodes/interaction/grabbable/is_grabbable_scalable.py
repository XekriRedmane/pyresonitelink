"""Generated component: IsGrabbableScalable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IsGrabbableScalable(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.IsGrabbableScalable.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Grabbable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.IsGrabbableScalable"

    def __init__(self, grabbable: str | INodeObjectOutput[IGrabbable] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grabbable: Initial value for Grabbable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grabbable is not None:
            self.grabbable = grabbable

    @property
    def grabbable(self) -> str | None:
        """Target ID of the Grabbable reference (targets INodeObjectOutput[IGrabbable])."""
        member = self.get_member("Grabbable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbable.setter
    def grabbable(self, target: str | INodeObjectOutput[IGrabbable] | None) -> None:
        """Set the Grabbable reference by target ID or INodeObjectOutput[IGrabbable] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Grabbable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Grabbable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IGrabbable>'),
            )

