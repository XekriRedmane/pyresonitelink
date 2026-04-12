"""Generated component: RandomBool."""

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


class RandomBool(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Random Bool node takes in an (optional) chance and returns a random bool value.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Random
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomBool"

    def __init__(self, chance: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            chance: Initial value for Chance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if chance is not None:
            self.chance = chance

    @property
    def chance(self) -> str | None:
        """The shift in probability to have a higher chance to get a certain result from this node. The default is ``0.5``."""
        member = self.get_member("Chance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chance.setter
    def chance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Chance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Chance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Chance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

