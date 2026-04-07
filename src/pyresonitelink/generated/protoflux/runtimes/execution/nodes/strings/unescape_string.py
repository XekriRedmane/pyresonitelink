"""Generated component: UnescapeString."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnescapeString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.UnescapeString.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.UnescapeString"

    def __init__(self, string: str | INodeObjectOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            string: Initial value for String.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if string is not None:
            self.string = string

    @property
    def string(self) -> str | None:
        """Target ID of the String reference (targets INodeObjectOutput[str])."""
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @string.setter
    def string(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the String reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "String",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

