"""Generated component: GetType."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.object import object
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetType(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Get Type node takes in an Object, and returns the Type of that object. For example, using a float and connecting it to this node will return System.Single.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GetType"

    def __init__(self, object_: str | INodeObjectOutput[object] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            object_: Initial value for Object.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if object_ is not None:
            self.object_ = object_

    @property
    def object_(self) -> str | None:
        """Target ID of the Object reference (targets INodeObjectOutput[object])."""
        member = self.get_member("Object")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_.setter
    def object_(self, target: str | INodeObjectOutput[object] | None) -> None:
        """Set the Object reference by target ID or INodeObjectOutput[object] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Object")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Object",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<object>'),
            )

