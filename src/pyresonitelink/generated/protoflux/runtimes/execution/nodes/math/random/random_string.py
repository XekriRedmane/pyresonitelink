"""Generated component: RandomString."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomString.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Random
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomString"

    def __init__(self, characters: str | INodeObjectOutput[primitives.String] | None = None, length: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            characters: Initial value for Characters.
            length: Initial value for Length.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if characters is not None:
            self.characters = characters
        if length is not None:
            self.length = length

    @property
    def characters(self) -> str | None:
        """Target ID of the Characters reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Characters")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @characters.setter
    def characters(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Characters reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Characters")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Characters",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def length(self) -> str | None:
        """Target ID of the Length reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length.setter
    def length(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Length reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Length",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

