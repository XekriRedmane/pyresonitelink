"""Generated component: FromUTF16."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FromUTF16(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.FromUTF16.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Characters
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.FromUTF16"

    def __init__(self, utf16: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            utf16: Initial value for UTF16.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if utf16 is not None:
            self.utf16 = utf16

    @property
    def utf16(self) -> str | None:
        """Target ID of the UTF16 reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("UTF16")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @utf16.setter
    def utf16(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the UTF16 reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UTF16")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UTF16",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

