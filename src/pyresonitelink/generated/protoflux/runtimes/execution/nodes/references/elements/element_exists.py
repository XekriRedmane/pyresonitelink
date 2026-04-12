"""Generated component: ElementExists."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ElementExists(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Element Exists`` node takes in a world element and returns if that element exists in the world currently. This node will not update in the way you think it does, due to the fact that destroying slots in a world does not remove them immediately, instead they are still referenced in the Assets Slot waiting to be garbage collected (and will still say ``true``). Once that slot has been garbage collected, the reference will be removed and this node will say ``false``.

    Category: ProtoFlux/Runtimes/Execution/Nodes/References/Elements
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Elements.ElementExists"

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
        """The world element in question."""
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

