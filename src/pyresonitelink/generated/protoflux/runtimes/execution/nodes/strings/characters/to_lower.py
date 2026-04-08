"""Generated component: ToLower."""

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


class ToLower(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ToLower node takes in a character or string and outputs it as lowercase. This node takes into account the local user's CultureInfo.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Characters

    **See also**: * ToUpper to turn strings or characters uppercase.
* Microsoft documentation for the ``String.ToLower() method``, which is used internally.

ProtoFlux:Strings:Characters
ProtoFlux:Strings:Formatting
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.ToLower"

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

