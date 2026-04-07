"""Generated component: SetCharacterGravity."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetCharacterGravity(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.SetCharacterGravity.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.SetCharacterGravity"

    def __init__(self, next: str | INodeOperation | None = None, gravity: str | INodeValueOutput[primitives.Float3] | None = None, character: str | INodeObjectOutput[CharacterController] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            gravity: Initial value for Gravity.
            character: Initial value for Character.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if gravity is not None:
            self.gravity = gravity
        if character is not None:
            self.character = character

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def gravity(self) -> str | None:
        """Target ID of the Gravity reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Gravity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gravity.setter
    def gravity(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Gravity reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Gravity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Gravity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def character(self) -> str | None:
        """Target ID of the Character reference (targets INodeObjectOutput[CharacterController])."""
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

