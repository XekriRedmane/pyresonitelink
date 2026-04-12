"""Generated component: CharacterLinearVelocity."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterLinearVelocity(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Character Linear Velocity`` node takes in a character controller reference and returns the current velocity that it is currently going at over time.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.CharacterLinearVelocity"

    def __init__(self, character: str | INodeObjectOutput[CharacterController] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The character controller reference."""
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character.setter
    def character(self, target: str | INodeObjectOutput[CharacterController] | None) -> None:
        """Set the Character reference by target ID or INodeObjectOutput[CharacterController] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Character",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.CharacterController>'),
            )

