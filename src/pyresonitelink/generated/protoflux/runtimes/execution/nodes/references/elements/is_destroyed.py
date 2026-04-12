"""Generated component: IsDestroyed."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.idestroyable import IDestroyable
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IsDestroyed(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Is Destroyed`` node takes in a destroyable world element and returns if that element was destroyed from the world. Destruction of the slot prevents the result from changing, as by the time the slot is gone, it is too late. There is however a method to check if something did get destroyed, see the examples below.

    Category: ProtoFlux/Runtimes/Execution/Nodes/References/Elements
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Elements.IsDestroyed"

    def __init__(self, element: str | INodeObjectOutput[IDestroyable] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The destroyable world element in question."""
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @element.setter
    def element(self, target: str | INodeObjectOutput[IDestroyable] | None) -> None:
        """Set the Element reference by target ID or INodeObjectOutput[IDestroyable] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Element",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IDestroyable>'),
            )

