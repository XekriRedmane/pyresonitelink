"""Generated component: TypeColor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.type import Type
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeColor(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Type Color node takes in a Type, and returns the color associated with that type's class inside the FrooxEngine.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.TypeColor"

    def __init__(self, type_: str | INodeObjectOutput[Type] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            type_: Initial value for Type.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if type_ is not None:
            self.type_ = type_

    @property
    def type_(self) -> str | None:
        """Target ID of the Type reference (targets INodeObjectOutput[Type])."""
        member = self.get_member("Type")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @type_.setter
    def type_(self, target: str | INodeObjectOutput[Type] | None) -> None:
        """Set the Type reference by target ID or INodeObjectOutput[Type] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Type")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Type",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Type>'),
            )

