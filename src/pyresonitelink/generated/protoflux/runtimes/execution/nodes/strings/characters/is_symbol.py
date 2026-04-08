"""Generated component: IsSymbol."""

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


class IsSymbol(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.IsSymbol.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Characters
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.IsSymbol"

    def __init__(self, character: str | INodeValueOutput[primitives.Char] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            character: Initial value for Character.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if character is not None:
            self.character = character

    @property
    def character(self) -> str | None:
        """Target ID of the Character reference (targets INodeValueOutput[primitives.Char])."""
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character.setter
    def character(self, target: str | INodeValueOutput[primitives.Char] | None) -> None:
        """Set the Character reference by target ID or INodeValueOutput[primitives.Char] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Character",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<char>'),
            )

