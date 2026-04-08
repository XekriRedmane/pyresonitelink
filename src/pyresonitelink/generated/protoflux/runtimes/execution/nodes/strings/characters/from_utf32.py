"""Generated component: FromUTF32."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FromUTF32(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.FromUTF32.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Characters
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.FromUTF32"

    def __init__(self, utf32: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            utf32: Initial value for UTF32.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if utf32 is not None:
            self.utf32 = utf32

    @property
    def utf32(self) -> str | None:
        """Target ID of the UTF32 reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("UTF32")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @utf32.setter
    def utf32(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the UTF32 reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UTF32")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UTF32",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

