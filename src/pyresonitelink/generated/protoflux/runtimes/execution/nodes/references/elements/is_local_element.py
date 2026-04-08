"""Generated component: IsLocalElement."""

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


class IsLocalElement(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Is Local Element node takes in a world element and returns if that element is local. A local element is simply an element which isn't synchronized at all, but is still part of the data model. One example of a local element can be observed with the Play One Shot node, which has an option to create a local clip, when the option is on the output of the node will be a local element.

    Category: ProtoFlux/Runtimes/Execution/Nodes/References/Elements
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Elements.IsLocalElement"

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

