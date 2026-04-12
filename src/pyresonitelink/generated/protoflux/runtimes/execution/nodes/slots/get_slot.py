"""Generated component: GetSlot."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetSlot(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Returns the slot the specified component is attached on.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.GetSlot"

    def __init__(self, component_: str | INodeObjectOutput[IComponent] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            component_: Initial value for Component.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if component_ is not None:
            self.component_ = component_

    @property
    def component_(self) -> str | None:
        """The component you want to find the slot of."""
        member = self.get_member("Component")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @component_.setter
    def component_(self, target: str | INodeObjectOutput[IComponent] | None) -> None:
        """Set the Component reference by target ID or INodeObjectOutput[IComponent] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Component")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Component",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IComponent>'),
            )

