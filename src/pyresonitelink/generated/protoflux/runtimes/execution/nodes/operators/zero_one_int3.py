"""Generated component: ZeroOneInt3."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ZeroOneInt3(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ZeroOneInt3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ZeroOneInt3"

    def __init__(self, boolean: str | INodeValueOutput[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            boolean: Initial value for Boolean.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if boolean is not None:
            self.boolean = boolean

    @property
    def boolean(self) -> str | None:
        """Target ID of the Boolean reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Boolean")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @boolean.setter
    def boolean(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Boolean reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Boolean")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Boolean",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

