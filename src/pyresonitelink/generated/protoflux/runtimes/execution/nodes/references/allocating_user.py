"""Generated component: AllocatingUser."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AllocatingUser(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.References.AllocatingUser.

    Category: ProtoFlux/Runtimes/Execution/Nodes/References
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.References.AllocatingUser"

    def __init__(self, element: str | INodeObjectOutput[IWorldElement] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            element: Initial value for Element.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if element is not None:
            self.element = element

    @property
    def element(self) -> str | None:
        """Target ID of the Element reference (targets INodeObjectOutput[IWorldElement])."""
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @element.setter
    def element(self, target: str | INodeObjectOutput[IWorldElement] | None) -> None:
        """Set the Element reference by target ID or INodeObjectOutput[IWorldElement] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Element",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IWorldElement>'),
            )

