"""Generated component: NotifyModified."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NotifyModified(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Notify Modified`` node takes in an IComponent, and when called will invoke the ``NotifyModified`` method on the input Component. Used for components which implement IModifiedEventReceiver like GridContainerPreset and Workspace.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interactions.NotifyModified"

    def __init__(self, next: str | INodeOperation | None = None, modified_component: str | INodeObjectOutput[IComponent] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            modified_component: Initial value for ModifiedComponent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if modified_component is not None:
            self.modified_component = modified_component

    @property
    def next(self) -> str | None:
        """Continue the code from here."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def modified_component(self) -> str | None:
        """The component to check."""
        member = self.get_member("ModifiedComponent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modified_component.setter
    def modified_component(self, target: str | INodeObjectOutput[IComponent] | None) -> None:
        """Set the ModifiedComponent reference by target ID or INodeObjectOutput[IComponent] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ModifiedComponent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ModifiedComponent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IComponent>'),
            )

